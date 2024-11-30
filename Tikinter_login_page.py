from tkinter import *
from functools import partial
from Tikinter_home import launchapp

import tkinter as tk
from tkinter import messagebox



import tkinter as tk
from tkinter import ttk

# Function to validate the login
def validate_login():
    USERNAME = u_entry.get()
    PASSWORD = p_entry.get()

    # You can add your own validation logic here
    if USERNAME == "admin" and PASSWORD == "password":
        launchapp()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Create the main window
root = tk.Tk()
root.title("Login Page")


#Create Window size
window_width=500
window_height=300
root.geometry(f"{window_width}x{window_height}")


#add color and bg
root.configure(bg="lightblue")

#username label and Entry
u_label=ttk.Label(root,text="USER NAME:",background="lightblue")
u_label.place(relx=0.1,rely=0.2)


u_entry=ttk.Entry(root)
u_entry.place(relx=0.3,rely=0.2,relwidth=0.6)

#password label and Entry
p_label=ttk.Label(root,text="PASSWORD:",background="lightblue")
p_label.place(relx=0.1,rely=0.4)


p_entry=ttk.Entry(root, show="*")
p_entry.place(relx=0.3,rely=0.4,relwidth=0.6)


#button
login_button=ttk.Button(root,text="LOGIN",command=validate_login)
login_button.place(relx=0.3,rely=0.6,relwidth=0.4)




#run the main loop
root.mainloop()


