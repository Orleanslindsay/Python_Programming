import tkinter as tk
teachers = "Surname","First Name","Subject,ID"

def fetch(entries):
	for entry in entries:
		teacher = entry[0]
		text = entry[1]
		print('%s: "%s"' % (teacher,field))

def makeform(root,teacher):
	entries = []
	for teacher in teachers:
		row = tk.Frame(root)
		lab = tk.Label(row,width=15,text=teachers,anchor="w")

		enter = tk.Entry(row)
		row.pack(side=tk.TOP,fill=tk.X, padx=5,pady=5)
		lab.pack(side=tk.RIGHT, expand=tk.YES,fill=tk.X)
		entries.append((teachers,enter))
	return entries

	if __name__ =="__main__":
		root = tk.Tk()
		ents=makeform(root,fields)
		root.bind('<Return>',(lambda event,e=ents:fetch(e)))

		b1= tk.Button(root,text="Save",
			command=(lambda e=ents:fetch()))
		b1.pack(side=tk.LEFT,padx=5,pady=5)
		root.mainloop()		