from prompt_toolkit import PromptSession
from prompt_toolkit.completion import Completer, Completion
import requests
OPENWEATHERMAP_API_KEY="a35f0c612e92762a5f9f081e45cc3c3a"
# # Define your custom completer
# class MyCompleter(Completer):
#     def get_completions(self, document, complete_event):
#         # Implement your logic to provide completions
#         completions = ["command1", "command2", "option1", "option2"]
#         word_before_cursor = document.get_word_before_cursor()

#         for completion in completions:
#             if completion.startswith(word_before_cursor):
#                 yield Completion(completion, start_position=-len(word_before_cursor))

# # Create a PromptSession with the custom completer
# session = PromptSession(completer=MyCompleter())

# # Use the session to prompt and handle user input
# user_input = session.prompt("Enter a command: ")

# api call to get weather report
response=requests.get(f"https://api.openweathermap.org/data/2.5/forecast?lat=44.34&lon=10.99&appid={OPENWEATHERMAP_API_KEY}")
print(response.json())





