import sys

from PyQt5.QtCore import (pyqtSignal, QLineF, QPointF, QRect, QRectF, QSize,
        QSizeF, Qt, QPoint)
from PyQt5.QtGui import (QBrush, QColor, QFont, QIcon, QIntValidator, QPainter,
        QPainterPath, QPen, QPixmap, QPolygonF)
from PyQt5.QtWidgets import (QAction, QApplication, QButtonGroup, QComboBox,
        QFontComboBox, QGraphicsItem, QGraphicsLineItem, QGraphicsPolygonItem,
        QGraphicsScene, QGraphicsTextItem, QGraphicsView, QGridLayout,
        QHBoxLayout, QLabel, QMainWindow, QMenu, QMessageBox, QSizePolicy,
        QToolBox, QToolButton, QWidget)
from PyQt5.QtCore import pyqtSlot
from qtslink import *
from qtsnode import *
from qtsreceiversqtbus import *

class QtsDeployView(QWidget):
    """
    :type scene: QGraphicsScene
    :type view: QGraphicsView
    :type seqNumber: int
    """
    def __init__(self):
        QWidget.__init__(self)
        self.scene = QGraphicsScene(0, 0, 600, 500)
        self.view = QGraphicsView()
        self.view.setScene(self.scene)
        self.view.setDragMode(QGraphicsView.RubberBandDrag)
        self.view.setRenderHints(QPainter.Antialiasing | QPainter.TextAntialiasing)
        self.view.setContextMenuPolicy(Qt.ActionsContextMenu)

        self.links = {}
        self.nodes = {}
        self.seqNumber = 0

        pyqtbus = QtsRMQReceiversPyQtBus()
        pyqtbus.EOnRemote.connect(self.on_remote, Qt.QueuedConnection)

    def on_remote(self, info, para):
        """
        :param para: QtsGProtoRemote
        """

        localid    = para.localid
        """:type localid: long"""

        localport  = para.localport
        """:type localport: long"""

        remoteid   = para.remoteid
        """:type remoteid: long"""

        remoteport = para.remoteport
        """:type remoteport: long"""

        appid      = para.appid
        """:type appid: long"""

        name       = para.name
        """:type name: string"""

        version    = para.version
        """:type version: string"""

        mode       = para.mode
        """:type version: EQtsGProtoPluginInMode"""

        status     = para.status
        """:type status: EQtsGProtoRemoteStatus"""

        group      = para.group
        """:type group: int"""

        if localid in self.nodes:
            self.nodes[localid].update_connection_info(para)
        else:
            local_node = Node(para)
            self.nodes[localid] = local_node
            self.setup_node(local_node)

        if remoteid in self.nodes:
            self.nodes[remoteid].update_connection_info(para)
        else:
            remote_node = Node(para)
            self.nodes[remoteid] = remote_node
            self.setup_node(remote_node)

        if (localid in self.nodes) and (remoteid in self.nodes):
            link_key = LinkKey(localid, remoteid)
            if link_key in self.links:
                self.links[link_key].update_connection_info(para)
            else:
                from_node = self.nodes[localid]
                to_node = self.nodes[remoteid]
                link = Link(from_node, to_node, para)
                self.scene.addItem(link)

    def setup_node(self, node):
        """
        :param node: Node
        :return:
        """
        node.setPos(QPoint(80 + (100 * (self.seqNumber % 5)),
                           80 + (50 * ((self.seqNumber / 5) % 7))))
        self.scene.addItem(node)





