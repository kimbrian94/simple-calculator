from tkinter import *

root = Tk()
root.title("Better Calculator")
root.geometry('500x600')

# create a text widget that will output the operands and output the answer
outputText = Text(root, height=1, state='disabled', padx=5, font=('Helvetica', 66), background='#1f1f2e', fg='white')
outputText.grid(row=0, column=0, columnspan=5, sticky=W+E+N+S)

# set the each rows and column to have weight of 1
for x in range(0,5):
    root.columnconfigure(x, weight=1)
    root.rowconfigure(x, weight=1)

# function for click event on each 0 - 9 buttons
def buttonClick(number):
    outputText.configure(state='normal')
    # append clicked number to the end of textbox
    outputText.insert(END, str(number))
    outputText.configure(state='disabled')

# function for clicking the divide button
def divideClick():
    global math
    global prev
    outputText.configure(state='normal')
    prev = float(outputText.get(1.0, END))
    outputText.delete(1.0, END)
    outputText.config(state='disabled')
    math = 'division'

# function for clicking the multiply button
def multiplyClick():
    global math
    global prev
    outputText.configure(state='normal')
    prev = float(outputText.get(1.0, END))
    outputText.delete(1.0, END)
    outputText.config(state='disabled')
    math = 'multiply'

# function for clicking the minus button
def minusClick():
    global math
    global prev
    outputText.configure(state='normal')
    prev = float(outputText.get(1.0, END))
    outputText.delete(1.0, END)
    outputText.config(state='disabled')
    math = 'subtraction'

# function for clicking the plus button
def plusClick():
    global math
    global prev
    outputText.configure(state='normal')
    prev = float(outputText.get(1.0, END))
    outputText.delete(1.0, END)
    outputText.config(state='disabled')
    math = 'addition'

# function for clearbutton
# clears the textbox for new arithmetic operations
def clearClick():
    outputText.config(state='normal')
    outputText.delete(1.0, END)
    outputText.config(state='disabled')

# function for clicking the equal button
# calculates the operation in terms of its operator and outputs 
def equalClick():
    outputText.config(state='normal')
    curr = float(outputText.get(1.0, END))
    outputText.delete(1.0, END)
    if math == 'division':
        outputText.insert(1.0, str((prev / curr)))
    elif math == 'multiply':
        outputText.insert(1.0, str((prev * curr)))
    elif math == 'addition':
        outputText.insert(1.0, str((prev + curr)))
    elif math == 'subtraction':
        outputText.insert(1.0, str((prev - curr)))
    outputText.config(state='disabled')

# create buttons
button1 = Button(root, text='7', command=lambda: buttonClick(7), font=('Helvetica', 28))
button2 = Button(root, text='8', command=lambda: buttonClick(8), font=('Helvetica', 28))
button3 = Button(root, text='9', command=lambda: buttonClick(9), font=('Helvetica', 28))
button4 = Button(root, text='4', command=lambda: buttonClick(4), font=('Helvetica', 28))
button5 = Button(root, text='5', command=lambda: buttonClick(5), font=('Helvetica', 28))
button6 = Button(root, text='6', command=lambda: buttonClick(6), font=('Helvetica', 28))
button7 = Button(root, text='1', command=lambda: buttonClick(1), font=('Helvetica', 28))
button8 = Button(root, text='2', command=lambda: buttonClick(2), font=('Helvetica', 28))
button9 = Button(root, text='3', command=lambda: buttonClick(3), font=('Helvetica', 28))
button0 = Button(root, text='0', command=lambda: buttonClick(0), font=('Helvetica', 28))

divideButton = Button(root, text='/', command=divideClick, font=('Helvetica', 28))
multiplyButton = Button(root, text='*', command=multiplyClick, font=('Helvetica', 28))
minusButton = Button(root, text='-', command=minusClick, font=('Helvetica', 28))
plusButton = Button(root, text='+', command=plusClick, font=('Helvetica', 28))

clearButton = Button(root, text='CE', command=clearClick, font=('Helvetica', 28))
equalButton = Button(root, text='=', command=equalClick, font=('Helvetica', 28))

# position each buttons 
button1.grid(row=1, column=0, sticky=W+E+N+S)
button2.grid(row=1, column=1, sticky=W+E+N+S)
button3.grid(row=1, column=2, sticky=W+E+N+S)

button4.grid(row=2, column=0, sticky=W+E+N+S)
button5.grid(row=2, column=1, sticky=W+E+N+S)
button6.grid(row=2, column=2, sticky=W+E+N+S)

button7.grid(row=3, column=0, sticky=W+E+N+S)
button8.grid(row=3, column=1, sticky=W+E+N+S)
button9.grid(row=3, column=2, sticky=W+E+N+S)

button0.grid(row=4, column=1, sticky=W+E+N+S)

divideButton.grid(row=1, column=3, sticky=W+E+N+S)
multiplyButton.grid(row=2, column=3, sticky=W+E+N+S)
minusButton.grid(row=3, column=3, sticky=W+E+N+S)
plusButton.grid(row=4, column=3, sticky=W+E+N+S)

clearButton.grid(row=1, column=4, rowspan=3, sticky=W+E+N+S)
equalButton.grid(row=4, column=4, sticky=W+E+N+S)

root.mainloop()