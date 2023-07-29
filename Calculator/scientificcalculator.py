# Made the Scientific Calculator, now i plan to add a switch between the two

from tkinter import *
import math
top = Tk() 
top.geometry("390x375")
top.resizable(0,0)
top.title("Calculator")

def create_button(parent, text, command, **kwargs):
    return Button(parent, text=text, command=command, font=('Helvetica', 9, "bold"), **kwargs)

class Operations: 
    expression = ""
    
    def bt_click(item):
        Operations.expression = Operations.expression + str(item)        
        input_text.set(Operations.expression)
    
    def bt_clear(): 
        Operations.expression = "" 
        input_text.set("")
    
    def bt_equal():
        result = str(eval(Operations.expression))
        x = Operations.expression
        input_text.set(result)
        Operations.expression = result

    def bt_square():
        Operations.expression = int(Operations.expression)**2
        input_text.set(Operations.expression)
        
    def bt_root():
        Operations.expression = int(Operations.expression)**0.5
        input_text.set(Operations.expression)
        
    def factorial_():
        Operations.expression=math.factorial(int(Operations.expression))
        input_text.set(Operations.expression)
        
    def delete_last_expression():
        Operations.expression = Operations.expression[:-1]
        input_text.set(Operations.expression)

    def bt_sin():
        Operations.expression = math.sin(math.radians(int(Operations.expression)))
        input_text.set(expression)
        
    def bt_cos():
        Operations.expression = math.cos(math.radians(int(Operations.expression)))
        input_text.set(Operations.expression)
        
    def bt_tan():
        Operations.expression = math.tan(math.radians(int(Operations.expression)))
        input_text.set(expression)
        
    def bt_cot():
        Operations.expression = 1/math.tan(math.radians(int(Operations.expression)))
        input_text.set(Operations.expression)
    def bt_sec():
        Operations.expression = 1/math.cos(math.radians(int(Operations.expression)))
        input_text.set(Operations.expression)
    def bt_cosec():
        Operations.expression = 1/math.sin(math.radians(int(Operations.expression)))
        input_text.set(Operations.expression)
        
input_text = StringVar()
input_frame = Frame(top, width=450, height=200, bd=0, highlightbackground="#3B3A3A", highlightcolor="#3B3A3A", highlightthickness=1)
input_frame.pack(side=TOP)
input_field = Entry(input_frame, font=('Helvetica', 18), textvariable=input_text,width=100, bg="#202121", bd=0, justify=RIGHT,fg="White")
input_field.grid(row=1, column=0)
input_field.pack(ipady=10)

button_frame = Frame(top, width=450, height=420, bg="#202121")
button_frame.pack()

#buttons
root=create_button(button_frame,text="√",fg="White",width=10,height=3,bd=0,bg = "#333332",command=lambda: Operations.bt_root()).grid(row=0,column=0, padx=1, pady=1)
squarex=create_button(button_frame,text="xⁿ",fg="White",width=10,height=3,bd=0,bg = "#333332",command=lambda: Operations.bt_click("**")).grid(row=0,column=1, padx=1, pady=1)
square=create_button(button_frame,text="x²",fg="White",width=10,height=3,bd=0,bg = "#333332",command=lambda: Operations.bt_square()).grid(row=0,column=2, padx=1, pady=1)
fact=create_button(button_frame,text="x!",fg="White",width=10,height=3,bd=0,bg = "#333332",command=lambda: Operations.factorial_()).grid(row=0,column=3, padx=1, pady=1)
sin=create_button(button_frame,text="sin",fg="White",width=10,height=3,bd=0,bg = "#333332",command=lambda: Operations.bt_sin()).grid(row=0,column=4, padx=1, pady=1)

#row1
powerten=create_button(button_frame,text="⌫",fg="White",width=10,height=3,bd=0,bg = "#333332",command=lambda: Operations.delete_last_expression()).grid(row=1,column=0, padx=1, pady=1)
clear=create_button(button_frame,text="C",fg="White",width=21,height=3,bd=0,bg = "#333332",command=lambda: Operations.bt_clear()).grid(row=1,column=1,columnspan=2, padx=1, pady=1)
div=create_button(button_frame,text="/",fg="White",width=10,height=3,bd=0,bg = "#333332",command=lambda: Operations.bt_click("/")).grid(row=1,column=3, padx=1, pady=1)
cos=create_button(button_frame,text="cos",fg="White",width=10,height=3,bd=0,bg = "#333332",command=lambda: Operations.bt_cos()).grid(row=1,column=4, padx=1, pady=1)

#row2
seven=create_button(button_frame,text="7",fg="White",width=10,height=3,bd=0,bg = "#3B3A3A",command=lambda: Operations.bt_click(7)).grid(row=2,column=0, padx=1, pady=1)
eight=create_button(button_frame,text="8",fg="White",width=10,height=3,bd=0,bg = "#3B3A3A",command=lambda: Operations.bt_click(8)).grid(row=2,column=1, padx=1, pady=1)
nine=create_button(button_frame,text="9",fg="White",width=10,height=3,bd=0,bg = "#3B3A3A",command=lambda: Operations.bt_click(9)).grid(row=2,column=2, padx=1, pady=1)
product=create_button(button_frame,text="*",fg="White",width=10,height=3,bd=0,bg = "#333332",command=lambda: Operations.bt_click("*")).grid(row=2,column=3, padx=1, pady=1)
tan=create_button(button_frame,text="tan",fg="White",width=10,height=3,bd=0,bg = "#333332",command=lambda: Operations.bt_tan()).grid(row=2,column=4, padx=1, pady=1)
#row3
four=create_button(button_frame,text="4",fg="White",width=10,height=3,bd=0,bg = "#3B3A3A",command=lambda: Operations.bt_click(4)).grid(row=3,column=0, padx=1, pady=1)
five=create_button(button_frame,text="5",fg="White",width=10,height=3,bd=0,bg = "#3B3A3A",command=lambda: Operations.bt_click(5)).grid(row=3,column=1, padx=1, pady=1)
six=create_button(button_frame,text="6",fg="White",width=10,height=3,bd=0,bg = "#3B3A3A",command=lambda: Operations.bt_click(6)).grid(row=3,column=2, padx=1, pady=1)
subtract=create_button(button_frame,text="-",fg="White",width=10,height=3,bd=0,bg = "#333332",command=lambda: Operations.t_click("-")).grid(row=3,column=3, padx=1, pady=1)
cot=create_button(button_frame,text="cot",fg="White",width=10,height=3,bd=0,bg = "#333332",command=lambda: Operations.bt_cot()).grid(row=3,column=4, padx=1, pady=1)
#row4
one=create_button(button_frame,text="1",fg="White",width=10,height=3,bd=0,bg = "#3B3A3A",command=lambda: Operations.bt_click(1)).grid(row=4,column=0, padx=1, pady=1)
two=create_button(button_frame,text="2",fg="White",width=10,height=3,bd=0,bg = "#3B3A3A",command=lambda: Operations.bt_click(2)).grid(row=4,column=1, padx=1, pady=1)
three=create_button(button_frame,text="3",fg="White",width=10,height=3,bd=0,bg = "#3B3A3A",command=lambda: Operations.bt_click(3)).grid(row=4,column=2, padx=1, pady=1)
add=create_button(button_frame,text="+",fg="White",width=10,height=3,bd=0,bg = "#333332",command=lambda: Operations.bt_click("+")).grid(row=4,column=3, padx=1, pady=1)
sec=create_button(button_frame,text="sec",fg="White",width=10,height=3,bd=0,bg = "#333332",command=lambda: Operations.Trigo.bt_sec()).grid(row=4,column=4, padx=1, pady=1)
#row5
zero=create_button(button_frame,text="0",fg="White",width=21,height=3,bd=0,bg="#3B3A3A",command=lambda: Operations.bt_click(0)).grid(row=5,column=0,columnspan=2,padx=1,pady=1)
point=create_button(button_frame,text=".",fg="white",width=10,height=3,bd=0,bg="#333332",command=lambda: Operations.bt_click(".")).grid(row=5,column=2,padx=1,pady=1)
evalu=create_button(button_frame,text="=",fg="White",width=10,height=3,bd=0,bg="#333332",command=lambda: Operations.bt_equal()).grid(row=5,column=3,padx=1,pady=1)
csc=create_button(button_frame,text="csc",fg="White",width=10,height=3,bd=0,bg = "#333332",command=lambda: Operations.Trigo.bt_cosec()).grid(row=5,column=4, padx=1, pady=1)
top.mainloop()
