import streamlit as st
import plotly.express as px
from backend import get_data

title = st.title("WEATHER FORECAST")
city = st.text_input(label="", placeholder="Select a city", key="city")
days = st.slider(label="Forecast Days", key="days", min_value=1, max_value=5)
data_type = st.selectbox(label="Type of data to visualize",
                         options=["Temperature", "Sky", "Both"])
if city:
    if data_type == "Both":
        st.subheader(f"Temperature and sky for the next {days} days in "
                     f"{city.capitalize()}")
    else:
        st.subheader(f"{data_type} for the next {days} days in "
                     f"{city.capitalize()}")

# get data for graph
data = get_data(city, days, data_type)

# graph creation
dates = ["2022-10-12", "2022-10-13", "2022-10-14"]
temperatures = [10, 11, 12]
figure = px.line(x=dates, y=temperatures, labels={"x": "Date",
                                                  "y": "Temperatures"})
st.plotly_chart(figure)