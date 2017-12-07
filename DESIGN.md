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

2. Unfortunately, the best online dictionary out there, Perseus Digital Library, is still not perfect. It does not even know many words, and gives weird translations for others. Some words' translations I had to strip stray punctuation from the ends of. For those untranslated words I used an alternate dictionary with the module "mtranslate" ("mtranslate-master" contains the README, etc. for this, "mtranslate" contains the actual code) which makes use of Google Translate's website.

3. I had to separate the punctuation and section headings from being translated. I also wanted to eliminate duplicates in the "translations" table, so I only had to translate the word once, so I checked the table for a translation and only proceeded if it was not there already. I also saved how many times that word has been encountered, for the vocab filtering feature that I will discuss later.

4. Additionally, the Greek language has words called articles which basically mean "the" but come in different forms. The dictionary wanted to translate them in other, alternately used ways, which are unusual. I had to manually make a dictionary of possible articles and separate them from the translation process, displaying their grammatical features instead. (i.e. "τῇ: article [dat f s]")

DISPLAYING THE DATA (application.py)

1. For displaying the website, I was able to use Flask's route pattern matching, so I did not have to manually enter a route/function for every single section of Greek text. I could make a generic one, which makes use of the section data in every url to decide which page to display. If this url does not have a valid section number, I display an apology meme as seen in pset7.

2. Nor did I have to create an html file for each section; I could use Jinja instead to customize a template html page. To feed the right data for Jinja, I took the section info provided in the url that was requested, and queried my databases for all the data related to that section.

3. Because each book of the Republic has a different number of sections, with different hrefs, I made a different html file for each book. I chose to display every word in the section in an ordered list, and making each word its own ordered list of the Greek and the English translation, to keep them together.

4. Additionally, I wanted the sidebar for vocab filtering to remain accessible no matter where you scroll on the page, so I made its position fixed on a certain part of the right side of the screen.

CHANGING THE DISPLAY (script.js)

1. Earlier, I fed into the html document the frequency that each word occurred throughout the text, storing them as ID's of each word. I used jQuery with the sidebar on the page to select the words with a certain frequency and hide their translations, depending on what difficulty was selected on the sidebar. I stored the difficulty level in the url, to retain the filtering even when the user switches to a different section.

2. I also used jQuery to have the correct links active (colored differently from the rest) depending on which page was currently displayed.


