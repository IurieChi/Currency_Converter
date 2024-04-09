# you need to install request pip3 install reqursts on mac and tkinter ,PIL
from tkinter import messagebox
import requests
import json


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
    import gui
    msg_empty_from = 'Please seletec curency FROM'
    msg_empty_to = 'Please seletec curency To'
    msg_empty_value = 'Please type amount to be converted'

    if gui.combo_from.get()== '':
        return messagebox.showwarning('Warning',msg_empty_from)
    elif gui.combo_to.get() =='':
        return messagebox.showwarning('Warning',msg_empty_to)
    elif gui.value.get() =='':
        return messagebox.showwarning('Warning',msg_empty_value)
    
# conet API to app and adjust it to frame
def conect_api():
    
    import gui
    
    
    url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"

    querystring = {"from":gui.combo_from.get(),"to":gui.combo_to.get(),"amount":gui.value.get()}

    headers = {
        "X-RapidAPI-Key": "2ddaf60a89mshbec8b2b15428b43p198731jsnbad46544d551",
        "X-RapidAPI-Host": "currency-converter18.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    data = json.loads(response.text)
    symbol = disply_symbol(file,  gui.combo_to.get())
    money_name = disply_name(file, gui.combo_to.get())

# format result for dysply
    converted = f"{symbol} {round(data['result']['convertedAmount'],2)} {money_name}"
    

# assigne value to lable
    gui.results['text'] = converted

def convert():
    
    # message is mandatory filds are empty 
    # message()
    conect_api()






