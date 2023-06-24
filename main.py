# Import API handlers
import server.handle_forecast5_api 

# Import the CLI handler
import frontend.interactive_calendar_cli
import frontend.city_name_choose_cli

# Import utilities
import utils.epoch_handlers

# Loading the dotenv configuration
from dotenv import load_dotenv
load_dotenv()

# Import datetime
import datetime

# Setting the API_KEY form the dotenv file
import os
API_KEY = os.getenv("OPENWEATHERMAP_API_KEY")

# TODO : Add error checks everywhere
def main():
    # Ask the user for the city name
    city_name=frontend.city_name_choose_cli.return_city_name()
    
    # Checking if the city_name is valid
    if city_name["error"]:
        print(city_name["message"])
        return

    # API call to get the forecast
    forecast_json = server.handle_forecast5_api.get_lat_lon_forecast(city_name["city_name"], API_KEY)

    # Checking if the forecast is valid
    # if forecast_json["cod"] != 200:
    #     print("Error with OpenWeatherMap API : ", forecast_json["message"])
    #     return

    # Get the epochs from the forecast
    epochs = server.handle_forecast5_api.get_epochs_from_forecast(forecast_json)

    # Get datetime from every epoch
    unique_date_epochs = utils.epoch_handlers.get_unique_date_epoch(epochs)

    # Send the datetime to the calendar handler and get the date
    selected_date = frontend.interactive_calendar_cli.get_user_input_calendar(unique_date_epochs, None)

    # Get all epochs for the selected date
    selected_date_epochs = utils.epoch_handlers.get_epochs_with_date(epochs, selected_date)

    print(selected_date_epochs)

if __name__ == "__main__":
    main()