Bryce McDonald

Greek Interlinear Dictionary

Inspiration: When studying Latin, I used the interlinear dictionary on nodictionaries.com, which was a huge help. I realized that there is not a comparable one for Ancient Greek, which would be a huge help for a Classics fan like myself.

SCRAPING PROCESS (scraper.py)

1. First, I had to get the Greek/translations before I could display it on the webpage. I decided to use the Python 'requests' library to retrieve the website data, and BeautifulSoup to parse it. I parsed as much as possible in xml instead of html, since xml is just cleaner.

2. It would not make sense to scrape all the data and display dynamically as the website loaded, so I decided to use a SQL database to store the Greek text and translations. I could have just stored the Greek line-by-line, but then it would be tricky to know where to position the translation relative to the original Greek.

3. Instead, I decided to store each word one at a time in one table ("original"), so I could know the order the words originally came in. As I separated each word out from the rest of the text, I looked up the translation, scraped that, and stored it in another table, with a column in the first table ("translation_id) to link to the translation in the second.

4. I decided to scrape one book of the Republic at a time, using "for" loops to get each section. I had to separate each word from each other and save it, including punctuation, and use special symbols (">", "|" ) to store newlines or paragraph breaks.

5. Finally, at the end of each section I added text to my html document for a link/button on the top of the page that redirects to that section on my website.

TRANSLATION PROCESS

1. From the Perseus dictionary, I was able to get a root/basic form of the Greek word, a simple translation, and a link to the dictionary entry for most pages.

2. Unfortunately, the best online dictionary out there, Perseus Digital Library, is still not perfect. It does not even know many words, and gives weird translations for others. Some words' translations I had to strip stray punctuation from the ends of. For those untranslated words I used an alternate dictionary with the module "mtranslate" which makes use of Google Translate's website.

3. I had to separate the punctuation and section headings from being translated. I also wanted to eliminate duplicates in the "translations" table, so I only had to translate the word once, so I checked the table for a translation and only proceeded if it was not there already. I also saved how many times that word has been encountered, for the vocab filtering feature that I will discuss later.

4. Additionally, the Greek language has words called articles which basically mean "the" but come in different forms. The dictionary wanted to translate them in other, alternately used ways, which are unusual. I had to manually make a dictionary of possible articles and separate them from the translation process, displaying their grammatical features instead. (i.e. "τῇ: article [dat f s]")

DISPLAYING THE DATA (application.py)


