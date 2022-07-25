from tkinter import *
from gen import *

password = ""

root = Tk()
root.config(bg="#0c0e12")
root.title("Password Gen")
root.geometry('400x400')
root.resizable(False, False)

var1 = IntVar()
var2 = IntVar()

lenLabel = Label(root, text="Length:", bg="#0c0e12", fg="#ffffff")
lenLabel.place(x=10, y=40)
lenEntry = Entry(root, width=3)
lenEntry.place(x=60, y=40)

upperBtn = Checkbutton(root, variable=var1, bg="#0c0e12", activebackground="#0c0e12")
upperBtn.place(x=115, y=70)
upperLabel = Label(root, text="Uppercase Letters?:", bg="#0c0e12", fg="#ffffff")
upperLabel.place(x=10, y=70)

specialBtn = Checkbutton(root, variable=var2, bg="#0c0e12", activebackground="#0c0e12")
specialBtn.place(x=125, y=100)
specialLabel = Label(root, text="Special Charachters?:", bg="#0c0e12", fg="#ffffff")
specialLabel.place(x=10, y=100)

scroll = Scrollbar(root)
scroll.place(x=370, y=40, height=325)

listbox = Listbox(root, width=30, height=20, yscrollcommand=scroll.set)
listbox.place(x=180, y=40)

scroll.config(command=listbox.yview)

genBtn = Button(root, text="Generate", bg="#ffffff", command= lambda: listbox.insert(0, gen_pass(int(lenEntry.get()), var1.get(), var2.get())))
genBtn.place(x=10, y=130)

root.mainloop()