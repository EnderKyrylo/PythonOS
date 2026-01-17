import os
import platform
import tkinter as tk
import shutil

based = platform.system()
based_interface = os.name

root = tk.Tk()
root.withdraw()

windows = []

# Sandbox root
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
VROOT = os.path.join(SCRIPT_DIR, "root")
os.makedirs(VROOT, exist_ok=True)
os.chdir(VROOT)

def Window(title):
    winw = tk.Toplevel(root)
    winw.title(title)
    windows.append(winw)

def vpath(path):
    if path.startswith("/"):
        path = path.lstrip("/")

    full = os.path.abspath(os.path.join(os.getcwd(), path))

    if os.path.commonpath([VROOT, full]) != VROOT:
        raise ValueError("Path escape blocked")

    return full




print(f"""Welcome to PythonOS 0.1!
Based on {based} with {based_interface}
             .........              
           :.   -++=-::..           
           ......:-++++:-           
                  -++++:-           
      ...........:-++++:- ====.     
     .-++++++++++++++++:: +%%#+     
    .:++++=-..........::  +%%%#=    
    .=+++-:--------***  -*#%%%#=    
    .:+++: .-+========++##%%%%#=    
     .-++. %+%%%%%%%%%%%%%%%%#+
     *.... %*%%%%#++++++======*
           #*%%%%*            
           #*%%%%#+=====+     
           *=+###%%#   =*     
            *#=======*
""")

running = True
while running:
    cwd_display = os.getcwd().replace(VROOT, "/root")
    cmd = input(f"{cwd_display} >> ").split()

    if not cmd:
        continue

    # Shutdown
    if cmd[0] == "shutdown":
        root.destroy()
        windows.clear()
        running = False

    # View file
    elif cmd[0] == "viewfile":
        if len(cmd) < 2:
            print("Error: File path not specified!")
        else:
            try:
                file_path = vpath(cmd[1])
                with open(file_path, "r") as f:
                    print(f.read())
            except FileNotFoundError:
                print("Error: File not found!")
            except UnicodeDecodeError:
                print("Error: Can't view non-text files.")
            except IsADirectoryError:
                print("Error: Can't view folders.")
            except ValueError:
                print("Error: Can't leave root!")

    # Change directory
    elif cmd[0] == "cdir":
        if len(cmd) < 2:
            print("Error: Directory path not specified!")
        else:
            try:
                new_dir = vpath(cmd[1])
                os.chdir(new_dir)
            except FileNotFoundError:
                print("Error: Directory doesn't exist!")
            except ValueError:
                print("Error: Can't leave root!")

    # List directory
    elif cmd[0] == "lsd":
        for f in os.listdir(os.getcwd()):
            if not f.startswith("."):
                print(f)

    # Clear terminal
    elif cmd[0] == "clear":
        os.system("cls" if based_interface == "nt" else "clear")

    # Open Tk window
    elif cmd[0] == "open-win":
        Window("Window")

    # Make folder
    elif cmd[0] == "mfold":
        if len(cmd) < 2:
            print("Error: Folder name not specified!")
        else:
            try:
                os.makedirs(vpath(cmd[1]), exist_ok=True)
            except ValueError:
                print("Error: Can't leave root!")

    # Remove file or folder
    elif cmd[0] == "rem":
        if len(cmd) < 2:
            print("Error: Path not specified!")
        else:
            try:
                target = vpath(cmd[1])
                if os.path.isdir(target):
                    shutil.rmtree(target)
                else:
                    os.remove(target)
            except FileNotFoundError:
                print("Error: Not found!")
            except ValueError:
                print("Error: Can't leave root!")
                
    elif cmd[0] == "mfile":
        if len(cmd) < 2:
            print("Error: File name not specified!")
        else:
            try:
                content = input()
                path = vpath(cmd[1])
                with open(path, "w") as f:
                    f.write(content)
            except ValueError:
                print("Error: Can't leave root!")

