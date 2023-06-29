import win32api
import win32gui

import tkinter as tk

# mic
WM_APPCOMMAND = 0x319
APPCOMMAND_MICROPHONE_VOLUME_MUTE = 0x180000
hwnd_active = win32gui.GetForegroundWindow()

# box
toggle = False

def mute(event=None):
    global toggle
    toggle = not toggle
    
    if toggle:
        label.configure(text="ON", foreground='white', background='green')
        root.configure(bg='green')
        win32api.SendMessage(hwnd_active, WM_APPCOMMAND, None, APPCOMMAND_MICROPHONE_VOLUME_MUTE)
    else:
        label.configure(text="OFF", foreground='white', background='red')
        root.configure(bg='red')
        win32api.SendMessage(hwnd_active, WM_APPCOMMAND, None, APPCOMMAND_MICROPHONE_VOLUME_MUTE)
        
def checkKey(e): 
    if e.keycode == 107: mute()
    
    print(e.keycode)
    
root = tk.Tk()

root.geometry('350x350')
root.title('Mic control')
root.configure(bg='black')


label = tk.Label(root,text="ON" if toggle else "OFF" , font=('Helvetica', 24), foreground='white', background='black', width=200, height=200)
label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

label.bind("<Button-1>", mute)
root.bind('<KeyPress>', checkKey)

root.mainloop()
