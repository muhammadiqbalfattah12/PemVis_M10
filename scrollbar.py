from tkinter import *
root = Tk()
Scrollbar = Scrollbar(root)
Scrollbar.pack (side= RIGHT, fill=Y)
mylist = Listbox(root, yscrollcommand= Scrollbar.set)
for line in range (100):
    mylist.insert(END, "This is line number" + str(line))
mylist.pack ( side = LEFT, fill=BOTH)
Scrollbar.config( command=mylist.yview)

mainloop()