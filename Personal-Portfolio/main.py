import streamlit as gui
import pandas as pd

gui.set_page_config(layout="wide")

col1, col2 = gui.columns(2)

with col1:
    gui.image("images/photo.jpg")

with col2:
    gui.title("Shivam Gupta")
    content = """
    I am Shivam Gupta, a seasoned professional with a rich background in data management and software development. Over the years, I have honed my skills in Data Warehousing, excelling in Oracle, SQL Server, and SQLite databases. My expertise extends to Informatica Data Integration and Data Quality tools, where I have successfully orchestrated efficient and high-quality data processes.

Recently, I embraced the realm of cloud integration through IICS (Informatica Intelligent Cloud Services), focusing on Cloud Data Integration (CDI) and Cloud Data Quality (CDQ) services. This endeavor has broadened my capabilities in harnessing the power of cloud technology for scalable and seamless data solutions.

In the programming landscape, I am adept at Java, Python, and Android application development. This multifaceted proficiency allows me to seamlessly bridge the gap between data management and application development, contributing to comprehensive and innovative solutions.

I am driven by a passion for staying at the forefront of technological advancements, ensuring that my skills remain relevant and impactful. With a commitment to excellence, I bring a wealth of experience to tackle challenges in dynamic environments, aiming to innovate and drive success in every endeavor.
    """
    gui.info(content)

gui.write("Below you can find some of the apps I have built in  Python. Feel free to contact me!")

df = pd.read_csv("data.csv", sep=";")

col3, empty_col, col4 = gui.columns([1.5, 0.5, 1.5])

with col3:
    for index, row in df[:10].iterrows():
        gui.header(row["title"])
        gui.write(row["description"])
        gui.image("images/" + row["image"])
        gui.write(f"[Source Code] ({row['url']})")


with col4:
    for index, row in df[10:].iterrows():
        gui.header(row["title"])
        gui.write(row["description"])
        gui.image("images/" + row["image"])
        gui.write(f"[Source Code] ({row['url']})")
