from PyQt5 import QtCore, QtGui, QtWidgets
from image_viewer import ImageViewer
from click_label import ClickableLabel
import requests

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 720)
        MainWindow.setMinimumSize(QtCore.QSize(1024, 720))
        MainWindow.setMaximumSize(QtCore.QSize(1024, 720))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color:#ffffff;")
        self.centralwidget.setObjectName("centralwidget")
        self.api_key_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.api_key_line_edit.setGeometry(QtCore.QRect(37, 18, 617, 62))
        self.api_key_line_edit.setMinimumSize(QtCore.QSize(617, 62))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        self.api_key_line_edit.setFont(font)
        self.api_key_line_edit.setStyleSheet("background-color:#FFFFFF;\n"
                "padding-left:20px;\n"
                "border-radius:30px;\n"
                "border: 1px solid;\n"
                "color:#424242;\n"
                "border-color: rgb(112, 112, 112);")
        self.api_key_line_edit.setText("")
        self.api_key_line_edit.setMaxLength(24)
        self.api_key_line_edit.setCursorPosition(0)
        self.api_key_line_edit.setObjectName("api_key_line_edit")
        self.image_holder = ImageViewer(self.centralwidget)
        self.image_holder.setGeometry(QtCore.QRect(37, 100, 950, 510))
        self.image_holder.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.image_holder.setStyleSheet("border-radius:30px;")
        self.image_holder.setObjectName("image_holder")
        self.remove_bg_btn = QtWidgets.QPushButton(self.centralwidget)
        self.remove_bg_btn.setGeometry(QtCore.QRect(141, 630, 272, 74))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.remove_bg_btn.setFont(font)
        self.remove_bg_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.remove_bg_btn.setStyleSheet("background-color:#9EFFB7;\n"
                "font: 14pt \"Segoe UI\";\n"
                "color:#414141;\n"
                "border-radius:37px;")
        self.remove_bg_btn.setObjectName("remove_bg_btn")
        self.save_btn = QtWidgets.QPushButton(self.centralwidget)
        self.save_btn.setGeometry(QtCore.QRect(597, 630, 272, 74))
        self.save_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.save_btn.setStyleSheet("background-color:#96F1FF;\n"
                "font: 14pt \"Segoe UI\";\n"
                "color:#414141;\n"
                "border-radius:37px;")
        self.save_btn.setObjectName("save_btn")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setEnabled(True)
        self.background.setGeometry(QtCore.QRect(0, 0, 1024, 768))
        self.background.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.background.setText("")
        self.background.setObjectName("background")
        self.drag_drop_label = ClickableLabel(self.centralwidget)
        self.drag_drop_label.setListener(self)
        self.drag_drop_label.setGeometry(QtCore.QRect(37, 100, 950, 510))
        self.drag_drop_label.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.drag_drop_label.setStyleSheet("border: 1px solid;\n"
                "font-family: \"Segoe UI\";\n"
                "border-radius: 30px;\n"
                "border-color:#707070;")
        self.drag_drop_label.setObjectName("drag_drop_label")
        self.background.raise_()
        self.api_key_line_edit.raise_()
        self.image_holder.raise_()
        self.remove_bg_btn.raise_()
        self.save_btn.raise_()
        self.drag_drop_label.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.api_key_line_edit.setPlaceholderText(_translate("MainWindow", "API Key here"))
        self.remove_bg_btn.setText(_translate("MainWindow", "Remove BG"))
        self.save_btn.setText(_translate("MainWindow", "Save"))
        self.drag_drop_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt; font-weight:600; color:#414141;\">Drag &amp; Drop</span></p><p align=\"center\"><span style=\" font-size:10pt; color:#414141;\">or</span></p><p align=\"center\"><span style=\" font-size:12pt; color:#414141;\">Click Here to Select</span></p></body></html>"))

        ########## CLICKED EVENTS #############
        self.remove_bg_btn.clicked.connect(lambda : self.getImageFromApi(self.current_file_path))
        self.save_btn.clicked.connect(self.save_file)

        ########## MY MESS ##########
        self.image_holder.hide()
        # self.image_holder.setPhoto(QtGui.QPixmap("test_image.jpg"))
        # self.drag_drop_label.hide()

    def open_file(self):
        options = QtWidgets.QFileDialog.Options()
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self.centralwidget,"Select Image", "","Images (*.jpg);;All Files (*)", options=options)

        if fileName == "":
            return

        self.current_file_path = fileName
        self.setImage(fileName)

    def save_file(self):
        file_name = self.current_file_path.split("/")[-1]
        print(file_name)
        option = QtWidgets.QFileDialog.Options()
        file,_ = QtWidgets.QFileDialog.getSaveFileName(self.centralwidget,"Save File",f"{file_name.split('.')[0]}_removedbg.jpg",".jpg",options=option)

        with open(file,"wb") as f:
            f.write(self.current_final_image_data)

        
    def setImage(self, image):
        self.image_holder.show()
        if type(image) == str:
            self.image_holder.setPhoto(QtGui.QPixmap(image))
        else:
            pm = QtGui.QPixmap()
            pm.loadFromData(image)
            self.image_holder.setPhoto(pm)
        self.drag_drop_label.hide()

    def getImageFromApi(self, image_path:str):
        api_key = self.api_key_line_edit.text()
        if api_key == "":
            api_key = "mf1Qab8PU2Ue5wnGP1oefjU3"

        response = requests.post(
            'https://api.remove.bg/v1.0/removebg',
            files={'image_file': open(image_path, 'rb')},
            data={'size': 'auto'},
            headers={'X-Api-Key': api_key},
        )
        if response.status_code == requests.codes.ok:
            self.current_final_image_data = response.content
            self.setImage(response.content)
        else:
            print("Error:", response.status_code, response.text)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())