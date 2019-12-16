try:
    import tkinter as tk
except:
    import Tkinter as tk


class ButtonsFrame(tk.Frame):
    def __init__(self, racine=None):
        tk.Frame.__init__(self, racine)
        self.racine = racine
        self.create_widgets()

    def create_widgets(self):
        self.button_play = tk.Button(self.racine, text="Play",
                                     fg="grey", command=self.quit)
        self.button_settings = tk.Button(self.racine, text="Settings",
                                         fg="grey", command=self.quit)
        self.button_play.pack()
        self.button_settings.pack()


