# Import API handlers
import server.handle_forecast5_api 

# Import the CLI handler
import frontend.interactive_calendar_cli
import frontend.city_name_choose_cli
import frontend.choose_time_cli
import frontend.display_forecast_cli

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

def main():

    try:
        # Ask the user for the city name
        city_name = frontend.city_name_choose_cli.return_city_name()
        if city_name.get("error"):
            raise Exception(city_name.get("message"))
    except Exception as e:
        print("Error in city_name_choose_cli.return_city_name():", str(e))
        print("Please try again:)")
        return
 
    try:
        # API call to get the forecast
        forecast_json = server.handle_forecast5_api.get_city_forecast(city_name.get("city_name"), API_KEY)
        if forecast_json.get("cod") != '200':
            raise Exception("Error with OpenWeatherMap API: " + forecast_json.get("message"))
    except Exception as e:
        print("Error in server.handle_forecast5_api.get_city_forecast():", str(e))
        print("Please try again:)")
        return

    try:
        # Get the epochs from the forecast
        epochs = server.handle_forecast5_api.get_epochs_from_forecast(forecast_json)
    except Exception as e:
        print("Error in server.handle_forecast5_api.get_epochs_from_forecast():", str(e))
        print("Please try again:)")
        return

    try:
        # Get unique date epochs for available dates
        unique_date_epochs = utils.epoch_handlers.get_unique_date_epoch(epochs)
    except Exception as e:
        print("Error in utils.epoch_handlers.get_unique_date_epoch():", str(e))
        print("Please try again:)")
        return

    try:
        # Send the available dates to the calendar handler and get the final selected date
        selected_date = frontend.interactive_calendar_cli.get_user_input_calendar(unique_date_epochs, None)
    except Exception as e:
        print("Error in frontend.interactive_calendar_cli.get_user_input_calendar():", str(e))
        print("Please try again:)")
        return

    try:
        # Get all epochs for the selected date
        selected_date_epochs = utils.epoch_handlers.get_epochs_with_date(epochs, selected_date)
    except Exception as e:
        print("Error in utils.epoch_handlers.get_epochs_with_date():", str(e))
        print("Please try again:)")
        return

    try:
        # Ask the user for the time
        selected_time = frontend.choose_time_cli.ask_for_preferred_time(selected_date_epochs)
    except Exception as e:
        print("Error in frontend.choose_time_cli.ask_for_preferred_time():", str(e))
        print("Please try again:)")
        return

    try:
        # Display the final weather forecast
        frontend.display_forecast_cli.display_weather_forecast_final(selected_time, forecast_json)
    except Exception as e:
        print("Error in frontend.display_forecast_cli.display_weather_forecast_final():", str(e))
        print("Please try again:)")
        return

if __name__ == "__main__":
    main()
