import streamlit as st
import plotly.express as px
from backend import get_data, get_dates_temp_cond

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
data = get_data(city, days)
dates, temperatures, conditions = get_dates_temp_cond(data, data_type)

# graph creation
figure = px.line(x=dates, y=temperatures, labels={"x": "Date",
                                                  "y": "Temperature (C)"})
# display graph
st.plotly_chart(figure)
