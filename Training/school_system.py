from tkinter import *
import mariadb
windows = Tk()
windows.title("School Management System")
windows.geometry("300x200")
windows.configure(bg="light pink")
windows.resizable(width=True,height=True)
# For teachers database 
teacher_label=Label(windows,text="TEACHER",fg="black",bg="light pink").grid(row=0,column=0)
firstname_Label=Label(windows,text="First name",fg='black',bg="light pink").grid(row=1,column=0)
surname_Label=Label(windows,text="surname",fg="black",bg="light pink").grid(row=2,column=0,sticky="w")
subject_label=Label(windows,text="Subject",bg="light pink").grid(row=3,column=0,sticky="w")
id_label=Label(windows,text="ID",bg="light pink").grid(row=4,column=0,sticky="w")

# For entry for teachers
entry_firstname=Entry(master=windows,width=25).grid(row=1,column=2)
entry_surname=Entry(master=windows,width=25).grid(row=2,column=2)
entry_subject=Entry(master=windows,width=25).grid(row=3,column=2)
entry_id=Entry(master=windows,width=25).grid(row=4,column=2)

# For students database
student_label=Label(windows,text="STUDENT",fg="black",bg="light pink").grid(row=7,column=0,sticky="s",pady=23)
surname_label=Label(windows,text="surname",fg="black",bg="light pink").grid(row=8,column=0,pady=7)



windows.mainloop()