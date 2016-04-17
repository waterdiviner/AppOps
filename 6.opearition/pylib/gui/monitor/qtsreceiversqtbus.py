from PyQt5.QtCore import pyqtSignal, QObject

import sys
import os
sys.path.append(os.path.join(os.getenv('QTS_BASE_PATH','../..'),'pylib/utility'))
sys.path.append(os.path.join(os.getenv('QTS_BASE_PATH','../..'),'pylib/monitor'))
from qtssingleton import singleton
try :
	from qtsgproto_pb2 import *
except :
	print('warning>> python lib no support protocol buffer')
from qtsrmqinfo import *
from qtsreceiversmsgbus import *

@singleton
class QtsRMQReceiversPyQtBus(QObject):
    EOnPosition   = pyqtSignal(QtsRMQInfo,QtsGProtoPosition)
    EOnAccount    = pyqtSignal(QtsRMQInfo,QtsGProtoAccount)
    EOnRecord     = pyqtSignal(QtsRMQInfo,QtsGProtoRecord)
    EOnMessage    = pyqtSignal(QtsRMQInfo,QtsGProtoMessage)
    EOnStrategy   = pyqtSignal(QtsRMQInfo,QtsGProtoStrategyInfo)
    EOnControl    = pyqtSignal(QtsRMQInfo,QtsGProtoControl)
    EOnParamete   = pyqtSignal(QtsRMQInfo,QtsGProtoParameter)
    EOnData       = pyqtSignal(QtsRMQInfo,QtsGProtoData)
    EOnPnl        = pyqtSignal(QtsRMQInfo,QtsGProtoPnl)
    EOnWorking    = pyqtSignal(QtsRMQInfo,QtsGProtoWorking)
    EOnBook       = pyqtSignal(QtsRMQInfo,QtsGProtoBook)
    EOnEvent      = pyqtSignal(QtsRMQInfo,QtsGProtoUserData)
    EOnRemote     = pyqtSignal(QtsRMQInfo,QtsGProtoRemote)

    def __init__(self):
        QObject.__init__(self)
        qts_rmq_receivers_msg_bus = QtsReceiversMsgBus()
        qts_rmq_receivers_msg_bus.EOnPosition    += self.OnPosition
        qts_rmq_receivers_msg_bus.EOnAccount     += self.OnAccount
        qts_rmq_receivers_msg_bus.EOnRecord      += self.OnRecord
        qts_rmq_receivers_msg_bus.EOnMessage     += self.OnMessage
        qts_rmq_receivers_msg_bus.EOnStrategy    += self.OnStrategy
        qts_rmq_receivers_msg_bus.EOnControl     += self.OnControl
        qts_rmq_receivers_msg_bus.EOnParameter   += self.OnParameter
        qts_rmq_receivers_msg_bus.EOnData        += self.OnData
        qts_rmq_receivers_msg_bus.EOnPnl         += self.OnPnl
        qts_rmq_receivers_msg_bus.EOnWorking     += self.OnWorking
        qts_rmq_receivers_msg_bus.EOnBook        += self.OnBook
        qts_rmq_receivers_msg_bus.EOnEvent       += self.OnEvent
        qts_rmq_receivers_msg_bus.EOnRemote      += self.OnRemote

    def OnPosition(self, info, para):
        self.EOnPosition.emit(info,para)

    def OnAccount(self, info, para):
        self.EOnAccount.emit(info,para)

    def OnRecord(self, info, para):
        self.EOnRecord.emit(info,para)

    def OnMessage(self, info, para):
        self.EOnMessage.emit(info,para)

    def OnStrategy(self, info, para):
        self.EOnStrategy.emit(info,para)

    def OnControl(self, info, para):
        self.EOnControl.emit(info,para)

    def OnParameter(self, info, para):
        self.EOnParamete.emit(info,para)

    def OnData(self, info, para):
        self.EOnData.emit(info,para)

    def OnPnl(self, info, para):
        self.EOnPnl.emit(info,para)

    def OnWorking(self, info, para):
        self.EOnWorking.emit(info,para)

    def OnBook(self, info, para):
        self.EOnBook.emit(info,para)

    def OnEvent(self, info, para):
        self.EOnEvent.emit(info,para)

    def OnRemote(self, info, para):
        self.EOnRemote.emit(info,para)

