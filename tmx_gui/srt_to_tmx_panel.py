from tkinter import Tk, Label, Button, Radiobutton, filedialog, messagebox
import tkinter

import CONSTANTS
from processors import tmx_processor
from tmx_gui import help_handles
from tmx_gui.help_handles import HelpDialog
from utilities import printing_utilities


SELECTION_SINGLE_FILE_PAIR = "SINGLE_PAIR"
SELECTION_DIRECTORY = 'DIRECTORY'


class SrtToTmxPanel:
    def __init__(self, master):
        self.master = self.top = tkinter.Toplevel(master)

        # -- Setup some decorations
        grid_configurations = CONSTANTS.GRID_CONFIGURATIONS

        # -- Configure invisible items
        self.string_var_single_file = tkinter.\
            StringVar(self.master, value='Path to tmx file ...')
        self.string_var_multiple_files = tkinter.\
            StringVar(self.master, value='Path to directory ...')
        self.string_var_target_language = tkinter.StringVar(self.master,
                                                            value="de")
        row = 0
        column = 0

        # -- Configure items for labeling and showing help
        label_help_text_single_pair = "Single Pair: Enter the path to a pair" \
                                      " of .srt files (source language file" \
                                      " and translation language file) that" \
                                      " you want to join into a single .tmx" \
                                      " file."
        label_help_text_multiple_files = "Multiple Files: Enter the path to" \
                                         " the directory where file pairs are" \
                                         " located to create .tmx files. The" \
                                         " files in the target directory" \
                                         " should be named the same, except" \
                                         " for the last three characters " \
                                         "which should be in the form of " \
                                         "'-XY' where XY is the abbreviation" \
                                         " for the source language and" \
                                         " translation language. In this" \
                                         " case, the translation language" \
                                         " is not needed because it will" \
                                         " be pulled off the translation" \
                                         " language file postfix."
        label_help_text_source_language = "Source Language: The abbreviation " \
                                          "of the source file language."
        label_help_text_translation_language = "Translation Language: " \
                                               "The abbreviation of the " \
                                               "language of the translation " \
                                               "file."
        # -- Configure menubar
        menubar = tkinter.Menu(self.master)
        menubar.\
            add_command(help_handles.
                        get_help_menu_item(self.master,
                                           [label_help_text_single_pair,
                                            label_help_text_multiple_files,
                                            label_help_text_source_language,
                                            label_help_text_translation_language
                                            ]
                                           ))
        self.master.config(menu=menubar)

        # Radiobutton string variable configuration
        self.string_var_selected_radio = tkinter.StringVar()
        self.string_var_selected_radio.set(SELECTION_SINGLE_FILE_PAIR)

        # Radio button for single file pair
        self.radio_single_pair = Radiobutton(self.master,
                                             text='Single Pair',
                                             indicator=1,
                                             value=SELECTION_SINGLE_FILE_PAIR,
                                             variable=self.
                                             string_var_selected_radio,
                                             command=self._radio_selection)
        self.radio_single_pair.grid(row=row, column=column, sticky=tkinter.W,
                                    **grid_configurations)

        # Configure frame for single pair components
        row += 1
        self.frame_single_pair = tkinter.Frame(self.master,
                                               highlightthickness=1,
                                               highlightbackground="black")
        self.frame_single_pair.grid(row=row, column=column, sticky='we',
                                    **grid_configurations,
                                    columnspan=2)

        # Configure Label for single pair source file
        inner_row = 0
        inner_column = 0
        self.label_single_pair_source_file = Label(
            self.frame_single_pair, text="Source file: "
        )
        self.label_single_pair_source_file.grid(row=inner_row,
                                                column=inner_column)
        # Configure entry for single pair source file
        self.string_var_single_pair = tkinter.StringVar()
        self.string_var_single_pair.set('Path to source .tmx file')
        inner_column += 1
        self.entry_single_pair_source_file = tkinter.Entry(
            self.frame_single_pair, textvariable=self.string_var_single_file
        )
        self.entry_single_pair_source_file.grid(row=inner_row,
                                                column=inner_column)
        # Configure browse single pair source file button
        inner_column += 1
        self.button_single_pair_source_file = Button(
            self.frame_single_pair, text="Browse",
            command=self._command_browse_single_file_source
        )
        self.button_single_pair_source_file.grid(row=inner_row,
                                                 column=inner_column)


        # Radio button for directory selection
        row += 1
        self.radio_single_pair = Radiobutton(self.master,
                                             text='Multiple Files',
                                             indicator=1,
                                             value=SELECTION_DIRECTORY,
                                             variable=self.
                                             string_var_selected_radio,
                                             command=self._radio_selection)
        self.radio_single_pair.grid(row=row, column=column, sticky=tkinter.W,
                                    **grid_configurations)


        # -- Configure exit button
        row += 1
        column = 0
        self.button_exit = Button(self.master, text="Back",
                                  command=self.close)
        self.button_exit.grid(row=row, column=column, **grid_configurations,
                              sticky='we')
        # -- Configure generate tmx file button
        column += 1
        self.button_generate = Button(self.master,
                                      text="Generate .tmx",
                                      command=self.generate_tmx)
        self.button_generate.grid(row=row, column=column,
                                  **grid_configurations,
                                  sticky='we')

        for idx in range(row):
            self.master.grid_rowconfigure(idx, weight=2)

        # -- Set modal and grab focus
        self.master.focus_set()
        self.master.grab_set()

    def _command_browse_single_file_source(self):
        pass

    def _radio_selection(self):
        selection = self.string_var_selected_radio.get()
        print(selection)
        if selection == SELECTION_SINGLE_FILE_PAIR:
            print('single pair')
        elif selection == SELECTION_DIRECTORY:
            print('directory')

    def generate_tmx(self):
        print('generate tmx')

    def close(self):
        self.master.grab_release()
        self.master.destroy()
