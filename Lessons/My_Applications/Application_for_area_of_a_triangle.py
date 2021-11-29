from tkinter import *
import tkinter as tk

#Is used for instantiating Tkinter GUI
window = tk.Tk()

#setting a title
window.title("Area of a triangle")

# window Resizability
window.resizable(width=True, height=False)

def area_triangle():
	breath = breath_entry.get()

	height = height_entry.get()
	area = (1/2) * (float(breath) * float(height))
	results.set(f'{round(area,3)}square meters')

#Initializing a frame
frame_entry = tk.Frame(master=window)
frame_entry.grid(row=1,column=2,sticky='e')

# creating an entry for breath
breath_entry = tk.Entry(master=frame_entry, width=15,)
breath_entry.grid(row=1,column=1,sticky=W+E)

# creating an entry for height
height_entry = tk.Entry(master=frame_entry, width=15)
height_entry.grid(row=2,column=1,sticky='w',pady=20)

# creating a label for entry widget for breath
breath_label = tk.Label(master=frame_entry,text=' BREATH',fg="black",bg= "grey")
breath_label.grid(row=1,column=2,sticky="w")

# creating a label for entry widger for height
height_label =tk.Label(master = frame_entry, text=' HEIGHT',fg="black",bg="grey")
height_label.grid(row=2,column=2,sticky="w")

# creating a button and passing the area_triangle() function to it
compute_button = tk.Button(master=window, text="CALCULATE",command=area_triangle)
compute_button.grid(row=3,column=2,pady=20)

#Initializinng a stringvar object
results = StringVar()
# setting string var to AREA
results.set("square meters")
#Creating a label  and passing the StringVar Object to it
result_label = tk.Label(master=window, textvariable=results)
result_label.grid(row=4,column=1, pady=20,sticky='e')
window.mainloop()
