from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 720)
        MainWindow.setMinimumSize(QtCore.QSize(1024, 720))
        MainWindow.setMaximumSize(QtCore.QSize(1024, 720))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("bacground-color:#ffffff;")
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
        self.image_holder = QtWidgets.QGraphicsView(self.centralwidget)
        self.image_holder.setGeometry(QtCore.QRect(37, 100, 950, 510))
        self.image_holder.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.image_holder.setStyleSheet("border-radius:1px;")
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
        self.dowload_btn = QtWidgets.QPushButton(self.centralwidget)
        self.dowload_btn.setGeometry(QtCore.QRect(597, 630, 272, 74))
        self.dowload_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dowload_btn.setStyleSheet("background-color:#96F1FF;\n"
                "font: 14pt \"Segoe UI\";\n"
                "color:#414141;\n"
                "border-radius:37px;")
        self.dowload_btn.setObjectName("dowload_btn")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setEnabled(True)
        self.background.setGeometry(QtCore.QRect(0, 0, 1024, 768))
        self.background.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.background.setText("")
        self.background.setObjectName("background")
        self.drag_drop_label = QtWidgets.QLabel(self.centralwidget)
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
        self.dowload_btn.raise_()
        self.drag_drop_label.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.api_key_line_edit.setPlaceholderText(_translate("MainWindow", "API Key here"))
        self.remove_bg_btn.setText(_translate("MainWindow", "Remove BG"))
        self.dowload_btn.setText(_translate("MainWindow", "Download"))
        self.drag_drop_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt; font-weight:600; color:#414141;\">Drag &amp; Drop</span></p><p align=\"center\"><span style=\" font-size:10pt; color:#414141;\">or</span></p><p align=\"center\"><span style=\" font-size:12pt; color:#414141;\">Click Here to Select</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
