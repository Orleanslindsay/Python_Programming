from tkinter import *
import tkinter as tk

#Is used for instantiating Tkinter GUI
window = tk.Tk()

#setting a title
window.title("Body mass index")

# window Resizability
window.resizable(width=True, height=True)

def body_mass_index():
	weight =weight_entry.get()
	height = height_entry.get()
	mass_index = float(weight) / (float(height) ** 2)
	results.set(f'{round(mass_index)}Kg/m^2')
if results.set() < 18.5:
	print("You are underweight")

#elif results >= 18.5 and < 25:
	print("You have a normal weight.")

elif results.set() >= 25 and results < 30:
	print("You are overweight.")

else:
	print("You are obese.")
result_label

#Initializing a frame
frame_entry = tk.Frame(master=window)
frame_entry.grid(row=1,column=2,sticky='e')

# creating an entry for weight
weight_entry = tk.Entry(master=frame_entry, width=15)
weight_entry.grid(row=1,column=1,sticky='s')

# creating an entry for height
height_entry = tk.Entry(master=frame_entry, width=15)
height_entry.grid(row=2,column=1,sticky='w',pady=20)

# creating a label for entry widget for height
weight_label = tk.Label(master=frame_entry,text=' ENTER WEIGHT / Kg')
weight_label.grid(row=1,column=2,sticky="w")

# creating a label for entry widger for height
height_label =tk.Label(master = frame_entry, text='ENTER HEIGHT / cubic metre')
height_label.grid(row=2,column=2,sticky="w")

# creating a button and passing the area_triangle() function to it
compute_button = tk.Button(master=window, text="CALCULATE",command=body_mass_index)
compute_button.grid(row=3,column=2,pady=20)

#Initializinng a stringvar object
results = StringVar()
# setting string var to AREA
results.set("Kg/m^2")
#Creating a label  and passing the StringVar Object to it
result_label = tk.Label(master=window, textvariable=results)
result_label.grid(row=4,column=2, pady=20,sticky='e')
window.mainloop()






















