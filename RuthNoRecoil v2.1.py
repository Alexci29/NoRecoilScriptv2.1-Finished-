"""Some python librarys imports"""
import tkinter as tkinter
from tkinter import *
from tkinter import messagebox
import os
import win32api
import winsound
import time

"""Main Screen Configuration"""
root = Tk()
root.title('Ruth NoRecoil')
root.config(bg='#400040')
root.iconphoto(False, tkinter.PhotoImage(file='img\icon.png'))
root.resizable(0,0)
"""Config to set app at the center screen when open it"""
window_width,window_height=400,600
screen_width = root.winfo_screenwidth()
screen_height= root.winfo_screenheight()
position_top = int(screen_height/2 - window_height/2)
position_right = int(screen_width/2 - window_width/2)
root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

"""All the functions below"""
"""Changing the status mode (ON/OFF) when clicking the setted key"""    
def StatusChange():
        if(StatusMode['text']=="OFF"):
                time.sleep(0.2)
                StatusMode.config(text="ON", fg="lightgreen")
                winsound.Beep(1000,900)
        elif(StatusMode['text']=="ON"):
                time.sleep(0.2)
                scriptStatusMode.config(text="OFF", fg="red")
                winsound.Beep(2500,900)

"""Exit the script (executed when click button below)"""
def Exit():
        Exit = tkinter.messagebox.askquestion('Salir de la aplicacion','Seguro que quieres salir?',icon='warning')
        if Exit == 'yes':
                root.destroy()
        else:
                tkinter.messagebox.showinfo('Volveeemos','Vuelves al script ;D')

"""Displaying valid keys information"""
def validKeysInfo():
        tkinter.messagebox.showinfo('Valid keys', 'Valid keys entrys (Case sensitive not activated): \n\n f1 to f12 \n\n CapsLock \n\n Supr \n\n Num_lock  \n\n Tab \n\n Ctrl \n\n Backspace \n\n Enter ')
validKeysInfo()

"""Getting the new on/off key inserted"""
def newKey():
        key = StartStopKeyEntry.get()
        key = key.strip().lower()
        if (not key=="f1" and not key=="backspace" and not key=="enter" and not key=="capslock" and not key=="num_lock" and not key=="supr" and not key=="tab" and not key=="ctrl" and not key=="f2" and not key=="f3" and not key=="f4" and not key=="f5" and not key=="f6" and not key=="f7" and not key=="f8" and not key=="f9" and not key=="f10" and not key=="f11" and not key=="f12"):
                tkinter.messagebox.showerror('Key error', 'Valid keys entrys: \n\n f1 to f12 \n\n CapsLock \n\n Supr \n\n Num_lock  \n\n Tab \n\n Ctrl \n\n Backspace \n\n Enter ')
        else:
                CurrentKey.config(text="Current key : "+key.upper())
        return key

def on_press():
        leftBtn = 0x01
        while True:
                key = win32api.GetKeyState(leftBtn)
                if key < 0:
                        print("Left click pressed")
                        time.sleep(0.1)
        root.after(100,on_press)
        
root.after(100,on_press)

"""Title frame box that contains label with the script name (not app name)"""
Title = Frame(root, width=600)
Title.pack()
Title = Label(Title,text="RuthNoRecoil Script V2.1", width=600, padx=80, pady=20, bg='#000000', fg="white", font=("Segoe UI", 14, "italic", "bold")).pack()

"""Frame where sees the script status (Off=no active / On = active)
   the label use a variable to get the text value. The variable value will
   be changed when the script is ON and then, the label text will be changed
   too"""
StatusFrame = Frame(root, bg='#400040')
StatusFrame.pack(anchor="w", padx=10,pady=2)
StatusLabel=Label(StatusFrame, text="MODE :", bg='#400040', font=("Segoe UI",12,"italic","bold"),fg="green")
StatusLabel.pack(side=LEFT)
Status = StringVar()
Status.set("OFF")
StatusMode=Label(StatusFrame, text=Status.get(),bg='#400040', font=("Segoe UI",11,"italic","bold"),fg="red")
StatusMode.pack(pady=5)

"""LabelFrame with script configs like :
        On/off key (start/stop script)
        Recoil entry values(down, up, left, right) inside another LabelFrame"""        
ConfigLabelFrame = LabelFrame(root, text="Script config",font=("Segoe UI", 12, "italic", "bold"), bg='#400040', fg="white")
ConfigLabelFrame.pack(anchor="w",padx=10, ipadx=100, ipady=100)
empty4margin= Label(ConfigLabelFrame, bg='#400040')
empty4margin.pack()
StartStopKeyLabel = Label(ConfigLabelFrame, text="On/Off Key", bg='#400040', font=("Segoe UI", 11, "bold"), fg="darkgrey")
StartStopKeyLabel.place(x=20,y=7)
StartStopKeyEntry = Entry(ConfigLabelFrame, width=10, font=("Segoe UI", 10, "bold", "italic"), fg="red")
StartStopKeyEntry.place(x=120,y=10)
StartStopKeyButton = Button(ConfigLabelFrame, command=newKey, text="Save Key", activebackground='#400040', bg='#400040',padx=5, activeforeground="white", fg="lightgreen", font=("Segoe UI", 10, "bold"))
StartStopKeyButton.place(x=210,y=7)
CurrentKey = Label(ConfigLabelFrame, text="Current key : EMPTY", bg='#400040', font=("Segoe UI", 10, "bold"), fg="white")
CurrentKey.place(x=90,y=38)


root.mainloop()
