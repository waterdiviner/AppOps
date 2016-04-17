from qtsmonitorreceiver import *
from qtsreceiversmsgbus import *

import sys
import os
sys.path.append(os.path.join(os.getenv('QTS_BASE_PATH','..'),'pylib/utility'))
from qtssingleton import singleton

class QtsComponentReceiver(QtsRMQMonitorThread):
    def __init__(self, _exchange, _exchange_type, _queue, _routing_key, amqp_url):
        QtsRMQMonitorThread.__init__(self,_exchange, _exchange_type, _queue, _routing_key, amqp_url)
        qts_rmq_receivers_msg_bus = QtsReceiversMsgBus()
        self.EOnPosition     += qts_rmq_receivers_msg_bus.EOnPosition
        self.EOnAccount      += qts_rmq_receivers_msg_bus.EOnAccount
        self.EOnRecord       += qts_rmq_receivers_msg_bus.EOnRecord
        self.EOnMessage      += qts_rmq_receivers_msg_bus.EOnMessage
        self.EOnStrategy     += qts_rmq_receivers_msg_bus.EOnStrategy
        self.EOnControl      += qts_rmq_receivers_msg_bus.EOnControl
        self.EOnParameter    += qts_rmq_receivers_msg_bus.EOnParameter
        self.EOnData         += qts_rmq_receivers_msg_bus.EOnData
        self.EOnPnl          += qts_rmq_receivers_msg_bus.EOnPnl
        self.EOnWorking      += qts_rmq_receivers_msg_bus.EOnWorking
        self.EOnBook         += qts_rmq_receivers_msg_bus.EOnBook
        self.EOnEvent        += qts_rmq_receivers_msg_bus.EOnEvent
        self.EOnRemote       += qts_rmq_receivers_msg_bus.EOnRemote
		