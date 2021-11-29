from tkinter import *

root = Tk()
# creating an Entry
e = Entry(root,width = 20,bg="light blue")
e.pack()
e.insert(0, "Enter your name")

# Creating a button
def my_button():
	my_label=Label(root,text=e.get() + " is a very good programmer",fg="red")
	my_label.pack()
my_button = Button(root,text="Click Me!",padx=5,pady=5,command=my_button,fg="white",bg="black")
my_button.pack()
root.mainloop()