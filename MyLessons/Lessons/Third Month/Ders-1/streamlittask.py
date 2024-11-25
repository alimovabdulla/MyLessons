import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
import requests

city = st.text_input("Seher ve ya Olke")
if city:
    api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=4555623f4b5f235427590131a9d5dca7"
    response = requests.get(api)
    if response.status_code == 200:
        data = response.json()
        options = st.selectbox(
            "Celsius, Kelvin ve ya Fahrenheit", ["Celsius", "Fahrenheit", "Kelvin"]
        )

        def convert_temperature(options, data):
            if options == "Celsius":
                celsius = data["main"]["temp"] - 273.15
                return celsius
            elif options == "Fahrenheit":
                fahrenheit = (data["main"]["temp"] - 273.15) * 9 / 5 + 32
                return fahrenheit
            elif options == "Kelvin":
                kelvin = data["main"]["temp"]
                return kelvin

        converted_temperature = convert_temperature(options, data)

        df = pd.DataFrame({"Hava": [converted_temperature]})

        plt.title(f"{city} Hava Proqnozu")
        plt.plot(df["Hava"], label="Temperatur", marker="o", color="red")
        plt.legend()
        st.pyplot(plt)
    else:
        st.error("Osibkaaa")
