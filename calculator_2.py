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
    print(first)
    

def two():
    global first
    x = "2"
    first += x
    print(first)

def three():
    global first
    x = "3"
    first += x
    print(first)

def four():
    global first
    x = "4"
    first += x
    print(first)

def five():
    global first
    x = "5"
    first += x
    print(first)

def six():
    global first
    x = "6"
    first += x
    print(first)

def seven():
    global first
    x = "7"
    first += x
    print(first)

def eight():
    global first
    x = "8"
    first += x
    print(first)

def nine():
    global first
    x = "9"
    first += x
    print(first)

def zero():
    global first
    x = "0"
    first += x
    print(first)



first = " "

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

app.exec_()