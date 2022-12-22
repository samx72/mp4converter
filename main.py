import moviepy.editor
from tkinter.filedialog import *
import os
from termcolor import colored
import time

work = True

while(work == True):
    os.system("cls")
    vid = askopenfilename()
    video = moviepy.editor.VideoFileClip(vid)

    aud = video.audio
    name = input("what do you want the file to be called: ")
    aud.write_audiofile (f"{name}.mp3")
    print(colored("convert is completed", "yellow"))
    time.sleep(2)
    os.system("cls")
    
    print(colored(f"the mp3 file is called {name}", "yellow"))

    end = input("""
do you want continue in this program?(y/n): """)
    
    if(end=='y'):
        continue
    
    else:
        print("program ended")
        exit()
