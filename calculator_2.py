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
    global first, number
    number = False
    x = "1"
    first += x
    form.textEdit.setText('%s' %first)
    print(first)
    

def two():
    global first, number
    number = False
    x = "2"
    first += x
    form.textEdit.setText('%s' %first)
    print(first)

def three():
    global first, number
    number = False
    x = "3"
    first += x
    form.textEdit.setText('%s' %first)
    print(first)

def four():
    global first, number
    number = False
    x = "4"
    first += x
    form.textEdit.setText('%s' %first)
    print(first)

def five():
    global first, number
    number = False
    x = "5"
    first += x
    form.textEdit.setText('%s' %first)
    print(first)

def six():
    global first, number
    number = False
    x = "6"
    first += x
    form.textEdit.setText('%s' %first)
    print(first)

def seven():
    global first, number
    number = False
    x = "7"
    first += x
    form.textEdit.setText('%s' %first)
    print(first)

def eight():
    global first, number
    number = False
    x = "8"
    first += x
    form.textEdit.setText('%s' %first)
    print(first)

def nine():
    global first, number
    number = False
    x = "9"
    first += x
    form.textEdit.setText('%s' %first)
    print(first)

def zero():
    global first, number
    number = False
    x = "0"
    first += x
    form.textEdit.setText('%s' %first)
    print(first)

def plus():
    global first, number
    if not number:
        x = "+"
        first += x
        form.textEdit.setText('%s' %first)
        number = True
    print(first)

def minus():
    global first, number
    if not number:
        x = "-"
        first += x
        form.textEdit.setText('%s' %first)
        number = True
    print(first)

def multiply():
    global first, number
    if not number:
        x = "*"
        first += x
        form.textEdit.setText('%s' %first)
        number = True
    print(first)

def division():
    global first, number
    if not number:
        x = "/"
        first += x
        form.textEdit.setText('%s' %first)
        number = True
    print(first)

def delete():
    global first, number
    first = first[:-1]
    form.textEdit.setText('%s' %first)
    number = False
    print(first)


   



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

app.exec_()