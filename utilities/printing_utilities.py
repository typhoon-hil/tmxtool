from tkinter import messagebox

import CONSTANTS as constants


def display_message(*messages, where_to_print=constants.PRINT_CONSOLE):
    """
    Prints a message for the user on the console.

    Use instead of printing, if later printing messages needs to be changed

    Arguments:
        messages: To be printed to the user

    Returns:
        None
    """
    if constants.SUPPRESS_PRINT:
        return

    text = ""
    for message in messages:
        text += message

    if where_to_print == constants.PRINT_CONSOLE:
        print(text)
    elif where_to_print == constants.PRINT_MESSAGEBOX:
        messagebox.showinfo("Info", text)
