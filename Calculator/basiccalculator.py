#Basic Calculator Made Using Tkinter, will upgrade it into a Scientic Calculator soon, with a mode to switch.

from tkinter import *
top = Tk() 
top.geometry("312x324")
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
    input_text.set(result)
    expression = ""

expression = ""
input_text = StringVar()
input_frame = Frame(top, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=1)
input_frame.pack(side=TOP)
input_field = Entry(input_frame, font=('arial', 18), textvariable=input_text, width=50, bg="#eee", bd=0, justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)

button_frame = Frame(top, width=312, height=272.5, bg="grey")
button_frame.pack()

#buttons
#row1
clear=Button(button_frame,text="C",fg="White",width=32,height=3,bd=0,bg = "#73706f",command=lambda: bt_clear())
clear.grid(row=0,column=0, columnspan=3, padx=1, pady=1)
div=Button(button_frame,text="/",fg="White",width=10,height=3,bd=0,bg = "#73706f",command=lambda: bt_click("/"))
div.grid(row=0,column=3, padx=1, pady=1)
#row2
nine=Button(button_frame,text="7",fg="Black",width=10,height=3,bd=0,bg = "#ccc",command=lambda: bt_click(7))
nine.grid(row=1,column=0, padx=1, pady=1)
eight=Button(button_frame,text="8",fg="Black",width=10,height=3,bd=0,bg = "#ccc",command=lambda: bt_click(8))
eight.grid(row=1,column=1, padx=1, pady=1)
seven=Button(button_frame,text="9",fg="Black",width=10,height=3,bd=0,bg = "#ccc",command=lambda: bt_click(9))
seven.grid(row=1,column=2, padx=1, pady=1)
product=Button(button_frame,text="*",fg="White",width=10,height=3,bd=0,bg = "#73706f",command=lambda: bt_click("*"))
product.grid(row=1,column=3, padx=1, pady=1)
#row3
four=Button(button_frame,text="4",fg="Black",width=10,height=3,bd=0,bg = "#ccc",command=lambda: bt_click(4))
four.grid(row=2,column=0, padx=1, pady=1)
five=Button(button_frame,text="5",fg="Black",width=10,height=3,bd=0,bg = "#ccc",command=lambda: bt_click(5))
five.grid(row=2,column=1, padx=1, pady=1)
six=Button(button_frame,text="6",fg="Black",width=10,height=3,bd=0,bg = "#ccc",command=lambda: bt_click(6))
six.grid(row=2,column=2, padx=1, pady=1)
subtract=Button(button_frame,text="-",fg="White",width=10,height=3,bd=0,bg = "#73706f",command=lambda: bt_click("-"))
subtract.grid(row=2,column=3, padx=1, pady=1)
#row4
one=Button(button_frame,text="1",fg="Black",width=10,height=3,bd=0,bg = "#ccc",command=lambda: bt_click(1))
one.grid(row=3,column=0, padx=1, pady=1)
two=Button(button_frame,text="2",fg="Black",width=10,height=3,bd=0,bg = "#ccc",command=lambda: bt_click(2))
two.grid(row=3,column=1, padx=1, pady=1)
three=Button(button_frame,text="3",fg="Black",width=10,height=3,bd=0,bg = "#ccc",command=lambda: bt_click(3))
three.grid(row=3,column=2, padx=1, pady=1)
add=Button(button_frame,text="+",fg="White",width=10,height=3,bd=0,bg = "#73706f",command=lambda: bt_click("+"))
add.grid(row=3,column=3, padx=1, pady=1)
#row5
zero=Button(button_frame,text="0",fg="black",width=21,height=3,bd=0,bg="#ccc",command=lambda:bt_click(0))
zero.grid(row=4,column=0,columnspan=2,padx=1,pady=1)
point=Button(button_frame,text=".",fg="white",width=10,height=3,bd=0,bg="#73706f",command=lambda:bt_click("."))
point.grid(row=4,column=2,padx=1,pady=1)
evalu=Button(button_frame,text="=",fg="White",width=10,height=3,bd=0,bg="#73706f",command=lambda:bt_equal())
evalu.grid(row=4,column=3,padx=1,pady=1)
top.mainloop()
