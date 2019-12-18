try:
    import tkinter as tk
except:
    import Tkinter as tk

import view as v

if __name__ == "__main__":    
    racine = tk.Tk()
    racine.title("Piano Training")
    main_frame = tk.Frame(racine, width=300, height=300)
    main_frame.pack()
    app = v.ButtonsFrame(main_frame)
    racine.mainloop()
