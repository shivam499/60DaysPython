import streamlit as gui
import requests

apiKey="IEqzADySw2eWgBBrvfKRi2ZxwzChcvoxbA6KS9HE"
url = f"https://api.nasa.gov/planetary/apod?api_key={apiKey}"

response = requests.get(url)
content = response.json()

# comment these lines if you don't want to download file
with open("apod_image.png", "wb") as file:
    file.write(requests.get(content["url"]).content)

gui.subheader(content["title"])
# gui.image(content["url"])
gui.image("apod_image.png")
gui.write(content["explanation"])