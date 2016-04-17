#coding=utf-8
import os
import sys
import string
import platform
import pika
try :
	from qtsgproto_pb2 import *
except :
	print('warning>> python lib no support protocol buffer')
from qtsutility import *
from qtsrmqinfo import *

################################################################################################
class QtsRMQPublisher(object):
    def __init__(self, _exchange, _exchange_type ,_queue, _routing_key, amqp_url):
        self._connection = None
        self._channel = None
        self._closing = False
        self._consumer_tag = None
        self._conninfo = QtsRMQInfo(_exchange, _exchange_type ,_queue, _routing_key, amqp_url)

    def ConnInfo(self):
        return self._conninfo
		
    def connect(self):
        return pika.BlockingConnection(pika.URLParameters(self._conninfo.URL()))
		
    def close_connection(self):
        self._connection.close()
		
    def setup_exchange(self):
        self._channel.exchange_declare(exchange=self._conninfo.Exchange(), type=self.conninfo.ExType())

    def setup_queue(self):
        self._channel.queue_declare(queue=self._conninfo.Queue())
        self._channel.queue_bind(exchange=self._conninfo.Exchange(),
                                    queue=self._conninfo.Queue(),
                                    routing_key=self._conninfo.RoutingKey())

    def open_channel(self):
        self._channel = self._connection.channel()

    def run(self):
        self._connection = self.connect()
        self.open_channel()
        self.setup_exchange()
        self.setup_queue()

    def stop(self):
        self._closing = True
 
    def publish_message(self,stype,ssubtype,message,scontent_type='application/text'):
        if self._closing:
            return False
        properties = pika.BasicProperties(message_id=stype, content_type=scontent_type)
        self._channel.basic_publish(exchange=self._conninfo.Exchange(), routing_key=self._conninfo.RoutingKey(), body=message,properties=properties)
        return True