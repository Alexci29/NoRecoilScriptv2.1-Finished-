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
window_width,window_height=320,500
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
                StatusMode.config(text="OFF", fg="red")
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
        tkinter.messagebox.showinfo('Valid keys', 'Valid keys entrys (No Case sensitive): \n\n f1 to f12 \n\n CapsLock \n\n Supr \n\n Num_lock  \n\n Tab \n\n Ctrl \n\n Backspace \n\n Enter ')
validKeysInfo()

"""Getting the new on/off key inserted"""
def newKey():
        key = StartStopKeyEntry.get()
        key = key.strip().lower()
        if (not key =="" and not key=="f1" and not key=="backspace" and not key=="enter" and not key=="capslock" and not key=="num_lock" and not key=="supr" and not key=="tab" and not key=="ctrl" and not key=="f2" and not key=="f3" and not key=="f4" and not key=="f5" and not key=="f6" and not key=="f7" and not key=="f8" and not key=="f9" and not key=="f10" and not key=="f11" and not key=="f12"):
                tkinter.messagebox.showerror('Key error', 'Current key Empty or Invalid Key enter\n\nValid keys entrys: \n\n f1 to f12 \n\n CapsLock \n\n Supr \n\n Num_lock  \n\n Tab \n\n Ctrl \n\n Backspace \n\n Enter ')
        else:
                if(key==""):
                        CurrentKey.config(text="Current key : EMPTY")
                else:
                        CurrentKey.config(text="Current key : "+key.upper())
        return key

"""If the setted on/off key is pressed on the newKey return then change the status mode"""
def on_press():
        f1Name = "f1"
        f1Code = win32api.GetKeyState(0x70)
        f2Name = "f2"
        f2Code = win32api.GetKeyState(0x71)
        f3Name = "f3"
        f3Code = win32api.GetKeyState(0x72)
        f4Name = "f4"
        f4Code = win32api.GetKeyState(0x73)
        f5Name = "f5"
        f5Code = win32api.GetKeyState(0x74)
        f6Name = "f6"
        f6Code = win32api.GetKeyState(0x75)
        f7Name = "f7"
        f7Code = win32api.GetKeyState(0x76)
        f8Name = "f8"
        f8Code = win32api.GetKeyState(0x77)
        f9Name = "f9"
        f9Code = win32api.GetKeyState(0x78)
        f10Name = "f10"
        f10Code = win32api.GetKeyState(0x79)
        f11Name = "f11"
        f11Code = win32api.GetKeyState(0x7A)
        f12Name = "f12"
        f12Code = win32api.GetKeyState(0x7B)
        
        if (f1Code<0 and f1Name == newKey() or f2Code<0 and f2Name == newKey() or f3Code<0 and f3Name == newKey() or f4Code<0 and f4Name == newKey() or f5Code<0 and f5Name == newKey() or f6Code<0 and f6Name == newKey() or f7Code<0 and f7Name == newKey() or f8Code<0 and f8Name == newKey() or f9Code<0 and f9Name == newKey() or f10Code<0 and f10Name == newKey() or f11Code<0 and f11Name == newKey() or f12Code<0 and f12Name == newKey()):
                StatusChange()
                time.sleep(0.1)
        root.after(100,on_press)
        
root.after(100,on_press)

def saveRecoil():
        tkinter.messagebox.showinfo('Recoil config','Recoil config saved correctlly!')

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

"""On/Off LabelFrame for key config (start/stop script)"""
ConfigKeyLabelFrame = LabelFrame(root, text="Script config",font=("Segoe UI", 12, "italic", "bold"), bg='#400040', fg="white")
ConfigKeyLabelFrame.pack(anchor="w",padx=10, ipadx=100, ipady=25)
onOffMargin= Label(ConfigKeyLabelFrame, bg='#400040')
onOffMargin.pack()
StartStopKeyLabel = Label(ConfigKeyLabelFrame, text="On/Off Key", bg='#400040', font=("Segoe UI", 11, "bold"), fg="darkgrey")
StartStopKeyLabel.place(x=20,y=7)
StartStopKeyEntry = Entry(ConfigKeyLabelFrame, width=10, font=("Segoe UI", 10, "bold", "italic"), fg="red")
StartStopKeyEntry.place(x=120,y=10)
StartStopKeyButton = Button(ConfigKeyLabelFrame, command=newKey, text="Save Key", activebackground='#400040', bg='#400040',padx=5, activeforeground="white", fg="lightgreen", font=("Segoe UI", 10, "bold"))
StartStopKeyButton.place(x=210,y=7)
CurrentKey = Label(ConfigKeyLabelFrame, text="Current key : EMPTY", bg='#400040', font=("Segoe UI", 10, "bold"), fg="white")
CurrentKey.place(x=90,y=38)

"""Recoil values LabelFrame config (Down/Up/Left/Right)"""
RecoilConfig  = LabelFrame(root, text="Recoil config", font=("Segoe UI",12,"bold","italic"), fg="white", bg='#400040')
RecoilConfig.pack(anchor="w",padx=10, ipadx=100, ipady=75, pady=10)
recoilEmptyMargin = Label(RecoilConfig, bg='#400040')
recoilEmptyMargin.pack()
recoilDown = Label(RecoilConfig, text="Recoil Down", bg='#400040', font=("Segoe UI", 10, "bold"), fg="lightgreen")
recoilDown.place(x=20,y=7)
recoilDownEntry = Entry(RecoilConfig, width=6, font=("Segoe UI", 10, "bold"), fg="black", justify="center")
recoilDownEntry.place(x=35,y=30)
recoilUp = Label(RecoilConfig, text="Recoil Up", bg='#400040', font=("Segoe UI", 10, "bold"), fg="lightgreen")
recoilUp.place(x=200,y=7)
recoilUpEntry = Entry(RecoilConfig, width=6, font=("Segoe UI", 10, "bold"), fg="black", justify="center")
recoilUpEntry.place(x=210,y=30)
recoilLeft = Label(RecoilConfig, text="Recoil Left", bg='#400040', font=("Segoe UI", 10, "bold"), fg="lightgreen")
recoilLeft.place(x=20,y=60)
recoilLeftEntry = Entry(RecoilConfig, width=6, font=("Segoe UI", 10, "bold"), fg="black", justify="center")
recoilLeftEntry.place(x=35,y=85)
recoilRight = Label(RecoilConfig, text="Recoil Right", bg='#400040', font=("Segoe UI", 10, "bold"), fg="lightgreen")
recoilRight.place(x=200,y=60)
recoilRightEntry = Entry(RecoilConfig, width=6, font=("Segoe UI", 10, "bold"), fg="black", justify="center")
recoilRightEntry.place(x=210,y=85)
recoilSaveButton = Button(RecoilConfig, command=saveRecoil, text="Save Recoil Config", activebackground='#400040', bg='#400040',padx=5, activeforeground="white", fg="lightgreen", font=("Segoe UI", 10, "bold"))
recoilSaveButton.place(x=85,y=130)
happyFace = Label(RecoilConfig, text="♥‿♥", bg='#400040', font=("Segoe UI", 20, "bold"), fg="pink")
happyFace.place(x=120,y=45)

"""Working on updates message"""
updates = Label(root, text="WORKING ON UPDATES (v.3.1) \n(Add and remove weapons menu,\nWeapon image recognition)", bg='#400040', font=("Segoe UI", 10, "bold"), fg="lightgreen")
updates.place(x=55,y=425)

root.mainloop()
