from PyQt5.QtCore import (pyqtSignal, QLineF, QPointF, QRect, QRectF, QSize,
        QSizeF, Qt)
from PyQt5.QtGui import (QBrush, QColor, QFont, QIcon, QIntValidator, QPainter,
        QPainterPath, QPen, QPixmap, QPolygonF, QFontMetricsF)
from PyQt5.QtWidgets import (QAction, QApplication, QButtonGroup, QComboBox,
        QFontComboBox, QGraphicsItem, QGraphicsLineItem, QGraphicsPolygonItem,
        QGraphicsScene, QGraphicsTextItem, QGraphicsView, QGridLayout,
        QHBoxLayout, QLabel, QMainWindow, QMenu, QMessageBox, QSizePolicy,
        QToolBox, QToolButton, QWidget, QStyleOption, QStyleOptionGraphicsItem, QStyle)
from qtslink import *

import sys
sys.path.append('../../utility')
from qtsgproto_pb2 import *


class Node(QGraphicsItem):
    """
    :type text_color: QColor
    :type outline_color: QColor
    :type background_color: QColor
    :type links: set[Link]
    :type connection_info: QtsGProtoRemote
    """
    def __init__(self, connection_info):
        super(Node, self).__init__()
        self.text_color = QColor(255, 255, 255)
        self.outline_color = QColor(255, 255, 255)
        self.background_color = QColor(255, 255, 255)
        self.links = set()
        self.connection_info = connection_info

    def update_connection_info(self, connection_info):
        pass

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.connection_info.appid == other.connection_info.appid
        else:
            return False

    def __hash__(self):
        return self.connection_info.appid

    def add_link(self, link):
        """:type link: Link"""
        self.links.add(link)

    def remove_link(self, link):
        """:type link: Link"""
        self.links.remove(link)

    def set_text_color(self, color):
        """:type color: QColor"""
        self.text_color = color
        self.update()

    def set_outline_color(self, color):
        """:type color: QColor"""
        self.outline_color = color
        self.update()

    def set_background_color(self, color):
        """:type color: QColor"""
        self.background_color = color
        self.update()

    def boundingRect(self):
        """:rtype QRectF"""
        margin = 1
        return self.__outline_rect().adjusted(-margin, -margin, +margin, +margin)

    def shape(self):
        """:rtype QPainterPath"""
        rect = self.__outline_rect()
        path = QPainterPath()
        path.addRoundRect(rect, self.__roundness(rect.width()), self.__roundness(rect.height()))
        return path

    def paint(self, painter, option, widget):
        """
        :type painter: QPainter
        :type option: QStyleOptionGraphicsItem
        :type widget: QWidget
        """
        pen = QPen()
        if self.isSelected():
            pen.setStyle(Qt.DotLine)
            pen.setWidth(2)
        painter.setPen(pen)
        painter.setBrush(self.background_color)
        rect = self.__outline_rect()
        painter.drawRoundedRect(rect, self.__roundness(rect.width()), self.__roundness(rect.height()))
        painter.setPen(self.text_color)
        painter.drawText(rect, Qt.AlignCenter, self.connection_info.name)

    def mouseMoveEvent(self, mouseEvent):
        """:type mouseEvent: QGraphicsSceneMouseEvent"""
        if mouseEvent.buttons() & Qt.LeftButton:
            for link in self.links:
                link.track_nodes()
        super(Node, self).mouseMoveEvent(mouseEvent)

    def __outline_rect(self):
        """:rtype QRectF"""
        padding = 8
        metrics = QFontMetricsF()
        rect = metrics.boundingRect(self.text)
        """:type rect: QRectF"""
        rect.adjust(-padding, -padding, padding, padding)
        rect.translate(-rect.center())
        return rect

    @staticmethod
    def __roundness(size):
        """
        :rtype int
        :type size: double
        """
        diameter = 12
        return 100 * diameter / int(size)