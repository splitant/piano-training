try:
    import tkinter as tk
except:
    import Tkinter as tk

import controller as cont


class ManagerFrames(tk.Frame):
    def __init__(self, root=None):
        tk.Frame.__init__(self, root)
        self.root = root
        self.pack(side="top", fill="both", expand=True)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.controller = cont.ControllerChores()

        self.create_frames()

    def create_frames(self):
        self.frames = {}
        for F in (HomepageFrame, ChoreFrame, SettingsFrame):
            page_name = F.__name__
            frame = F(manager_frame=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("HomepageFrame")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class HomepageFrame(tk.Frame):
    def __init__(self, manager_frame):
        tk.Frame.__init__(self, manager_frame)
        self.manager_frame = manager_frame

        self.create_widgets()

    def create_widgets(self):
        self.container = tk.Frame(self.manager_frame)
        self.button_play = tk.Button(self.container, text="Play",
                                     fg="black", command=self.button_play_command)
        self.button_settings = tk.Button(self.container, text="Settings",
                                         fg="black", command=self.button_settings_command)

        self.button_play.grid(row=0, column=0, sticky='nesw', pady=10)
        self.button_settings.grid(row=1, column=0, sticky='nesw', pady=10)
        self.container.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def button_play_command(self):
        self.manager_frame.show_frame('ChoreFrame')

    def button_settings_command(self):
        self.manager_frame.show_frame('SettingsFrame')


class ChoreFrame(tk.Frame):
    def __init__(self, manager_frame):
        tk.Frame.__init__(self, manager_frame)
        self.manager_frame = manager_frame
        self.index = 0
        
        self.create_widgets()

    def create_widgets(self):
        self.container = tk.Frame(self.manager_frame)
        self.button_play = tk.Button(self.container, text="Play",
                                     fg="black", command=self.button_play_command)
        self.button_settings = tk.Button(self.container, text="Settings",
                                         fg="black", command=self.button_settings_command)

        self.button_play.grid(row=0, column=0, sticky='nesw', pady=10)
        self.button_settings.grid(row=1, column=0, sticky='nesw', pady=10)
        self.container.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def button_play_command(self):
        self.manager_frame.show_frame('ChoreFrame')

    def button_settings_command(self):
        self.manager_frame.show_frame('SettingsFrame')


class SettingsFrame(tk.Frame):
    def __init__(self, manager_frame):
        tk.Frame.__init__(self, manager_frame)
        self.manager_frame = manager_frame

        self.create_widgets()

    def create_widgets(self):
        self.container = tk.Frame(self.manager_frame)
        self.button_play = tk.Button(self.container, text="Play",
                                     fg="black", command=self.button_play_command)
        self.button_settings = tk.Button(self.container, text="Settings",
                                         fg="black", command=self.button_settings_command)

        self.button_play.grid(row=0, column=0, sticky='nesw', pady=10)
        self.button_settings.grid(row=1, column=0, sticky='nesw', pady=10)
        self.container.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def button_play_command(self):
        self.manager_frame.show_frame('ChoreFrame')

    def button_settings_command(self):
        self.manager_frame.show_frame('SettingsFrame')
