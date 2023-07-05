import calendar
import datetime
import click

import utils.epoch_handlers
import time

def shift_cursor_position(lines_up, lines_down):
    # ANSI escape sequence to move cursor up or down
    if lines_up > 0:
        print("\033[{}A".format(lines_up), end='')
    elif lines_down > 0:
        print("\033[{}B".format(lines_down), end='')

def get_calendar_from_epochs(epochs : list, highlight_epoch : int):
    """
    This returns a calendar object that represents the
    calendar for the given epochs.

    Arguments:
        epochs (list): A list of epoch timestamps.
        highlight_epoch (int): The date to highlight.

    Returns:
        calendar: The calendar object.
    """

    # Check if the epochs_list is empty
    if len(epochs) == 0:
        # Return a json with error : True
        return {"error": True, "message": "The epochs list is empty."}
    
    # Assign the highlight date a default value of epochs[0]
    # Or, check if the highlight date is present in epochs
    if highlight_epoch == None:
        highlight_epoch = epochs[0]
    else:
        if highlight_epoch not in epochs:
            # Return a json with error : True
            return {"error": True, "message": "The highlight epoch is not present in the epochs list."}

    # Get the datetime from epoch
    highlight_date = datetime.datetime.fromtimestamp(highlight_epoch)

    # Get the month and year
    highlight_month = highlight_date.month
    highlight_year = highlight_date.year

    # Create a calendar object
    cal = calendar.TextCalendar()

    # To Change color of the highligh_date cell

    # Create a list of the calendar lines
    calendar_lines = cal.formatmonth(highlight_year, highlight_month).split("\n")

    # Iterate over the calendar lines and every sublist
    for i in range(int(len(calendar_lines))):
        if (i <= 1) or (i >= len(calendar_lines) - 1):
            continue
        
        # Iterate over the calendar lines split by whitespace
        # replace the highlighted date with the ANSI code
        for j in range(len(calendar_lines[i].split())):
            if calendar_lines[i].split()[j] == str(highlight_date.day):
                calendar_lines[i] = calendar_lines[i].replace(str(highlight_date.day), "\033[7m" + str(highlight_date.day) + "\033[0m")

    # Join the calendar_lines to form the calendar_text
    calendar_text = "\n".join(calendar_lines)

    # Get the highlighted date 


    return {"error": False, "message": "All OK.", "calendar": calendar_text}

def get_user_input_calendar(epochs : list, highlight_epoch : int):
    """
    Refreshes the terminal to display the calendar and highlights the 
    selected epoch. If the user clicks on the right arrow key (If present), 
    the calendar is refreshed to the epoch present after the highlighted
    epoch. If the user clicks on the left arrow key, the calendar is
    refreshed to the epoch present before the highlighted epoch (If 
    present).

    Arguments:
        epochs (list): A list of epoch timestamps.
        highlight_epoch (int): The date to highlight.

    Returns:
        int: The epoch selected by the user.
    """

    shift_cursor_position(lines_up=0, lines_down=1)
    click.echo("Please press the arrow keys to navigate the calendar.")
    click.echo("Press 's' to Select and move forward.")

    shift_cursor_position(lines_up=0, lines_down=2)

    # Set the highlight_epoch to first epoch if it is None
    if highlight_epoch == None:
        highlight_epoch = epochs[0]

    # Get the calendar from the epochs
    calendar = get_calendar_from_epochs(epochs, highlight_epoch)

    # Check if there was an error
    if calendar["error"]:
        # Return the error
        return calendar
    
    # Print the calendar
    click.echo(calendar["calendar"])

    # Get the user input
    user_input = click.getchar()

    # Check if the user wants to quit
    if (user_input == "s") or (user_input == "S") or (user_input != "\x1b[C" and user_input != "\x1b[D"):
        # Return the highlight_epoch
        return highlight_epoch
    
    # Check if the user wants to go to the next epoch
    if user_input == "\x1b[C":
        # Get the next epoch
        next_epoch = utils.epoch_handlers.get_next_epoch(epochs, highlight_epoch)

        # # Check if there was an error
        # if next_epoch["error"]:
        #     # Return the error
        #     return next_epoch
        
        # Refresh the calendar
        shift_cursor_position(lines_up=14, lines_down=0)
        return get_user_input_calendar(epochs, next_epoch)
    
    # Check if the user wants to go to the previous epoch
    if user_input == "\x1b[D":
        # Get the previous epoch
        previous_epoch = utils.epoch_handlers.get_previous_epoch(epochs, highlight_epoch)

        # # Check if there was an error
        # if previous_epoch["error"]:
        #     # Return the error
        #     return previous_epoch
        
        # Refresh the calendar
        shift_cursor_position(lines_up=14, lines_down=0)
        return get_user_input_calendar(epochs, previous_epoch)
    
def get_normal_user_input(epochs : list, highlight_epoch : int):
    """
    Prints the calendar and highlights the selected epoch. If the user
    enter "+" then it will move the highlighted epoch to the next epoch.
    If the user enters "-" then it will move the highlighted epoch to
    the previous epoch.

    Then the user can type in "done" to select the highlighted epoch.

    Arguments:
        epochs (list): A list of epoch timestamps.
        highlight_epoch (int): The date to highlight.
 
    """
    while (True):
        # Get the calendar from the epochs
        calendar = get_calendar_from_epochs(epochs, highlight_epoch)

        # Check if there was an error
        if calendar["error"]:
            # Return the error
            return calendar
        
        # Print the calendar
        click.echo(calendar["calendar"])

        # Get the user input
        user_input = click.prompt("Please enter the epoch to select or enter '+' or '-' to move the highlighted epoch or enter 'done' to select the highlighted epoch.")

        # Check if the user wants to quit
        if user_input == "done":
            # Return the highlight_epoch
            return highlight_epoch
        
        # Check if the user wants to go to the next epoch
        if user_input == "+":
            # Get the next epoch
            next_epoch = utils.epoch_handlers.get_next_epoch(epochs, highlight_epoch)

            # Check if there was an error
            if next_epoch["error"]:
                # Return the error
                return next_epoch
            
            # Refresh the calendar
            highlight_epoch = next_epoch["epoch"]
            continue
        
        # Check if the user wants to go to the previous epoch
        if user_input == "-":
            # Get the previous epoch
            previous_epoch = utils.epoch_handlers.get_previous_epoch(epochs, highlight_epoch)

            # Check if there was an error
            if previous_epoch["error"]:
                # Return the error
                return previous_epoch
            
            # Refresh the calendar
            highlight_epoch = previous_epoch["epoch"]
            continue
        
        # Check if the user wants to select the epoch
        if user_input.isnumeric():
            # Check if the epoch is present in the epochs
            if int(user_input) in epochs:
                # Return the epoch
                return int(user_input)
            else:
                # Return an error
                return {"error": True, "message": "The epoch is not present in the epochs list."}
        
        # Return an error
        return {"error": True, "message": "The user input is not valid."}