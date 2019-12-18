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
        self.button_play = tk.Button(self, text="Play",
                                     fg="grey", command=self.quit)
        self.button_settings = tk.Button(self, text="Settings",
                                         fg="grey", command=self.quit)
        
        self.button_play.grid(row=0)
        self.button_settings.grid(row=1)
        self.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.pack()
    


