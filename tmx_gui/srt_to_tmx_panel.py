from tkinter import Tk, Label, Button, Radiobutton, filedialog, messagebox
import tkinter

import CONSTANTS
from processors import tmx_processor
from tmx_gui import help_handles
from tmx_gui.help_handles import HelpDialog
from utilities import printing_utilities

SELECTION_SINGLE_FILE = 'SINGLE_FILE'
SELECTION_MULTIPLE_FILES = 'MULTIPLE_FILES'


"""
        column += 1
        self.help_button = HelpButton(self.master,
                                      [label_help_text_single_pair,
                                       label_help_text_multiple_files,
                                       label_help_text_source_language,
                                       label_help_text_translation_language])
        self.help_button.grid(row=row, column=column,
                              **grid_configurations, sticky='we')
        qrf()
"""

class SrtToTmxPanel:
    def __init__(self, master):
        self.master = self.top = tkinter.Toplevel(master)

        # -- Setup some decorations
        grid_configurations = CONSTANTS.GRID_CONFIGURATIONS

        # -- Configure invisible items
        self.string_var_selected_radio = tkinter.StringVar()
        self.string_var_single_file = tkinter.\
            StringVar(self.master, value='Path to tmx file ...')
        self.string_var_multiple_files = tkinter.\
            StringVar(self.master, value='Path to directory ...')
        self.string_var_target_language = tkinter.StringVar(self.master,
                                                            value="de")

        def quick_row_config():
            self.master.grid_rowconfigure(row, weight=2)
        qrf = quick_row_config

        # -- Configure items for labeling and showing help
        row = 0
        column = 0
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
        menubar.add_command(
            help_handles.get_help_menu_item(self.master,
                                            [label_help_text_single_pair,
                                             label_help_text_multiple_files,
                                             label_help_text_source_language,
                                             label_help_text_translation_language]
                                            ))
        self.master.config(menu=menubar)

        # -- Configure items for selecting single file
        # -- Radio
        self.radio_single_file = Radiobutton(self.master,
                                             text='Single File',
                                             indicator=1,
                                             value=SELECTION_SINGLE_FILE,
                                             variable=self.
                                             string_var_selected_radio,
                                             command=self.radio_selection)
        self.radio_single_file.grid(row=row, column=column, sticky=tkinter.W,
                                    **grid_configurations)
        qrf()
        # -- Textbox
        column += 1
        self.textbox_single_file = tkinter. \
            Entry(self.master, textvariable=self.string_var_single_file, )
        self.textbox_single_file.grid(row=row, column=column, sticky='we',
                                      **grid_configurations)
        qrf()
        # -- Button
        column += 1
        self.button_browse_single_file = \
            tkinter.Button(self.master,
                           text="Browse",
                           command=self.browse_button_file_clicked)
        self.button_browse_single_file.grid(row=row, column=column,
                                            **grid_configurations, sticky='we')
        qrf()

        # -- Configure items for selecting directory
        # -- Radio
        row += 1
        column = 0
        self.radio_multiple_files = Radiobutton(self.master,
                                                text='Multiple Files',
                                                indicator=1,
                                                value=SELECTION_MULTIPLE_FILES,
                                                variable=self.
                                                string_var_selected_radio,
                                                command=self.radio_selection)
        self.radio_single_file.select()
        self.radio_multiple_files.grid(row=row, column=column, sticky=tkinter.W,
                                       **grid_configurations)
        qrf()
        # -- Textbox
        column += 1
        self.textbox_multiple_files = tkinter.\
            Entry(self.master, textvariable=self.string_var_multiple_files,
                  state=tkinter.DISABLED)
        self.textbox_multiple_files.grid(row=row, column=column, sticky='we',
                                         **grid_configurations)
        qrf()
        # -- Button
        column += 1
        self.button_browse_multiple_files = \
            tkinter.Button(self.master,
                           text="Browse",
                           command=self.browse_button_directory_clicked,
                           state=tkinter.DISABLED)
        self.button_browse_multiple_files.grid(row=row, column=column,
                                               **grid_configurations,
                                               sticky='we')
        qrf()

        # -- Configure selection of target language
        row += 1
        column = 0
        self.label_target_language = Label(self.master, text="Target Language:")
        self.label_target_language.grid(row=row, column=column,
                                        **grid_configurations)
        column += 1
        self.entry_target_language = tkinter.\
            Entry(self.master, textvariable=self.string_var_target_language)
        self.entry_target_language.grid(row=row, column=column, sticky='we',
                                        **grid_configurations, columnspan=2)
        qrf()

        #  -- Configure items for generating based on selection and exiting
        # -- Configure generate action
        row += 1
        column = 0
        self.button_exit = Button(self.master, text="Back",
                                  command=self.close)
        self.button_exit.grid(row=row, column=column, **grid_configurations,
                              sticky='we')
        qrf()
        column += 1
        self.button_generate = Button(self.master,
                                      text="Generate .vtt",
                                      command=self.generate_vtt)
        self.button_generate.grid(row=row, column=column,
                                  columnspan=2, **grid_configurations,
                                  sticky='we')
        qrf()

        self.master.columnconfigure(1, weight=2)

        # -- Set modal and grab focus
        self.master.focus_set()
        self.master.grab_set()

    def close(self):
        self.master.grab_release()
        self.master.destroy()

    def generate_vtt(self):
        selection = self.string_var_selected_radio.get()
        if selection == SELECTION_MULTIPLE_FILES:
            path = self.string_var_multiple_files.get()
        else:
            path = self.string_var_single_file.get()
        lang = self.string_var_target_language.get()
        path = tmx_processor.process_tmx_file((path, lang))
        printing_utilities.display_message(
            "Result saved to: [" + path + "]",
            where_to_print=CONSTANTS.PRINT_MESSAGEBOX
        )

    def radio_selection(self):
        selection = self.string_var_selected_radio.get()

        if selection == SELECTION_MULTIPLE_FILES:
            self.button_browse_multiple_files.configure(state=tkinter.NORMAL)
            self.button_browse_single_file.configure(state=tkinter.DISABLED)
            self.textbox_multiple_files.configure(state=tkinter.NORMAL)
            self.textbox_single_file.configure(state=tkinter.DISABLED)
        else:
            self.button_browse_multiple_files.configure(state=tkinter.DISABLED)
            self.button_browse_single_file.configure(state=tkinter.NORMAL)
            self.textbox_multiple_files.configure(state=tkinter.DISABLED)
            self.textbox_single_file.configure(state=tkinter.NORMAL)

    def browse_button_directory_clicked(self):
        dirname = filedialog.askdirectory(initialdir="/",
                                          title="Select a directory")
        self.string_var_multiple_files.set(dirname)

    def browse_button_file_clicked(self):
        filename = filedialog.askopenfilename(initialdir="/",
                                              title="Select .tmx File",
                                              filetype=(("tmx files", "*.tmx"),
                                                        ("all files", "*.*")))
        self.string_var_single_file.set(filename)