# backend intro, test, server, etc.

from flask import Flask, render_template, request, make_response

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("/index.html")


@app.route("/about")
def about():

    user_name = request.cookies.get("user_name")
    programming_languages = ["Python", "Javascript", "HTML", "CSS"]
    mood = "happy"

    return render_template("/about.html",
                           user_name=user_name,
                           languages=programming_languages,
                           mood=mood)


# login data form
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("/login.html")

    # if POST request check form data and return success/fail
    if request.method == "POST":
        # extract form data
        login_account = request.form.get("login-account")
        login_password = request.form.get("login-password")

    # check login data is not empty
    is_data_missing = not login_account or not login_password

    # return response
    if is_data_missing:
        return render_template("fail.html")

    # set cookie with account name & pass
    response = make_response(render_template("/success.html"))
    response.set_cookie("user_name", login_account)

    return response


# contact data form
@app.route("/contact", methods=["GET", "POST"])
def contact():
    # if GET request return contact form
    if request.method == "GET":
        return render_template("contact.html")

    # if POST request check form data and return success/fail
    if request.method == "POST":
        # extract form data
        contact_name = request.form.get("contact-name")
        contact_email = request.form.get("contact-email")
        contact_message = request.form.get("contact-message")

    # check login data is not empty
    is_data_missing = not contact_name or not contact_email or not contact_message

    # return response
    if is_data_missing:
        return render_template("fail.html")

    return render_template("/success.html")


if __name__ == '__main__':
    app.run()