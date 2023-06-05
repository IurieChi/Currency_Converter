# you need to install request pip3 install reqursts on mac and tkinter ,PIL


# create a window
import tkinter as tk
from tkinter import Frame, messagebox, Label
from PIL import ImageTk, Image


# window colors
col1 ="#FFFFFF" #white
col2 ="#333333" #black
col3 ="#80FF00" #red

window = tk.Tk()
window.geometry('400x450')
window.title('Curency Converter')
window.iconbitmap('curency64.ico')
window.configure(bg=col1)
window.resizable(width=False, height=False)

#create top frame 
top_frame = Frame(window, width=400, height = 65, bg= col3)
top_frame.grid(row=0, column=0)

img = Image.open('Curency/curency.ico')
img = img.resize((60,60)) 
img = ImageTk.PhotoImage(img)
app_name = Label (top_frame, image = img, compound='left', text="Curency Converter", padx= 40,  anchor= 'w' , font=('Arial 16 bold'), bg=col3, fg=col2)
app_name.place(x=0,y=0)

#Main frame


# result label
result = Label(window, text='',width=20,height=2, anchor= 'w', font=('Ivy 15 bold'),bg= col1, relief='solid')
result.place(x=50 , y=100)


if __name__ == "__main__":
    window.mainloop()
