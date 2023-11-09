from tkinter import *


cal = Tk()


cal.title("Calculator")



# + - * /
operator = ""
text_input = StringVar()


def btnClick(number):
    global operator
    operator = operator + str(number)
    text_input.set(operator)


def btnCleanDisplay():
    global operator
    operator = ""
    text_input.set("")


def btnEqual():
    global operator
    sumup = str(eval(operator))
    text_input.set(sumup)
    operator = ""



textDisplay = Entry(cal, font=('arial', 20), textvariable= text_input).grid(columnspan=4)

btn7 = Button(cal,font=('arial', 20), text='7', command=lambda:btnClick(7)).grid(row=1, column=0)
btn8 = Button(cal,font=('arial', 20), text='8', command=lambda:btnClick(8)).grid(row=1, column=1)
btn8 = Button(cal,font=('arial', 20), text='9', command=lambda:btnClick(9)).grid(row=1, column=2)
addition = Button(cal,font=('arial', 20), text='+', command=lambda:btnClick("+")).grid(row=1, column=3)


btn4 = Button(cal,font=('arial', 20), text='4', command=lambda:btnClick(4)).grid(row=2, column=0)
btn5 = Button(cal,font=('arial', 20), text='5', command=lambda:btnClick(5)).grid(row=2, column=1)
btn6 = Button(cal,font=('arial', 20), text='6', command=lambda:btnClick(6)).grid(row=2, column=2)
subtration = Button(cal,font=('arial', 20), text='-', command=lambda:btnClick("-")).grid(row=2, column=3)


btn1 = Button(cal,font=('arial', 20), text='1', command=lambda:btnClick(1)).grid(row=3, column=0)
btn2 = Button(cal,font=('arial', 20), text='2', command=lambda:btnClick(2)).grid(row=3, column=1)
btn3 = Button(cal,font=('arial', 20), text='3', command=lambda:btnClick(3)).grid(row=3, column=2)
multiply = Button(cal,font=('arial', 20), text='*', command=lambda:btnClick("*")).grid(row=3, column=3)


btn0 = Button(cal,font=('arial', 20), text='0', command=lambda:btnClick(0)).grid(row=4, column=0)
btnClear = Button(cal,font=('arial', 20), text='C', command=btnCleanDisplay).grid(row=4, column=1)
btnEquel = Button(cal,font=('arial', 20), text='=', command=btnEqual).grid(row=4, column=2)
division = Button(cal,font=('arial', 20), text='/', command=lambda:btnClick("/")).grid(row=4, column=3)

cal.mainloop()