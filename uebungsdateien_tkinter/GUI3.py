from tkinter import *
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
root = Tk()
app = Application(master=root)
app.mainloop()

