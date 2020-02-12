from tkinter import Tk, Label, Button, Radiobutton, filedialog, messagebox
import tkinter

import CONSTANTS
from processors import tmx_processor
from tmx_gui import help_handles
from utilities import printing_utilities, error_manager

SELECTION_SINGLE_FILE = 'SINGLE_FILE'
SELECTION_MULTIPLE_FILES = 'MULTIPLE_FILES'


class TmxToVttPanel:
    def __init__(self, master):
        self.master = self.top = tkinter.Toplevel(master)

        # -- Setup some decorations
        grid_configurations = CONSTANTS.GRID_CONFIGURATIONS

        # -- Configure invisible items
        self.string_var_selected_radio = tkinter.StringVar()
        self.string_var_selected_radio.set(SELECTION_SINGLE_FILE)
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
        label_help_text_single_file = "Single File: Choose from which " \
                                      "specific .tmx file you want " \
                                      "to create a .vtt."
        label_help_text_multiple_files = "Multiple Files: Choose a directory" \
                                         " from which you want to scan for" \
                                         " .tmx files and create .vtt files."
        label_help_text_lang = "Target Language: Enter the target language" \
                               " you want to extract form the .tmx file(s)" \
                               " and place into the resulting .vtt file(s)."

        # -- Configure menubar
        menubar = tkinter.Menu(self.master)
        menubar.add_command(
            help_handles.get_help_menu_item(self.master,
                                            [label_help_text_single_file,
                                             label_help_text_multiple_files,
                                             label_help_text_lang]
                                            ))
        self.master.config(menu=menubar)

        # -- Configure items for selecting single file
        self.string_var_selected_radio = tkinter.StringVar()
        self.string_var_selected_radio.set(SELECTION_SINGLE_FILE)

        # -- Radio for single file pair
        self.radio_single_file = Radiobutton(self.master,
                                             text='Single File',
                                             indicator=1,
                                             value=SELECTION_SINGLE_FILE,
                                             variable=self.
                                             string_var_selected_radio,
                                             command=self._radio_selection)
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
                           command=self._browse_button_file_clicked)
        self.button_browse_single_file.grid(row=row, column=column,
                                            **grid_configurations)
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
                                                command=self._radio_selection)
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
                           command=self._browse_button_directory_clicked,
                           state=tkinter.DISABLED)
        self.button_browse_multiple_files.grid(row=row, column=column,
                                               **grid_configurations)
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
                                  command=self._close)
        self.button_exit.grid(row=row, column=column, **grid_configurations,
                              sticky='we')
        qrf()
        column += 1
        self.button_generate = Button(self.master,
                                      text="Generate .vtt",
                                      command=self._generate_vtt)
        self.button_generate.grid(row=row, column=column,
                                  columnspan=2, **grid_configurations,
                                  sticky='we')
        qrf()

        self.master.columnconfigure(1, weight=2)

        # -- Set modal and grab focus
        self.master.focus_set()
        self.master.grab_set()

    def _close(self):
        self.master.grab_release()
        self.master.destroy()

    def _generate_vtt(self):
        selection = self.string_var_selected_radio.get()
        if selection == SELECTION_MULTIPLE_FILES:
            path = self.string_var_multiple_files.get()
        else:
            path = self.string_var_single_file.get()
        lang = self.string_var_target_language.get()

        error_manager.clean_warning_buffer()
        path = tmx_processor.process_tmx_file((path, lang))
        warnings = error_manager.fetch_warning_buffer()

        text = "Results saved to : [" + path + "]"
        if len(warnings) != 0:
            text += "Warnings encountered: \n"
            text += warnings
        messagebox.showinfo('Complete', text)

    def _radio_selection(self):
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

    def _browse_button_directory_clicked(self):
        dir_name = filedialog.askdirectory(initialdir="/",
                                           title="Select a directory")
        self.string_var_multiple_files.set(dir_name)

    def _browse_button_file_clicked(self):
        filename = filedialog.askopenfilename(initialdir="/",
                                              title="Select .tmx File",
                                              filetype=(("tmx files", "*.tmx"),
                                                        ("all files", "*.*")))
        self.string_var_single_file.set(filename)
