# sample_input_list=[1688018400,1687996800,1687986000]
from pprint import pprint
import inquirer
import datetime



def get_times_from_epochs(epochs : list):
    """
    Returns a list of times from epochs

    Arguments:
        epochs(list): List of epochs

    Returns:
        list: List of times
    """
    list_of_times=[]
    for epoch_time in epochs:
        date_conv = datetime.datetime.fromtimestamp(epoch_time)
        list_of_times.append(date_conv.strftime('%H:%M:%S'))
    return list_of_times

def find_epoch_with_chosen_time(answers : dict, epochs : list):
    """
    Finds the epoch with the chosen time

    Arguments:
        answers (dict): Dictionary containing the time
        epochs (list): List of epochs

    Returns:
        int: The epoch with the chosen time
    """
    for epoch in epochs:
        date_conv = datetime.datetime.fromtimestamp(epoch)
        if (date_conv.strftime('%H:%M:%S') == answers["Time"]):
            return epoch
        
def ask_for_preferred_time(epochs : list):
    """
    Enquires the user for their preferred time interactively

    Arguments:
        epochs (list): List of epochs

    Returns:
        dict: Dictionary containing the time
    """
    # print(epochs)
    list_of_times=get_times_from_epochs(epochs)
    questions = [
        inquirer.List(
            "Time",
            message="What time do you need the Weather for?",
            choices=list_of_times,
        ),
    ]

    answers = inquirer.prompt(questions)
    # pprint(type(answers))

    final_epoch=find_epoch_with_chosen_time(answers, epochs)
    # print(final_epoch)
    # print(type(final_epoch))

    return final_epoch

# ask_for_preferred_time(sample_input_list)