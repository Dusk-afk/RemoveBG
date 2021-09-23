from PyQt5 import QtCore, QtGui, QtWidgets

class ImageViewer(QtWidgets.QGraphicsView):
    def __init__(self, parent):
        super(ImageViewer, self).__init__(parent)
        self._zoom = 0
        self._empty = True
        self._scene = QtWidgets.QGraphicsScene(self)
        self._photo = QtWidgets.QGraphicsPixmapItem()
        self._scene.addItem(self._photo)
        self._limit_zoom = 15
        self._zoom_disabled = False
        self.setScene(self._scene)
        self.setTransformationAnchor(QtWidgets.QGraphicsView.AnchorUnderMouse)
        self.setResizeAnchor(QtWidgets.QGraphicsView.AnchorUnderMouse)
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setBackgroundBrush(QtGui.QBrush(QtGui.QColor(30, 30, 30)))
        self.setFrameShape(QtWidgets.QFrame.NoFrame)


    def fitInView(self, scale=True):
        rect = QtCore.QRectF(self._photo.pixmap().rect())
        if not rect.isNull():
            self.setSceneRect(rect)
            if not self._empty:
                unity = self.transform().mapRect(QtCore.QRectF(0, 0, 1, 1))
                self.scale(1 / unity.width(), 1 / unity.height())
                viewrect = self.viewport().rect()
                scenerect = self.transform().mapRect(rect)
                factor = min(viewrect.width() / scenerect.width(),
                             viewrect.height() / scenerect.height())
                self.scale(factor, factor)
            self._zoom = 0

    def setPhoto(self, pixmap:QtGui.QPixmap = None):
        self._zoom = 0
        if pixmap and not pixmap.isNull():
            self._empty = False
            self.setDragMode(QtWidgets.QGraphicsView.ScrollHandDrag)
            self._photo.setPixmap(pixmap)
        else:
            self._empty = True
            self.setDragMode(QtWidgets.QGraphicsView.NoDrag)
            self._photo.setPixmap(QtGui.QPixmap())
        self.fitInView()

    def wheelEvent(self, event):
        if self._zoom_disabled:
            return
        if not self._empty:
            if event.angleDelta().y() > 0:
                factor = 1.15
                self._zoom += 1
            else:
                factor = 0.85
                if self._zoom >= self._limit_zoom:
                    self._zoom = self._limit_zoom
                self._zoom -= 1

            if self._zoom > self._limit_zoom: pass
            elif self._zoom > 0: self.scale(factor, factor)
            else: self.fitInView()

    def mouseDoubleClickEvent(self, event: QtGui.QMouseEvent) -> None:
        if self._zoom == 0:
            self._zoom = self._limit_zoom
            self.scale(1*(self._limit_zoom/2), 1*(self._limit_zoom/2))

        else:
            self._zoom = 0
            self.fitInView()

        return super().mouseDoubleClickEvent(event)

    def disablePanZoom(self):
        self._zoom_disabled = True
        self.setDragMode(QtWidgets.QGraphicsView.NoDrag)

    def enablePanZoom(self):
        if not self._photo.pixmap().isNull():
            self._zoom_disabled = False
            self.setDragMode(QtWidgets.QGraphicsView.ScrollHandDrag)