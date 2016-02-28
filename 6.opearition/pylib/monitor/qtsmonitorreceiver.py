#coding=utf-8
import os
import sys
import threading
import string
import platform
import pika
import time

sys.path.append('../utility')
sys.path.append('../net/rabbitmq')
from qtsdelegate import delegate
from qtsgproto_pb2 import *
from qtsutility import *
from qtsbiz import *
from qtsrmqreceiver import *

################################################################################################
class QtsMonitorReceiver(QtsRMQReceiver):
    def __init__(self, _exchange, _exchange_type, _queue, _routing_key, amqp_url):
        QtsRMQReceiver.__init__(self,_exchange, _exchange_type, _queue, _routing_key, amqp_url)
        self.EOnPosition    = delegate (proto='OnPosition()')
        self.EOnAccount     = delegate (proto='OnAccount()')
        self.EOnRecord      = delegate (proto='OnRecord()')
        self.EOnMessage     = delegate (proto='OnMessage()')
        self.EOnStrategy    = delegate (proto='OnStrategy()')
        self.EOnControl     = delegate (proto='OnControl()')
        self.EOnParameter   = delegate (proto='OnParameter()')
        self.EOnData        = delegate (proto='OnData()')
        self.EOnPnl         = delegate (proto='OnPnl()')
        self.EOnWorking     = delegate (proto='OnWorking()')
        self.EOnBook        = delegate (proto='OnBook()')
        self.EOnEvent       = delegate (proto='OnEvent()')
        self.EOnRemote      = delegate (proto='OnRemote()')
		
    def on_message(self, unused_channel, basic_deliver, properties, body):
        if properties.message_id is not None:
            itype = string.atoi(properties.message_id)
            size = len(body)
            if itype == QTS_GPROTO_EVENT_TYPE_DATA :
                market = QtsGProtoData()
                if ParseFromPointer(body,size,market) :
                    self.EOnData(self.ConnInfo(),market)
            elif itype == QTS_GPROTO_EVENT_TYPE_ERROR :
                errinfo = QtsGProtoMessage()
                if ParseFromPointer(body,size,errinfo) :
                    self.EOnMessage(self.ConnInfo(),errinfo)
            elif itype == QTS_GPROTO_EVENT_TYPE_ACCOUNT :
                account = QtsGProtoAccount()
                if ParseFromPointer(body,size,account) :
                    self.EOnAccount(self.ConnInfo(),account)
            elif itype == QTS_GPROTO_EVENT_TYPE_POSITION :
                position = QtsGProtoPosition()
                if ParseFromPointer(body,size,position) :
                    self.EOnPosition(self.ConnInfo(),position)
            elif itype == QTS_GPROTO_EVENT_TYPE_RECORD :
                record = QtsGProtoRecord()
                if ParseFromPointer(body,size,record) :
                    self.EOnRecord(self.ConnInfo(),record)
            elif itype == QTS_GPROTO_EVENT_TYPE_STRATEGYINFO :
                strategyinfo = QtsGProtoStrategyInfo()
                if ParseFromPointer(body,size,strategyinfo) :
                    self.EOnStrategy(self.ConnInfo(),strategyinfo)
            elif itype == QTS_GPROTO_EVENT_TYPE_PARAMETER :
                parameter = QtsGProtoParameter()
                if ParseFromPointer(body,size,parameter) :
                    self.EOnParameter(self.ConnInfo(),parameter)
            elif itype == QTS_GPROTO_EVENT_TYPE_CONTROL :
                control = QtsGProtoControl()
                if ParseFromPointer(body,size,control) :
                    self.EOnControl(self.ConnInfo(),control)
            elif itype == QTS_GPROTO_EVENT_TYPE_WORKING :
                working = QtsGProtoWorking()
                if ParseFromPointer(body,size,working) :
                    self.EOnWorking(self.ConnInfo(),working)
            elif itype == QTS_GPROTO_EVENT_TYPE_BOOK :
                book = QtsGProtoBook()
                if ParseFromPointer(body,size,book) :
                    self.EOnBook(self.ConnInfo(),book)
            elif itype == QTS_GPROTO_EVENT_TYPE_PNL :
                pnl = QtsGProtoPnl()
                if ParseFromPointer(body,size,pnl) :
                    self.EOnPnl(self.ConnInfo(),pnl)
            elif itype == QTS_GPROTO_EVENT_TYPE_MESSAGE :
                msg = QtsGProtoMessage()
                if ParseFromPointer(body,size,msg) :
                    self.EOnMessage(self.ConnInfo(),msg)
            elif itype == QTS_GPROTO_EVENT_TYPE_REMOTE :
                remote = QtsGProtoRemote()
                if ParseFromPointer(body,size,remote) :
                    self.EOnRemote(self.ConnInfo(),remote)
            elif itype == QTS_GPROTO_EVENT_TYPE_EVENT :
                usrdata = QtsGProtoUserData()
                if ParseFromPointer(body,size,usrdata) :
                    self.EOnEvent(self.ConnInfo(),properties.user_id,usrdata)
        QtsRMQReceiver.on_message(self, unused_channel, basic_deliver, properties, body)
        time.sleep(0.01)

 ##############################################################
class QtsRMQMonitorThread(threading.Thread, QtsMonitorReceiver) :
    def __init__(self, _exchange, _exchange_type, _queue, _routing_key, amqp_url):       
		QtsMonitorReceiver.__init__(self,_exchange, _exchange_type, _queue, _routing_key, amqp_url)
		threading.Thread.__init__(self,target=self.run)		
		
    def run(self):
        QtsMonitorReceiver.run(self)
		
	def start(self):
		threading.Thread.start(self)
		
	def stop(self):
		QtsMonitorReceiver.stop(self)
		threading.Thread.join(self)
