#Q1 Write a python program using tkinter interface to write Hello World and a exit button that closes the interface.
import tkinter
from tkinter import *
import sys
root= Tk()
l1=Label(root,text='Hello world!',fg='Blue',bg='black',width=25)
l1.pack()
b=Button(root,text='Exit',command=exit)
b.pack()
root.mainloop()
print("\n")


#Q2. Write a python program to in the same interface as above and create a action
#when the button is click it will display some text.
from tkinter import *
def show():
    print("Hello guys welcome to my GUI")
root= Tk()
b=Button(root,text='Click here',fg='red',bg='Black',command=show)
b.pack()
root.mainloop()



#Q3. Create a frame using tkinter with any label text and two buttons.
   #One to exit and other to change the label to some other text.

from tkinter import *

def display():
    var.set("Hello Everyone!,welcome to our python class")

def terminate():
    exit(0)

root = Tk()

var=StringVar()

root.geometry("300x300")

b1 = Button(root,text="click",width=60,bg='blue',font='black',command=display)
b1.pack()

b2 = Button(root,text="exit",width=60,bg='blue',font='black',command=terminate)
b2.pack()

var.set("This class will definitely going to help you all to understand about pyhton language ")
label=Label(textvariable=var)
label.pack()
root.mainloop()
print("\n")


#Q4-Write a python program using tkinter interface to take an input in the GUI program and print it
from tkinter import *

def show():
    print(entry.get())

root=Tk()

entry=Entry(root,width=60,bg='orange',font='black')
entry.pack()
a=Button(root,text='click here',width=20,bg='red',command=show)
a.pack()
b=Button(root,text="exit",width=20,fg='green',bg="blue",command=exit)
b.pack()
root.mainloop()