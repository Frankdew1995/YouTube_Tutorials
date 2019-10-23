
from flask import Flask, render_template, url_for, request
import requests

app = Flask(__name__)


def subscribe_user(email, user_group_email, api_key):

    resp = requests.post(f"https://api.mailgun.net/v3/lists/{user_group_email}/members",
                         auth=("api", api_key),
                         data={"subscribed": True,
                               "address": email}
                         )

    print(resp.status_code)

    return resp


@app.route("/", methods=["GET", "POST"])
def index():

    # if user submits the form
    if request.method == "POST":

        email = request.form.get('email')

        subscribe_user(email=email,
                       user_group_email="newsletter@bot.frankdu.co",
                       api_key="key-6fb07823b068bc4469c5cab80e0f5590")

    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)