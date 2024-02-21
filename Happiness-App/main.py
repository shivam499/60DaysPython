import streamlit as gui
import plotly.express as px
import pandas as pd

gui.header("In Search for Happiness")

x_axis = gui.selectbox("Select data for the X-axis", ("GDP", "Happiness", "Generosity"))

y_axis = gui.selectbox("Select data for the Y-axis", ("GDP", "Happiness", "Generosity"))

gui.subheader(f"{x_axis} and {y_axis}")

df = pd.read_csv("happy.csv")

if x_axis == "GDP":
    x_data = df["gdp"]
elif x_axis == "Happiness":
    x_data = df["happiness"]
elif x_axis == "Generosity":
    x_data = df["generosity"]

if y_axis == "GDP":
    y_data = df["gdp"]
elif y_axis == "Happiness":
    y_data = df["happiness"]
elif y_axis == "Generosity":
    y_data = df["generosity"]

figure = px.scatter(x=x_data, y=y_data, labels={"x": x_axis, "y": y_axis})
gui.plotly_chart(figure)
