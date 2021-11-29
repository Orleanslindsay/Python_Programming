from tkinter import *
import mariadb
root = Tk()
root.title('SCHOOL MANAGEMENT')

root.geometry("900x700")


counter=2
for i in range(1,20):
	
	label=Entry(root).grid(row=counter,column=0)
	counter += 2



root.mainloop()