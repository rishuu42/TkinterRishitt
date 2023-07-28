#Basic Calculator Made Using Tkinter, will upgrade it into a Scientic Calculator soon, with a mode to switch.

from tkinter import *
import math
top = Tk() 
top.geometry("312x370")
top.resizable(0,0)
top.title("Calculator")

def bt_click(item):
    global expression
    expression = expression + str(item)        
    input_text.set(expression)
    
def bt_clear(): 
    global expression 
    expression = "" 
    input_text.set("")

def bt_equal():
    global expression
    result = str(eval(expression))
    x = expression
    input_text.set(result)
    expression = result
def bt_square():
    global expression
    expression = int(expression)**2
    input_text.set(expression)
def bt_root():
    global expression
    expression = int(expression)**0.5
    input_text.set(expression)
    
def factorial_():
    global expression
    expression=math.factorial(int(expression))
    input_text.set(expression)
    
def power():
    global expression
    
    
expression = ""
input_text = StringVar()
input_frame = Frame(top, width=312, height=100, bd=0, highlightbackground="#3B3A3A", highlightcolor="#3B3A3A", highlightthickness=1)
input_frame.pack(side=TOP)
input_field = Entry(input_frame, font=('arial', 18), textvariable=input_text,width=75, bg="#202121", bd=0, justify=RIGHT,fg="White")
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)

button_frame = Frame(top, width=312, height=372.5, bg="#202121")
button_frame.pack()

#buttons
root=Button(button_frame,text="√",fg="White",width=10,height=3,bd=0,bg = "#333332",command=lambda: bt_root())
root.grid(row=0,column=0, padx=1, pady=1)
squarex=Button(button_frame,text="x^y",fg="White",width=10,height=3,bd=0,bg = "#333332",command=lambda: bt_click("**"))
squarex.grid(row=0,column=1, padx=1, pady=1)
square=Button(button_frame,text="x²",fg="White",width=10,height=3,bd=0,bg = "#333332",command=lambda: bt_square())
square.grid(row=0,column=2, padx=1, pady=1)
fact=Button(button_frame,text="x!",fg="White",width=10,height=3,bd=0,bg = "#333332",command=lambda: factorial_())
fact.grid(row=0,column=3, padx=1, pady=1)

#row1
clear=Button(button_frame,text="C",fg="White",width=33,height=3,bd=0,bg = "#333332",command=lambda: bt_clear())
clear.grid(row=1,column=0,columnspan=3, padx=1, pady=1)
div=Button(button_frame,text="/",fg="White",width=10,height=3,bd=0,bg = "#333332",command=lambda: bt_click("/"))
div.grid(row=1,column=3, padx=1, pady=1)

#row2
nine=Button(button_frame,text="7",fg="White",width=10,height=3,bd=0,bg = "#3B3A3A",command=lambda: bt_click(7))
nine.grid(row=2,column=0, padx=1, pady=1)
eight=Button(button_frame,text="8",fg="White",width=10,height=3,bd=0,bg = "#3B3A3A",command=lambda: bt_click(8))
eight.grid(row=2,column=1, padx=1, pady=1)
seven=Button(button_frame,text="9",fg="White",width=10,height=3,bd=0,bg = "#3B3A3A",command=lambda: bt_click(9))
seven.grid(row=2,column=2, padx=1, pady=1)
product=Button(button_frame,text="*",fg="White",width=10,height=3,bd=0,bg = "#333332",command=lambda: bt_click("*"))
product.grid(row=2,column=3, padx=1, pady=1)
#row3
four=Button(button_frame,text="4",fg="White",width=10,height=3,bd=0,bg = "#3B3A3A",command=lambda: bt_click(4))
four.grid(row=3,column=0, padx=1, pady=1)
five=Button(button_frame,text="5",fg="White",width=10,height=3,bd=0,bg = "#3B3A3A",command=lambda: bt_click(5))
five.grid(row=3,column=1, padx=1, pady=1)
six=Button(button_frame,text="6",fg="White",width=10,height=3,bd=0,bg = "#3B3A3A",command=lambda: bt_click(6))
six.grid(row=3,column=2, padx=1, pady=1)
subtract=Button(button_frame,text="-",fg="White",width=10,height=3,bd=0,bg = "#333332",command=lambda: bt_click("-"))
subtract.grid(row=3,column=3, padx=1, pady=1)
#row4
one=Button(button_frame,text="1",fg="White",width=10,height=3,bd=0,bg = "#3B3A3A",command=lambda: bt_click(1))
one.grid(row=4,column=0, padx=1, pady=1)
two=Button(button_frame,text="2",fg="White",width=10,height=3,bd=0,bg = "#3B3A3A",command=lambda: bt_click(2))
two.grid(row=4,column=1, padx=1, pady=1)
three=Button(button_frame,text="3",fg="White",width=10,height=3,bd=0,bg = "#3B3A3A",command=lambda: bt_click(3))
three.grid(row=4,column=2, padx=1, pady=1)
add=Button(button_frame,text="+",fg="White",width=10,height=3,bd=0,bg = "#333332",command=lambda: bt_click("+"))
add.grid(row=4,column=3, padx=1, pady=1)
#row5
zero=Button(button_frame,text="0",fg="White",width=22,height=3,bd=0,bg="#3B3A3A",command=lambda:bt_click(0))
zero.grid(row=5,column=0,columnspan=2,padx=1,pady=1)
point=Button(button_frame,text=".",fg="white",width=10,height=3,bd=0,bg="#333332",command=lambda:bt_click("."))
point.grid(row=5,column=2,padx=1,pady=1)
evalu=Button(button_frame,text="=",fg="White",width=10,height=3,bd=0,bg="#333332",command=lambda:bt_equal())
evalu.grid(row=5,column=3,padx=1,pady=1)
top.mainloop()
