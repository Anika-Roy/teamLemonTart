import datetime

def get_unique_date_epoch(epochs : list):
    """
    Returns a list of unique date epochs from the list of epochs.

    Arguments:
        epochs (list): The list of epochs.

    Returns:
        list: The list of unique date epochs.
    """

    # Storing the list of unique date epochs
    unique_date_epochs = []

    # Iterating over the list of epochs
    for epoch in epochs:
        # Converting the epoch to a datetime object
        epoch_datetime = datetime.datetime.fromtimestamp(epoch)

        # Checking if the epoch_datetime is already present in the unique_date_epochs list
        if epoch_datetime.date() not in unique_date_epochs:
            # Appending the epoch_datetime to the unique_date_epochs list
            unique_date_epochs.append(epoch_datetime.date())

    # Convert the list of unique date epochs to a list of unique date epochs in epoch format
    unique_date_epochs = [int(datetime.datetime.combine(epoch, datetime.datetime.min.time()).timestamp()) for epoch in unique_date_epochs]

    # Returning the list of unique date epochs
    return unique_date_epochs

def get_epochs_with_date(epochs : list, date_epoch : int):
    """
    Filters list of epochs with the given date. It checks
    if the date corresponding to date_epoch also corresponds
    to the epoch in epochs.

    Arguments:
        epochs (list): The list of epochs.
        epoch_date (int): The epoch to filter the epochs with.
    """

    # Storing the list of epochs with the given date
    epochs_with_date = []

    # Converting the date_epoch to a datetime object
    date_to_check = datetime.datetime.fromtimestamp(date_epoch).date()

    # Iterating over the list of epochs
    for epoch in epochs:
        # Converting the epoch to a datetime object
        epoch_datetime = datetime.datetime.fromtimestamp(epoch)

        # Checking if the date_to_check is equal to the date of epoch_datetime
        if date_to_check == epoch_datetime.date():
            # Appending the epoch to the epochs_with_date list
            epochs_with_date.append(epoch)

    # Returning the list of epochs with the given date
    return epochs_with_date

def get_next_epoch(epochs : list,  curr_epoch : int):
    """
    Find the next largest epoch in the list of epochs.

    Arguments:
        epochs (list): The list of epochs.
        curr_epoch (int): The current epoch.

    Returns:
        int: The next largest epoch.
    """

    # Storing the next epoch
    next_epoch = None

    # Iterating over the list of epochs
    for epoch in epochs:
        # Checking if the epoch is greater than the curr_epoch
        if epoch > curr_epoch:
            # Checking if the next_epoch is None or not
            if next_epoch == None:
                # Assigning the epoch to the next_epoch
                next_epoch = epoch
            else:
                # Checking if the epoch is less than the next_epoch
                if epoch < next_epoch:
                    # Assigning the epoch to the next_epoch
                    next_epoch = epoch

    # Returning the next_epoch
    return next_epoch

def get_previous_epoch(epochs : list, curr_epoch : int):
    """
    Find the previous smallest epoch in the list of epochs.

    Arguments:
        epochs (list): The list of epochs.
        curr_epoch (int): The current epoch.

    Returns:
        int: The previous smallest epoch.
    """

    # Storing the previous epoch
    previous_epoch = None

    # Iterating over the list of epochs
    for epoch in epochs:
        # Checking if the epoch is less than the curr_epoch
        if epoch < curr_epoch:
            # Checking if the previous_epoch is None or not
            if previous_epoch == None:
                # Assigning the epoch to the previous_epoch
                previous_epoch = epoch
            else:
                # Checking if the epoch is greater than the previous_epoch
                if epoch > previous_epoch:
                    # Assigning the epoch to the previous_epoch
                    previous_epoch = epoch

    # Returning the previous_epoch
    return previous_epoch