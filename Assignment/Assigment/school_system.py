from tkinter import *
root = Tk()
root.geometry("700x900")


info = ["surname:","firstname:","subject:"]
for i in info:
	Label(root,
		Text=info[i]).grid(row=1,column=0)

	




root.mainloop()
