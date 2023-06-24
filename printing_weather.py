from utils import response
from utils import ascii_art_dictionary

selected= "2022-09-04 12:00:00"
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
    
