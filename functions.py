# Functions for events etc.

# Function for checking input error when empty input is given in task field
def inputError():
    # check for enter task field is empty or not
    if enterTaskField.get() == "":
        # show the error message
        messagebox.showerror("Input Error")
        return 0
    return 1

def which_selected():
    print("At {0}".format(select.curselection()))
    return int(select.curselection()[0])


def which_selected():
    print("At {0}".format(select.curselection()))
    return int(select.curselection()[0])


def add_entry():
    # get the task string concatenating with new line character
    firstname = enterFirstField.get() + "\n"
    lastname = enterLastField.get() + "\n"
    date = enterDateField.get() + "\n"
    info_label.configure(text="Saved:\n" + firstname + lastname + date + "to your birthday-library")

    phonelist.append([fnamevar.get(), lnamevar.get(), phonevar.get()])
    set_select()


def update_entry():
    phonelist[which_selected()] = [fnamevar.get(),
                                   lnamevar.get(),
                                   phonevar.get()]


def delete_entry():
    del phonelist[which_selected()]
    set_select()


def load_entry():
    fname, lname, phone = phonelist[which_selected()]
    fnamevar.set(fname)
    lnamevar.set(lname)
    phonevar.set(phone)


def openFrame():
    t = "Fill this window with last weeks birthday once saved dates in birthday db"
    top = Toplevel().title("Past Birthdays")
    msg = Message(top, text=t, bg="black", fg="pink", font=("Times", 32))
    msg.pack()

    button = Button(top, text="Schließen", command=top.destroy)
    button.pack()