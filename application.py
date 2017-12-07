import os
from flask import Flask, render_template, request
from cs50 import SQL

# Configure application
app = Flask(__name__)

app.debug = True

db = SQL("sqlite:///words.db")

# Ensure responses aren't cached
if app.config["DEBUG"]:
    @app.after_request
    def after_request(response):
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response.headers["Expires"] = 0
        response.headers["Pragma"] = "no-cache"
        return response

def apology(message, code=400):
    """Renders message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/republic/book<book>/section<section>/<vocab>', methods=['GET'])
def text(book, section, vocab):

    # Query the words and translations to display for the specified section
    text = db.execute("SELECT * FROM original INNER JOIN translations ON original.translation_id=translations.translation_id WHERE section = :section", section=section)

    # If there are no words to display, they've gone to the wrong url
    if len(text) < 1:
        return apology("Page not found", 404)

    # Output a tuple into the template with all the info that needs to be displayed
    for i in range(len(text)):
        text[i] = (text[i]["greek"], text[i]["original"], text[i]["url"], text[i]["translation"], text[i]["frequency"])

    return render_template(f"republic{book}.html", words=text, vocab=vocab)
