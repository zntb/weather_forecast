import streamlit as st
import plotly.express as px
from backend import get_data

# App title,text input, slider, selectbox and subheader
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the number of forecast days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} in {place}")

if place:
# Get the temperature/sky data
    filtered_data = get_data(place, days)


    if option == "Temperature":
        temperatures = [dict["main"]["temp"] for dict in filtered_data]
        dates = [dict["dt_txt"] for dict in filtered_data]
    # Create a temperature plot
        figure = px.line(x=dates, y=temperatures, 
                        labels={"x": "Date", "y": "Temperature (°C)"},
                        title=f"{option} for the next {days} day(s)")
        st.plotly_chart(figure)

    if option == "Sky":
        images = {
            "Clear": "images/clear.png", 
            "Clouds": "images/cloud.png", 
            "Rain": "images/rain.png", 
            "Snow": "images/snow.png"
        }
        sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
        
        # Split into chunks of 5 for rows
        for i in range(0, len(sky_conditions), 5):
            cols = st.columns(5)
            row_conditions = sky_conditions[i:i+5]
            for col, condition in zip(cols, row_conditions):
                with col:
                    st.image(images[condition], width=115, use_container_width='auto')
                    st.write("")  # Add vertical padding