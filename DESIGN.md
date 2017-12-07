Bryce McDonald

Greek Interlinear Dictionary

Inspiration: When studying Latin, I used the interlinear dictionary on nodictionaries.com, which was a huge help. I realized that there is not a comparable one for Ancient Greek, which would be a huge help for a Classics fan like myself.

SCRAPING PROCESS

1. First, I had to get the Greek/translations before I could display it on the webpage. I decided to use the Python 'requests' library to retrieve the website data, and BeautifulSoup to parse it. I parsed as much as possible in xml instead of html, since xml is just cleaner.

2. It would not make sense to scrape all the data and display dynamically as the website loaded, so I decided to use a SQL database to store the Greek text and translations. I could have just stored the Greek line-by-line, but then it would be tricky to know where to position the translation relative to the original Greek.

3. Instead, I decided to store each word one at a time in one table ("original"), so I could know the order the words originally came in. As I separated each word out from the rest of the text, I looked up the translation, scraped that, and stored it in another table, with a column in the first table ("translation_id) to link to the translation in the second.

TRANSLATION PROCESS

1. Unfortunately, the best online dictionary out there is still not perfect. 

3. Additionally, the Greek language has words called articles which basically mean "the" but come in different forms. The dictionary wanted to translate them in other, alternately used ways, which are unusual. I had to manually make a dictionary of possible articles and separate them from the translation process, displaying their grammatical features instead.
