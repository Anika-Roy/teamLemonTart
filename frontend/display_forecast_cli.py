# Import the WEATHER_SYMBOL map from constant.py
from utils.constants import WEATHER_SYMBOL

def get_weather_symbol(weather_main : int):
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

    # Iterating over the WEATHER_SYMBOL map
    for key in WEATHER_SYMBOL:
        # Checking if the weather_main is in the key
        if weather_main in key:
            # Assigning the weather symbol
            weather_symbol = WEATHER_SYMBOL[key]

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

