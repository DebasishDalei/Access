from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget,QApplication
from PyQt5.QtCore import QObject
from PyQt5.QtGui import QPixmap
import cv2
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt, QThread
import numpy as np
import sys

class VideoThread(QThread):
    change_pixmap_signal = pyqtSignal(np.ndarray)
    
    def run(self):
        self._run_flag = True
        cap = cv2.VideoCapture(0)
        while self._run_flag:
            ret, cv_img = cap.read()
            if ret:
                self.change_pixmap_signal.emit(cv_img)
        cap.release()
        print("A")

    def stop(self):
        self._run_flag = False
        self.wait()
        print("B")

class Ui_MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1500, 850)
        self.setStyleSheet("background-color:rgb(170, 170, 255)")

        self.thread = VideoThread()
        self.thread.change_pixmap_signal.connect(self.update_image)
        
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(10, 10, 121, 101))
        self.label.setText("LOGO")
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(160, 10, 811, 101))
        self.label_2.setText("AUTOMATED SERVELENCE")
        font = QtGui.QFont()
        font.setPointSize(35)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

        self.display = QtWidgets.QLabel(self)
        self.display.setGeometry(QtCore.QRect(340,200,800,640))
        self.display.setText("")
        self.display.setObjectName("display")
        
        self.recent = QtWidgets.QListView(self)
        self.recent.setGeometry(QtCore.QRect(1150, 250, 330, 550))
        self.recent.setObjectName("recent")
        
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(1150, 200, 330, 40))
        self.label_4.setText("RECENT ENTRIES")
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        
        self.get_in = QtWidgets.QPushButton(self)
        self.get_in.setGeometry(QtCore.QRect(20, 200, 300, 200))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.get_in.setFont(font)
        self.get_in.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.get_in.setStyleSheet("background-color:rgb(0, 136, 0)")
        self.get_in.setText("IN")
        self.get_in.setObjectName("get_in")
        self.get_in.clicked.connect(self.startCamera)
        
        self.get_out = QtWidgets.QPushButton(self)
        self.get_out.setGeometry(QtCore.QRect(20, 420, 300, 200))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.get_out.setFont(font)
        self.get_out.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.get_out.setStyleSheet("background-color:rgb(255, 0, 0)")
        self.get_out.setText("OUT")
        self.get_out.setObjectName("get_out")
        self.get_out.clicked.connect(self.stopCamera)
        
        self.reset = QtWidgets.QPushButton(self)
        self.reset.setGeometry(QtCore.QRect(20, 640, 300, 200))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.reset.setFont(font)
        self.reset.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.reset.setStyleSheet("background-color:rgb(255, 255, 0)")
        self.reset.setText("RESET")
        self.reset.setObjectName("reset")

    def startCamera(self):
        self.thread.start()

    def stopCamera(self):
        self.thread.stop()
    
    @pyqtSlot(np.ndarray)
    def update_image(self, cv_img):
        """Updates the image_label with a new opencv image"""
        qt_img = self.convert_cv_qt(cv_img)
        self.display.setPixmap(qt_img)
    
    def convert_cv_qt(self, cv_img):
        """Convert from an opencv image to QPixmap"""
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(800, 640, Qt.KeepAspectRatio)
        return QPixmap.fromImage(p)

if __name__=="__main__":
    app = QApplication(sys.argv)
    window = Ui_MainWindow()
    window.show()
    sys.exit(app.exec_())
