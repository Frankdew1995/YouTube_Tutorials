
from flask import (Flask, render_template,
                   url_for, redirect, request)

import requests

app = Flask(__name__)


def subscribe_user(email, user_group_email, api_key):

    r = requests.post(
            f"https://api.mailgun.net/v3/lists/{user_group_email}/members",
            auth=('api', api_key),
            data={'subscribed': True,
                  'address': email})
    return r


@app.route('/', methods=["POST", "GET"])
def index():

    if request.method == "POST":

        subscriber_email = request.form.get('email')

        subscribe_user(email=subscriber_email,
                       user_group_email="no-reply@bot.frankdu.co",
                       api_key="key")

    return render_template("index.html")


if __name__ == '__main__':

    app.run(debug=True)
