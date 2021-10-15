from tkinter import *
import tkinter as tk
# is used for instantiate Tkinter GUI
window = tk.Tk()

# set title
window.title("Area  of  a circle")

# for  resizing
window.resizable(width=True, height=True)

def area_circle():
	"""
	function to compute the area of  a circle
	"""
	radius = radius_entry.get()
	area = (22/7) * (float(radius) ** 2)
	results.set(f'{round(area,3)}AREA')

# Initializzing a frame
frame_entry = tk.Frame(master=window)
frame_entry.grid(row=0, column=0, padx=10)

# creating an Enntry widget for raaduis
radius_entry = tk.Entry(master=frame_entry, width=10)
radius_entry.grid(row=0, column=0, sticky = 'e') #the e represents east

# Creating a laabel for the Entry widgget
radius_label = tk.Label(master=frame_entry, text = 'RADIUS')
radius_label.grid(row=0, column=1, sticky="w")

# Creating a button and passing the area_circle()function to it
compute_button = tk.Button(master=window, text="Calculate",command=area_circle)
compute_button.grid(row=0, column=1,padx=10)

#Initializinng a stringvar object
results = StringVar()
# setting string var to AREA
results.set("AREA")
#Creating a label  and passing the StringVar Object to it
result_label = tk.Label(master=window, textvariable=results)
result_label.grid(row=0,column=2, padx=10)
window.mainloop()
