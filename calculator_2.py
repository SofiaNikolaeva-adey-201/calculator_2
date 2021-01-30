import pickle
from PyQt5 import uic
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QApplication

Form, Window = uic.loadUiType("calculator_2.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()



def one():
    global first
    x = "1"
    first += x
    form.textEdit.setText('%s' %first)
    print(first)
    

def two():
    global first
    x = "2"
    first += x
    form.textEdit.setText('%s' %first)
    print(first)

def three():
    global first
    x = "3"
    first += x
    form.textEdit.setText('%s' %first)
    print(first)

def four():
    global first
    x = "4"
    first += x
    form.textEdit.setText('%s' %first)
    print(first)

def five():
    global first
    x = "5"
    first += x
    form.textEdit.setText('%s' %first)
    print(first)

def six():
    global first
    x = "6"
    first += x
    form.textEdit.setText('%s' %first)
    print(first)

def seven():
    global first
    x = "7"
    first += x
    form.textEdit.setText('%s' %first)
    print(first)

def eight():
    global first
    x = "8"
    first += x
    form.textEdit.setText('%s' %first)
    print(first)

def nine():
    global first
    x = "9"
    first += x
    form.textEdit.setText('%s' %first)
    print(first)

def zero():
    global first
    x = "0"
    first += x
    form.textEdit.setText('%s' %first)
    print(first)

def plus():
    global first
    x = "+"
    first += x
    form.textEdit.setText('%s' %first)
    print(first)

def minus():
    global first
    x = "-"
    first += x
    form.textEdit.setText('%s' %first)
    print(first)

def multiply():
    global first
    x = "*"
    first += x
    form.textEdit.setText('%s' %first)
    number = True
    print(first)

def division():
    global first
    x = "/"
    first += x
    form.textEdit.setText('%s' %first)
    print(first)

def delete():
    global first
    first = first[:-1]
    form.textEdit.setText('%s' %first)
    print(first)

def comma():
     global first
     x = "."
     first += x
     form.textEdit.setText('%s' %first)
     print(first)

def right_bracket():
    global first
    x = "("
    first += x
    form.textEdit.setText('%s' %first)
    print(first)

def left_bracket():
    global first
    x = ")"
    first += x
    form.textEdit.setText('%s' %first)
    print(first)

def rate():
     global first
     x = "**"
     first += x
     form.textEdit.setText('%s' %first)
     print(first)





def equals():
    global first
    try:
        result = eval(first)
        form.textEdit_2.setText('%s' %result)
        print(result)
    except IndentationError:
        form.textEdit_2.setText('Проверьте корректность введенного выражения')
    except ZeroDivisionError:
        form.textEdit_2.setText('На ноль делить нельзя')
    except ArithmeticError:
        form.textEdit_2.setText('Проверьте корректность введенного выражения')
    except SyntaxError:
        form.textEdit_2.setText('Проверьте корректность введенного выражения')


        






   



first = " "
number = True

form.pushButton.clicked.connect(one)
form.pushButton_2.clicked.connect(two)
form.pushButton_3.clicked.connect(three)
form.pushButton_4.clicked.connect(four)
form.pushButton_5.clicked.connect(five)
form.pushButton_6.clicked.connect(six)
form.pushButton_7.clicked.connect(seven)
form.pushButton_8.clicked.connect(eight)
form.pushButton_9.clicked.connect(nine)
form.pushButton_10.clicked.connect(zero)
form.pushButton_11.clicked.connect(plus)
form.pushButton_12.clicked.connect(minus)
form.pushButton_14.clicked.connect(multiply)
form.pushButton_13.clicked.connect(division)
form.pushButton_15.clicked.connect(delete)
form.pushButton_16.clicked.connect(equals)
form.pushButton_17.clicked.connect(comma)
form.pushButton_18.clicked.connect(right_bracket)
form.pushButton_19.clicked.connect(left_bracket)
form.pushButton_20.clicked.connect(rate)

app.exec_()