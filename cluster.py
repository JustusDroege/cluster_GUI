# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cluster.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel, QMainWindow, QApplication, QWidget, QGraphicsScene
from PyQt5.QtGui import QPixmap
import sys
import numpy as np
import cv2

img = cv2.imread('arc.JPG')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
pyImg = QtGui.QImage(img, img.shape[1],\
                            img.shape[0], img.shape[1] * 3,QtGui.QImage.Format_RGB888)
        
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1073, 707)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        #self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        #self.graphicsView.setGeometry(QtCore.QRect(120, 140, 256, 192))
        #self.graphicsView.setObjectName("graphicsView")
        self.picLabel = QtWidgets.QLabel(self.centralwidget)
        self.picLabel.setGeometry(QtCore.QRect(170, 460, 47, 13))
        self.picLabel.setObjectName("picLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1073, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.dockWidgetContents)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 81, 641))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        self.checkBox_2 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout.addWidget(self.checkBox_2)
        self.spinBox_2 = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinBox_2.setObjectName("spinBox_2")
        self.spinBox_2.setMinimum(1)
        self.spinBox_2.setValue(1)
        self.verticalLayout.addWidget(self.spinBox_2)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.doubleSpinBox.setMinimum(1.00)
        self.doubleSpinBox.setValue(1.00)
        self.verticalLayout.addWidget(self.doubleSpinBox)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.spinBox_3 = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinBox_3.setObjectName("spinBox_3")
        self.spinBox_3.setValue(10)
        self.spinBox_3.setMinimum(1)
        self.verticalLayout.addWidget(self.spinBox_3)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.spinBox = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinBox.setObjectName("spinBox")
        self.spinBox.setValue(1)
        self.spinBox.setMinimum(1)
        self.verticalLayout.addWidget(self.spinBox)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget)
        self.retranslateUi(MainWindow)
        #self.pushButton_2.clicked.connect(self.picLabel.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        pixmapp=QPixmap(pyImg)
        self.picLabel.move(0,0)
        self.picLabel.resize(MainWindow.width(), MainWindow.height())
        self.picLabel.setPixmap(pixmapp.scaled(MainWindow.width(),MainWindow.height()))
        
        self.pushButton_2.clicked.connect(self.cluster_img)
        self.spinBox.valueChanged.connect(self.valueChanged_k)
        self.spinBox_3.valueChanged.connect(self.valueChanged_attempts)
        #k=self.spinBox.value()
        #attempts=self.spinBox_3.value()
    def valueChanged_attempts(self):
        attempts = self.spinBox_3.value()
        return attempts
    def valueChanged_k(self):
        k = self.spinBox.value()
        return k
    def cluster_img(self):
        k = self.spinBox.value()
        attempts = self.spinBox_3.value()
        maxIter = self.spinBox_2.value()
        accuracy = self.doubleSpinBox.value()
        criteria_check = cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER
        criteria_eps = cv2.TERM_CRITERIA_EPS
        criteria_max_iter = cv2.TERM_CRITERIA_MAX_ITER
        if self.checkBox.isChecked() & self.checkBox_2.isChecked():
            criteria_check = cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER
        elif self.checkBox.isChecked() & self.checkBox_2.isChecked() == False:
            criteria_check = criteria_max_iter
        elif self.checkBox.isChecked() == False & self.checkBox_2.isChecked():
            criteria_check = criteria_eps
        Z = img.reshape((-1,3))
        Z = np.float32(Z)
        criteria = (criteria_check, maxIter, accuracy)
        #K = 8
        ret,label,center=cv2.kmeans(Z,k,None,criteria,attempts,cv2.KMEANS_RANDOM_CENTERS)
        center = np.uint8(center)
        res = center[label.flatten()]
        res2 = res.reshape((img.shape))
        res2=QtGui.QImage(res2, res2.shape[1],\
                            res2.shape[0], res2.shape[1] * 3,QtGui.QImage.Format_RGB888)
        pixmap=QPixmap(res2)
        self.picLabel.setPixmap(pixmap.scaled(MainWindow.width(),MainWindow.height()))
    def show_img(self, img):
        pixmapp=QPixmap(img)
        self.picLabel.move(0,0)
        self.picLabel.resize(MainWindow.width(), MainWindow.height())
        self.picLabel.setPixmap(pixmapp.scaled(MainWindow.width(),MainWindow.height()))
        
    def update(self):
        if self.checkBox.isChecked() == True:
            print("Hallo")
        if self.spinBox_2.value() == 2:
            print("2")
        k = self.spinBox.value()
        attempts = self.spinBox_3.value()
        return k, attempts
    
    

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "k-Means-Cluster GUI"))
        self.picLabel.setText(_translate("MainWindow", "TextLabel"))
        self.checkBox.setText(_translate("MainWindow", "MAX_ITER"))
        self.checkBox_2.setText(_translate("MainWindow", "EPS"))
        self.label_2.setText(_translate("MainWindow", "ATTEMPTS"))
        self.label.setText(_translate("MainWindow", "k"))
        self.pushButton_2.setText(_translate("MainWindow", "UPDATE"))
        
        

        
        
#class viewImage(Ui_MainWindow):
#    def __init__(self):
#        super().__init__()
#        pixmap = QPixmap('arc.JPG')
#        picLabel=Ui_MainWindow.picLabel(self)
#        picLabel.setPixmap(pixmap)
#        self.show()
#   	
	#@pyqtSlot( )
    # def function(self):
	    # image_path = r'C:\Users\User\Desktop\Fotos Trip\arc.JPG'
	    # self.show_frame_in_display(image_path)
		
    # def show_frame_in_display(self, image_path):
	    # frame = QtGui.QWidget()
	    # picLabel = QtGui.QImage(image_path)
	    # image_profile = image_profile.scaled(250,250, aspectRatioMode=QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
	    # picLabel.setPixmap(QtGui.QtPixmap.fromImage(image_profile))
    # def loadImage(self):
        # image_path = r'C:\Users\User\Desktop\Fotos Trip\arc.JPG'
        # pixmap = QPixmap(image_path)
        # picLabel.setPixmap(pixmap)
        # self.show()
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

