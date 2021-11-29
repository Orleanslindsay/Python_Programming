import os

from tkinter import *

window=Tk()
    

large_font = ('calculator',25)

window.geometry("300x400")
window.title("Progressive Python")
window.configure(bg="grey40")



def btnClick(numbers):
    global operator
    operator=operator + str(numbers)
    text_input.set(operator)


operator=""
text_input=StringVar()


window.resizable(height=False,width=False)
entryfram=Frame(window,bg="grey")
entryfram.pack(fill="x")

buttonframe=Frame(window,bg="grey40")
buttonframe.pack(fill="x",padx=15,pady=15)

displaytext=Entry(entryfram,font=large_font,bg="#ffef90",textvariable=text_input)
displaytext.pack(fill="x",padx=15,pady=15)



content = [{"value": 0, "x": 5, "y": 1}, 
{"value": 1, "x": 3, "y": 0}, 
{"value": 2, "x": 3, "y": 1},
{"value": 3, "x": 3, "y": 2}
,{"value": 4, "x": 3, "y": 3}
,{"value": 5, "x": 4, "y": 0}
,{"value": 6, "x": 4, "y": 1}
,{"value": 7, "x": 4, "y": 2}
,{"value": 8, "x": 4, "y": 3}
,{"value": 9, "x": 5, "y": 0}
,{"value": "+", "x": 5, "y":2}
,{"value": 5, "x": 4, "y": 0}]


for item in content:
    Button(buttonframe,width="5",font="bold",text=str(item["value"]), bg="gold",command= lambda :btnClick(text_input)).grid(column=item["y"], 
    row=item["x"])
    


window.mainloop()