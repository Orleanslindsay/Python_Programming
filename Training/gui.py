from tkinter import *
root = Tk()

#creating a Label widget
my_label1 = Label(root, text="Hello Orleans")

my_label2 = Label(root, text="My name is Joseph Orleans")


my_label1.grid(row=0,column=0)
my_label2.grid(row=1,column=1)

#Showing it onto the screen
root.mainloop( )