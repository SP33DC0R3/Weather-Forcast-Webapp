import streamlit as sl
import plotly.express as px
from backend import get_data

# Added title, text input, slider, selectbox and subheader
sl.title("Weather Forecast for the Next Days")
place = sl.text_input("Place:")
days = sl.slider("Forecast Days", max_value=5, min_value=1,
                 help="Select the number of forecasted days")
type_data = sl.selectbox("Select data to view", ("Temperature", "Sky"))

if place:
    try:
        # Get the temperature/sky data
        filtered_data = get_data(place, days)
        sl.subheader(f"{type_data} for the next {days} days in {place}")

        if type_data == "Temperature":
            temperature = [i["main"]["temp"]/10 for i in filtered_data]
            date = [i["dt_txt"] for i in filtered_data]
            # Create a temperature plot
            figure = px.line(x=date, y=temperature, labels={'x': "Date", 'y': "Temperature"})
            sl.plotly_chart(figure)

        if type_data == "Sky":
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                      "Rain": "images/rain.png", "Snow": "images/snow.png"}
            sky_conditions = [i["weather"][0]["main"] for i in filtered_data]
            image_paths = [images[conditions] for conditions in sky_conditions]
            # Render icons for sky
            sl.image(image_paths, width=115)
    except KeyError:
        sl.error("Please Enter A Correct City Name!!!!!".upper())