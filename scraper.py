import bs4
from bs4 import BeautifulSoup
import urllib
import http.client
import socket
import requests
import sys
import re
from lxml import etree

from cs50 import SQL

db = SQL("sqlite:///words.db")


def translation(gkWord):
    print(gkWord)
    URL = "http://www.perseus.tufts.edu/hopper/morph?l=" + gkWord + "&la=greek"
    translation = ""
    # if !isnumber(str(gkWord[0])):
    print(URL)
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html.parser')
    definition = soup.findAll('span', attrs={'class': 'lemma_definition'})
    if len(definition) > 0:

        print(len(definition))
        print(definition[0].text)
        translation = definition[0].text
    else:
        translation = "None"

    return (URL, translation)


if __name__ == "__main__":
    # Scrape the original Greek text section by section
    for i in range(327, 355):
            for j in range(5):
                URL = "http://www.perseus.tufts.edu/hopper/xmlchunk?doc=Perseus%3Atext%3A1999.01.0167%3Abook%3D1%3Asection%3D" + str(i) + "" + str(chr(j + ord('a')))
                print(URL)
                print()
                try:
                    r = requests.get(URL)
                    soup = BeautifulSoup(r.content, 'xml')
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

                            # Deal with quotation elements
                            elif element.name == 'quote':
                                element = '"' + element.text + '"'

                            paragraph += element

                    # Separate punctuation, incl. paragraph and line breaks ("|" and ">") from words
                    paragraph = re.sub(r'(?<=[.,;:|>])(?=[^\s])', r'\n', paragraph)

                    # Separate each word, incl punctuation/line breaks
                    words = paragraph.split()

                    # Find the starting and ending id for words of the Greek passage so it is easier to display the right words.
                    start = db.execute("SELECT * FROM original WHERE ID= (SELECT MAX(ID) FROM original)")
                    start = int(start[0]["ID"]) + 1
                    end = start + (len(words - 1))

                    for word in words:
                        translation(word)
                        db.execute("INSERT INTO original (greek) VALUES (:word)", word=word)
                    # if len(milestone) > 0:
                    #     words.append(milestone[0]["n"])
                    # for p in paragraphs:
                    # print(p[0].contents)
                    # for element in p[0].contents:
                    #     print(element)

                    # if (len(div) < 1):
                    #     continue
                    # print(div[0].text)
                    # paragraph = div[0].text
                    # # Denote paragraph breaks with '\n'
                    #
                    # paragraph = re.sub('([.,:"])', r' \1 ', paragraph)
                    # pArray =
                    # print(pArray)
                    # for word in pArray:
                    #     translation(word)
                    #     db.execute("INSERT INTO original (word) VALUES (:paragraph)", paragraph=word)


                except urllib.error.HTTPError as e:
                    print(e.code, file=sys.stderr)
                except urllib.error.URLError as e:
                    print('URL_Error', file=sys.stderr)
                except socket.timeout as e:
                    print("timeout", file=sys.stderr)
                except http.client.HTTPException as e:
                    print("HTTPException", file=sys.stderr)