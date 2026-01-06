import os
import tkinter as tk
import subprocess
import sys

root = tk.Tk()
root.title("void updater")
root.geometry("525x300")
root["bg"] = "Black"
returned_output = ""

if os.name == 'nt':

    import ctypes
    kernel32 = ctypes.windll.kernel32
    if not kernel32.GetConsoleWindow():

        kernel32.AllocConsole()

        sys.stdout = open('CONOUT$', 'w')
        sys.stderr = open('CONOUT$', 'w')
        

def pipUpdateCommand():
    cmd = "python -m pip install --upgrade pip"
    returned_output = subprocess.check_output(cmd)
    print('Результат выполнения команды:', returned_output.decode("utf-8")) 
print("VOID UPDATER/BY CHAOSSW")
print("all results here \n update pip and you see result")

title = tk.Label(root , text="VOID UPDATER" , font=("Arial",30) , background="Green")
ver = tk.Label(root , text="first version" , font=("Arial",10) , background="Green")
infoUpdate = tk.Label(root , text="This is the first version of this program, so for now you can only update pip packages here." , font=("Arial",10) , background="Green")
updateButton = tk.Button(text="update pip", command=pipUpdateCommand)
authorButton = tk.Button(text="author")
result = tk.Label(root ,text="result:"+returned_output)

title.pack()
ver.pack()
infoUpdate.pack()
updateButton.pack()
authorButton.pack()
result.pack()


root.mainloop()

