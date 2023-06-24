import display_forecast_cli

input={
      "dt": 1661871600,
      "main": {
        "temp": 296.76,
        "feels_like": 296.98,
        "temp_min": 296.76,
        "temp_max": 297.87,
        "pressure": 1015,
        "sea_level": 1015,
        "grnd_level": 933,
        "humidity": 69,
        "temp_kf": -1.11
      },
      "weather": [
        {
          "id": 500,
          "main": "Rain",
          "description": "light rain",
          "icon": "10d"
        }
      ],
      "clouds": {
        "all": 100
      },
      "wind": {
        "speed": 0.62,
        "deg": 349,
        "gust": 1.18
      },
      "visibility": 10000,
      "pop": 0.32,
      "rain": {
        "3h": 0.26
      },
      "sys": {
        "pod": "d"
      },
      "dt_txt": "2022-08-30 15:00:00"
    }

final_symbol=display_forecast_cli.get_weather_symbol(input["weather"][0]["icon"])["weather_symbol"]

weather_info = [
    f"{input['weather'][0]['main']} -- {input['weather'][0]['description']}",
    f"{input['main']['temp_min']} °C- {input['main']['temp_max']} °C",
    f"{input['wind']['speed']} km/hr {input['wind']['deg']}°",
    f"{input['main']['humidity']}% humidity",
    f"Chances of rain: {input['pop']}",
]

for line_art, line_info in zip(final_symbol, weather_info):
    print(f"{line_art}   {line_info}")