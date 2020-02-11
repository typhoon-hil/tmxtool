from tkinter import Tk, Label, Button, Radiobutton, filedialog, messagebox
import tkinter

from processors import tmx_processor

SELECTION_SINGLE_FILE = 'SINGLE_FILE'
SELECTION_MULTIPLE_FILES = 'MULTIPLE_FILES'


class TmxToVttPanel:
    def __init__(self, master):
        self.master = self.top = tkinter.Toplevel(master)

        # -- Setup some decorations
        grid_configurations = {'padx': 5,
                               'pady': 5, }

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
        label_help_text_single_file = "Single File: Choose from which " \
                                      "specific .tmx file you want " \
                                      "to create a .vtt."
        label_help_text_multiple_files = "Multiple Files: Choose a directory" \
                                         " from which you want to scan for" \
                                         " .tmx files and create .vtt files."
        label_help_text_lang = "Target Language: Enter the target language" \
                               " you want to extract form the .tmx file(s)" \
                               " and place into the resulting .vtt file(s)."

        grid_label_configurations = {
            'columnspan': 3,
            'padx': 10,
            'pady': 0,
            'sticky': 'we'
        }
        self.label_help_single_file = Label(self.master,
                                            text=label_help_text_single_file)
        self.label_help_single_file.grid(row=row, column=column,
                                         **grid_label_configurations)
        qrf()
        row += 1
        self.label_help_multiple_files = \
            Label(self.master,text=label_help_text_multiple_files)
        self.label_help_multiple_files.grid(row=row, column=column,
                                            **grid_label_configurations)
        qrf()
        row += 1
        self.label_help_language = Label(self.master, text=label_help_text_lang)
        self.label_help_language.grid(row=row, column=column,
                                      **grid_label_configurations)
        qrf()

        # -- Configure items for selecting single file
        # -- Radio
        row += 1
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
        lang = self.string_var_target_language
        path = tmx_processor.process_tmx_file((path, lang))
        messagebox.showinfo("Tmx to Vtt", "File saved to: [" + path + "]")

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