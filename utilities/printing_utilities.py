

def display_message(*messages):
    """
    Prints a message for the user on the console.

    Use instead of printing, if later printing messages needs to be changed

    Arguments:
        messages: To be printed to the user

    Returns:
        None
    """
    for message in messages:
        print(message)
