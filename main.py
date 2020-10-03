
from tkinter import *
from tkinter import messagebox
from functions import *
import os
import os.path
import sqlite3
from datenbank import *


# Driver code
if __name__ == "__main__":
    def initDB():
        if not os.path.exists('bdaydb.db'):
            connection=sqlite3.connect('bdaydb.db')
            cursor=connection.cursor()
            cursor.execute('''CREATE TABLE personen (name TEXT, vorname TEXT, birthdate TEXT)''')
            print("Datenbank erstellt")
        else:
            print("Datenbank vorhanden")

    def add_entry():
        connection = sqlite3.connect('bdaydb.db')
        cursor = connection.cursor()
        cursor.execute('''INSERT INTO personen VALUES(:fname,:lname, :bdate)''',
                       {'fname': fname.get(), 'lname': lname.get(), 'bdate': bdate.get()})
        connection.commit()
        connection.close()
        print("Daten geschrieben: " + fname.get() + ", " + lname.get() + ", " + bdate.get())

    def submit():
        if os.path.exists('bdaydb.db'):
            add_entry()
        else:
            initDB()


        # clear text boxes:
        fname.delete(0, END)
        lname.delete(0, END)
        bdate.delete(0, END)


    gui = Tk()  # create a GUI window
    gui.configure(bg="black")  # set the background colour of GUI window
    gui.title("Birthday App")  # set the title of GUI window

    # Descriptive label
    top_label = Label(gui, text="Birthday tracker", font=("Helvetica", 18, 'bold'), bg="black", fg="pink").pack()

    frame1 = Frame(gui)
    frame1.pack(padx=10, pady=10)

    # Label and text entry box for entry points: firstname, lastname, birthdate
    Label(frame1, text="First Name", font=("Helvetica", 14), fg="pink", bg="Black").grid(row=0, column=0, sticky=W)
    # fnamevar = StringVar()
    # fname = Entry(frame1, textvariable=fnamevar, fg="black", bg="lavenderblush2")
    fname = Entry(frame1, fg="black", bg="lavenderblush2")
    fname.grid(row=0, column=1, sticky=W)

    Label(frame1, text="Last Name", font=("Helvetica", 14), fg="pink", bg="Black").grid(row=1, column=0, sticky=W)
    lname = Entry(frame1, fg="black", bg="lavenderblush2")
    lname.grid(row=1, column=1, sticky=W)

    Label(frame1, text="Birthdate", font=("Helvetica", 14), fg="pink", bg="Black").grid(row=2, column=0, sticky=W)
    bdate = Entry(frame1, fg="black", bg="lavenderblush2")
    bdate.grid(row=2, column=1, sticky=W)

    frame2 = Frame(gui)  # Row of buttons
    frame2.pack(padx=10, pady=10)

    info_label = Label(frame2, font=("Helvetica", 14), bg="black", fg="pink", pady=15).place()
    b1 = Button(frame2, text=" Add  ", font=("Helvetica", 12), fg="lightcyan2", bg="Black", command=submit)  # , command=action
    b1.pack(side=LEFT)

    # frame3 = Frame(gui)  # Row of buttons (2)
    # frame3.pack(padx=10, pady=10)
    #
    # b6 = Button(frame3, font=("Helvetica", 12), text="Past Birthdays", fg="lightcyan2", bg="black")#command=openFrame
    # b7 = Button(frame3, font=("Helvetica", 12), text="Upcoming Birthdays", fg="lightcyan2", bg="black")  # , command=upcoming_bds
    # b6.pack(side=LEFT)
    # b7.pack(side=LEFT)

    frame4 = Frame(gui)  # select of names
    frame4.pack(padx=10, pady=10)
    scroll = Scrollbar(frame4, orient=VERTICAL)
    select = Listbox(frame4, yscrollcommand=scroll.set, height=6)
    scroll.config(command=select.yview)
    scroll.pack(side=RIGHT, fill=Y)
    select.pack(side=LEFT, fill=BOTH, expand=1)
###

    # start the GUI
    gui.mainloop()






















# ideas for later:
# Spinbox für datumpicker

