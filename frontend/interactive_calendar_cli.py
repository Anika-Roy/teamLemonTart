# Make an interactive calendar display on the CLI
# It will display the current month and allow the user to
# navigate to other months

import calendar
import datetime


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

    return {"error": False, "message": "All OK.", "calendar": calendar_text}
