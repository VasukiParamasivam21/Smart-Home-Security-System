from tkinter import *
from tkinter import messagebox
from functools import partial
from detect import detectcam
from trainer import trainimage
from face_recog import captureimage


import tkinter as tk
from tkinter import ttk

def launchapp():
    tkWindow = Tk()  
    tkWindow.geometry('500x350')  
    tkWindow.title('Home Security system')
    tkWindow.configure(bg='lightblue')

    # Capture Image button
    capturebutton = ttk.Button(tkWindow, text="CAPTURE IMAGE", command=captureimage)
    capturebutton.place(relx=0.3,rely=0.2,relwidth=0.4)
    # Train Images Button
    trainButton = ttk.Button(tkWindow, text="TRAINIMAGES", command=trainimage)
    trainButton.place(relx=0.3,rely=0.4,relwidth=0.4)
    # Detect person button
    detectButton = ttk.Button(tkWindow, text="DETECT", command=detectcam)
    detectButton.place(relx=0.3,rely=0.6,relwidth=0.4)

    tkWindow.mainloop()
    
