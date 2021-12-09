from tkinter import *
from tkinter import messagebox
from tkinter import font
from math import *

calc = Tk()
calc.title('R-CALCULATOR')
#calc.iconbitmap('icon.ico')
calc.geometry('450x440')
calc.configure(bg='orange')


def Log2(x):
    return log(x, 2)


def Log(x):
    return log(x, 10)


def Ln(x):
    return log(x)


def arcsin(x):
    return asin(x)


def arccos(x):
    return acos(x)


def arctan(x):
    return atan(x)


hist = []
key = []
ans = ''


def show(x):
    global key
    key.append(str(x))
    eq.set(''.join(key))


def solve(x=0):
    global key, ans, his, ent
    result = ent.get()
    ans = eval(result)
    eq.set(ans)
    hist.insert(0, result + ' = ' + str(ans) + '\n')
    key = []


def ans(x=0):
    key.append(str(ans))
    eq.set(''.join(key))


def clear(x=0):
    global key
    key = []
    eq.set('')


def delete():
    key.pop()
    eq.set(''.join(key))


def history(x=0):
    messagebox.showinfo('HISTORY', ''.join(hist))


eq = StringVar()
eq.set('')
ent = Entry(calc, textvariable=eq, font=('comic sans ms', 19, 'bold'), width=23)
ent.place(x=50, y=10)
ent.bind('<Return>', solve)
ent.bind('<C>', clear)
ent.bind('<c>', clear)
ent.bind('<H>', history)
ent.bind('<h>', history)
ent.bind('<A>', ans)
ent.bind('<a>', ans)

Button(calc, text='1', height=2, width=5, bg='silver', command=lambda: show(1)).place(x=1 * 50, y=1 * 70)
Button(calc, text='2', height=2, width=5, bg='silver', command=lambda: show(2)).place(x=2 * 50, y=1 * 70)
Button(calc, text='3', height=2, width=5, bg='silver', command=lambda: show(3)).place(x=3 * 50, y=1 * 70)
Button(calc, text='4', height=2, width=5, bg='silver', command=lambda: show(4)).place(x=1 * 50, y=2 * 50 + 20)
Button(calc, text='5', height=2, width=5, bg='silver', command=lambda: show(5)).place(x=2 * 50, y=2 * 50 + 20)
Button(calc, text='6', height=2, width=5, bg='silver', command=lambda: show(6)).place(x=3 * 50, y=2 * 50 + 20)
Button(calc, text='7', height=2, width=5, bg='silver', command=lambda: show(7)).place(x=1 * 50, y=3 * 50 + 20)
Button(calc, text='8', height=2, width=5, bg='silver', command=lambda: show(8)).place(x=2 * 50, y=3 * 50 + 20)
Button(calc, text='9', height=2, width=5, bg='silver', command=lambda: show(9)).place(x=3 * 50, y=3 * 50 + 20)
Button(calc, text='0', height=2, width=12, bg='silver', command=lambda: show(0)).place(x=1 * 50, y=4 * 50 + 20)
Button(calc, text='.', height=2, width=5, bg='silver', command=lambda: show('.')).place(x=3 * 50, y=4 * 50 + 20)
Button(calc, text='+', height=2, width=5, bg='silver', fg='red', command=lambda: show('+')).place(x=4 * 50, y=1 * 70)
Button(calc, text='-', height=2, width=5, bg='silver', fg='red', command=lambda: show('-')).place(x=4 * 50,
                                                                                                  y=2 * 50 + 20)
Button(calc, text='*', height=2, width=5, bg='silver', fg='red', command=lambda: show('*')).place(x=4 * 50,
                                                                                                  y=3 * 50 + 20)
Button(calc, text='/', height=2, width=5, bg='silver', fg='red', command=lambda: show('/')).place(x=4 * 50,
                                                                                                  y=4 * 50 + 20)
Button(calc, text='log2', height=2, width=5, bg='silver', fg='blue', command=lambda: show('Log2(')).place(x=7 * 50,
                                                                                                          y=1 * 50 + 20)
Button(calc, text='log', height=2, width=5, bg='silver', fg='blue', command=lambda: show('Log(')).place(x=6 * 50,
                                                                                                        y=1 * 50 + 20)
Button(calc, text='ln', height=2, width=5, bg='silver', fg='blue', command=lambda: show('Ln(')).place(x=5 * 50,
                                                                                                      y=1 * 50 + 20)
Button(calc, text='^', height=2, width=5, bg='silver', fg='red', command=lambda: show('**')).place(x=5 * 50,
                                                                                                   y=2 * 50 + 20)
Button(calc, text='(', height=2, width=5, bg='silver', fg='purple', command=lambda: show('(')).place(x=6 * 50,
                                                                                                     y=2 * 50 + 20)
Button(calc, text=')', height=2, width=5, bg='silver', fg='purple', command=lambda: show(')')).place(x=7 * 50,
                                                                                                     y=2 * 50 + 20)
Button(calc, text='e', height=2, width=5, bg='silver', fg='green', command=lambda: show('e')).place(x=5 * 50,
                                                                                                    y=3 * 50 + 20)
Button(calc, text=chr(928), height=2, width=5, bg='silver', fg='green', command=lambda: show('pi')).place(x=6 * 50,
                                                                                                          y=3 * 50 + 20)
Button(calc, text='arc', height=2, width=5, bg='silver', fg='brown', command=lambda: show('arc')).place(x=7 * 50,
                                                                                                        y=3 * 50 + 20)
Button(calc, text='sin', height=2, width=5, bg='silver', fg='brown', command=lambda: show('sin(')).place(x=5 * 50,
                                                                                                         y=4 * 50 + 20)
Button(calc, text='cos', height=2, width=5, bg='silver', fg='brown', command=lambda: show('cos(')).place(x=6 * 50,
                                                                                                         y=4 * 50 + 20)
Button(calc, text='tan', height=2, width=5, bg='silver', fg='brown', command=lambda: show('tan(')).place(x=7 * 50,
                                                                                                         y=4 * 50 + 20)

Button(calc, text='ans', height=2, width=5, bg='silver', command=ans).place(x=1 * 50, y=5 * 50 + 20)
Button(calc, text='history', height=2, width=12, bg='silver', command=lambda: history()).place(x=2 * 50, y=5 * 50 + 20)
Button(calc, text='C', height=2, width=5, bg='red', command=lambda: clear(), font=('calibiri', 9, 'bold'),
       fg='white').place(x=4 * 50, y=5 * 50 + 20)
Button(calc, text='DEL', height=2, width=5, bg='light blue', command=lambda: delete(),
       font=('calibiri', 9, 'bold')).place(x=5 * 50, y=5 * 50 + 20)
Button(calc, text='ENTER', height=2, width=12, bg='light green', command=lambda: solve(),
       font=('calibiri', 9, 'bold')).place(x=6 * 50, y=5 * 50 + 20)

Label(calc, text=' >>> R-CALCULATOR ', font=('comic sans ms', 13, 'bold'), bg='orange', fg='red').place(x=0, y=320)
Label(calc, text='a calculator made by ', font=('comic sans ms', 10, 'italic'), bg='orange', fg='green').place(x=189,
                                                                                                               y=323)
Label(calc, text='RITESH <<<   ', font=('comic sans ms', 13, 'bold'), bg='orange', fg='purple').place(x=330, y=320)

calc.mainloop()
