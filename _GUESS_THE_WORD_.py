#!/usr/bin/env python
# coding: utf-8

# In[5]:


import tkinter
from tkinter import *
import random
from tkinter import messagebox


answers = [
    "python",
    "java",
    "hostel",
    "canada",
    "india",
    "panjab",
    "lovely",
]

words = [
    "nptoyh",
    "avja",
    "steloh",
    "cdanaa",
    "aidin",
    "bjaanp",
    "evloyl",
]


num =  random.randrange(0, len(words), 1)

def default():
    global words,answers,num
    lbl.config(text = words[num])

def res():
    global words,answers,num
    num = random.randrange(0, len(words), 1)
    lbl.config(text = words[num])
    e1.delete(0, END)


def checkans():
    global words,answers,num
    var = e1.get()
    if var == answers[num]:
        messagebox.showinfo("Success", "This is a correct answer")
        res()
    else:
        messagebox.showerror("Error", "This is not Correct")
        e1.delete(0, END)




root = tkinter.Tk()
root.geometry("500x500")
root.title("_GUESS_THE_WORD_")
root.configure(background = "cornflowerblue")

NAME = Label(
    
    text = "Made by",
    font = ("Verdana", 18),
    bg = "cornflowerblue",
    fg = "lawngreen",
)
NAME.pack()

NAME1 = Label(
    
    text = "Toushik Sarkar & Manish Das",
    font = ("Comic sans ms", 16),

     bg = "cornflowerblue",
    fg = "lawngreen",
)
NAME1.pack()

NAME1 = Label(
    
    text = "Mentor:-Neha Bagga",
    font = ("Verdana", 18),
    bg = "cornflowerblue",
    fg = "lawngreen",
)
NAME1.pack()

lebel = Label(
    
    text = "Now try to solve the question",
    font = ("Verdana", 18),
    bg = "gray",
    fg = "#FFFFFF",
)
lebel.pack()

lbl = Label(
    root,
    text = "Your here",
    font = ("Verdana", 18),
    bg = "gray",
    fg = "#FFFFFF",
)
lbl.pack(pady = 30,ipady=10,ipadx=10)


ans1 = StringVar()
e1 = Entry(
    root,
    font = ("Verdana", 16),
    textvariable = ans1,
)
e1.pack(ipady=5,ipadx=5)

btncheck = Button(
    root,
    text = "Check",
    font = ("Comic sans ms", 16),
    width = 16,
    bg = "#4c4b4b",
    fg = "#6ab04c",
    relief = GROOVE,
    command = checkans,
)
btncheck.pack(pady = 40)

btnreset = Button(
    root,
    text = "Reset",
    font = ("Comic sans ms", 16),
    width = 16,
    bg = "#4c4b4b",
    fg = "#EA425C",
    relief = GROOVE,
    command = res,
)
btnreset.pack()

default()
root.mainloop()


# In[ ]:




