# Simple GUI Calculator

from tkinter import *

def button_press(num):
    global equation_text

    equation_text = equation_text + str(num)
    equation_label.set(equation_text)

def equals():
    global equation_text
    try:
        total = str(eval(equation_text))

        equation_label.set(total)
        equation_text = total
    except SyntaxError:
        equation_label.set("Syntax Error")
        equation_text = ""

    except ZeroDivisionError:
        equation_label.set("Arithmetic Error")
        equation_text = ""
def clear():

    global equation_text
    equation_label.set("")
    equation_text = ""

root = Tk()
root.title("Simple GUI Calculator")
root.geometry("1600x1200")

equation_text = ""

equation_label = StringVar()

label  = Label(root, textvariable = equation_label, font=('consolas', 20), bg='white', width=40, height=2)
label.pack(pady=10)

frame = Frame(root)
frame.pack(expand=True)

#Buttons
button0 = Button(frame, text='0',       command=lambda:button_press(0),     height=4, width=8, font=('Consolas', 14))
button1 = Button(frame, text='1',       command=lambda:button_press(1),     height=4, width=8, font=('Consolas', 14))
button2 = Button(frame, text='2',       command=lambda:button_press(2),     height=4, width=8, font=('Consolas', 14))
button3 = Button(frame, text='3',       command=lambda:button_press(3),     height=4, width=8, font=('Consolas', 14))
button4 = Button(frame, text='4',       command=lambda:button_press(4),     height=4, width=8, font=('Consolas', 14))
button5 = Button(frame, text='5',       command=lambda:button_press(5),     height=4, width=8, font=('Consolas', 14))
button6 = Button(frame, text='6',       command=lambda:button_press(6),     height=4, width=8, font=('Consolas', 14))
button7 = Button(frame, text='7',       command=lambda:button_press(7),     height=4, width=8, font=('Consolas', 14))
button8 = Button(frame, text='8',       command=lambda:button_press(8),     height=4, width=8, font=('Consolas', 14))
button9 = Button(frame, text='9',       command=lambda:button_press(9),     height=4, width=8, font=('Consolas', 14))
buttonEQ = Button(frame, text='=',      command=equals,                     height=4, width=8, font=('Consolas', 14))
buttonPLUS = Button(frame, text='+',    command=lambda:button_press('+'),   height=4, width=8, font=('Consolas', 14))
buttonMIN = Button(frame, text='-',     command=lambda:button_press('-'),   height=4, width=8, font=('Consolas', 14))
buttonMUL = Button(frame, text='*',     command=lambda:button_press('*'),   height=4, width=8, font=('Consolas', 14))
buttonDIV = Button(frame, text='/',     command=lambda:button_press('/'),   height=4, width=8, font=('Consolas', 14))
buttonPL = Button(frame, text='(',      command=lambda:button_press('('),   height=4, width=8, font=('Consolas', 14))
buttonPR = Button(frame, text=')',      command=lambda:button_press(')'),   height=4, width=8, font=('Consolas', 14))
buttonMOD = Button(frame, text='mod',   command=lambda:button_press('mod'), height=4, width=8, font=('Consolas', 14))
buttonN = Button(frame, text='n',       command=lambda:button_press('n'),   height=4, width=8, font=('Consolas', 14))
buttonSQ = Button(frame, text='x²',     command=lambda:button_press('x²'),  height=4, width=8, font=('Consolas', 14))
buttonSQRT = Button(frame, text='√',    command=lambda:button_press('√'),   height=4, width=8, font=('Consolas', 14))
buttonERASE = Button(frame, text='x', command=lambda:button_press('√'),   height=4, width=8, font=('Consolas', 14))
buttonDECIMAL = Button(frame, text='.', command=lambda:button_press('.'),   height=4, width=8, font=('Consolas', 14))
buttonPERCENT = Button(frame, text='%', command=lambda:button_press('%'),   height=4, width=8, font=('Consolas', 14))
clearBTN = Button(root, text='Clear',   command=clear,                      height=4, width=8, font=('Consolas', 14))
clearBTN.pack(pady=20)


#Grids
button0.grid(column=0, row=4)
button1.grid(column=0, row=3)
button2.grid(column=1, row=3)
button3.grid(column=2, row=3)
button4.grid(column=0, row=2)
button5.grid(column=1, row=2)
button6.grid(column=2, row=2)
button7.grid(column=0, row=1)
button8.grid(column=1, row=1)
button9.grid(column=2, row=1)
buttonEQ.grid(column=4, row=3, rowspan=2, sticky='nsew')
frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)
buttonPLUS.grid(column=3, row=4)
buttonMIN.grid(column=3, row=3)
buttonMUL.grid(column=3, row=2)
buttonDIV.grid(column=3, row=1)
buttonPL.grid(column=1, row=0)
buttonPR.grid(column=2, row=0)
buttonMOD.grid(column=3, row=0)
buttonN.grid(column=4, row=0)
buttonSQ.grid(column=4, row=2)
buttonSQRT.grid(column=4, row=1)
buttonERASE.grid(column=0, row=0)
buttonDECIMAL.grid(column=1, row=4)
buttonPERCENT.grid(column=2, row=4)


root.mainloop()