from utils import ascii_art_dictionary

response={
    "dt": 1661893200,
    "main": {
    "temp": 292.46,
    "feels_like": 292.54,
    "temp_min": 290.31,
    "temp_max": 292.46,
    "pressure": 1015,
    "sea_level": 1015,
    "grnd_level": 931,
    "humidity": 80,
    "temp_kf": 2.15
    },
    "weather": [
    {
        "id": 500,
        "main": "Rain",
        "description": "light rain",
        "icon": "10n"
    }
    ],
    "clouds": {
    "all": 68
    },
    "wind": {
    "speed": 2.66,
    "deg": 210,
    "gust": 3.58
    },
    "visibility": 10000,
    "pop": 0.7,
    "rain": {
    "3h": 0.49
    },
    "sys": {
    "pod": "n"
    },
    "dt_txt": "2022-08-30 21:00:00"
}

for item in response["list"]:
    if item["dt_txt"] == selected:
        print("weather: ",item["weather"][0]["main"])
        print(ascii_art_dictionary[item["weather"][0]["main"]])
        print("temperature: ",item["main"]["temp"])
        print("feels like: ",item["main"]["feels_like"])
        print("temp_min: ",item["main"]["temp_min"])
        print("temp_max: ",item["main"]["temp_max"])
        print("pressure: ",item["main"]["pressure"])
        print("humidity: ",item["main"]["humidity"])
        print("wind speed: ",item["wind"]["speed"])
        print("wind deg: ",item["wind"]["deg"])
        print("wind gust: ",item["wind"]["gust"])
        print("visibility: ",item["visibility"])
        print("pop: ",item["pop"])
        print("rain: ",item["rain"])
        print("sys: ",item["sys"])
        print("dt_txt: ",item["dt_txt"])
        break
    
