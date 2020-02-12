from tkinter import messagebox


import CONSTANTS as constants


def display_message(*messages, where_to_print=constants.PRINT_CONSOLE,
                    what_type=constants.MESSAGE_INFO):
    """
    Prints a message for the user on the console.

    Use instead of printing, if later printing messages needs to be changed

    Arguments:
        messages: To be printed to the user
        where_to_print: Where the output should be printed
        what_type: What type is the message

    Returns:
        None
    """

    text = ""
    for message in messages:
        text += message

    if where_to_print & constants.PRINT_CONSOLE == constants.PRINT_CONSOLE:
        if not constants.SUPPRESS_CONSOLE_PRINT:
            print(text)

    if where_to_print & constants.PRINT_MESSAGEBOX == \
            constants.PRINT_MESSAGEBOX:
        if what_type == constants.MESSAGE_ERROR:
            messagebox.showerror('Error', text)
        elif what_type == constants.MESSAGE_INFO:
            messagebox.showinfo("Info", text)
