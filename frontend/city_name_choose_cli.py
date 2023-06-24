# Import the list of cities
from utils.constants import CITY_LIST

def return_city_name(user_input : str):
    """
    Returns the name of the city using autocomplete

    Arguments:
        user_input (string): The user input

    Returns:
        string: The name of the city
    """

    # Storing the city name
    city_name = ""

    # Iterating over the list of cities
    for city in CITY_LIST:
        # Checking if the city name starts with the user input
        if city.lower().startswith(user_input.lower()):
            # Assigning the city name
            city_name = city
            # Breaking out of the loop
            break

    # Error handling
    if city_name == "":
        # Returning a json with error : True
        return {"error": True, "message": "The city name is invalid."}
    else:
        # Returning the city name
        return {"error": False, "city_name": city_name}
    
def get_user_city_input():
    """
    Read the 
    """