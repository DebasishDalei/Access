from random import random
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget,QApplication,QLabel,QHBoxLayout,QListWidgetItem
import cv2
import numpy as np
import mysql.connector
import sys
import qrcode
import random
from datetime import datetime
import csv

db = mysql.connector.connect(host="localhost", user="root", passwd="",database="OpenCV")
cursor = db.cursor()

class CustomQWidget(QWidget):
    def __init__(self, row):
        super().__init__()
        label1 = QLabel(row[0])
        label2 = QLabel()
        label3 = QLabel()
        label1.setAlignment(QtCore.Qt.AlignCenter)
        label2.setAlignment(QtCore.Qt.AlignCenter)
        label3.setAlignment(QtCore.Qt.AlignCenter)
        if row[2]==0:
            label2.setText(str(row[1]))
        else:
            label3.setText(str(row[1]))
        layout = QHBoxLayout()
        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(label3)
        self.setLayout(layout)

class Ui_MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(994, 620)
        self.tabs = QtWidgets.QTabWidget(self)
        self.tabs.setGeometry(QtCore.QRect(0, 0, 981, 611))
        self.tabs.setObjectName("tabs")
        self.recent = QtWidgets.QWidget()
        self.recent.setObjectName("recent")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.recent)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 581, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)

        self.sign_button = QtWidgets.QPushButton(self.recent)
        self.sign_button.setGeometry(QtCore.QRect(670, 160, 241, 181))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(20)
        self.sign_button.setFont(font)
        self.sign_button.setAutoFillBackground(False)
        self.sign_button.setStyleSheet("background-color:rgb(238, 238, 238)")
        self.sign_button.setCheckable(False)
        self.sign_button.setObjectName("sign_button")

        self.export_button = QtWidgets.QPushButton(self.recent)
        self.export_button.setGeometry(QtCore.QRect(670, 351, 241, 50))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(13)
        self.export_button.setFont(font)
        self.export_button.setAutoFillBackground(False)
        self.export_button.setStyleSheet("background-color:rgb(238, 238, 238)")
        self.export_button.setCheckable(False)
        self.export_button.setObjectName("export_button")

        self.reset_button = QtWidgets.QPushButton(self.recent)
        self.reset_button.setGeometry(QtCore.QRect(670, 411, 241, 50))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(13)
        self.reset_button.setFont(font)
        self.reset_button.setAutoFillBackground(False)
        self.reset_button.setStyleSheet("background-color:rgb(238, 238, 238)")
        self.reset_button.setCheckable(False)
        self.reset_button.setObjectName("reset_button")

        self.recent_list = QtWidgets.QListWidget(self.recent)
        self.recent_list.setGeometry(QtCore.QRect(10, 50, 581, 531))
        self.recent_list.setObjectName("recent_list")
        self.tabs.addTab(self.recent, "")
        self.reg = QtWidgets.QWidget()
        self.reg.setObjectName("reg")
        self.save_button = QtWidgets.QPushButton(self.reg)
        self.save_button.setGeometry(QtCore.QRect(420, 330, 121, 31))
        self.save_button.setObjectName("save_button")
        self.generate_button = QtWidgets.QPushButton(self.reg)
        self.generate_button.setGeometry(QtCore.QRect(360, 250, 251, 31))
        self.generate_button.setObjectName("generate_button")
        self.label_4 = QtWidgets.QLabel(self.reg)
        self.label_4.setGeometry(QtCore.QRect(280, 80, 389, 108))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.eid_textbox = QtWidgets.QLineEdit(self.reg)
        self.eid_textbox.setGeometry(QtCore.QRect(290, 200, 389, 24))
        self.eid_textbox.setObjectName("eid_textbox")
        self.label_5 = QtWidgets.QLabel(self.reg)
        self.label_5.setGeometry(QtCore.QRect(340, 300, 281, 20))
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.tabs.addTab(self.reg, "")

        self.setWindowTitle("MainWindow")
        self.tabs.setToolTip("<html><head/><body><p><br/></p></body></html>")
        self.label_3.setText("Name")
        self.label_2.setText("Arrival Time")
        self.label.setText("Depature Time")
        self.sign_button.setText("SIGN")
        self.export_button.setText("EXPORT")
        self.reset_button.setText("RESET")
        self.tabs.setTabText(self.tabs.indexOf(self.recent), "Recent Users")
        self.save_button.setText("Save")
        self.generate_button.setText("Generate QR")
        self.label_4.setText("Employee ID")
        self.tabs.setTabText(self.tabs.indexOf(self.reg),"Register")
        
        #export
        self.export_button.clicked.connect(self.export)
        self.entries=[]
        
        #fill the list(recent entries)
        cursor.execute("select * from register")
        result=cursor.fetchall()
        for row in result:
            item = QListWidgetItem()
            item_widget = CustomQWidget(row)
            item.setSizeHint(item_widget.sizeHint())
            self.recent_list.insertItem(0,item)
            self.recent_list.setItemWidget(item, item_widget)
            if row[2]==0:
                self.entries.insert(0,[row[0],"Arrival",row[1]])
            else:
                self.entries.insert(0,[row[0],"Depature",row[1]])

        #generation module
        self.generate_button.clicked.connect(self.generate)
        self.eid=None
        self.code=None
        self.save_button.clicked.connect(self.save)
        self.img=None

        #registration module
        self.sign_button.clicked.connect(self.sign)

        #reset
        self.reset_button.clicked.connect(self.reset)

    def generate(self):
        self.eid=self.eid_textbox.text()
        #check valid eid
        cursor.execute("select * from employee where eid=%s",(self.eid,))
        result=cursor.fetchall()
        if len(result)==0:
            self.label_5.setText("Wrong employee id")
            return
        #generate unique security code
        cursor.execute("select security_code from employee")
        result=cursor.fetchall()
        while True:
            self.code=random.randrange(111111111,999999999)
            if self.code not in result[0]:
                break 
        cursor.execute("update employee set security_code=%s where eid=%s",(self.code,self.eid))
        db.commit()
        #generate qr code
        self.img=qrcode.make(self.code)
        self.label_5.setText("QRCode generated successfully")

    def save(self):
        #check if generation is successfull
        if self.img==None:
            self.label_5.setText("No QRCode found")
            return
        #save to device
        self.img.save(self.eid+".jpg")
        self.label_5.setText("QRCode saved")
    
    
    def sign(self):
        self.video=cv2.VideoCapture(0)
        self.qr=cv2.QRCodeDetector()
        self.security_code=""
        while True:    
            check,img=self.video.read()
            cv2.imshow("Face",img)
            self.security_code,points,straight_qrcode=self.qr.detectAndDecode(img)
            if self.security_code!="":
                r=self.check_valid_employee()
                if r==True:
                    break
            key=cv2.waitKey(1)
            if key==ord('x'):
                break
        self.video.release()
        #register entry/exit       
        self.register()
        cv2.destroyAllWindows()

    def check_valid_employee(self):
        cursor.execute("select * from employee where security_code=%s",(self.security_code,))
        result=cursor.fetchall()
        if len(result)==0:
            return False
        cursor.execute("select * from register where eid=%s",(result[0][0],))
        result=cursor.fetchall()
        if len(result)>=2:
            return False
        return True

    def register(self):
        if self.security_code=="":
            return
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        cursor.execute("select eid,name from employee where security_code=%s",(self.security_code,))
        result=cursor.fetchall()
        emp_id=result[0][0]
        emp_name=result[0][1]
        cursor.execute("select * from register where eid=%s",(emp_id,))
        result=cursor.fetchall()
        if len(result)==0:
            cursor.execute("insert into register values(%s,%s,%s,%s)",(emp_name,current_time,0,emp_id))
            db.commit()
            row=(emp_name,current_time,0)
            item = QListWidgetItem()
            item_widget = CustomQWidget(row)
            item.setSizeHint(item_widget.sizeHint())
            self.recent_list.insertItem(0,item)
            self.recent_list.setItemWidget(item, item_widget)
            self.entries.insert(0,[emp_name,"Arrival",current_time])
        else:
            cursor.execute("insert into register values(%s,%s,%s,%s)",(emp_name,current_time,1,emp_id))
            db.commit()
            row=(emp_name,current_time,1)
            item = QListWidgetItem()
            item_widget = CustomQWidget(row)
            item.setSizeHint(item_widget.sizeHint())
            self.recent_list.insertItem(0,item)
            self.recent_list.setItemWidget(item, item_widget)
            self.entries.insert(0,[emp_name,"Depature",current_time])
        
    def export(self):
        fields=['Name','Status','Time']
        with open('entries.csv', 'w') as f:
            write = csv.writer(f)    
            write.writerow(fields)
            write.writerows(self.entries)

    def reset(self):
        cursor.execute("delete from register")
        db.commit()
        self.recent_list.clear()
        self.entries=[]

if __name__=="__main__":
    app = QApplication(sys.argv)
    window = Ui_MainWindow()
    window.show()
    sys.exit(app.exec_())
