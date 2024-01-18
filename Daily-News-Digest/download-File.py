import requests

url="https://upload.wikimedia.org/wikipedia/commons/a/a6/Pink_lady_and_cross_section.jpg"
response = requests.get(url)

with open("apple.jpg", "wb") as file:
    file.write(response.content)
