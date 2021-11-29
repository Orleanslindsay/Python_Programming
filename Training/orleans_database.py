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
		database='school_system')
except mariadb.Error as e:
	print('Error',e)

	sys.exit(1)

#Function for teachers
def saveData(Surname,First_name,Subject):
	Surname=Surname.get()
	firstname=First_name.get()
	subject=Subject.get()


#Creating the widget for the teacher 
root=tk.Tk()
cur=conn.cursor()

root.geometry("700x500")
root.title("School Management System")
root.configure(bg='light pink')

#username =os.environ.get("")



# For the reset button
def reset():
	return IntVar().set(0)


# Defining the first row
teacher_label=tk.Label(root,text='TEACHER',bg="white")
teacher_label.place(x=25,y=10)

surname_label=tk.Label(root,text='Surname:',bg="light pink").place(x=20,y=30)
firstname_label=tk.Label(root,text='First Name:',bg="light pink").place(x=20,y=55)
subject_label=tk.Label(root,text='Subject:',bg="light pink").place(x=20,y=80)

# Defining entries for the teacher
Subject=tk.Entry(root,width=30).place(x=85,y=80)
Surname=tk.Entry(root,width=30).place(x=80,y=30,)
First_name=tk.Entry(root,width=30).place(x=85,y=55)

# Defining rows for student 
student_label=tk.Label(root,text='STUDENT').place(x=385,y=10)
sn_student=tk.Label(root,text='Surname:',bg="light pink").place(x=385,y=30)
fn_student=tk.Label(root,text='First Name:',bg="light pink").place(x=385,y=52)
s_student=tk.Label(root,text='Stream:',bg="light pink").place(x=385,y=72)
g_student=tk.Label(root,text='Guardian:',bg="light pink").place(x=385,y=92)
gen_student=tk.Label(root,text='Gender:',bg="light pink").place(x=385,y=112)

# Defining entries for student
sn_student=tk.Entry(root,width=30).place(x=450,y=30,)
fn_student=tk.Entry(root,width=30).place(x=450,y=52,)
s_student=tk.Entry(root,width=30).place(x=450,y=72,)
g_student=tk.Entry(root,width=30).place(x=450,y=92,)
Radiobutton(root,text='Male',variable=StringVar(),value=1).place(x=450,y=112)
Radiobutton(root,text='Female',variable=StringVar(),value=2).place(x=520,y=112)
Radiobutton(root,text='None',variable=StringVar(),value=3).place(x=600,y=112)
Button(root,text="reset",command=reset()).place(x=490,y=150,width=100)

# Defining row for course
course=tk.Label(root,text='COURSE').place(x=310,y=220)

# Defining label for course
c_label=tk.Label(root,text="Subject:",bg="light pink").place(x=250,y=240)
stream_label=tk.Label(root,text='Stream:',bg="light pink").place(x=250,y=280)

#Defining enteries for course
c_label=tk.Entry(root,width=30).place(x=300,y=240)
stream_label=tk.Entry(root,width=30).place(x=300,y=280)

def getData(course,stram):
	return(course,stream)

def saveData():
	cur=conn.cursor()
	sqlinsert="INSERT INTO course(subject,stream) VALUES(?,?)"
	mydata = getData(c_label,stream_label)
	cur.execute(sqlinsert,mydata)
	conn.commit()
	conn.close()
saveData()	

root.mainloop()


