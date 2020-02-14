try:
    import tkinter as tk
    from tkinter.ttk import Combobox
except:
    import Tkinter as tk
    from ttk import Combobox

from PIL import Image, ImageTk
import controller as cont
import threading as thr
import importlib as i

class ManagerFrames(tk.Frame):
    def __init__(self, root=None):
        tk.Frame.__init__(self, root)
        self.root = root
        self.controller = cont.ControllerChores()
        self.frames = {}

        self.pack(side="top", fill="both", expand=True)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.create_frames()

    def create_frames(self):
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
        self.chore_length = len(self.manager_frame.controller.choreMode.chores)
        self.timeout = self.manager_frame.controller.settings.timer

        self.create_widgets()

    def create_widgets(self):
        self.container = tk.Frame(self.manager_frame)

        chore_data_label = self.manager_frame.controller.choreMode.chores[self.index]
        chore_data_path_picture = self.manager_frame.controller.choreData[chore_data_label]

        self.label_chore = tk.Label(self.container, text=chore_data_label)
        self.picture_chore = ImageTk.PhotoImage(Image.open(chore_data_path_picture))
        self.label_picture_chore = tk.Label(self.container, image=self.picture_chore)

        self.label_chore.grid(row=0, column=0, sticky='nesw', pady=10)
        self.label_picture_chore.grid(row=1, column=0, sticky='nesw', pady=10)
        self.container.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def change_chore(self):
        self.index = self.index + 1

        if self.index < self.chore_length:
            chore_data_label = self.manager_frame.controller.choreMode.chores[self.index]
            chore_data_path_picture = self.manager_frame.controller.choreData[chore_data_label]
            
            self.label_chore.config(text=chore_data_label)
            self.picture_chore = ImageTk.PhotoImage(Image.open(chore_data_path_picture))
            self.label_picture_chore.config(image=self.picture_chore)
            
            timer = thr.Timer(self.timeout, self.change_chore)
            timer.start()
        else:
            self.manager_frame.show_frame('SettingsFrame')

class SettingsFrame(tk.Frame):
    def __init__(self, manager_frame):
        tk.Frame.__init__(self, manager_frame)
        self.manager_frame = manager_frame

        self.create_widgets()

    def create_widgets(self):
        self.container = tk.Frame(self.manager_frame)
        self.settings = self.manager_frame.controller.settings
        
        self.loop_var = tk.BooleanVar()
        self.loop_var.set(self.settings.loop)
        self.loop = tk.Checkbutton(
            self.container, text="loop", variable=self.loop_var)
        
        self.ordered_var = tk.BooleanVar()
        self.ordered_var.set(self.settings.ordered)
        self.ordered = tk.Checkbutton(
            self.container, text="ordered", variable=self.loop_var)

        self.timer_var = tk.IntVar()
        self.timer_var.set(self.settings.timer)
        self.timer = tk.Scale(
            self.container, orient='horizontal', from_=100, to=5000,
            resolution=100, length=350, variable=self.timer_var,
            label='Duration (ms)')

        module = i.import_module('mode.chores_mode')
        class_name_chore_modes = self.settings.availableModes()
        self.chore_modes = dict()
        for class_name_chore_mode in class_name_chore_modes:
            class_ = getattr(module, class_name_chore_mode)
            self.chore_modes[class_name_chore_mode] = class_.MODE
        self.mode_var = tk.StringVar()
        self.modes = Combobox(
            self.container, textvariable=self.mode_var, values=self.chore_modes.values())
        self.modes.current(0)

        self.container_source_file = tk.Frame(self.container)
        self.source_file_var = tk.StringVar()
        self.source_file_var.set(self.settings.sourceFile)
        self.source_file = tk.Entry(
            self.container_source_file, textvariable=self.source_file_var)
        self.source_file_button = tk.Button(self.container_source_file, text="Browse file",
                                            fg="black", command=self.get_filename_csv)

        self.source_file.grid(row=0, column=0, sticky='nesw', padx=5)
        self.source_file_button.grid(row=0, column=1, sticky='nesw', padx=5)

        self.container_buttons = tk.Frame(self.container)
        self.button_save = tk.Button(self.container_buttons, text="Save",
                                     fg="black", command=self.button_save_command)
        self.button_back = tk.Button(self.container_buttons, text="Back",
                                     fg="black", command=self.button_back_command)

        self.button_save.grid(row=0, column=0, sticky='nesw', padx=5)
        self.button_back.grid(row=0, column=1, sticky='nesw', padx=5)

        self.loop.grid(row=0, column=0, sticky='nesw', pady=10)
        self.ordered.grid(row=1, column=0, sticky='nesw', pady=10)
        self.timer.grid(row=2, column=0, sticky='nesw', pady=10)
        self.modes.grid(row=3, column=0, sticky='nesw', pady=10)
        self.container_source_file.grid(
            row=4, column=0, sticky='nesw', pady=10)
        self.container_buttons.grid(row=5, column=0, sticky='nesw', pady=10)
        self.container.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def button_save_command(self):
        error = self.validation()

        if len(error) > 0:
            tk.messagebox.showerror('Error', error)
        else:
            self.settings.loop = self.loop_var.get()
            self.settings.ordered = self.ordered_var.get()
            self.settings.timer = self.timer_var.get()
            self.settings.sourceFile = self.source_file_var.get()
            self.settings.mode = self.mode_var.get()
            self.settings.saveSettings()
            tk.messagebox.showinfo('Info', 'Settings updated.')

    def button_back_command(self):
        self.manager_frame.show_frame('HomepageFrame')
    
    def validation(self):
        if not self.source_file_var.get():
            return 'File entry must not empty !'
        
        return ''

    def get_filename_csv(self):
        filename = tk.filedialog.askopenfilename(
            title='Select file',
            initialdir='/',
            filetypes=[
                ("CSV Files", "*.csv"),
                ("All files", "*")
            ])
        self.source_file_var.set(filename)
        
