import tkinter

import CONSTANTS

#
# class HelpMenuButton(tkinter.Button):
#     def __init__(self, master, label_texts):
#         self.label_texts = label_texts
#         super().__init__(master, text='Help', command=self.activate_help_text)
#         # self.setvar('text', 'Help')
#         # self.setvar('command', self.activate_help_text)
#
#     def activate_help_text(self):
#         help_dialog = HelpDialog(self.master, self.label_texts)
#         self.master.wait_window(help_dialog.top)
#


def get_help_menu_item(master, label_texts):
    return {'label': 'Help', 'command': lambda: _activate_help_text(
        master, label_texts)}


def _activate_help_text(master, label_texts):
    help_dialog = HelpDialog(master, label_texts)
    master.wait_window(help_dialog.top)


class HelpDialog:
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
        for label_text in label_texts:
            label = tkinter.Label(self.master, text=label_text,
                                  **label_text_configuration)
            label.grid(row=row, column=column, **grid_label_configurations)
            row += 1

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
        self.master.grab_release()
        self.master.destroy()
