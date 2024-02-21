import streamlit as gui
import plotly.express as px
from backend import get_data

gui.title("Weather Forecast for the Next Days")
place = gui.text_input("Place: ")
days = gui.slider("forecast Days", min_value=1, max_value=5, help="Select the number of forecasted days")

option = gui.selectbox("Select data to view", ("Temperature", "Sky"))

gui.subheader(f"{option} for the next {days} in {place}")

if place:
    try:
        filtered_data = get_data(place, days)

        if option == "Temperature":
            temp = [dic["main"]["temp"]/10 for dic in filtered_data]
            # dates = [datetime.date.fromtimestamp(dic["dt"]).isoformat() for dic in filtered_data]
            dates = [dic["dt_txt"] for dic in filtered_data]
            figure = px.line(x=dates, y=temp, labels={"x": "Date", "y": "Temp (C)"})
            gui.plotly_chart(figure)
        elif option == "Sky":
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png", "Rain": "images/rain.png",
                      "Snow": "images/snow.png"}
            sky_conditions = [dic["weather"][0]["main"] for dic in filtered_data]
            image = [images[condition] for condition in sky_conditions]
            gui.image(image, width=115, caption=sky_conditions)

    except KeyError:
        gui.info("Location does not found.")


