"""Some python librarys imports"""
import tkinter as tkinter
from tkinter import *
from tkinter import messagebox, ttk
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
window_width,window_height=320,480
screen_width = root.winfo_screenwidth()
screen_height= root.winfo_screenheight()
position_top = int(screen_height/2 - window_height/2)
position_right = int(screen_width/2 - window_width/2)
root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

"""Displaying welcome message when starts the app"""
def welcome():
        tkinter.messagebox.showinfo('RuthNoRecoil', 'Welcome to RuthNoRecoil v2.1!\n\nUsable for any game, enjoy it!')
welcome()

"""Changing the status mode (ON/OFF) when clicking the setted key"""    
def StatusChange():
        if(StatusMode['text']=="OFF"):
                time.sleep(0.2)
                StatusMode.config(text="ON", fg="lightgreen")
                winsound.Beep(1000,200)
        elif(StatusMode['text']=="ON"):
                time.sleep(0.2)
                StatusMode.config(text="OFF", fg="red")
                winsound.Beep(2500,200)

"""Saving setted key when click Save Key button"""
def saveKey():
        key = KeyCombobox.get()
        return key
        
"""On press the setted key change the status mode"""
def on_key_press():
        VK_F1 = win32api.GetKeyState(0x70)
        VK_F2 = win32api.GetKeyState(0x71)
        VK_F3 = win32api.GetKeyState(0x72)
        VK_F4 = win32api.GetKeyState(0x73)
        VK_F5 = win32api.GetKeyState(0x74)
        VK_F6 = win32api.GetKeyState(0x75)
        VK_F7 = win32api.GetKeyState(0x76)
        VK_F8 = win32api.GetKeyState(0x77)
        VK_F9 = win32api.GetKeyState(0x78)
        VK_F10 = win32api.GetKeyState(0x79)
        VK_F11 = win32api.GetKeyState(0x7A)
        VK_F12 = win32api.GetKeyState(0x7B)
        VK_Delete = win32api.GetKeyState(0x2E)
        VK_RETURN = win32api.GetKeyState(0x0D)
        VK_CAPITAL = win32api.GetKeyState(0x14)
        VK_NumLOCK = win32api.GetKeyState(0x90)
        if(VK_F1<0 and "F1"==saveKey() or VK_F2<0 and "F2"==saveKey() or VK_F3<0 and "F3"==saveKey() or VK_F4<0 and "F4"==saveKey()
        or VK_F5<0 and "F5"==saveKey() or VK_F6<0 and "F6"==saveKey() or VK_F7<0 and "F7"==saveKey() or VK_F8<0 and "F8"==saveKey()
        or VK_F9<0 and "F9"==saveKey() or VK_F11<0 and "F11"==saveKey() or VK_F12<0 and "F12"==saveKey() or VK_Delete<0 and "SUPR"==saveKey() 
        or VK_RETURN<0 and "ENTER"==saveKey() or VK_CAPITAL<0 and "CAPSLOCK"==saveKey() 
        or VK_NumLOCK<0 and "NUM_LOCK"==saveKey()):
            StatusChange()
            
        root.after(100,on_key_press)
root.after(100,on_key_press)

def saveRecoil():
        tkinter.messagebox.showinfo('Recoil config','Recoil config saved correctlly!')

"""Title frame box that contains label with the script name (not app name)"""
Title = Frame(root, width=600)
Title.pack()
Title = Label(Title,text="RuthNoRecoil Script V2.1", width=600, padx=80, pady=20, bg='#000000', fg="white", font=("Segoe UI", 14, "italic", "bold")).pack()

"""Frame where sees the script status (Off=no active / On = active)
   the status change when the setted start/stop key is pressed"""
StatusFrame = Frame(root, bg='#400040')
StatusFrame.pack(anchor="w", padx=10,pady=2)
StatusLabel=Label(StatusFrame, text="MODE :", bg='#400040', font=("Segoe UI",12,"italic","bold"),fg="green")
StatusLabel.pack(side=LEFT)
StatusMode=Label(StatusFrame, text="OFF",bg='#400040', font=("Segoe UI",11,"italic","bold"),fg="red")
StatusMode.pack(pady=5)

"""On/Off LabelFrame for key config (start/stop script)"""
"""Creating the labelFrame"""
ConfigKeyLabelFrame = LabelFrame(root, text="Script config",font=("Segoe UI", 12, "italic", "bold"), bg='#400040', fg="white")
ConfigKeyLabelFrame.pack(anchor="w",padx=10, ipadx=100, ipady=15)

"""Empty margin (ingore this)"""
margin1= Label(ConfigKeyLabelFrame, bg='#400040')
margin1.pack()

"""Setting label text"""
KeyLabel = Label(ConfigKeyLabelFrame, text="On/Off Key", bg='#400040', font=("Segoe UI", 11, "bold"), fg="darkgrey")
KeyLabel.place(x=50,y=7)

"""Key options combobox"""
KeyCombobox = ttk.Combobox(ConfigKeyLabelFrame, values=["F1","F2","F3","F4","F5","F6","F7","F8","F9","F11","F12","ENTER","SUPR","CAPSLOCK","NUM_LOCK","0","1","2","3","4","5","6","7","8","9"], width=10, font=("Segoe UI", 10, "bold"))
KeyCombobox.place(x=160,y=11)

"""Recoil values LabelFrame config (Down/Up/Left/Right)"""
"""Recoil config label frame"""
RecoilConfig  = LabelFrame(root, text="Recoil config", font=("Segoe UI",12,"bold","italic"), fg="white", bg='#400040')
RecoilConfig.pack(anchor="w",padx=10, ipadx=100, ipady=75, pady=10)

"""Empty margin"""
recoilEmptyMargin = Label(RecoilConfig, bg='#400040')
recoilEmptyMargin.pack()

"""Recoil DOWN config label and entry"""
recoilDown = Label(RecoilConfig, text="Recoil Down", bg='#400040', font=("Segoe UI", 10, "bold"), fg="lightgreen")
recoilDown.place(x=20,y=7)
recoilDownEntry = Entry(RecoilConfig, width=6, font=("Segoe UI", 10, "bold"), fg="black", justify="center")
recoilDownEntry.place(x=35,y=30)

"""Recoil UP config label and entry"""
recoilUp = Label(RecoilConfig, text="Recoil Up", bg='#400040', font=("Segoe UI", 10, "bold"), fg="lightgreen")
recoilUp.place(x=200,y=7)
recoilUpEntry = Entry(RecoilConfig, width=6, font=("Segoe UI", 10, "bold"), fg="black", justify="center")
recoilUpEntry.place(x=210,y=30)

"""Recoil LEFT config label and entry"""
recoilLeft = Label(RecoilConfig, text="Recoil Left", bg='#400040', font=("Segoe UI", 10, "bold"), fg="lightgreen")
recoilLeft.place(x=20,y=60)
recoilLeftEntry = Entry(RecoilConfig, width=6, font=("Segoe UI", 10, "bold"), fg="black", justify="center")
recoilLeftEntry.place(x=35,y=85)

"""Recoil RIGHT config label and entry"""
recoilRight = Label(RecoilConfig, text="Recoil Right", bg='#400040', font=("Segoe UI", 10, "bold"), fg="lightgreen")
recoilRight.place(x=200,y=60)
recoilRightEntry = Entry(RecoilConfig, width=6, font=("Segoe UI", 10, "bold"), fg="black", justify="center")
recoilRightEntry.place(x=210,y=85)

"""Recoil SAVE configs BUTTON"""
recoilSaveButton = Button(RecoilConfig, command=saveRecoil, text="Save Recoil Config", activebackground='#400040', bg='#400040',padx=5, activeforeground="white", fg="lightgreen", font=("Segoe UI", 10, "bold"))
recoilSaveButton.place(x=85,y=130)

"""Happy face on the center of recoil config label frame"""
happyFace = Label(RecoilConfig, text="♥‿♥", bg='#400040', font=("Segoe UI", 20, "bold"), fg="pink")
happyFace.place(x=120,y=42)

"""Working on updates message"""
updates = Label(root, text="WORKING ON UPDATES (v.2.2) \n(Add and remove weapons menu,\nWeapon image recognition)", bg='#400040', font=("Segoe UI", 10, "bold"), fg="lightgreen")
updates.place(x=55,y=405)

root.mainloop()
