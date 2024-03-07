import streamlit as sl
import plotly.express as px

sl.title("Weather Forecast for the Next Days")
place = sl.text_input("Place:")
days = sl.slider("Forecast Days", max_value=5, min_value=1,
                 help="Select the number of forecasted days")
option = sl.selectbox("Select data to view", ("Temperature", "Sky"))
sl.subheader(f"{option} for the next {days} days in {place}")


def get_data(days):
    dates = ["2024-01-25", "2024-01-26", "2024-01-27"]
    temperatures = [10, 11, 16]
    temperatures = [days * i for i in temperatures]
    return dates, temperatures


d, t = get_data(days)

figure = px.line(x=d, y=t, labels={'x': "Date", 'y': "Temperature"})
sl.plotly_chart(figure)