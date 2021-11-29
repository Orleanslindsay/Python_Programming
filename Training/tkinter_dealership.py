from tkinter import *
import sys
import mariadb
import tkinter as tk


# Accessing your database portal
try:
	conn=mariadb.connect(
		user='root',
		password='benooriginal',
		host='localhost',
		port=3306,
		database='dealership')
except mariadb.Error as e:
	print('Error',e)
	sys.exit(1)



# Creating the widgets
root=tk.Tk()
root.geometry("200x200")
root.title("dealership Management")
root.configure(bg="light pink")

# Creating labels
labels=["Name: ","Model: ","Year: ","Chassis: ","Brand: "]
counter=2 #To give the row
for i in labels:
	Label(root,text=i,bg="pink").grid(row=counter,column=0,sticky=W)
	counter +=1
# creating entries
name_entry=Entry(root,).grid(row=2,column=1)
model_entry=Entry(root).grid(row=3,column=1)
year_entry=Entry(root).grid(row=4,column=1)
chassis_entry=Entry(root).grid(row=5,column=1)
brand_entry=Entry(root).grid(row=6,column=1)

def getData(na,mo,ye,ch,br):
	if na.get() and mo.get() and ye.get() and ch.get() and br.get():
		return (n.get(),m.get(),y.get(),c.get(),b.get())
	else:
		return None
def saveData():
	cur =conn.cursor()
	sqlinsert="INSERT INTO car(name,model,year,chassis,brand) VALUES(?,?,?,?,?)"
	mydata = getData(name_entry,model_entry,year_entry,chassis_entry,brand_entry)
	if mydata:
		cur.execute(sqlinsert,mydata)
		conn.commit()
		conn.close()


Button(root,text="Save",width=15,command=saveData).grid(row=7,column=1,pady=20)

root.mainloop()


