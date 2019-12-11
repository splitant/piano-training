# coding: utf-8

import tkinter as tk

class Application(tk.Frame):
    def __init__(self, racine=None):
        tk.Frame.__init__(self, racine)
        self.racine = racine
        self.create_widgets()

    def create_widgets(self):
        self.button_play = tk.Button(self.racine, text="Play",
                                 fg="white", command=self.quit)
        self.button_settings = tk.Button(self.racine, text="Settings",
                                 fg="white", command=self.quit)
        self.button_play.pack()
        self.button_settings.pack()

if __name__ == "__main__":
    racine = tk.Tk()
    racine.title("Piano Training")
    app = Application(racine)
    racine.mainloop()