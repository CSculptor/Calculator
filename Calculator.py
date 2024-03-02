import tkinter as tk
from tkinter import *
from tkinter import ttk
state = 0
which = 0
def left() :
    global which
    if which == 0 :
        result.insert(0, '(')
    else :
        result.insert(END, '(')
    which = 1
def right() :
    if result.get() :
        result.insert(END, ')')
def delets() :
    string = 0
    string = result.get()
    string = string[:-1]
    result.delete(0, END)
    result.insert(END, string)
def expone() :
    if result.get() :
        result.insert(END, '**')
def e_nombre() :
    result.insert(END, '2.71828')
def deleting() :
    result.delete(0, END)
def add() :
    if result.get() :
        result.insert(END, '+')
def div() :
    if result.get() :
        result.insert(END, '/')
def sub() :
    if result.get() :
        result.insert(END, '-')
def mul() :
    if result.get() :
        result.insert(END, '*')
def clear() :
    global state
    global which
    state = 0
    which = 0
    result.delete(0, END)
def dot() :
    if result.get() :
        result.insert(END, '.')
def pi() :
    result.insert(END, '3.14159265')
def handr() :
    result.insert(END, '100')
def min_plu() :
    if result.get() :
        if '-' not in result.get() :
            result.insert(0, '-')
        else :
            result.delete(0, END)
            result.insert(END, "Only one minus allowed")
            result.after(2000, deleting)
def zero() :
    if result.get() :
        result.insert(END, '0')
def one() :
    result.insert(END, '1')
def two() :
    result.insert(END, '2')
def three() :
    result.insert(END, '3')
def four() :
    result.insert(END, '4')
def five() :
    result.insert(END, '5')
def six() :
    result.insert(END, '6')
def seven() :
    result.insert(END, '7')
def eigth() :
    result.insert(END, '8')
def nine() :
    result.insert(END, '9')
def equal():
    global number
    if result.get() :
        number = result.get()
        if number.startswith('0') :
            number = '+'+number[1:]
            try : 
                number = eval(number)
                number = "{:.2f}".format(number)
                result.insert(END, ' = ')
                result.insert(END, str(number))
            except :
                result.delete(0, END)
                result.insert(END, 'Cannot divide by Zero')
                result.after(2000, deleting)
        else :
            try:
                number = eval(result.get())
                number = "{:.2f}".format(number)
                result.insert(END, ' = ')
                result.insert(END, str(number))
            except :
                result.delete(0, END)
                result.insert(END, 'Cannot divide by Zero')
                result.after(2000, deleting)
def exiting(event) :
    wndw.destroy()
wndw = Tk()
wndw.title('Calculator')
wndw.minsize(365, 500)
wndw.maxsize(365, 500)
wndw.geometry('365x365+400+80')
result = Entry(wndw, width=27, font=("Arial", 16), background = 'grey', fg = 'black', justify = CENTER, relief = RAISED)
result.place(x = 20, y = 50)
button_0 = Button(wndw, text = '0', width = 7, height = 4, font = ("Arial", 10) ,background = "grey", fg = 'white', command = zero, activebackground = "grey", activeforeground = 'white', borderwidth = 3)
button_0.place(x = 7, y = 100)
button_1 = Button(wndw, text = '1', width = 7, height = 4, font = ("Arial", 10) , background = "grey", fg = 'white', command = one, activebackground = "grey", activeforeground = 'white', borderwidth = 3)
button_1.place(x = 77, y = 100)
button_2 = Button(wndw, text = '2', width = 7, height = 4, font = ("Arial", 10) ,background = "grey", fg = 'white',command = two, activebackground = "grey", activeforeground = 'white', borderwidth = 3)
button_2.place(x = 7, y = 180)
button_3 = Button(wndw, text = '3', width = 7, height = 4, font = ("Arial", 10) , background = "grey", fg = 'white', command = three, activebackground = "grey", activeforeground = 'white', borderwidth = 3)
button_3.place(x = 77, y = 180)
button_4 = Button(wndw, text = '4', width = 7, height = 4, font = ("Arial", 10) , background = "grey", fg = 'white',command = four, activebackground = "grey", activeforeground = 'white', borderwidth = 3)
button_4.place(x = 7, y = 260)
button_5 = Button(wndw, text = '5', width = 7, height = 4, font = ("Arial", 10) ,background = "grey", fg = 'white', command = five, activebackground = "grey", activeforeground = 'white', borderwidth = 3)
button_5.place(x = 77, y = 260)
button_6 = Button(wndw, text = '6', width = 7, height = 4, font = ("Arial", 10) , background = "grey", fg = 'white', command = six, activebackground = "grey", activeforeground = 'white', borderwidth = 3)
button_6.place(x = 7, y = 340)
button_7 = Button(wndw, text = '7', width = 7, height = 4, font = ("Arial", 10) , background = "grey", fg = 'white', command = seven, activebackground = "grey", activeforeground = 'white', borderwidth = 3)
button_7.place(x = 77, y = 340)
button_8 = Button(wndw, text = '8', width = 7, height = 4, font = ("Arial", 10) , background = "grey", fg = 'white', command = eigth, activebackground = "grey", activeforeground = 'white', borderwidth = 3)
button_8.place(x = 7, y = 420)
button_9 = Button(wndw, text = '9', width = 7, height = 4, font = ("Arial", 10) ,background = "grey", fg = 'white', command = nine, activebackground = "grey", activeforeground = 'white', borderwidth = 3)
button_9.place(x = 77, y = 420)
button_ad = Button(wndw, text = '+', width = 7, height = 4, font = ("Arial", 10) ,background = "orange", fg = 'white', command = add, activebackground = "orange", activeforeground = 'white', borderwidth = 3)
button_ad.place(x = 217, y = 100)
button_sub = Button(wndw, text = '-', width = 7, height = 4, font = ("Arial", 10) , background = "orange", fg = 'white', command = sub, activebackground = "orange", activeforeground = 'white', borderwidth = 3)
button_sub.place(x = 217, y = 180)
button_div = Button(wndw, text = '÷', width = 7, height = 4, font = ("Arial", 10) , background = "orange", fg = 'white', command = div, activebackground = "orange", activeforeground = 'white', borderwidth = 3)
button_div.place(x = 217, y = 260)
button_mul = Button(wndw, text = '×', width = 7, height = 4, font = ("Arial", 10) , background = "orange", fg = 'white', command = mul, activebackground = "orange", activeforeground = 'white', borderwidth = 3)
button_mul.place(x = 217, y = 340)
button_cle = Button(wndw, text = 'C', width = 7, height = 4, font = ("Arial", 10) , background = "orange", activebackground = "orange", activeforeground = 'white', fg = 'white', command = clear, borderwidth = 3)
button_cle.place(x = 147, y = 100)
button_dot = Button(wndw, text = '•', width = 7, height = 4, font = ("Arial", 10) , background = "orange", activebackground = "orange", activeforeground = 'white', fg = 'white', command = dot, borderwidth = 3)
button_dot.place(x = 147, y = 420)
button_hand = Button(wndw, text = '%', width = 7, height = 4, font = ("Arial", 10) , background ="orange", activebackground = "orange", activeforeground = 'white', fg = 'white', command = handr, borderwidth = 3)
button_hand.place(x = 147, y = 260)
button_pi = Button(wndw, text = 'π', width = 7, height = 4, font = ("Arial", 10) , background = "orange", activebackground = "orange", activeforeground = 'white', fg = 'white', command = pi, borderwidth = 3)
button_pi.place(x = 147, y = 180)
button_mi_p = Button(wndw, text = '±', width = 7, height = 4, font = ("Arial", 10) , background = "orange", activebackground = "orange", activeforeground = 'white', fg = 'white', command = min_plu, borderwidth = 3)
button_mi_p.place(x = 147, y = 340)
button_equal = Button(wndw, text = '=', background = "orange", font = ("Arial", 10) , fg = 'white', width = 7, height = 4, command = equal, activebackground = "orange", activeforeground = 'white', borderwidth = 3)
button_equal.place(x = 217, y = 420)
button_left = Button(wndw, text = '(', background = "orange", font = ("Arial", 10) , fg = 'white', width = 7, height = 4, command = left, activebackground = "orange", activeforeground = 'white', borderwidth = 3)
button_left.place(x = 287, y = 100)
button_right = Button(wndw, text = ')', background = "orange", font = ("Arial", 10) , fg = 'white', width = 7, height = 4, command = right, activebackground = "orange", activeforeground = 'white', borderwidth = 3)
button_right.place(x = 287, y = 180)
button_right = Button(wndw, text = 'e', background = "orange", font = ("Arial", 10) , fg = 'white', width = 7, height = 4, command = e_nombre, activebackground = "orange", activeforeground = 'white', borderwidth = 3)
button_right.place(x = 287, y = 260)
button_right = Button(wndw, text = '<', background = "orange", font = ("Arial", 10) , fg = 'white', width = 7, height = 4, command = delets, activebackground = "orange", activeforeground = 'white', borderwidth = 3)
button_right.place(x = 287, y = 340)
button_right = Button(wndw, text = '^', background = "orange", font = ("Arial", 10) , fg = 'white', width = 7, height = 4, command = expone, activebackground = "orange", activeforeground = 'white', borderwidth = 3)
button_right.place(x = 287, y = 420)
wndw.resizable(False, False)
menu_bar = Menu(wndw)
wndw.config(menu = menu_bar)
file = Menu(menu_bar, tearoff = 0)
file.add_command(label = 'Exit', command = wndw.destroy)
menu_bar.add_cascade(label = 'File', menu = file)
wndw.bind('<Control-e>', exiting)
wndw.mainloop()
