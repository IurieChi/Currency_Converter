# you need to install request pip3 install reqursts on mac and tkinter ,PIL
import tkinter as tk
from tkinter import ttk 
from tkinter import messagebox
from PIL import ImageTk
from PIL import Image
import json
import requests



file = 'currency-format.json'
# Find currency symbol
def disply_symbol(file, key):
    with open(file) as f:
        content = json.load(f)
        symbol = content[key]['symbol']['grapheme']
        return symbol
# extract name
def disply_name(file, key):
    with open(file) as f:
        content = json.load(f)
        name = content[key]['name']
        return name
    
def message():
    #message 
    
    msg_empty_from = 'Please seletec curency FROM'
    msg_empty_to = 'Please seletec curency To'
    msg_empty_value = 'Please type amount to be converted'

    if combo_from.get()== '':
        return messagebox.showwarning('Warning',msg_empty_from)
    elif combo_to.get() =='':
        return messagebox.showwarning('Warning',msg_empty_to)
    elif value.get() =='':
        return messagebox.showwarning('Warning',msg_empty_value)
    
# conet API to app and adjust it to frame
def conect_api(from_currency, to_currency, amount):
        
    url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"

    querystring = {"from":from_currency,"to":to_currency,"amount":amount}

    headers = {
        "X-RapidAPI-Key": "2ddaf60a89mshbec8b2b15428b43p198731jsnbad46544d551",
        "X-RapidAPI-Host": "currency-converter18.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    data = json.loads(response.text)
    symbol = disply_symbol(file,  combo_to.get())
    money_name = disply_name(file, combo_to.get())

# format result for dysply
    converted = f"{symbol} {round(data['result']['convertedAmount'],2)} {money_name}"
    

# assigne value to lable
    results['text'] = converted

def convert():
    
    # message is mandatory filds are empty 
    message()
    conect_api(combo_from.get(), combo_to.get(), value.get())

# window colors
col1 ="#FFFFFF" #white
col2 ="#333333" #black
col3 ="#80FF00" #green
col4 = "#d31818" #red

window = tk.Tk()
window.geometry('350x400')
window.title('Curency Converter')
window.iconbitmap('curency64.ico')
window.configure(bg = col1)
window.resizable(width=False, height=False)

#create top frame 
top_frame = tk.Frame(window, width=350, height = 65, bg = col3)
top_frame.grid(row=0, column=0)

img = Image.open('curency_.png')
img = img.resize((60,60)) 
img = ImageTk.PhotoImage(img)
app_name = tk.Label (top_frame, image = img, compound='left', text="Curency Converter", padx= 40,  anchor= 'w' , font=('Arial 16 bold'), bg=col3, fg=col2)
app_name.place(x=0,y=0)


# fill curency list from json for combo_from and combo_to 
currency =[] 
file = 'currency-format.json'
with open(file) as f:
    content = json.load(f)
        # print(content)
    for key in content.keys():
        if key != " ":
            currency.append(key) 

#Main frame

from_lable = tk.Label(text='From', width=8, height= 1, padx=0, pady=0, relief= 'flat', anchor= 'nw', font= ('Ivy 15 bold'), bg= col1, fg= col2)
from_lable.place(x= 50, y= 80)
to_lable = tk.Label(text='To', width=8, height= 1, padx=0, pady=0, relief= 'flat', anchor= 'nw', font= ('Ivy 15 bold'), bg= col1, fg= col2)
to_lable.place(x= 200, y= 80)

combo_from = ttk.Combobox(window, width=5, justify='center', font= ('Iwy 15 bold'))  
combo_from['values']= (currency)
combo_from.place(x= 50, y=100)

combo_to = ttk.Combobox(window, width=5, justify='center', font=('Iwy 15 bold'))  
combo_to['values']= (currency)
combo_to.place(x= 200, y=100)

value = tk.Entry(window, width=20, justify= 'center', font=('Iwy 15 bold'), relief='solid')
value.place(x=50, y=150)

button = tk.Button(window, text='Convert', width=18, height=1, bg=col4 , fg=col2, font=('Ivy 15 bold'), relief='solid', command = convert)
button.place(x=50, y=200)

# result label
results = tk.Label(window, text='',width=20,height=2, justify='center', font=('Ivy 15 bold'),bg= col1, relief='solid')
results.place(x=50, y=270)


if __name__ == "__main__":
    window.mainloop()




