from tkinter import Tk, Label, Button, Radiobutton, filedialog
import tkinter

SELECTION_SINGLE_FILE = 'SINGLE_FILE'
SELECTION_MULTIPLE_FILES = 'MULTIPLE_FILES'


class TmxToVttPanel(tkinter.Frame):
    def __init__(self, master, *args, **kwargs):
        super(TmxToVttPanel, self).__init__(master, *args, **kwargs)
        self.master = master

        # -- Setup some decorations
        grid_configurations = {'padx': 5,
                               'pady': 5, }

        # -- Configure invisible items
        self.string_var_selected_radio = tkinter.StringVar()
        self.string_var_single_file = tkinter.\
            StringVar(self.master, value='Path to tmx file ...')
        self.string_var_multiple_files = tkinter.\
            StringVar(self.master, value='Path to directory ...')

        # -- Configure items for labeling and showing help
        

        # -- Configure items for selecting single file
        # -- Radio
        row = 0
        column = 0
        self.radio_single_file = Radiobutton(self.master,
                                             text='Single File',
                                             indicator=1,
                                             value=SELECTION_SINGLE_FILE,
                                             variable=self.
                                             string_var_selected_radio,
                                             command=self.radio_selection)
        self.radio_single_file.grid(row=row, column=column, sticky=tkinter.W,
                                    **grid_configurations)
        # -- Textbox
        column += 1
        self.textbox_single_file = tkinter. \
            Entry(self.master, textvariable=self.string_var_single_file, )
        self.textbox_single_file.grid(row=row, column=column, sticky='we',
                                      **grid_configurations)
        # -- Button
        column += 1
        self.button_browse_single_file = \
            tkinter.Button(self.master,
                           text="Browse",
                           command=self.browse_button_file_clicked)
        self.button_browse_single_file.grid(row=row, column=column,
                                            **grid_configurations)

        # -- Configure items for selecting directory
        # -- Radio
        row += 1
        column = 0
        self.radio_multiple_files = Radiobutton(self.master,
                                                text='Multiple Files',
                                                indicator=1,
                                                value=SELECTION_MULTIPLE_FILES,
                                                variable=
                                                self.string_var_selected_radio,
                                                command=self.radio_selection)
        self.radio_single_file.select()
        self.radio_multiple_files.grid(row=row, column=column, sticky=tkinter.W,
                                       **grid_configurations)
        # -- Textbox
        column += 1
        self.textbox_multiple_files = tkinter.\
            Entry(self.master, textvariable=self.string_var_multiple_files,
                  state=tkinter.DISABLED)
        self.textbox_multiple_files.grid(row=row, column=column, sticky='we',
                                         **grid_configurations)
        # -- Button
        column += 1
        self.button_browse_multiple_files = \
            tkinter.Button(self.master,
                           text="Browse",
                           command=self.browse_button_directory_clicked,
                           state=tkinter.DISABLED)
        self.button_browse_multiple_files.grid(row=row, column=column,
                                               **grid_configurations)

        #  -- Configure items for generating based on selection
        # -- Configure generate action
        row += 1
        column = 0
        self.button_generate = Button(self.master,
                                      text="Generate .vtt",
                                      command=self.generate_vtt)
        self.button_generate.grid(row=row, column=column,
                                  columnspan=3, **grid_configurations)

        self.master.columnconfigure(1, weight=2)

    def generate_vtt(self):
        print("Generate vtt")

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
