import streamlit as st
import plotly.express as px
from backend import get_data
from datetime import datetime, timedelta

# App title, text input, slider, selectbox
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the number of forecast days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))

if place:
    try:
        filtered_data = get_data(place, days)
        st.subheader(f"{option} in {place}")
        
        if option == "Temperature":
            temperatures = [dict["main"]["temp"] for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            figure = px.line(x=dates, y=temperatures, 
                           labels={"x": "Date", "y": "Temperature (°C)"},
                           title=f"{option} for the next {days} day(s)")
            st.plotly_chart(figure)

        elif option == "Sky":
            images = {
                "Clear": "images/clear.png", 
                "Clouds": "images/cloud.png", 
                "Rain": "images/rain.png", 
                "Snow": "images/snow.png"
            }
            
            # Group forecasts by day
            daily_forecasts = {}
            for forecast in filtered_data:
                dt_str = forecast["dt_txt"]
                date = dt_str.split()[0]  # Extract just the date part
                if date not in daily_forecasts:
                    daily_forecasts[date] = []
                daily_forecasts[date].append(forecast)
            
            # Display one row per day
            for date, forecasts in daily_forecasts.items():
                # Format date header (e.g., "Monday, Jan 15")
                dt_obj = datetime.strptime(date, "%Y-%m-%d")
                date_header = dt_obj.strftime("%A, %b %d")
                st.write(f"**{date_header}**")
                
                # Create columns for the day's forecasts
                cols = st.columns(len(forecasts))
                
                for col, forecast in zip(cols, forecasts):
                    with col:
                        # Display weather image
                        condition = forecast["weather"][0]["main"]
                        st.image(images[condition], width=70)
                        
                        # Display time interval
                        dt_str = forecast["dt_txt"]
                        dt_obj = datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S")
                        time_str = dt_obj.strftime("%H:%M")
                        next_time = (dt_obj + timedelta(hours=3)).strftime("%H:%M")
                        st.caption(f"{time_str}-{next_time}")
                
                # Add spacing between days
                st.write("")

    except Exception as e:
        st.error(f"Error: Could not find weather data for '{place}'. Please check the place name and try again.")
        st.stop()