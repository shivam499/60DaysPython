import glob
import streamlit as gui
import plotly.express as px

from nltk.sentiment import SentimentIntensityAnalyzer

filepaths = sorted(glob.glob("diary/*.txt"))

negativity = []
positivity = []

analyzer = SentimentIntensityAnalyzer()

for filepath in filepaths:
    with open(filepath, "r") as file:
        content = file.read()
    score = analyzer.polarity_scores(content)

    positivity.append(score["pos"])
    negativity.append(score["neg"])

dates = [name.strip(".txt").strip("diary/") for name in filepaths]

gui.title("Diary Tone")
gui.subheader("Positivity")

pos_figure = px.line(x=dates, y=positivity, labels={"x": "Date", "y": "Positivity"})

gui.plotly_chart(pos_figure)


gui.subheader("Negativity")

neg_figure = px.line(x=dates, y=negativity, labels={"x": "Date", "y": "Negativity"})

gui.plotly_chart(neg_figure)
