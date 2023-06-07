# you need to install request pip3 install reqursts on mac and tkinter ,PIL


# create a window
import tkinter as tk
from tkinter import Frame, messagebox, Label, ttk, Entry, Button
from PIL import ImageTk, Image


# window colors
col1 ="#FFFFFF" #white
col2 ="#333333" #black
col3 ="#80FF00" #green

window = tk.Tk()
window.geometry('350x400')
window.title('Curency Converter')
window.iconbitmap('curency64.ico')
window.configure(bg=col1)
window.resizable(width=False, height=False)

#create top frame 
top_frame = Frame(window, width=350, height = 65, bg= col3)
top_frame.grid(row=0, column=0)

img = Image.open('curency.ico')
img = img.resize((60,60)) 
img = ImageTk.PhotoImage(img)
app_name = Label (top_frame, image = img, compound='left', text="Curency Converter", padx= 40,  anchor= 'w' , font=('Arial 16 bold'), bg=col3, fg=col2)
app_name.place(x=0,y=0)

# Currensy list
currency = ['USD','EUR','SEK','DKK','GBP','CHF','JPY','CAD','ISK','AUD']

#Main frame

from_lable = Label(text='From', width=8, height= 1, padx=0, pady=0, relief= 'flat', anchor= 'nw', font= ('Iwy 15 bold'), bg= col1, fg= col2)
from_lable.place(x= 50, y= 80)
to_lable = Label(text='To', width=8, height= 1, padx=0, pady=0, relief= 'flat', anchor= 'nw', font= ('Iwy 15 bold'), bg= col1, fg= col2)
to_lable.place(x= 200, y= 80)

combo_from = ttk.Combobox(window, width=5, justify='center', font= ('Iwy 15 bold'))  
combo_from['values']= (currency)
combo_from.place(x= 50, y=100)

combo_to = ttk.Combobox(window, width=5, justify='center', font=('Iwy 15 bold'))  
combo_to['values']= (currency)
combo_to.place(x= 200, y=100)

value = Entry(window, width=20, justify= 'center', font=('Iwy 15 bold'), relief='solid')
value.place(x=50, y=150)

button = Button(window, text='Convert', width=18, height=1, bg= col2, fg= col2, font=('Iwy 15 bold'), relief='solid')
button.place(x=50, y=200)

# result label
result = Label(window, text='',width=20,height=2, anchor= 'w', font=('Ivy 15 bold'),bg= col1, relief='solid')
result.place(x=50, y=270)


if __name__ == "__main__":
    window.mainloop()
