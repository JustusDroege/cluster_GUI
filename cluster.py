
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
import sys
import numpy as np
import cv2

path = "jj"
imgx = cv2.imread('python.jpg')
imgx = cv2.cvtColor(imgx, cv2.COLOR_BGR2RGB)
height, width, channels = imgx.shape
pyImg = QtGui.QImage(imgx, imgx.shape[1],\
                           imgx.shape[0], imgx.shape[1] * 3,QtGui.QImage.Format_RGB888)
save_location = '/home/justus/Desktop/cluster_gui'
resolution = np.zeros((height, width, 3), np.uint8)

        
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1073, 707)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.picLabel = QtWidgets.QLabel(self.centralwidget)
        self.picLabel.setGeometry(QtCore.QRect(170, 460, 47, 13))
        self.picLabel.move(200,50)
        self.picLabel.setObjectName("picLabel")
        self.picLabel.setText("Cluster_GUI")
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
        self.dockWidget_2 = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget_2.setObjectName("dockWidget_2")
        self.dockWidget.setAllowedAreas(QtCore.Qt.RightDockWidgetArea)#|QtCore.Qt.RightDockWidgetArea)
        self.dockWidget2Contents = QtWidgets.QWidget()
        self.dockWidget2Contents.setObjectName("dockWidget2Contents")
        self.treeView = QtWidgets.QTreeView(self.dockWidget2Contents)
        self.treeView.setObjectName("treeView")
        self.dockWidget_2.setWidget(self.treeView)
        self.fileModel = QtWidgets.QFileSystemModel()
        self.fileModel.setRootPath('/home/justus')
        self.treeView.setModel(self.fileModel)
        self.treeView.setWindowTitle("Choose file")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.dockWidgetContents)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(1, 1, 100, 641))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.checkBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        self.checkBox_2 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout.addWidget(self.checkBox_2)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.spinBox_2 = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinBox_2.setObjectName("spinBox_2")
        self.spinBox_2.setMinimum(1)
        self.spinBox_2.setValue(10)
        self.verticalLayout.addWidget(self.spinBox_2)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
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
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout.addWidget(self.pushButton_5)
        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget_2)
        file_menu = self.menubar.addMenu('File')
        open_file = file_menu.addMenu('&Open')
        exit_menu = self.menubar.addMenu('Info')
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.picLabel.resize(MainWindow.width(), MainWindow.height())
        
        self.pushButton_2.clicked.connect(self.cluster_img)
        self.spinBox.valueChanged.connect(self.valueChanged_k)
        self.spinBox_3.valueChanged.connect(self.valueChanged_attempts)
        self.pushButton_3.clicked.connect(self.reset)
        self.pushButton_4.clicked.connect(self.save_current)
        self.pushButton_5.clicked.connect(self.upload)
        self.treeView.clicked.connect(self.onClicked)
        #k=self.spinBox.value()
        #attempts=self.spinBox_3.value()
        ####SET DEFAULT IMAGE
        global pyImg
        pixmap = QPixmap(pyImg)
        self.picLabel.setPixmap(pixmap.scaled(MainWindow.width(),MainWindow.height()))
    def upload(self):
        try:
            print(path)
            imgx = cv2.imread(path)
            imgx = cv2.cvtColor(imgx, cv2.COLOR_BGR2RGB)
            print(imgx.shape)
            global pyImg
            pyImg = QtGui.QImage(imgx, imgx.shape[1],\
                            imgx.shape[0], imgx.shape[1] * 3,QtGui.QImage.Format_RGB888)
            pixmap = QPixmap(pyImg)
            global imgx
            imgx = imgx
            #self.picLabel.resize(MainWindow.width(), MainWindow.height())
            self.picLabel.setPixmap(pixmap.scaled(MainWindow.width(),MainWindow.height()))
        except:
            print("Not an image")
    def onClicked(self, index):
        global path
        path = self.fileModel.filePath(index) 
        name = self.fileModel.fileName(index)
        #print(path)
        #print(name)
        #return path
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
        elif self.checkBox.isChecked() == False & self.checkBox_2.isChecked() == False:
            criteria_check = cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER #default case
        Z = imgx.reshape((-1,3))
        Z = np.float32(Z)
        criteria = (criteria_check, maxIter, accuracy)
        ret,label,center=cv2.kmeans(Z,k,None,criteria,attempts,cv2.KMEANS_RANDOM_CENTERS)
        center = np.uint8(center)
        res = center[label.flatten()]
        res2 = res.reshape((imgx.shape))
        res_width = res2.shape[0]
        res_heigth = res2.shape[1]
        for i in range(res_width):
            for j in range(res_heigth):
                resolution[i][j] = res2[i][j]
        res2=QtGui.QImage(res2, res2.shape[1],\
                            res2.shape[0], res2.shape[1] * 3,QtGui.QImage.Format_RGB888)
        pixmap=QPixmap(res2)
        self.picLabel.setPixmap(pixmap.scaled(self.picLabel.width(),self.picLabel.height()))
    def reset(self):
        pixmap=QPixmap(pyImg)
        self.picLabel.setPixmap(pixmap.scaled(self.picLabel.width(),self.picLabel.height()))
        
    def save_current(self):
        resolution_img = cv2.cvtColor(resolution, cv2.COLOR_BGR2RGB)
        cv2.imwrite(str(self.spinBox.value()) + '_' + str(self.spinBox_3.value()) + '_MAX_ITER_' + str(self.spinBox_2.value()) + '_ACC_' + str(self.doubleSpinBox.value()) + '.jpg', resolution_img) 

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "k-Means-Cluster GUI"))
        self.picLabel.setText(_translate("MainWindow", "TextLabel"))
        self.checkBox.setText(_translate("MainWindow", "MAX_ITER"))
        self.checkBox_2.setText(_translate("MainWindow", "EPS"))
        self.label_2.setText(_translate("MainWindow", "ATTEMPTS"))
        self.label_3.setText(_translate("MainWindow", "MAX_ITER"))
        self.label_4.setText(_translate("MainWindow", "EPSILON"))
        self.label_5.setText(_translate("MainWindow", "FLAGS"))
        self.label.setText(_translate("MainWindow", "k"))
        self.pushButton_2.setText(_translate("MainWindow", "UPDATE"))
        self.pushButton_3.setText(_translate("MainWindow", "RESET"))
        self.pushButton_4.setText(_translate("MainWindow", "SAVE"))
        self.pushButton_5.setText(_translate("MainWindow", "UPLOAD"))

        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.showMaximized()
    sys.exit(app.exec_())

