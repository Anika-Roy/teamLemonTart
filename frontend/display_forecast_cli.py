# Import the WEATHER_SYMBOL map from constant.py
from frontend.frontend_symbols import WEATHER_SYMBOL, ICON_CODE_MAPPING

def get_weather_symbol(weather_icon : int):
    """
    Returns ASCII art representation from a given
    main description from the forecast_json

    Arguments:
        weather_main (string): The main description from the forecast_json

    Returns:
        string: The ASCII art representation of the weather
    """

    # Storing the weather symbol
    weather_symbol = ""

    # Storing if the key was found
    key_found = False

    # Iterating over the ICON_CODE_MAPPING map
    for icon in ICON_CODE_MAPPING:
        # Checking if the weather_icon is in the key
        if weather_icon == icon:
            # Assigning the weather symbol
            weather_symbol = WEATHER_SYMBOL[ICON_CODE_MAPPING[icon]]

            # Assigning the key_found
            key_found = True

            # Breaking out of the loop
            break

    # Declaring the json to return
    json_to_return = {
        "error": False,
        "weather_symbol": weather_symbol
    }

    if (not key_found):
        # Assigning the weather symbol
        json_to_return["weather_symbol"] = WEATHER_SYMBOL["default"]
        json_to_return["error"] = True

    # Returning the weather symbol
    return json_to_return

def display_weather_forecast_final(epoch : int, forecast_json):
    """
    Displays the weather forecast for the given epoch

    Arguments:
        epoch (int): The epoch for which the weather forecast is to be displayed
        forecast_json (json): The json containing the weather forecast
    Returns:
        None
    """
    # Get the entry in the forecast_json for the given epoch
    for entry in forecast_json["list"]:
        if entry["dt"] == epoch:
            forecast_json = entry
            break

    # Get the symbol to display
    final_symbol = get_weather_symbol(forecast_json["weather"][0]["icon"])["weather_symbol"]

    # Get the weather symbol
    weather_info = [
        f"{forecast_json['weather'][0]['main']} -- {forecast_json['weather'][0]['description']}",
        f"{round(forecast_json['main']['temp_min']-273,2)} °C- {round(forecast_json['main']['temp_max']-273,2)} °C",
        f"{forecast_json['wind']['speed']} km/hr {forecast_json['wind']['deg']}°",
        f"{forecast_json['main']['humidity']}% humidity",
        f"Chances of rain: {forecast_json['pop']}",
    ]

    # Printing the weather forecast
    print("+"+"-"*40+"+")
    for line_art, line_info in zip(final_symbol, weather_info):
        print("|"+f"{line_art}"+f"{line_info}"+" "*(27 -len(line_info))+"|")
    print("+"+"-"*40+"+")
        
    