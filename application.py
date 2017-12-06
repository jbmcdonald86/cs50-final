import os
from flask import Flask, render_template, request
from cs50 import SQL

import sys

# Configure application
app = Flask(__name__)

app.debug = True

db = SQL("sqlite:///words.db")

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/republic/book<book>/section<section>/<vocab>', methods=['GET'])
def text(book, section, vocab):

    # Query the words and translations to display for the specified section
    text = db.execute("SELECT * FROM original INNER JOIN translations ON original.translation_id=translations.translation_id WHERE section = :section", section=section)

    # Output a tuple into the template with all the info that needs to be displayed
    for i in range(len(text)):
        text[i] = (text[i]["greek"], text[i]["original"], text[i]["url"], text[i]["translation"], text[i]["frequency"])
    return render_template(f"republic{book}.html", words=text, vocab=vocab)

# Iterate through all p elements in the relevant div.
# Scrape all content within p elements.
# Create a copy of the html file with the book and section numbers in the name.
# Have to have each word individually, but also the punctuation. Could check if array/database
# element is in the Unicode range of Greek, and if not, not make it an a element.
# Could have one table that is just the straight text, with each word a different entry, including the punctuation.
# Have a second table that has all the dictionary definitions, and have its own automatic primary key, for which there is a colunn on the first, text, table.
# Use jinja, with an if stmt inside the for loop that check whether
# Could use a dictionary with the key as the word, the value as the link, but this would not preserve the paragraph breaks (could insert a key like '\n'). And, it might be too large to store.

# Have a dropdown link in toolbar "Texts", where you can click directly on the text, or go to a texts page where it has "Plato, \iRepublic\", with the title name as a link.
# Better would be to have the list of texts on the home page, and there is a link for each text on the toolbar, until it gets too many.

# Store the words in the database, with punctuation as separate entries, with that table's primary key as a translation's secondary key. On the punctuation, leave the column for the key of the translation blank.
# Store integers that represent how many entries of the database to grab for each page.
# Query the database for that range of words/punctuation (with the hfref for it in that table, joining to the translation table for the lexical form, and translatoion.
# Store these either: as an array of tuples, as a dictionary with the word as key, translation as value, as two different arrays, making sure the punctuation in the first array has a corresponding blank space in the second.
# Start a string for the html insertion with "<p>", then use for loop to iterate through the array,
# if stmt to check if value's first char is in the Gk unicode range.
# If so, make new a element with

# Like nodictionaries does, for each line in the Perseus Greek, create a new entry in the "text" table, and in the translation table
# have each word with a line-number column, and with a column for its order within that line.
# Need to make the section/book numbers adaptable for window size, but can't do this with the lines.

# Limit lines by number of characters, go down to the nearest word.

# If you display by line, you don't know where to put the translations, especially if there's punctuation.
# Better way is to put everything in one table, words, punctuation, translation, everything. If the a certain word is in the Gk
# range of unicode, then you put a space before it, to deal with punctuation. Put this as one of the columns in the table, a binary
# of whether it is punctuation. Also have a column for number of characters.
# Will have to have a binary as well for whether an entry starts with "[" for the paragraph number, and just do a paragraph after that.
# As far as paragraph spacing, everytime it goes to a new div tag, start the p element, and whenever there is a new p element, end
# that one and start the next one.
# If there is a period followed by a word w/ no space in b/w, that is a par break.
# If there is a "" or a " " in the array, label it newline.

# Translations table : "CREATE TABLE 'translations' ('translation_id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 'original' TEXT, 'url' TEXT, 'translation' TEXT, 'frequency' INTEGER)"
# Original table: "CREATE TABLE 'original' ('greek_id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 'greek' TEXT, 'translation_id' INTEGER, 'length' INTEGER, 'book' TEXT, 'section' TEXT")

# Add function to use Google Translate for Gk words that aren't in Perseus, but only if they aren't numbers/punctuation.

# Have to make a case for when the translation is "[definition unavailable]"

# Need to make a case for when the translation ends in a comma, to strip that comma

# Have an area near the navbar that says the number of the a element you're hovering over.

# Make an exception for the articles, will hav to look them up, deal with them individually.

# Could add div wrapper for each word to make size-responsive

# Main priorities:
# Make field that displays section number when you hover over it XXX
# Make navbar change color based on what page you're on XXXXXX
# Make difficulty slider/grouped buttons with JS
# Take care of definition unavailable
# Add below under border-bottom element with @ Bryce McDonald, CS 50 Final Project. Thanks to Perseus Digital Library for the Greek text and online dictionary. XXX
# Fix punctuation XXX
# Makes exception for articles
# Fix sidebar position
# Strip punctuation from end of translations