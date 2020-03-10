try:
    import tkinter as tk
except:
    import Tkinter as tk

import view as v

class PianoTrainingMain:
    def __init__(self):
        self.window = v.ManagerFrames()
        self.fullScreenState = False
        self.window.bind("<F11>", self.toggleFullScreen)
        self.window.bind("<Escape>", self.quitFullScreen)
        self.window.geometry('500x500')
        self.window.mainloop()

    def toggleFullScreen(self, event):
        self.fullScreenState = not self.fullScreenState
        self.window.attributes("-fullscreen", self.fullScreenState)

    def quitFullScreen(self, event):
        self.fullScreenState = False
        self.window.attributes("-fullscreen", self.fullScreenState)

if __name__ == "__main__":
    app = PianoTrainingMain()

