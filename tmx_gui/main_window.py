from tkinter import Tk, Button, Frame

import CONSTANTS
import CONSTANTS as const
from tmx_gui.srt_to_tmx_panel import SrtToTmxPanel
from tmx_gui.tmx_to_vtt_panel import TmxToVttPanel


class MainWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        # -- Shorthand for grid configurations - add to all grid configs
        gc = CONSTANTS.GRID_CONFIGURATIONS.copy()
        gc.update({'sticky': 'we'})

        master.title("Linguist Support")

        # -- Create buttons
        self.button_generate_tmx = Button(self.master,
                                          text="Generate .tmx",
                                          command=lambda: self.open_window(
                                              const.WINDOW_GENERATE_TMX))
        self.button_generate_vtt = Button(self.master,
                                          text="Generate .vtt",
                                          command=lambda: self.open_window(
                                              const.WINDOW_GENERATE_VTT))
        self.button_about = Button(self.master,
                                   text="About",
                                   command=lambda: self.open_window(
                                       const.WINDOW_ABOUT
                                   ))
        self.button_exit = Button(self.master,
                                  text="Exit",
                                  command=lambda: exit(0))

        row = 0
        column = 0
        self.button_generate_tmx.grid(row=row, column=column, **gc)
        self.master.grid_rowconfigure(row, weight=2)
        row += 1
        self.button_generate_vtt.grid(row=row, column=column, **gc)
        self.master.grid_rowconfigure(row, weight=2)
        row += 1
        self.button_about.grid(row=row, column=column, **gc)
        self.master.grid_rowconfigure(row, weight=2)
        row += 1
        self.button_exit.grid(row=row, column=column, **gc)
        self.master.grid_rowconfigure(row, weight=2)

        self.master.grid_columnconfigure(0, weight=2)
        self.master.grid_rowconfigure(row, weight=2)

    def open_window(self, window_flag):
        if window_flag == const.WINDOW_GENERATE_TMX:
            dialog = SrtToTmxPanel(self.master)
            self.master.wait_window(dialog.top)
        elif window_flag == const.WINDOW_GENERATE_VTT:
            dialog = TmxToVttPanel(self.master)
            self.master.wait_window(dialog.top)


if __name__ == '__main__':
    root = Tk()
    root.geometry(str(const.WINDOW_WIDTH) + "x" + str(const.WINDOW_HEIGHT))

    my_gui = MainWindow(root, width=400)

    root.mainloop()
