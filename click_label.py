from PyQt5 import QtCore
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import QLabel

class ClickableLabel(QLabel):
    def setListener(self, listener):
        self.mListener = listener

    def event(self, e: QtCore.QEvent) -> bool:
        if (e.type() == QtCore.QEvent.MouseButtonRelease):
            self.mListener.open_file()
        return super().event(e)

    def mouseDoubleClickEvent(self, a0: QMouseEvent) -> None:
        # print("Yo")
        return super().mouseDoubleClickEvent(a0)