
from tkinter import *
from tkinter import messagebox



# Driver code
if __name__ == "__main__":
    gui = Tk()  # create a GUI window
    gui.configure(bg="black")  # set the background colour of GUI window
    gui.title("Birthday App")  # set the title of GUI window

    # Descriptive label
    top_label = Label(gui, text="Birthday tracker", font=("Helvetica", 18, 'bold'), bg="black", fg="pink").pack()

    frame1 = Frame(gui)
    frame1.pack(padx=10, pady=10)

    # Label and text entry box for entry points: firstname, lastname, birthdate
    Label(frame1, text="First Name", font=("Helvetica", 14), fg="pink", bg="Black").grid(row=0, column=0, sticky=W)
    fnamevar = StringVar()
    fname = Entry(frame1, textvariable=fnamevar, fg="black", bg="lavenderblush2").grid(row=0, column=1, sticky=W)

    Label(frame1, text="Last Name", font=("Helvetica", 14), fg="pink", bg="Black").grid(row=1, column=0, sticky=W)
    lnamevar = StringVar()
    lname = Entry(frame1, textvariable=lnamevar, fg="black", bg="lavenderblush2").grid(row=1, column=1, sticky=W)

    Label(frame1, text="Birthdate", font=("Helvetica", 14), fg="pink", bg="Black").grid(row=2, column=0, sticky=W)
    bdatevar = StringVar()
    bdate = Entry(frame1, textvariable=bdatevar, fg="black", bg="lavenderblush2").grid(row=2, column=1, sticky=W)

    frame2 = Frame(gui)  # Row of buttons
    frame2.pack(padx=10, pady=10)

    info_label = Label(frame2, font=("Helvetica", 14), bg="black", fg="pink", pady=15).place()
    b1 = Button(frame2, text=" Add  ", font=("Helvetica", 12), fg="lightcyan2", bg="Black")  # , command=add_entry
    b2 = Button(frame2, text="Update", font=("Helvetica", 12), fg="lightcyan2", bg="Black") # , command=update_entry
    b3 = Button(frame2, text="Delete", font=("Helvetica", 12), fg="lightcyan2", bg="Black")  # , command=delete_entry
    b4 = Button(frame2, text="Load  ", font=("Helvetica", 12), fg="lightcyan2", bg="Black")  # , command=load_entry
    b5 = Button(frame2, text="Refresh", font=("Helvetica", 12), fg="lightcyan2", bg="Black")  # , command=set_select // create: search
    b1.pack(side=LEFT)
    b2.pack(side=LEFT)
    b3.pack(side=LEFT)
    b4.pack(side=LEFT)
    b5.pack(side=LEFT)

    frame3 = Frame(gui)  # Row of buttons (2)
    frame3.pack(padx=10, pady=10)

    b6 = Button(frame3, font=("Helvetica", 12), text="Past Birthdays", fg="lightcyan2", bg="black")#command=openFrame
    b7 = Button(frame3, font=("Helvetica", 12), text="Upcoming Birthdays", fg="lightcyan2", bg="black")  # , command=upcoming_bds
    b6.pack(side=LEFT)
    b7.pack(side=LEFT)

    frame4 = Frame(gui)  # select of names
    frame4.pack(padx=10, pady=10)
    scroll = Scrollbar(frame4, orient=VERTICAL)
    select = Listbox(frame4, yscrollcommand=scroll.set, height=6)
    scroll.config(command=select.yview)
    scroll.pack(side=RIGHT, fill=Y)
    select.pack(side=LEFT, fill=BOTH, expand=1)

    # start the GUI
    gui.mainloop()

# todo: create functions for buttons!!

# ideas for later:
# Spinbox für datumpicker