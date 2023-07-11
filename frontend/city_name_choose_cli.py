# Import the hardcoded list of cities
from utils.constants import CITY_LIST
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import Completer, Completion

# Define custom completer
class MyCompleter(Completer):
    def get_completions(self, document, complete_event):
        # Implement logic to provide completions
        completions = CITY_LIST
        word_before_cursor = document.get_word_before_cursor()

        for completion in completions:
            if completion.startswith(word_before_cursor):
                yield Completion(completion, start_position=-len(word_before_cursor))



def return_city_name():
    """
    Returns the name of the city either what was typed or using a drop-down menu 
    consisting of a limited number of cities

    Arguments:
        No arguments needed

    Returns:
        json object containing the error status and the city name
    """

    try:
        # Create a PromptSession with the custom completer
        session = PromptSession(completer=MyCompleter())

        # Getting the city name from the user
        city_name = session.prompt("Enter a City name: ")

        # return the obtained city name
        return {"error": False, "city_name": city_name}
    except:
        return {"error": True, "message": "Error in getting the city name"}

    
