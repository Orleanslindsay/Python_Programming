from tkinter import *
import math
root = Tk()
root.title("The Orleans Calculator")
#root.iconbitmap('C:\Users\FREEDOM OUTREACH\Desktop.ico')
e = Entry(root,width=25,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def button_click(number):
	current = e.get()
	e.delete(0,END)
	e.insert(0,str(current) + str(number))

def button_clear():
	e.delete(0,END)

def button_add():
	first_number = e.get()
	global f_num
	global math
	math = "addition"		
	f_num = int(first_number)
	e.delete(0,END)

def button_equal():
	second_number = e.get()
	e.delete(0,END)
	
	if math == "multiplication":
		e.insert(0, f_num * int(second_number))

	if math == "addition":
		e.insert(0,f_num + int(second_number))

	if math == "division":
		e.insert(0,f_num / int(second_number))
def button_multiply():
	first_number = e.get()
	global f_num
	global math
	math = "multiplication"		
	f_num = int(first_number)
	e.delete(0,END)

def button_division():
	first_number = e.get()
	global f_num
	global math
	math = "division"		
	f_num = int(first_number)
	e.delete(0,END)	

def button_substract():
	first_number = e.get()
	global f_num
	global math
	math = "substraction"		
	f_num = int(first_number)
	e.delete(0,END)
# Define buttons
button_1 = Button(root,text="1",padx=40,pady=20,command=lambda:button_click(1),fg = "black",bg = "grey")
button_2 = Button(root,text="2",padx=40,pady=20,command=lambda:button_click(2),fg = "black",bg = "grey")
button_3 = Button(root,text="3",padx=40,pady=20,command=lambda:button_click(3),fg = "black",bg = "grey")
button_4 = Button(root,text="4",padx=40,pady=20,command=lambda:button_click(4),fg = "black",bg = "grey")
button_5 = Button(root,text="5",padx=40,pady=20,command=lambda:button_click(5),fg = "black",bg = "grey")
button_6 = Button(root,text="6",padx=40,pady=20,command=lambda:button_click(6),fg = "black",bg = "grey")
button_7 = Button(root,text="7",padx=40,pady=20,command=lambda:button_click(7),fg = "black",bg = "grey")
button_8 = Button(root,text="8",padx=40,pady=20,command=lambda:button_click(8),fg = "black",bg = "grey")
button_9 = Button(root,text="9",padx=40,pady=20,command=lambda:button_click(9),fg = "black",bg = "grey")
button_0 = Button(root,text="0",padx=40,pady=20,command=lambda:button_click(0),fg = "black",bg = "grey")
button_add = Button(root,text="+",padx=39,pady=20,command=button_add,fg = "black",bg = "grey")
button_equal = Button(root,text="=",padx=40,pady=20,command=button_equal,fg = "black",bg = "grey")
button_substract = Button(root,text="-",padx=40.45,pady=20,command=button_substract,fg = "black",bg = "grey")
button_multiply = Button(root,text="*",padx=40,pady=20,command=button_multiply,fg = "black",bg = "grey")
button_divide = Button(root,text="/",padx=40,pady=20,command=button_division,fg = "black",bg = "grey")
button_clear = Button(root,text="clear",padx=47,pady=20,command=button_clear,fg = "black",bg = "grey")

# This code helps to exit the program
button_quit = Button(root,text="Exit Program",padx=60,pady=20,command=root.quit,bg="red").grid(row=8,column=1)


# Put the buttons on the screen
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
 
button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)
 
button_0.grid(row=4,column=0)

button_add.grid(row=5,column=0)
button_clear.grid(row=7,column=1)
button_equal.grid(row=4,column=2)
button_substract.grid(row=6,column=0)
button_add.grid(row=6,column=1)
button_divide.grid(row=6,column=2)
button_multiply.grid(row=4,column=1)
root.mainloop()
