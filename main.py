from typing import Text
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QPushButton
import sys

class Window(QWidget):
    def __init__(self):# команда для создания окна
        super(Window, self).__init__()
        self.set_UI()

    def set_UI(self):# что будет в окне
        self.setWindowTitle('КАЛЬКУЛЯТОР')# название окна
        self.setGeometry(200, 200, 600, 600)#устанавливает геометрию сдвиги и размеры
        
        self.le = QLineEdit(self)#le-название элемента 
        self.le.setGeometry(50, 50, 500, 50)

        self.lbl = QLabel(self)# надпись в окне
        self.lbl.setGeometry(250, 20, 100, 30)
        self.lbl.setText('Введите пример')

        self.btn0 = QPushButton(self)
        self.btn0.setGeometry(175, 265, 120, 50)
        self.btn0.setText('0')
        self.btn0.clicked.connect(self.set_text_0)

        self.btn1 = QPushButton(self)
        self.btn1.setGeometry(50, 100, 120, 50)
        self.btn1.setText('1')
        self.btn1.clicked.connect(self.set_text1)

        self.btn2 = QPushButton(self)
        self.btn2.setGeometry(175, 100, 120, 50)
        self.btn2.setText('2')
        self.btn2.clicked.connect(self.set_text2)
        
        self.btn3 = QPushButton(self)
        self.btn3.setGeometry(300, 100, 120, 50)
        self.btn3.setText('3')
        self.btn3.clicked.connect(self.set_text3)
        
        self.btn4 = QPushButton(self)
        self.btn4.setGeometry(50, 155,120, 50)
        self.btn4.setText('4')
        self.btn4.clicked.connect(self.set_text4)
        
        self.btn5 = QPushButton(self)
        self.btn5.setGeometry(175, 155, 120, 50)
        self.btn5.setText('5')
        self.btn5.clicked.connect(self.set_text5)
        
        self.btn6 = QPushButton(self)
        self.btn6.setGeometry(300, 155, 120, 50)
        self.btn6.setText('6')
        self.btn6.clicked.connect(self.set_text6)
        
        self.btn7 = QPushButton(self)
        self.btn7.setGeometry(50, 210, 120, 50)
        self.btn7.setText('7')
        self.btn7.clicked.connect(self.set_text7)
        
        self.btn8= QPushButton(self)
        self.btn8.setGeometry(175, 210, 120, 50)
        self.btn8.setText('8')
        self.btn8.clicked.connect(self.set_text8)
        
        self.btn9 = QPushButton(self)
        self.btn9.setGeometry(300, 210, 120, 50)
        self.btn9.setText('9')
        self.btn9.clicked.connect(self.set_text9)

        self.plus= QPushButton(self)
        self.plus.setGeometry(425, 100, 120, 50)
        self.plus.setText('+')
        self.plus.clicked.connect(self.set_res1)
         
        self.minus = QPushButton(self)
        self.minus.setGeometry(425, 155, 120, 50)
        self.minus.setText('-')
        self.minus.clicked.connect(self.set_res2)

        self.umnojenie = QPushButton(self)
        self.umnojenie.setGeometry(425, 210, 120, 50)
        self.umnojenie.setText('*')
        self.umnojenie.clicked.connect(self.set_res3)
     
        self.delenie = QPushButton(self)
        self.delenie.setGeometry(425, 265, 120, 50)
        self.delenie.setText('/')
        self.delenie.clicked.connect(self.set_res4)
        
        self.btn = QPushButton(self)
        self.btn.setGeometry(425, 320, 120, 50)
        self.btn.setText('=')
        self.btn.clicked.connect(self.set_text)

        self.show()

    def set_text_0(self):
        text= self.btn0.text()
        self.le.setText(self.le.text()+text)
    def set_text1(self):
        text= self.btn1.text()
        self.le.setText(self.le.text()+text)
    def set_text2(self):
        text = self.btn2.text()
        self.le.setText(self.le.text()+text)
    def set_text3(self):
        text = self.btn3.text()
        self.le.setText(self.le.text()+text)
    def set_text4(self):
        text = self.btn4.text()
        self.le.setText(self.le.text()+text)
    def set_text5(self):
        text = self.btn5.text()
        self.le.setText(self.le.text()+text)
    def set_text6(self):
        text = self.btn6.text()
        self.le.setText(self.le.text()+text)
    def set_text7(self):
        text = self.btn7.text()
        self.le.setText(self.le.text()+text)
    def set_text8(self):
        text = self.btn8.text()
        self.le.setText(self.le.text()+text)
    def set_text9(self):
        text = self.btn9.text()
        self.le.setText(self.le.text()+text)
    def set_res1(self):
        text = self.plus.text()
        self.le.setText(self.le.text()+text)
    def set_res2(self):
        text =  self.minus.text()
        self.le.setText(self.le.text()+text)
    def set_res3(self):
        text= self.umnojenie.text()
        self.le.setText(self.le.text()+text)
    def set_res4 (self):
        text= self.delenie.text()
        self.le.setText(self.le.text()+text)

    def set_text(self):
        char=self.le.text()
        dict=["1","2","3","4","5","6","7","8","9","0"]
        for num in range(10):
            char=char.replace(dict[num],"") 
        if char:
            nums=self.le.text().split(char)
            for id in range(2):
                nums[id]=int(nums[id])
                if char=="+":
                    plus=nums[0]+nums[1]
                    self.le.setText(str(plus))
                if char=="-":
                    minus=nums[0]-nums[1]
                    self.le.setText(str(minus))
                if char=="*":
                    umnojenie=nums[0]*nums[1]
                    self.le.setText(str(umnojenie))
                if char=="/":
                    if nums[1]==0:
                        self.le.setText("на ноль делить нельзя!")
                    else:   
                        delenie=nums[0]/nums[1]
                        self.le.setText(str(delenie))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())