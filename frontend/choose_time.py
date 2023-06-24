sample_input_list=[1688018400,1687996800,1687986000]
from pprint import pprint
import inquirer
import datetime



def get_times_from_epochs(input_list_of_epochs):
    list_of_times=[]
    for epoch_time in input_list_of_epochs:
        date_conv = datetime.datetime.fromtimestamp(epoch_time)
        list_of_times.append(date_conv.strftime('%H:%M:%S'))
    return list_of_times


def ask_for_preferred_time(input_list_of_epochs):
    list_of_times=get_times_from_epochs(input_list_of_epochs)
    questions = [
        inquirer.List(
            "Time",
            message="What time do you need the Weather for?",
            choices=list_of_times,
        ),
    ]
# questions = [
#     inquirer.List(
#         "size",
#         message="What size do you need?",
#         choices=["Jumbo", "Large", "Standard", "Medium", "Small", "Micro"],
#     ),
# ]

    answers = inquirer.prompt(questions)
    pprint(answers)

ask_for_preferred_time(sample_input_list)