try:
    import tkinter as tk
except:
    import Tkinter as tk

import view as v

if __name__ == "__main__":
    racine = tk.Tk()
    racine.title("Piano Training")
    racine.geometry("500x500")
    app = v.ManagerFrames(racine)
    racine.mainloop()
