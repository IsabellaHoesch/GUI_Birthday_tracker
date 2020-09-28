from tkinter import *
from PIL import Image, ImageTk
import time

# class Application(Frame):
#     def __init__(self, master = None):
#         Frame.__init__(self, master)
#
#
# root = Tk()
# app = Application(master=root)
# app.geometry("500x200")
# app.mainloop()


# Label(master, text="Isa´s GUI", font=("Arial", 22)).pack(fill=X, padx=20, pady=10)
# Text(master, height=5, width=40, fg="green", bg="lightblue").pack(padx=20, pady=10)
# Button(master, text="Klick my button").place(x=20, y=30, width=100, height=50)
# master.geometry("500x200")
# image = Image.open("pic.jpg")
# photo = ImageTk.PhotoImage(image)
# master.create_image(250, 250, image=photo)


********************************************************************************************

## Timer und scheduler
master = Tk()
clock = Label(master, font=("Times", 42), text="1")
clock.pack(fill=BOTH)
def ticken():
    zeit=time.strftime("%H:%M:%S")
    clock.config(text=zeit)
    clock.after(1000, ticken)
ticken()
master.mainloop()


********************************************************************************************
## Ereignisbehandlung mit command
master = Tk()
def clicked():
    lbl.config(text="Clicked")
Button(master, text="Click my button", command=clicked).grid(row=0, column=0)
lbl = Label(master)
lbl.grid(row=1, column=0)
master.mainloop()

********************************************************************************************
## Texteingabe
def aktion():
    lbl.configure(text="Hallo " + eingabe.get())

master = Tk()
Button(master, text="Verwenden", font=("Arial",20), bg="red", fg="white", command=aktion).grid(row=1, sticky=W+E)
lbl=Label(master, font=("Arial",20), bg="grey", fg="red", pady=15)
lbl.grid(row=2,sticky=W+E)
eingabe=Entry(master, font=("Arial",20), bg="grey", fg="red")
eingabe.grid(row=0, sticky=W+E)
master.mainloop()


********************************************************************************************