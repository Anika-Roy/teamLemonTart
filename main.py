# Import API handlers
import server.handle_forecast5_api 

# Import the CLI handler
import frontend.interactive_calendar_cli

# Loading the dotenv configuration
from dotenv import load_dotenv
load_dotenv()

# Setting the API_KEY form the dotenv file
import os
API_KEY = os.getenv("OPENWEATHERMAP_API_KEY")

def main():
    

# # Get the forecast for the city
# city_name = "Zocca"
# forecast_json = server.handle_forecast5_api.get_lat_lon_forecast(city_name, API_KEY)

# print("forecast : ", forecast_json)

# # Get the epochs from the forecast
# epochs = server.handle_forecast5_api.get_epochs_from_forecast(forecast_json)

# # Get the calendar from the epochs
# calendar = frontend.interactive_calendar_cli.get_calendar_from_epochs(epochs, None)

# # Print the calendar
# print(calendar['calendar'])