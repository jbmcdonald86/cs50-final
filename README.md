# CS50-Final-Project

Bryce McDonald

Greek Interlinear Dictionary

Abstract: Have you ever been doing your Ancient Greek translation homework (theoretically of course) and not known a certain vocab word?
You likely had to look it up manually in some online or physical dictionary, going through the whole effort of switching tabs or looking up from your text, and typing it in, only to have to navigate the actual dictionary entries.

Not anymore! With this interlinear dictionary, the Greek text and the translation are integrated to make your homework time much more efficient.

SETUP

1. Open up CS50 IDE, in a workspace with Harvard's CS50 template and change into the /final directory with ~/workspace/ $ cd final

2. Once you are in the directory, install all the required packages with ~/workspace/final $ sudo pip3 install --user -r requirements.txt

3. If for some reason, you cannot use Harvard's CS50 workspace template, you will need to change to Python version 3 with ~/workspace/final $ sudo mv /usr/bin/python /usr/bin/python2 and then ~/workspace/final $ sudo ln -s /usr/bin/python3 /usr/bin/python

4. In a new terminal window, change to the same directory /final and export the flask application variable with ~/workspace/final $ export FLASK_APP=application.py

5. Start the flask application in that same terminal window with ~/workspace/final $ flask run

6. Copy and paste into a new web browser tab the url that flask gives you shortly after you enter the flask run command, which should be on the same line as "* Running on [url] (Press CTRL+C to quit)".

7. To open up the database file "words.db" enter the terminal command ~/workspace/final $ phpliteadmin words.db

USAGE

1. You will be greeted with the homepage of the website, and will be given a list of texts to select. (Currently only Plato's Republic is supported)

2. Click the link in the middle of the page, or the one on the navbar, and you will be taken straight into the Greek text of Plato's masterpiece.

3. At the top are links to each of the five books, and to all of the sections in each book (which links change depending on what book you are currently in).

4. Hover over the links with your mouse to have the section/book number displayed next to the heading. Click on one to be taken to that part of the Greek text.

5. Moving down the page, you will see a bold heading with the section number on it, and below that, the section of text itself.

6. For each Greek word in the original text, displayed below it is its root form, the most simplified version of that word, and a simple translation of the word. 

7. Each of these words also serves as a link to the entry page in an online Greek dictionary, where you can find all the details about the word, including alternate translations or possible parsings of it.

8. One quirk of Greek is that most nouns have an "article" in front of them, a little word that really means nothing more than "the". In the text, I have specified these as articles instead of translating them, and given some salient grammatical details about them in brackets. (i.e. τῇ: article [dat f s])

9. Moving to the right of the page, you'll see a sidebar that has three links on it. If you are more advanced in your Greek, and already know many of the words and don't want to clutter up your screen with all those translations, you can filter out the easier words (the most common ones) so they are not shown. The higher the number, the less translations you will be shown.
