import streamlit as st
import plotly.express as px
from backend import get_data


st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the number of forecast days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} in {place}")

# All available data
all_dates = ["2025-01-01", "2025-01-02", "2025-01-03", "2025-01-04", "2025-01-05"]
all_temperatures = [-1, 2, 1, -5, 0]

data = get_data(place, days, option)

d, t  = get_data(days)

figure = px.line(x=d, y=t, 
                 labels={"x": "Date", "y": "Temperature (°C)"},
                 title=f"{option} for the next {days} day(s)")
st.plotly_chart(figure)