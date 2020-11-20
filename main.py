import tkinter as tk
from tkinter import ttk
from tkinter import END,INSERT
from tkinter import font
from functools import partial
from gtts import gTTS
import os
from playsound import playsound
from predict import predict
from predict import load_model

keyb = tk.Tk()  # Root Window
model = load_model()

# region of Variables
keyb.title('Keasy Keyboard') # title Name
button_wd = 6 # width of keys
button_hg = 18 # height of buttons-09876543
entry_font = font.Font(family="Helvetica",size=20) # font used
button_font = font.Font(family="Helvetica",size= 15,weight="bold") # font used
alt_font = font.Font(family="Helvetica",size= 11,weight="bold") # font used
Key_colour = '#FFDDFF'
Accent_colour = '#967bb6'
Accent_colour2 = '#FF99FF'
Accent_colour3 = '#E1AD01'
Bg_Colour = '#FFFFFF'
Row_index = (3,4,5,6,7,8,2)

#endregion of Variables

# Keyboard configuration Area
keyb.geometry('1210x650')  # normal size
keyb.minsize(width= 1210 , height = 650)  # minimum size
keyb.maxsize(width= 1210 , height = 650)  # minimum size
keyb.configure(bg = Bg_Colour)  # add background color 

# Text Entry Area
inp_text = tk.Text(keyb,font = entry_font,height = 2)
inp_text.grid(rowspan = 2 , column = 0, columnspan = 500, ipadx = 3 , ipady = 4)
inp_text.focus_set()

# definition of Key Functions
def press(inp):
    inp_text.insert(INSERT,str(inp))
    inp_text.see(INSERT)
    try:
        playsound("Audios/"+str(inp)+".mp3")
    except: pass 
def clear():
    inp_text.delete(1.0,END)
    inp_text.see(INSERT)
def up():
    inp_text.mark_set("insert", "insert-1l")
    inp_text.see(INSERT)
def down():
    inp_text.mark_set("insert", "insert+1l")
    inp_text.see(INSERT)
def right():
    inp_text.mark_set("insert", "insert+1c")
    inp_text.see(INSERT)
def left():
    inp_text.mark_set("insert", "insert-1c")
    inp_text.see(INSERT)
def enter():
    inp_text.insert(INSERT,'\n')
    inp_text.see(INSERT)
def backs():
    inp_text.delete("insert-1c",INSERT)    
    inp_text.see(INSERT)
def speak(inp = ''):
    if inp == '':
        inp = inp_text.get(1.0,END)
    tts = gTTS(inp.lower(),lang='en')
    tts.save("voice.mp3")
    playsound("voice.mp3")
    os.remove("voice.mp3")
def space():
    inp_text.insert(INSERT," ")
    inp_text.see(INSERT)
    text = inp_text.get(1.0,END)
    try: speak(text.rsplit(' ',2)[1])
    except : speak()

# region of Basic Keys

# First Line

line = "~!@#$%^&*()_+["
l1 =  [0 for x in range(len(line))]
j = 0
for i in range(len(line)):
    l1[i] = tk.Button(keyb,text = str(line[i]), width = button_wd, command = partial(press,line[i]), font = button_font,bd = 4, bg = Accent_colour2)
    l1[i].grid(row = Row_index[0] , column = j, ipady = button_hg-18)
    j = j + 1

# Second Line

line = "`1234567890-=]"
l2 =  [0 for x in range(len(line))]
j = 0
for i in range(len(line)):
    l2[i] = tk.Button(keyb,text = str(line[i]), width = button_wd, command = partial(press,line[i]), font = button_font,bd = 4, bg = Key_colour)
    l2[i].grid(row = Row_index[1] , column = j, ipady = button_hg-10)
    j = j + 1

# Third Line

line = "QWERTYUIOP{}|\\"
l3 =  [0 for x in range(len(line))]
j = 0
for i in range(len(line)):
    l3[i] = tk.Button(keyb,text = str(line[i]), width = button_wd, command = partial(press,line[i]), font = button_font,bd = 4, bg = Key_colour)
    l3[i].grid(row = Row_index[2] , column = j, ipady = button_hg)
    j = j + 1

# Fourth Line

line = "ASDFGHJKL:;\"'/"
l4 =  [0 for x in range(len(line))]
j = 0
for i in range(len(line)):
    l4[i] = tk.Button(keyb,text = str(line[i]), width = button_wd, command = partial(press,line[i]), font = button_font,bd = 4, bg = Key_colour)
    l4[i].grid(row = Row_index[3] , column = j, ipady = button_hg)
    j = j + 1

# Fifth Line

line = "ZXCVBNM,.?<"
l5 =  [0 for x in range(len(line))]
j = 0
for i in range(len(line)):
    l5[i] = tk.Button(keyb,text = str(line[i]), width = button_wd, command = partial(press,line[i]), font = button_font,bd = 4, bg = Key_colour)
    l5[i].grid(row = Row_index[4] , column = j, ipady = button_hg)
    j = j + 1

# endregion of Basic Keys

# region of Function Keys

# Tab Key
Tab = tk.Button(keyb,text = "Tab", width = button_wd, command =  partial(press,"\t"), font = button_font,bd = 4,bg = Accent_colour)
Tab.grid(row = Row_index[5] , column = 0, ipady = button_hg-10)

# Clear Key
Clear = tk.Button(keyb,text = "Clear", width = button_wd+7, command =  lambda : clear(), font = button_font,bd = 4,bg = Accent_colour)
Clear.grid(row = Row_index[5] , column = 1, columnspan = 2, ipady = button_hg-10)

# Space Key
Space = tk.Button(keyb,text = "Space", width = button_wd+22, command =  lambda : space(), font = button_font,bd = 4,bg = Accent_colour)
Space.grid(row = Row_index[5] , column = 3, columnspan = 4, ipady = button_hg-10)

# Enter Key
Enter = tk.Button(keyb,text = "Enter", width = button_wd+7, command =  lambda : enter(), font = button_font,bd = 4,bg = Accent_colour)
Enter.grid(row = Row_index[5] , column = 7, columnspan = 2, ipady = button_hg-10)

# Up Key
Up = tk.Button(keyb,text = "Up", width = button_wd, command =  lambda : up(), font = button_font,bd = 4,bg = Accent_colour2)
Up.grid(row = Row_index[5]-1 , column = 12, ipady = button_hg-10,pady = (20,0))

# Down Key
Down = tk.Button(keyb,text = "Down", width = button_wd, command =  lambda : down(), font = button_font,bd = 4,bg = Accent_colour2)
Down.grid(row = Row_index[5] , column = 12, ipady = button_hg-10)

# Right Key
Right = tk.Button(keyb,text = "Right", width = button_wd-1, command =  lambda : right(), font = button_font,bd = 4,bg = Accent_colour2)
Right.grid(row = Row_index[5] , column = 13, ipady = button_hg-10,padx = (0,11))

# Left Key
Left = tk.Button(keyb,text = "Left", width = button_wd-1, command =  lambda : left(), font = button_font,bd = 4,bg = Accent_colour2)
Left.grid(row = Row_index[5] , column = 11, ipady = button_hg-10,padx = (11,0))

# BackSpace Key
Backs = tk.Button(keyb,text = "Backspace", width = button_wd+7, command =  lambda : backs(), font = button_font,bd = 4,bg = Accent_colour)
Backs.grid(row = Row_index[5] , column = 9, columnspan = 2, ipady = button_hg-10)

#Speak Key
Speak = tk.Button(keyb,text = "Speak", width = button_wd+127, command =  lambda : speak(), font = alt_font,bd = 4,bg = Accent_colour3)
Speak.grid(row = Row_index[6] , column = 0, columnspan = 15, ipady = button_hg-18)

# endregion of Functional Keys

keyb.mainloop()  # using ending point