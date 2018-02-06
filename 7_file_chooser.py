# 7_file_chooser.py

from tkinter import *
import tkinter.filedialog as fd

class App:

    def __init__(self, master):
        b=Button(master, text='File..', command=self.ask_file).pack()

    def ask_file(self):
        """ This function opens the file chooser
            and then prints out the name of chosen file """
        file = fd.askopenfilename()
        print("File name= " + str(file))

root =Tk()
app = App(root)
root.mainloop()
