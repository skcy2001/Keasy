import tkinter as tk
from tkinter import ttk
from tkinter import END,INSERT
from tkinter import font
from functools import partial

keyb = tk.Tk()  # key window name
keyb.title('Keasy Keyboard')  # title Name

wd = 6 # width of keys
entry_font = font.Font(family="Helvetica",size=20) # font used
button_font = font.Font(family="Helvetica",size= 15,weight="bold") # font used
alt_font = font.Font(family="Helvetica",size= 11,weight="bold") # font used
button_y = 18 # height of buttons

# Size window size
keyb.geometry('930x550')  # normal size
keyb.minsize(width= 1230 , height = 550)  # minimum size
keyb.configure(bg = '#FF99FF')  # add background color 

inp_text = tk.Text(keyb,font = entry_font,height = 2)
inp_text.grid(rowspan = 2 , column = 0, columnspan = 500, ipadx = 8 , ipady = 4, padx = 5, pady = 6)
inp_text.focus_set()


# Press function
def press(inp):
    inp_text.insert(INSERT,str(inp))

# Clear function
def clear():
    inp_text.delete(0,END)

# First Line

line = "~1234567890-+"
k1 =  [0 for x in range(len(line))]
j = 1
for i in range(len(line)):
    k1[i] = tk.Button(keyb,text = str(line[i]), width = wd, command = partial(press,line[i]), font = button_font,bd = 4)
    k1[i].grid(row = 3 , column = j, ipady = button_y)
    j = j + 1

# Second Line

line = "QWERTYUIOP{}|"
k2 =  [0 for x in range(len(line))]
j = 1
for i in range(len(line)):
    k2[i] = tk.Button(keyb,text = str(line[i]), width = wd, command = partial(press,line[i]), font = button_font,bd = 4)
    k2[i].grid(row = 4 , column = j, ipady = button_y)
    j = j + 1

# Third Line

line = "ASDFGHJKL:;\"'"
k3 =  [0 for x in range(len(line))]
j = 1
for i in range(len(line)):
    k3[i] = tk.Button(keyb,text = str(line[i]), width = wd, command = partial(press,line[i]), font = button_font,bd = 4)
    k3[i].grid(row = 5 , column = j, ipady = button_y)
    j = j + 1

# Fourth Line

line = "ZXCVBNM,.?<>/"
k4 =  [0 for x in range(len(line))]
j = 1
for i in range(len(line)):
    k4[i] = tk.Button(keyb,text = str(line[i]), width = wd, command = partial(press,line[i]), font = button_font,bd = 4)
    k4[i].grid(row = 6 , column = j, ipady = button_y)
    j = j + 1

keyb.mainloop()  # using ending point
