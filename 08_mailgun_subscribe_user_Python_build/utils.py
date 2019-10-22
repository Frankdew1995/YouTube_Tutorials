import requests

r = requests.post(

        # Here goes your Base API URL
        "https://api.mailgun.net/v3/bot.frankdu.co/messages",
        # Authentication part - A Tuple
        auth=("api", "key"),

        # mail data will be used to send emails
        data={"from": "Robot <bot@bot.frankdu.co>",
              "to": ["no-reply@bot.frankdu.co"],
              "subject": "Testing some awesomeness of Mailgun",
              "text": " Mailgun test"})

print(r.status_code)
