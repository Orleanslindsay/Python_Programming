from tkinter import *
import os
app = Tk()

entryframe = Frame(app)
entryframe.pack()

textentry = Entry(entryframe)
textentry.pack(fill="x")

buttonframe = Frame(app)
buttonframe.pack()

def entryhandler(val, textentry):
    oldentry = textentry.get()
    textentry.delete(0, END)
    textentry.insert(0, f'{oldentry}{val}')

def equating(textentry):
    oldvalue = textentry.get()
    if 'x' in oldvalue:
        oldvalue = oldvalue.replace('x', '*')
    newvalue = eval(oldvalue)
    textentry.delete(0, END)
    textentry.insert(0, f'{newvalue}')




content = [
    {"value": 0, "x": 3, "y": 0}, 
    {"value": 1, "x": 2, "y": 0}, 
    {"value": 2, "x": 2, "y": 1},
    {"value": 3, "x": 2, "y": 2},
    {"value": 4, "x": 1, "y": 0},
    {"value": 5, "x": 1, "y": 1},
    {"value": 6, "x": 1, "y": 2},
    {"value": 7, "x": 0, "y": 0},
    {"value": 8, "x": 0, "y": 1},
    {"value": 9, "x": 0, "y": 2},
    {"value": ".", "x": 3, "y": 1},
    {"value": "=", "x": 3, "y": 2},
    {"value": "+", "x": 3, "y": 3},
    {"value": "/", "x": 0, "y": 3},
    {"value": "x", "x": 1, "y": 3},
    {"value": "-", "x": 2, "y": 3}
]


for item in content:
    if item["value"] == "=":
        Button(buttonframe, text=str(item["value"]), bg="#ffef90", command= lambda x=str(item["value"]) : equating(textentry)).grid(column=item["y"], 
            row=item["x"])
    else:   
        Button(buttonframe, text=str(item["value"]), bg="#ffef90", command= lambda x=str(item["value"]) : entryhandler(x, textentry)).grid(column=item["y"], 
            row=item["x"])


"""for item in os.listdir(os.path.expanduser('~')):
     if item.isfile():
         print()
     elif item.isdir():
         print()
     else:
        print(item)"""

if __name__ == '__main__':
    # app.geometry("400x600")
    app.resizable()
    app.title("File Manager")
    app.mainloop()

# try class representation 
# complete app logic
# try using double loop
#
