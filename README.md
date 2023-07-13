# Weather Forecasting Tool
## Team Details:
- [Anika Roy](https://www.linkedin.com/in/anika-roy-210379223/)
- [Ujjwal Shekhar](https://www.linkedin.com/in/ujjwal-shekhar-iiith/)

## A Short Demo:)



https://github.com/Anika-Roy/teamLemonTart/assets/102136135/6be9ae61-9725-49b8-a954-88849e6aa3fb




## Problem Statement

Create a command-line tool that accepts a city's name and returns the weather forecast. Leverage Open Weather Map API to get the weather forecast.
![Screenshot from 2023-06-24 09-31-41](https://github.com/Fastest-Coder-First/teamLemonTart/assets/102136135/041b4c28-5a69-4c74-9b3d-3d89984356c4)

## How to run:
1. Setup a conda/pip environment using the requirements.txt file provided
2. Activate the environment and cd into the project directory
3. run main.py using
     ```
     python3 main.py
     ```
5. Type out the name of the required city
6. If the city is amongst the hardcoded cities, it can be found in the drop-down (case sensitive, first letter should be capital). Otherwise, the full city name must be typed out to get a valid output
7. Use the left and right arrow keys to navigate the calendar shown. The forecast for only the next five days will be made available.
8. Use the up and down arrow keys to select the required time
9. And finally, you can see the required output!!
    
# Judging critrions satisfied
## Functionality and Completeness
> This section lists the features and highlights the points adhering to the judging criteria of `Functionality and Completeness`.

- CLI has an autocomplete feature to get the city name.
- CLI has an interactive interface to select the date of forecast.
- CLI has an interactive interface to select the time of forecast.
- A pretty-printed output is shown in the terminal.

## Github Copilot utilization
> This section is an explanation of how we used Github copilot to speedup our process of writing code.

- Almost all of our functions were autcompleted by Github Copilot.
- To do this, we declared functions and added docstrings below them. This allowed Copilot to be able to autogenerate the rest of the code.
- A lot of pretty printing and util functions were mostly written by Github Copilot. This saves a lot of time and grunt work that would otherwise be expensive.

## Code Quality and Readability
- Almost all of these functions have a docstring with them
- Almost every line of code has a comment preceding it, this also allowed Copilot to quickly autocomplete most lines of code (rarely requiring our intervention).
- We have followed proper variable naming conventions for Python.

## UI and UX
- We have used interactive features in the CLI to make it look pretty and increase ease of use.
- Easy to read output for the forecast is provided with a fun looking symbol for the weather.

## Error Handling and Validation
- Most functions return a json object containing the error message
- The main function is protected by a try-except clause that will catch the error and display the error message.

## Innovation and Creativity
- We have tried keeping the user in mind while making the forecast tool, adding autocomplete(prev version), option of choosing dates through calendars etc to make it more user-friendly. 
