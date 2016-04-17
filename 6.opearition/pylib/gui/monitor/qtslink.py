from PyQt5.QtCore import (pyqtSignal, QLineF, QPointF, QRect, QRectF, QSize,
        QSizeF, Qt)
from PyQt5.QtGui import (QBrush, QColor, QFont, QIcon, QIntValidator, QPainter,
        QPainterPath, QPen, QPixmap, QPolygonF)
from PyQt5.QtWidgets import (QAction, QApplication, QButtonGroup, QComboBox,
        QFontComboBox, QGraphicsItem, QGraphicsLineItem, QGraphicsPolygonItem,
        QGraphicsScene, QGraphicsTextItem, QGraphicsView, QGridLayout,
        QHBoxLayout, QLabel, QMainWindow, QMenu, QMessageBox, QSizePolicy,
        QToolBox, QToolButton, QWidget)
from qtsnode import Node

import sys
import os
sys.path.append(os.path.join(os.getenv('QTS_BASE_PATH','../..'),'pylib/utility'))
try :
	from qtsgproto_pb2 import *
except :
	print('warning>> python lib no support protocol buffer')


class LinkKey(object):
    """
    :type fromid: long
    :type toid: long
    """
    def __init__(self, fromid, toid):
        self.fromid = fromid
        self.toid = toid

    def __eq__(self, other):
        if isinstance(other, Node):
            return ((self.fromNode == other.fromNode) and (self.toNode == other.toNode)) or \
                   ((self.fromNode == other.toNode) and (self.toNode == other.fromNode))
        else:
            return False

    def __hash__(self):
        return self.fromid * self.toid

class Link(QGraphicsLineItem):
    """
    :type fromNode: Node
    :type toNode: Node
    """
    def __init__(self, fromNode, toNode, connection_info):
        super(Link, self).__init__()
        self.fromNode = fromNode
        self.toNode = toNode
        self.fromNode.add_link(self)
        self.toNode.add_link(self)
        self.setZValue(-1)
        self.setPen(QPen(Qt.black, 2, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
        self.connection_info = connection_info

    def update_connection_info(self, connection_info):
        pass

    def __eq__(self, other):
        if isinstance(other, Link):
            return ((self.fromNode == other.fromNode) and (self.toNode == other.toNode)) or \
                   ((self.fromNode == other.toNode) and (self.toNode == other.fromNode))
        else:
            return False

    def set_color(self, color):
        """:type color: QColor"""
        self.setPen(QPen(color, 2, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))

    def color(self):
        """:rtype QColor"""
        return self.pen().color()

    def track_nodes(self):
        self.setLine(self, QLineF(self.fromNode.pos(), self.toNode.pos()))



