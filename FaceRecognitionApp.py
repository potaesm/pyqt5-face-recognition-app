# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FaceRecognitionApp.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 520)
        MainWindow.setMinimumSize(QtCore.QSize(800, 520))
        MainWindow.setMaximumSize(QtCore.QSize(800, 520))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/src/Themes/eyeIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/src/Themes/eyeIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap(":/src/Themes/eyeIcon.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/src/Themes/eyeIcon.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap(":/src/Themes/eyeIcon.png"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/src/Themes/eyeIcon.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap(":/src/Themes/eyeIcon.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/src/Themes/eyeIcon.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolTip("")
        MainWindow.setStatusTip("")
        MainWindow.setWhatsThis("")
        MainWindow.setAccessibleName("")
        MainWindow.setAccessibleDescription("")
        MainWindow.setWindowFilePath("")
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 781, 482))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.imageLabel = QtWidgets.QLabel(self.layoutWidget)
        self.imageLabel.setMinimumSize(QtCore.QSize(640, 480))
        self.imageLabel.setMaximumSize(QtCore.QSize(640, 480))
        self.imageLabel.setStyleSheet("background-color: rgb(112, 112, 112);")
        self.imageLabel.setText("")
        self.imageLabel.setObjectName("imageLabel")
        self.horizontalLayout_2.addWidget(self.imageLabel)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.toggleCameraButton = QtWidgets.QPushButton(self.layoutWidget)
        self.toggleCameraButton.setObjectName("toggleCameraButton")
        self.verticalLayout.addWidget(self.toggleCameraButton)
        self.captureButton = QtWidgets.QPushButton(self.layoutWidget)
        self.captureButton.setObjectName("captureButton")
        self.verticalLayout.addWidget(self.captureButton)
        self.chooseCompareImageButton = QtWidgets.QPushButton(self.layoutWidget)
        self.chooseCompareImageButton.setObjectName("chooseCompareImageButton")
        self.verticalLayout.addWidget(self.chooseCompareImageButton)
        self.CompareButton = QtWidgets.QPushButton(self.layoutWidget)
        self.CompareButton.setObjectName("CompareButton")
        self.verticalLayout.addWidget(self.CompareButton)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.resultTitleLabel = QtWidgets.QLabel(self.layoutWidget)
        self.resultTitleLabel.setObjectName("resultTitleLabel")
        self.horizontalLayout.addWidget(self.resultTitleLabel)
        self.resultLabel = QtWidgets.QLabel(self.layoutWidget)
        self.resultLabel.setObjectName("resultLabel")
        self.horizontalLayout.addWidget(self.resultLabel)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Face Recognition App"))
        self.toggleCameraButton.setText(_translate("MainWindow", "Turn On"))
        self.captureButton.setText(_translate("MainWindow", "Capture"))
        self.chooseCompareImageButton.setText(_translate("MainWindow", "Choose Image"))
        self.CompareButton.setText(_translate("MainWindow", "Compare"))
        self.resultTitleLabel.setText(_translate("MainWindow", "Result:"))
        self.resultLabel.setText(_translate("MainWindow", "False"))
import resource_rc
