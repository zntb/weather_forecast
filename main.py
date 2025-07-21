import streamlit as st
import plotly.express as px
from backend import get_data


st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the number of forecast days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))

if place:  # Only proceed if a place is entered
    try:
        st.subheader(f"{option} in {place}")
        dates, values = get_data(place, days, option)
        
        if option == "Temperature":
            y_label = "Temperature (°C)"
            title = f"Temperature for the next {days} day(s) in {place}"
        else:
            y_label = "Sky Condition"
            title = f"Sky conditions for the next {days} day(s) in {place}"
        
        figure = px.line(x=dates, y=values, 
                        labels={"x": "Date", "y": y_label},
                        title=title)
        st.plotly_chart(figure)
    except Exception as e:
        st.error(f"Error: {e}. Please check the place name and try again.")