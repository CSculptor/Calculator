
from tkinter import *
import customtkinter
class app(Tk):
    state = 0
    which = 0
    def __init__(self):
        super().__init__()
        self.resizable(0,0)
        self.title('Calculator')
        self.geometry('365x500')
        self.bind('<Control-e>', self.destroy)
        self.widgets()

    def widgets(self):
        self.main = Frame(self)
        self.main.pack()
        self.result = Entry(self.main, width=27, font=("Arial", 16), background = 'grey', fg = 'black', justify = CENTER, relief = RAISED)
        self.result.grid(row=0, column=0,pady=(50,30), padx=17, columnspan=6)
        self.minplu = button(self.main, '±', 'grey',self.min_plu, 1, 4)
        self.eq = button(self.main, '=', 'grey',self.equal, 5, 5)
        self.dl = button(self.main, '<', 'grey',self.delete, 2, 4)
        self.C = button(self.main, 'C', 'grey',self.clear, 2, 5)
        self.left = button(self.main, '(', 'grey', lambda : self.insert('('), 1, 1)
        self.right = button(self.main, ')', 'grey', lambda : self.insert(')'), 1, 2)
        self.perc = button(self.main, '%', 'grey', lambda : self.insert('%'), 1, 3)
        self.square = button(self.main, '^', 'grey', lambda : self.insert('^'), 1, 5)
        self.mul = button(self.main, 'x', 'grey', lambda : self.insert('x'), 3, 4)
        self.div = button(self.main, '÷', 'grey', lambda : self.insert('÷'), 3, 5)
        self.add = button(self.main, '+', 'grey', lambda : self.insert('+'), 4, 4)
        self.sub = button(self.main, '-', 'grey', lambda : self.insert('-'), 4, 5)
        self.dot = button(self.main, '.', 'grey', lambda : self.insert('.'), 5, 2)
        self.pi = button(self.main, 'π', 'grey', lambda : self.insert('π'), 5, 3)
        self.expo = button(self.main, 'e', 'grey', lambda : self.insert('e'), 5, 4)

        self.seven = button(self.main, '7', 'orange', lambda : self.insert('7'), 2, 1)
        self.eight = button(self.main, '8', 'orange', lambda : self.insert('8'), 2, 2)
        self.nine = button(self.main, '9', 'orange', lambda : self.insert('9'), 2, 3)
        self.six = button(self.main, '6', 'orange', lambda : self.insert('6'), 3, 3)
        self.five = button(self.main, '5', 'orange', lambda : self.insert('5'), 3, 2)
        self.four = button(self.main, '4', 'orange', lambda : self.insert('4'), 3, 1)
        self.three = button(self.main, '3', 'orange', lambda : self.insert('3'), 4, 3)
        self.two = button(self.main, '2', 'orange', lambda : self.insert('2'), 4, 2)
        self.one = button(self.main, '1', 'orange', lambda : self.insert('1'), 4, 1)
        self.zero = button(self.main, '0', 'orange', lambda : self.insert('0'), 5, 1)
    
    def insert(self, num : str):
        if num == '(':
            if self.which == 0 :
                self.result.insert(0, '(')
            else :
                self.result.insert(END, '(')
            self.which = 1

        elif not(num.isnumeric()):
            if self.result.get() :
                self.result.insert(END, num)

        else:
            self.result.insert(END, num)
    
    def min_plu(self) :
        if self.result.get() :
            if '-' not in self.result.get() :
                self.result.insert(0, '-')
            else :
                self.result.delete(0, END)
                self.result.insert(END, "Only one minus allowed")
                self.result.after(2000, self.result.delete(0, END))
    
    def equal(self):
        if self.result.get():
            try:
                ans = self.filterStr(self.result.get())
                print(ans)
                number = eval(ans)
                number = "{:.2f}".format(number)
                self.result.insert(END, f' = {number}')
            except:
                self.result.delete(0, END)
                self.result.insert(END, 'Cannot divide by Zero')
                self.result.after(2000, self.result.delete(0, END))

    def filterStr(self, string : str):
        string = string.replace('^', '**')
        string = string.replace('e', '2.71828')
        string = string.replace('π', '3.14159265')
        string = string.replace('%', '100')
        string = string.replace('x', '*')
        string = string.replace('÷', '/')
        return string
    def delete(self):
        temp = self.result.get()
        self.result.delete(0, END)
        self.result.insert(END, temp[:-1])

    def clear(self):
            self.state = 0
            self.which = 0
            self.result.delete(0, END)

class button(Button):
    def __init__(self,master, text, background, command, row, column):
        self
        super().__init__(master, text = text, width = 7, height = 4, font = ("Arial", 10), fg = 'white', borderwidth = 3, background=background, command=command)
        self.grid(row=row, column=column)

if __name__ == '__main__':
    a = app()
    a.mainloop()




        # row = 1
        # column = 0
        # for i in range(len(l)):
        #     column += 1
        #     if l[i] == '±':
        #         self.wid.append(button(self.main, l[i], 'grey' if l[i].isnumeric() else 'orange',self.min_plu, row, column))
        #     elif l[i] == '=':
        #         self.wid.append(button(self.main, l[i], 'grey' if l[i].isnumeric() else 'orange', self.equal , row, column))
        #     elif l[i] == '<':
        #         self.wid.append(button(self.main, l[i], 'grey' if l[i].isnumeric() else 'orange', self.delete, row, column))
        #     elif l[i] == 'C':
        #         self.wid.append(button(self.main, l[i], 'grey' if l[i].isnumeric() else 'orange', self.clear, row, column))
        #     else:
        #         self.wid.append(button(self.main, l[i], 'grey' if l[i].isnumeric() else 'orange', lambda : self.insert(str(l[i])), row, column))
        #     if column >= 5:
        #         column = 0
        #         row += 1

        # l = ['(', ')','%','±','^',
        #      '7','8','9','<','C',
        #      '4','5','6','x','÷',
        #      '1','2','3','+','-',
        #      '0','.','π','e','=']
# class button(Button):
#     def __init__(self,master, text, background, command, row, column):
#         self.row = row
#         self.column = column
#         super().__init__()
#         self['master'] = master
#         self['text'] = text
#         self['bg'] = background
#         self['command'] = command
#         self['width'] = 7
#         self['height'] = 4
#         self['font'] = ("Arial", 10)
#         self['fg'] = 'white'
#         self['borderwidth'] = 3
#         self.grid(row=self.row, column=self.column)

# menu_bar = Menu(wndw)
# wndw.config(menu = menu_bar)
# file = Menu(menu_bar, tearoff = 0)
# file.add_command(label = 'Exit', command = wndw.destroy)
# menu_bar.add_cascade(label = 'File', menu = file)
# wndw.bind('<Control-e>', exiting)
# wndw.mainloop()
