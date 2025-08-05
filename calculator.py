from tkinter import*
from tkinter import Tk
abc=Tk()
abc.geometry("500x500")
abc.title("CALCULATOR")
app_name= Label(text="CALCULATOR APPLICATION",font="bold 10 italic")
app_name.place(x=150,y=50)
def btn_click(value):
    screen.insert(END, str(value))

def calculate():
    try:
        result = eval(screen.get().replace('x', '*').replace('÷', '/'))
        screen.delete(0, END)
        screen.insert(0, result)
    except:
        screen.delete(0, END)
        screen.insert(0, "Error")

def clear():
    screen.delete(0,END)

def backspace():
    current = screen.get()
    screen.delete(0, END)
    screen.insert(0, current[:-1])

screen=Entry(width=40,bd=10,relief="ridge")
screen.place(x=130,y=100)

#buttons
butt_on=Button(text="7",width=5,bg="grey",command=lambda: btn_click(7))
butt_on.place(x=130,y=150)

butt_on8=Button(text="8",width=5,bg="grey",command=lambda: btn_click(8))
butt_on8.place(x=200,y=150)

butt_on9=Button(text="9",width=5,bg="grey",command=lambda: btn_click(9))
butt_on9.place(x=270,y=150)

butt_onx=Button(text="x",width=5,bg="grey",command=lambda: btn_click("x"))
butt_onx.place(x=340,y=150)

butt_on4=Button(text="4",width=5,bg="grey",command=lambda: btn_click(4))
butt_on4.place(x=130,y=200)

butt_on5=Button(text="5",width=5,bg="grey",command=lambda: btn_click(5))
butt_on5.place(x=200,y=200)

butt_on6=Button(text="6",width=5,bg="grey",command=lambda: btn_click(6))
butt_on6.place(x=270,y=200)

butt_on_sub=Button(text="-",width=5,bg="grey",command=lambda: btn_click("-"))
butt_on_sub.place(x=340,y=200)

butt_on1=Button(text="1",width=5,bg="grey",command=lambda: btn_click(1))
butt_on1.place(x=130,y=250)

butt_on2=Button(text="2",width=5,bg="grey",command=lambda: btn_click(2))
butt_on2.place(x=200,y=250)

butt_on3=Button(text="3",width=5,bg="grey",command=lambda: btn_click(3))
butt_on3.place(x=270,y=250)

butt_on_add=Button(text="+",width=5,bg="grey",command=lambda: btn_click("+"))
butt_on_add.place(x=340,y=250)

butt_on_0=Button(text="0",width=5,bg="grey",command=lambda: btn_click(0))
butt_on_0.place(x=200,y=300)

butt_on_equ=Button( text="÷",width=5,bg="grey",font=('Arial', 9),command=lambda: btn_click("÷"))
butt_on_equ.place(x=340,y=300)

butt_on_equ=Button( text="=",width=5,font=('Arial', 9,"bold"),background="skyblue",command=calculate)
butt_on_equ.place(x=270,y=300)

butt_on_equ=Button( text=".",width=5,bg="grey",font=('Arial', 10,"bold"),command=lambda: btn_click("."))
butt_on_equ.place(x=130,y=300)

butt_on_equ=Button( text="Clear",width=5,bg="grey",font=('Arial', 10,"bold"),command=clear)
butt_on_equ.place(x=130,y=350)

butt_on_equ=Button( text="⌫",width=5,bg="grey",font=('Arial', 10,"bold"),command=backspace)
butt_on_equ.place(x=200,y=350)
abc.mainloop()

