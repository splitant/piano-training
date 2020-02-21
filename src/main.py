try:
    import tkinter as tk
except:
    import Tkinter as tk

import view as v

if __name__ == "__main__":
    app = v.ManagerFrames()
    app.title("Piano Training")
    app.geometry("500x500")
    app.mainloop()
