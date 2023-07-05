# Import the list of cities
from utils.constants import CITY_LIST
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import Completer, Completion

# Define your custom completer
class MyCompleter(Completer):
    def get_completions(self, document, complete_event):
        # Implement your logic to provide completions
        completions = CITY_LIST
        word_before_cursor = document.get_word_before_cursor()

        for completion in completions:
            if completion.startswith(word_before_cursor):
                yield Completion(completion, start_position=-len(word_before_cursor))



def return_city_name():
    """
    Returns the name of the city using autocomplete

    Arguments:
        No arguments needed

    Returns:
        string: The name of the city
    """

    # Create a PromptSession with the custom completer
    session = PromptSession(completer=MyCompleter())

    # Getting the city name from the user
    city_name = session.prompt("Enter a City name: ")

    # Error handling
    if city_name in CITY_LIST:
        # Returning the city name
        return {"error": False, "city_name": city_name}
        
    else:
        # Returning a json with error : False
        return {"error": False, "city_name": city_name}
    
