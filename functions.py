import os
import sqlite3
# Functions for events etc.

    # # display in label
    # info_label.configure(text="Saved:\n" + enterFirstField.get() + "\n" + enterLastField.get() + "\n" + enterDateField.get() + "\n" + "to your birthday-library")
    #
    # phonelist.append([enterFirstField.get(), enterLastField.get(), enterDateField.get()])
    # set_select()
    # # save in database
    #
    # db.schreibDB(enterFirstField.get(), enterLastField.get(), enterDateField.get())
    #
    # anzeige.configure(state='normal')
    # result = db.leseDB()
    # anzeige.delete(1.0, END)
    # anzeige.insert(END, result[0])
    # anzeige.configure(state='disabled')
    # datensaetze['text'] = "Anzahl Datensätzer: " + result[1]

def action(self):
    db = DB()
    self.status['text'] = ""
    db.schreibDB(self.nname.get(), self.vname.get())
    self.anzeige.configure(state='normal')
    result = db.leseDB()
    self.anzeige.delete(1.0, END)
    self.anzeige.insert(END, result[0])
    self.anzeige.configure(state='disabled')
    self.datensaetze['text'] = "Anzahl Datensätzer: " + result[1]

# # Function for checking input error when empty input is given in task field
# def inputError():
#     # check for enter task field is empty or not
#     if enterTaskField.get() == "":
#         # show the error message
#         messagebox.showerror("Input Error")
#         return 0
#     return 1