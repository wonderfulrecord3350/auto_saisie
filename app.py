import time 
import pyautogui
from tkinter import *
from datetime import datetime
import pyperclip

#Gui creation 
window = Tk()
window.title("Auto_Fill")
window.geometry('400x270')
window.resizable(0,0)


#Username entry
name_label = Label(text="Username")
name_label.config(font=("Arial", 12))
name_entry = Entry(width=40 ,borderwidth=5,font=("Arial", 12))
name_label.pack()
name_entry.pack(ipady=8)

#Password entry
pass_label = Label(text="Password")
pass_label.config(font=("Arial", 12))
pass_entry = Entry(show="*",width=40, borderwidth=5,font=("Arial", 12))
pass_label.pack()
pass_entry.pack(ipady=8)



#Function to save the input
def save_creds():
    username = name_entry.get()
    password = pass_entry.get()
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    Box.insert(0,'Saved Successfully!'+" at "+current_time)

#Save button to execute the function
Save_Button = Button(window, text="Save", padx=30,pady=10,command=save_creds)
Save_Button.config(font=("Arial", 12))
Save_Button.place(x=70,y=150)



#Function to auto fill with pyautogui
def use_creds():
    username = name_entry.get()
    password = pass_entry.get()

    #Function to paste entries
    def combination():
        pyautogui.keyDown('shiftleft')
        pyautogui.keyDown('shiftright')
        pyautogui.keyDown('insert')
        pyautogui.keyUp('insert')
        pyautogui.keyUp('shiftright')
        pyautogui.keyUp('shiftleft')
        pyautogui.press('enter')

    time.sleep(4)

    pyperclip.copy(username)
    time.sleep(0.5)
    combination()
    time.sleep(0.5)
    pyperclip.copy(password)
    time.sleep(0.5)
    combination()



#Button to execute pyautogui function
Use_Button = Button(window, text="Use", padx=30,pady=10,command=use_creds)
Use_Button.config(font=("Arial", 12))
Use_Button.place(x=200,y=150)


#List box
Box=Listbox(window,width=30,height=1,font=("Arial", 14))
Box.place(x=30,y=215)


window.mainloop()
