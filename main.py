# you need to install request pip3 install reqursts on mac and tkinter


# create a window
import tkinter as tk
from tkinter import messagebox


# window colors
col1 ="#FFFFFF" #white
col2 ="#333333" #black
col3 ="EB5D51" #red

window = tk.Tk()
window.geometry('300x320')
window.title('Curency Converter')
window.configure(bg=col1)
window.resizable(width=False, height=False)

if __name__ == "__main__":
    window.mainloop()
