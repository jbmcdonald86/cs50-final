import bs4
from bs4 import BeautifulSoup
import socket
import requests
import re

from cs50 import SQL

db = SQL("sqlite:///words.db")

TEXT = "republic"

def translation(gkWord):
    print(gkWord)
    URL = "http://www.perseus.tufts.edu/hopper/morph?l=" + gkWord + "&la=greek"
    translation = ""
    data = requests.get(URL)
    soup = BeautifulSoup(data.content, 'html.parser')
    definition = soup.findAll('span', attrs={'class': 'lemma_definition'})

    # Check if Perseus has a translation for the word.
    if len(definition) > 0:
        translation = definition[-1].text
    else:
        translation = ""

    # Insert data into the translations table, preventing the addition of duplicate words
    translationLine = db.execute("SELECT * FROM translations WHERE original = :gkWord", gkWord=gkWord)
    if len(translationLine) < 1:
        new_line = db.execute("INSERT INTO translations (original, url, translation, frequency) VALUES (:original, :url, :translation, :frequency)",
                            original=gkWord, url=URL, translation=translation, frequency=1)

        translationLine = db.execute("SELECT * FROM translations WHERE translation_id= (SELECT MAX(translation_id) FROM translations)")
    else:
        db.execute("UPDATE translations SET frequency = :frequency WHERE original = :gkWord", frequency=translationLine[0]['frequency'] + 1, gkWord=gkWord)
    translation_id = translationLine[0]['translation_id']

    # Return the ID of the new row, to link the translation to the original Greek table
    return translation_id


if __name__ == "__main__":
    # Scrape the original Greek text section by section
    for i in range(327, 355):
            for j in range(5):
                URL = "http://www.perseus.tufts.edu/hopper/xmlchunk?doc=Perseus%3Atext%3A1999.01.0167%3Abook%3D1%3Asection%3D" + str(i) + "" + str(chr(j + ord('a')))
                print(URL)
                print()
                r = requests.get(URL)
                print(r.text)
                soup = BeautifulSoup(r.content, 'html.parser')
                # soup = etree.parse(StringIO(r.text))
                # context = etree.iterparse(StringIO(r.text))
                div1 = soup.findAll('div1')
                # Check if the url is a valid one
                if len(div1) < 1:
                    continue
                paragraphs = div1[0].findAll('p')
                paragraph = ""

                for p in paragraphs:
                    for element in p:

                        # Replace xml tag with its section number attribute
                        if element.name == 'milestone':
                            if element["unit"] == "section":
                                element = element["n"] + " > "
                            else:
                                element = " | "

                        # Deal with quotation/citation elements
                        elif element.name == 'quote':
                            element = '"' + element.text + '"'
                        elif element.name == 'q':
                            element = "'" + element.text + "'"
                        elif element.name == 'cit':
                            element = " | " + element.text + " | "
                        elif element.name == 'bibl':
                            element = element.text + " | "
                        print(element)
                        paragraph += element

                # Separate punctuation, incl. paragraph and line breaks ("|" and ">"), from words
                paragraph = re.sub('([.,:;])', r' \1 ', paragraph)

                # Separate each word, incl punctuation/line breaks
                words = paragraph.split()

                # Insert each word into the "original" table, along with its translation_id and character length
                for word in words:
                    translation_id = translation(word)
                    db.execute("INSERT INTO original (greek, translation_id, length, section) VALUES (:word, :translation_id, :length, :section)",
                            word=word, translation_id=translation_id, length=len(word), section=str(i) + str(chr(j + ord('a'))))

                # Open the html file to add the links for each section
                # https://stackoverflow.com/questions/10507230/insert-line-at-middle-of-file-with-python
                html = open("/home/ubuntu/workspace/final/templates/republic.html", "r")
                contents = html.readlines()
                html.close()

                # Insert the link to the newly scraped passage
                section = str(chr(j + ord('a')))
                value = f'<a href="/{TEXT}/book1/section{str(i)}{section}" class="list-group-item list-group-item-action section-link"></a>\n'
                contents.insert(-25, value)

                html = open("/home/ubuntu/workspace/final/templates/republic.html", "w")
                contents = "".join(contents)
                html.write(contents)
                html.close()