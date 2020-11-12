import tkinter as tk
from tkinter import ttk
from tkinter import END,INSERT
from tkinter import font
from functools import partial

keyb = tk.Tk()  # key window name
keyb.title('Keasy Keyboard')  # title Name

wd = 4 # width of keys
entry_font = font.Font(family="Helvetica",size=12) # font used
button_font = font.Font(family="Helvetica",size= 15,weight="bold") # font used
alt_font = font.Font(family="Helvetica",size= 11,weight="bold") # font used
button_y = 4 # height of buttons

# Size window size
keyb.geometry('895x550')  # normal size
keyb.minsize(width= 895 , height = 550)  # minimum size
keyb.configure(bg = '#FF99FF')  # add background color 

inp_text = tk.Text(keyb,font = entry_font,height = 2)
inp_text.grid(rowspan = 3 , columnspan = 5000, ipadx = 80 , ipady = 4, padx = 4, pady = 10)
inp_text.focus_set()


# Press function
def press(inp):
    inp_text.insert(INSERT,str(inp))

# Clear function
def clear():
    inp_text.delete(0,END)

# First Line
line = "`1234567890"
k1 =  [0 for x in range(15)]

j = 0 
for j in range(15):
    k1[j] = tk.Button(keyb)
    k1[j].grid(row = 3 , column = j)

"""
k1[0] = tk.Button(keyb,text = "~    \n     `", width = wd, command = partial(press,line[0]), font = alt_font,bd = 4)
k1[0].grid(row = 3 , column = j, columnspan = 2*wd, ipady = button_y-4)
j = j + 2*wd

for i in range(1,11):
    k1[i] = tk.Button(keyb,text = str(line[i]), width = wd, command = partial(press,line[i]), font = button_font,bd = 4)
    k1[i].grid(row = 3 , column = j, columnspan = 2*wd, ipady = button_y)
    j = j + 2*wd
"""


# Second Line
line = "QWERTYUIOP"
k2 =  [0 for x in range(14)]

ktab = tk.Button(keyb,text = "Tab", width = wd+7, command = print("a") ,font = alt_font, bd = 4)
ktab.grid(row = 4 , column = 0, columnspan = 22, sticky = 'nsew',padx = (5,0),ipady = button_y+5)

j = 22 

for i in range(10):
    k2[i] = tk.Button(keyb,text = str(line[i]), width = wd, command = partial(press,line[i]), font = button_font,bd = 4)
    k2[i].grid(row = 4 , column = j, columnspan = 2*wd, ipady = button_y)
    j = j + 2*wd

k2[11] = tk.Button(keyb,text = "{    \n     ]", width = wd, command = partial(press,line[i]), font = alt_font,bd = 4)
k2[11].grid(row = 4 , column = j, columnspan = 2*wd, ipady = button_y-4)
j = j + 2*wd

k2[12] = tk.Button(keyb,text = "}    \n     [", width = wd, command = partial(press,line[i]), font = alt_font,bd = 4)
k2[12].grid(row = 4 , column = j, columnspan = 2*wd, ipady = button_y-4)
j = j + 2*wd

k2[13] = tk.Button(keyb,text = "|    \n     \\", width = wd, command = partial(press,line[i]), font = alt_font,bd = 4)
k2[13].grid(row = 4 , column = j, columnspan = 2*wd, ipady = button_y-4)
j = j + 2*wd

# second line end

keyb.mainloop()  # using ending point
