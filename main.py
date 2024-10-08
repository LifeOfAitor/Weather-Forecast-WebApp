import streamlit as st
import plotly.express as px
from backend import get_data, get_dates_temp_cond

title = st.title("WEATHER FORECAST")
city = st.text_input(label="", placeholder="Select a city", key="city")
days = st.slider(label="Forecast Days", key="days", min_value=1, max_value=5)
data_type = st.selectbox(label="Type of data to visualize",
                         options=["Temperature", "Sky"])
try:
    if city:
        st.subheader(f"{data_type} for the next {days} days in "
                     f"{city.capitalize()}")
        # get data for graph, ready to work no mater the "data_type"
        data = get_data(city, days)
        # filter data
        dates, temperatures, conditions = get_dates_temp_cond(data)

        if data_type == "Temperature":
            # graph creation
            figure = px.line(x=dates, y=temperatures, labels={"x": "Date",
                                                              "y": "Temperature (C)"})
            # display graph
            st.plotly_chart(figure)

        if data_type == "Sky":
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                      "Rain": "images/rain.png", "Snow": "images/snow.png"}
            output_data = [images[current_condition]
                           for current_condition in conditions]
            # Maximum number of columns per row
            max_columns_per_row = 4
            num_rows = (len(output_data) + max_columns_per_row - 1) // max_columns_per_row

            for row in range(num_rows):
                cols = st.columns(max_columns_per_row)
                for i in range(max_columns_per_row):
                    idx = row * max_columns_per_row + i
                    if idx < len(output_data):
                        with cols[i]:
                            st.image(output_data[idx], width=115)
                            st.write(dates[idx][:-3])

except KeyError:
    st.error("Please enter a valid place")