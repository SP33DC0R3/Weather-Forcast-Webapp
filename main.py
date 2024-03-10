import streamlit as sl
import plotly.express as px
from backend import get_data


sl.title("Weather Forecast for the Next Days")
place = sl.text_input("Place:")
days = sl.slider("Forecast Days", max_value=5, min_value=1,
                 help="Select the number of forecasted days")
type_data = sl.selectbox("Select data to view", ("Temperature", "Sky"))
sl.subheader(f"{type_data} for the next {days} days in {place}")

d , t = get_data(place, days, type_data)

figure = px.line(x=d, y=t, labels={'x': "Date", 'y': "Temperature"})
sl.plotly_chart(figure)