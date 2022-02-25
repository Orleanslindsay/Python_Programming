from tkinter import *
root = Tk()
root.title("Sales Management System")
root.geometry("600x400")
root.configure(bg='light blue')

actual_price=Label(root,text='price').place(x=15,y=20)
actual_price=Entry(root,width=30).place(x=54,y=20)




root.mainloop()