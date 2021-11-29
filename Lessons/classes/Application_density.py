from tkinter import *
import tkinter as tk

#Is used for instantiating Tkinter GUI
window = tk.Tk()

#setting a title
window.title("Density of a body")

# window Resizability
window.resizable(width=True, height=True)


def density_of_a_body():
	mass = mass_entry.get()
	volume = volume_entry.get()
	density = float(mass) /float(volume)
	results.set(f'{round(density,3)}kilograms per cubic metre')

#Initializing a frame
frame_entry = tk.Frame(master=window)
frame_entry.grid(row=1,column=2,sticky='e')

# creating an entry for breath
mass_entry = tk.Entry(master=frame_entry, width=15)
mass_entry.grid(row=1,column=1,sticky='s')

# creating an entry for height
volume_entry = tk.Entry(master=frame_entry, width=15)
volume_entry.grid(row=2,column=1,sticky='w',pady=20)

# creating a label for entry widget for breath
mass_label = tk.Label(master=frame_entry,text='ENTER MASS / Kg')
mass_label.grid(row=1,column=2,sticky="w")

# creating a label for entry widger for height
volume_label =tk.Label(master = frame_entry, text='ENTER VOLUME / cubic metre')
volume_label.grid(row=2,column=2,sticky="w")

# creating a button and passing the density of the body () function to it
compute_button = tk.Button(master=window, text="CALCULATE",command=density_of_a_body)
compute_button.grid(row=3,column=2,pady=20)

#Initializinng a stringvar object
results = StringVar()
# setting string var to AREA
results.set("kilogram per cubic metre")
#Creating a label  and passing the StringVar Object to it
result_label = tk.Label(master=window, textvariable=results)
result_label.grid(row=4,column=2, pady=20,sticky='e')
window.mainloop()
