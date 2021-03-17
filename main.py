# backend intro, test, server, etc.

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("/index.html")


@app.route("/about")
def about():

    user_name = "Ivan"
    programming_languages = ["Python", "Javascript", "HTML", "CSS"]
    mood = "happy"

    return render_template("/about.html",
                           user_name=user_name,
                           languages=programming_languages,
                           mood=mood)


if __name__ == '__main__':
    app.run()