import os
import platform
import tkinter as tk

based = platform.system()
based_interface = os.name

root = tk.Tk()
root.withdraw()

windows = []

def Window(title):
    winw = tk.Toplevel(root)
    winw.title(title)
    windows.append(winw)

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
    cwd = os.getcwd()
    cmd = input(f"{cwd} >> ").split()

    if not cmd:  # handle empty input
        continue

    if cmd[0] == "shutdown":
        root.destroy()
        windows.clear()
        running = False

    elif cmd[0] == "viewfile":
        if len(cmd) < 2:
            print("Error: File path not specified!")
        else:
            # Handle absolute or relative paths
            file_path = cmd[1]
            if not os.path.isabs(file_path):
                file_path = os.path.join(cwd, file_path)
            try:
                with open(file_path, "r") as f:
                    print(f.read())
            except FileNotFoundError:
                print("Error: File not found!")
            except UnicodeDecodeError:
                print("Error: Can't view other file formats other than text or code.")
            except IsADirectoryError:
                print("Error: Can't view folders.")

    elif cmd[0] == "cdir":
        if len(cmd) < 2:
            print("Error: Directory path not specified!")
        else:
            # Handle absolute or relative paths
            new_dir = cmd[1]
            if not os.path.isabs(new_dir):
                new_dir = os.path.join(cwd, new_dir)
            try:
                os.chdir(new_dir)
            except:
                print("Error: Directory doesn't exist!")
    elif cmd[0] == "lsd":
      for f in os.listdir(cwd):
          if not f.startswith("."):
            print(f)
    elif cmd[0] == "clear":
      os.system("cls" if based_interface == "nt" else "clear")
    
    elif cmd[0] == "open-win":
        Window("Window")
        
