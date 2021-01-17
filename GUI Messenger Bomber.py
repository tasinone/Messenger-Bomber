import pyautogui 
import tkinter as tk 
from tkinter import messagebox as m_box 
import time 

# GUI start here____________________
root = tk.Tk()
root.title('Facebook Messenger Bomber')
# root.geometry('600x400') 
root.configure(bg = 'red') 
root.resizable(width = False, height = False) 

heading = tk.Label(root, text = 'Press START and keep your cursor on message box', bg = 'red', fg = 'white', font = ('helvetica', 12, 'bold')) 
heading.grid(row = 0, columnspan = 2, padx = 10, pady = 15) 

# _________________Message Box 
msg = tk.Label(root, text = 'Enter Your Message', font = ('Helvetica', 12, 'bold'), bg ='red', fg = 'white') 
msg.grid(row = 1, column = 0, padx = 10, pady = 5)  

msgVar = tk.StringVar() 
msg_box = tk.Entry(root, textvariable = msgVar) 
msg_box.grid(row = 1, column = 1, padx = 5, pady = 10) 
msg_box.focus() 

# ____________________Delay Box 
tm = tk.Label(root, text = 'Enter Delay Time', font = ('Helvetica', 12, 'bold'), bg ='red', fg = 'white') 
tm.grid(row = 2, column = 0, padx = 10, pady = 10)


timeVar = tk.IntVar()
time_box = tk.Entry(root, textvariable = timeVar)
time_box.grid(row = 2, column = 1, padx = 10, pady = 10) 

#_____________________Function
def action():
    msgValueGet = msgVar.get()
    timeValueGet = timeVar.get()

    if timeValueGet == '':
        m_box.showerror('Error', "Delay box can't be empty") 
    if msgValueGet == '':
        m_box.showerror('Error',"Message box can't be empty")
    if timeValueGet == 0:
        m_box.showwarning('Warning', "If delay time is 0\n Facebook may block you")
    else:
        try:
            timeValueGet == int(timeValueGet)
        except ValueError:
            m_box.showerror('Warning', "Only digits are allowed")
        else:
            while True:
                time.sleep(timeValueGet)
                pyautogui.typewrite(msgValueGet)  
                pyautogui.press('ENTER') 

#_____________________Start Button
startBtn = tk.Button(root, text = 'START', command = action)
startBtn.grid(row = 3, columnspan = 2, pady = 10)

root.mainloop() 

