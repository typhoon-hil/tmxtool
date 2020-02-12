import tkinter

import CONSTANTS


def get_help_menu_item(master, label_texts):
    """
    Returns an object in the form that the menu item wants (Dict cell)

    Arguments:
        master: the master component that holds this item
        label_texts: Text that the help menu will show when clicked

    Returns:
        A help menu item formatted with a label and command.
    """
    return {'label': 'Help', 'command': lambda: _activate_help_text(
        master, label_texts)}


def _activate_help_text(master, label_texts):
    """
    Function that shows a help dialog.

    Arguments:
        master: The master component that holds the dialog.
        label_texts: The text that the Help dialog will present.

    Returns:
        None
    """
    help_dialog = HelpDialog(master, label_texts)
    master.wait_window(help_dialog.top)


class HelpDialog:
    """
    Class that shows help text for some component.

    Arguments:
        master: The component that holds this dialog
        label_texts: Text that the dialog will show
    """
    def __init__(self, master, label_texts: []):
        self.master = self.top = tkinter.Toplevel(master)

        # -- Setup some decorations
        grid_configurations = CONSTANTS.GRID_CONFIGURATIONS.copy()
        grid_configurations.update({'sticky': 'we'})

        row = 0
        column = 0
        grid_label_configurations = {
            'columnspan': 3,
            'padx': 10,
            'pady': 0,
            'sticky': 'we'
        }
        label_text_configuration = {
            'justify': tkinter.LEFT,
            'wraplength': CONSTANTS.WINDOW_WIDTH + 200
        }
        # -- Generate the labels for the dialog
        for label_text in label_texts:
            label = tkinter.Label(self.master, text=label_text,
                                  **label_text_configuration)
            label.grid(row=row, column=column, **grid_label_configurations)
            row += 1

        # -- Make OK button
        self.button_ok = tkinter.Button(self.master, text='OK',
                                        command=self.close)
        button_grid_config = grid_configurations.copy()
        button_grid_config['padx'] = 200
        self.button_ok.grid(row=row, column=column, **button_grid_config)
        self.master.grid_columnconfigure(column, weight=1)

        # -- Set modal and grab focus
        self.master.focus_set()
        self.master.grab_set()

    def close(self):
        """
        Closes the dialog and returns focus to master component.

        Returns:
            None
        """
        self.master.grab_release()
        self.master.destroy()
