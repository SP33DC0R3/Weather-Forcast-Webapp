import streamlit as sl

sl.title("Weather Forecast for the Next Days")
place = sl.text_input("Place:")
days = sl.slider("Forecast Days", max_value=5, min_value=1,
                 help="Select the number of forecasted days")
option = sl.selectbox("Select data to view", ("Temperature", "Sky"))
sl.subheader(f"{option} for the next {days} days in {place}")
