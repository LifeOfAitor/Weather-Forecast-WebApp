import streamlit as st

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
