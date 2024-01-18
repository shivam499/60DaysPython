import requests
from send_email import send_email

apiKey = "dedcf54bd7a74cbc922f5c99d4e9f0ba"
topic = "tesla"

url = f"https://newsapi.org/v2/everything?q={topic}&from=2023-12-18" \
      f"&sortBy=publishedAt&apiKey={apiKey}&language=en"

response = requests.get(url)
content = response.json()

body = "Subject: Today's News"+"\n"
for article in content["articles"][:20]:
    if article["title"] and article["description"] is not None:
        body = body + article["title"] + "\n" \
               + article["description"] + "\n" \
               + article["url"] + 2 * "\n"

body = body.encode("UTF-8")
print(body)
send_email(body)
