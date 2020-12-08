from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QMessageBox, QFileDialog
import resource
import cv2
import tempfile
import requests
import os


# noinspection PyAttributeOutsideInit
class UiMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.__toggleCam = False
        self.__onCaptureClicked = False
        self.__onCompareImageClicked = False
        self.__compareImagePath = ""

    def changeEvent(self, event):
        if event.type() == QtCore.QEvent.WindowStateChange:
            if self.windowState() and QtCore.Qt.WindowMinimized:
                print("WindowMinimized")
            elif self.windowState() == QtCore.Qt.WindowNoState or event.oldState() == QtCore.Qt.WindowMaximized:
                print("WindowMaximized")

    def closeEvent(self, event):
        reply = QMessageBox.question(self, "Quit", "Are you sure to quit?", QMessageBox.No | QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            self.__toggleCam = False
            event.accept()
        else:
            event.ignore()

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(800, 520)
        self.setMinimumSize(QtCore.QSize(800, 520))
        self.setMaximumSize(QtCore.QSize(800, 520))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/src/Themes/eyeIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/src/Themes/eyeIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap(":/src/Themes/eyeIcon.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/src/Themes/eyeIcon.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap(":/src/Themes/eyeIcon.png"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/src/Themes/eyeIcon.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap(":/src/Themes/eyeIcon.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/src/Themes/eyeIcon.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.setWindowIcon(icon)
        self.setToolTip("")
        self.setStatusTip("")
        self.setWhatsThis("")
        self.setAccessibleName("")
        self.setAccessibleDescription("")
        self.setWindowFilePath("")
        self.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(self)
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
        self.resultLabel.setWordWrap(True)
        self.horizontalLayout.addWidget(self.resultLabel)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.setCentralWidget(self.centralwidget)

        self.toggleCameraButton.clicked.connect(self.displayImage)
        self.captureButton.clicked.connect(self.captureImage)
        self.chooseCompareImageButton.clicked.connect(self.chooseImageToCompare)
        self.CompareButton.clicked.connect(self.compareImage)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Face Recognition App"))
        self.toggleCameraButton.setText(_translate("MainWindow", "Turn On"))
        self.captureButton.setText(_translate("MainWindow", "Capture"))
        self.chooseCompareImageButton.setText(_translate("MainWindow", "Choose Image"))
        self.CompareButton.setText(_translate("MainWindow", "Compare"))
        self.resultTitleLabel.setText(_translate("MainWindow", "Result:"))
        self.resultLabel.setText(_translate("MainWindow", "False"))

    def captureImage(self):
        if self.__toggleCam:
            self.__onCaptureClicked = True

    def destroyImage(self):
        self.toggleCameraButton.setText("Turn On")
        self.imageLabel.setText(" ")
        cv2.destroyAllWindows()

    def saveImage(self, img):
        path = QFileDialog.getSaveFileName()
        cv2.imwrite(path[0], img)

    def chooseImageToCompare(self):
        path = QFileDialog.getOpenFileName()
        self.__compareImagePath = os.path.normpath(path[0])
        print(self.__compareImagePath)

    def compareImage(self):
        if self.__toggleCam:
            self.__onCompareImageClicked = True

    def sendCompareRequest(self, img):
        with tempfile.TemporaryDirectory() as tmpDirName:
            filePath = tmpDirName + ".jpg"
            cv2.imwrite(filePath, img)
            imgName = os.path.basename(filePath)
            compareImgName = os.path.basename(self.__compareImagePath)
            proxy_dict = {}
            # proxy_dict = {"http": "http://10.186.208.15:8080"}
            imageFileDescriptor = open(filePath, 'rb')
            compareImageFileDescriptor = open(self.__compareImagePath, 'rb')
            print(compareImageFileDescriptor, imageFileDescriptor)
            # Single file
            # files = {'img': (imgName, imageFileDescriptor, 'multipart/form-data', {'Expires': '0'})}
            # Multiple files
            files = [
                ("imgs", (imgName, imageFileDescriptor, 'multipart/form-data', {'Expires': '0'})),
                ("imgs", (compareImgName, compareImageFileDescriptor, 'multipart/form-data', {'Expires': '0'}))
            ]
            response = requests.request("POST", "https://node-js-face-api.herokuapp.com/compare", files=files,
                                        proxies=proxy_dict)
            # self.resultLabel.setText(response.text)
            self.resultLabel.setText(response.text)
            # print(response.text)
            imageFileDescriptor.close()
            if os.path.exists(filePath):
                os.remove(filePath)

    def displayImage(self):
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        self.__toggleCam = not self.__toggleCam
        if not self.__toggleCam:
            self.destroyImage()
        else:
            self.toggleCameraButton.setText("Turn Off")
            captureImage = None
            while cap.isOpened() and not self.__onCaptureClicked and not self.__onCompareImageClicked and self.__toggleCam:
                ret, img = cap.read()
                if ret:
                    captureImage = img
                    qformat = QImage.Format_Indexed8
                    if len(img.shape) == 3:
                        if (img.shape[2]) == 4:
                            qformat = QImage.Format_RGBA888
                        else:
                            qformat = QImage.Format_RGB888
                    img = QImage(img, img.shape[1], img.shape[0], qformat)
                    img = img.rgbSwapped()
                    self.imageLabel.setPixmap(QPixmap.fromImage(img))
                    cv2.waitKey()
            if self.__onCaptureClicked:
                self.__toggleCam = False
                self.__onCaptureClicked = False
                self.destroyImage()
                self.saveImage(captureImage)
            if self.__onCompareImageClicked:
                self.__toggleCam = False
                self.__onCompareImageClicked = False
                self.destroyImage()
                self.sendCompareRequest(captureImage)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    mainWindow = UiMainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
