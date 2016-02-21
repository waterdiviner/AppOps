#coding=utf-8
import os
import sys
import string
import platform
import pika
import threading
from qtsgproto_pb2 import *
from qtsutility import *
from qtsrmqinfo import *
		
################################################################################################		
class QtsRMQReceiver(object):
    def __init__(self, _exchange, _exchange_type ,_queue, _routing_key, amqp_url):
        self._connection = None
        self._channel = None
        self._closing = False
        self._consumer_tag = None
        self._conninfo = QtsRMQInfo(_exchange, _exchange_type ,_queue, _routing_key, amqp_url)

    def ConnInfo(self):
        return self._conninfo
		
    def connect(self):
        return pika.SelectConnection(pika.URLParameters(self._conninfo.URL()),
                                     self.on_connection_open,
                                     stop_ioloop_on_close=False)

    def close_connection(self):
        self._connection.close()

    def add_on_connection_close_callback(self):
        self._connection.add_on_close_callback(self.on_connection_closed)

    def on_connection_closed(self, connection, reply_code, reply_text):
        self._channel = None
        if self._closing:
            self._connection.ioloop.stop()
        else:
            self._connection.add_timeout(5, self.reconnect)

    def on_connection_open(self, unused_connection):
        self.add_on_connection_close_callback()
        self.open_channel()

    def reconnect(self):
        self._connection.ioloop.stop()
        if not self._closing:
            self._connection = self.connect()
            self._connection.ioloop.start()

    def add_on_channel_close_callback(self):
        self._channel.add_on_close_callback(self.on_channel_closed)

    def on_channel_closed(self, channel, reply_code, reply_text):
        self._connection.close()

    def on_channel_open(self, channel):
        self._channel = channel
        self.add_on_channel_close_callback()
        self.setup_exchange(self._conninfo.Exchange())

    def setup_exchange(self, exchange_name):
        self._channel.exchange_declare(self.on_exchange_declareok, exchange_name, self._conninfo.ExType())

    def on_exchange_declareok(self, unused_frame):
        self.setup_queue(self._conninfo.Queue())

    def setup_queue(self, queue_name):
        self._channel.queue_declare(self.on_queue_declareok, queue_name)

    def on_queue_declareok(self, method_frame):
        self._channel.queue_bind(self.on_bindok, self._conninfo.Queue(),self._conninfo.Exchange(), self._conninfo.RoutingKey())

    def add_on_cancel_callback(self):
        self._channel.add_on_cancel_callback(self.on_consumer_cancelled)

    def on_consumer_cancelled(self, method_frame):
        if self._channel:
            self._channel.close()

    def acknowledge_message(self, delivery_tag):
         self._channel.basic_ack(delivery_tag)

    def on_message(self, unused_channel, basic_deliver, properties, body):
        self.acknowledge_message(basic_deliver.delivery_tag)

    def on_cancelok(self, unused_frame):
        self.close_channel()

    def stop_consuming(self):
        if self._channel:
            self._channel.basic_cancel(self.on_cancelok, self._consumer_tag)

    def start_consuming(self):
        self.add_on_cancel_callback()
        self._consumer_tag = self._channel.basic_consume(self.on_message, self._conninfo.Queue())

    def on_bindok(self, unused_frame):
        self.start_consuming()

    def close_channel(self):
        self._channel.close()

    def open_channel(self):
        self._connection.channel(on_open_callback=self.on_channel_open)

    def run(self):
        self._connection = self.connect()
        self._connection.ioloop.start()

    def stop(self):
        self._closing = True
        self.stop_consuming()
        self._connection.ioloop.stop()

###################################################################################################################
class QtsAsynRMQReceiver(threading.Thread, QtsRMQReceiver) :
    def __init__(self, _exchange, _exchange_type, _queue, _routing_key, amqp_url):
        QtsRMQReceiver.__init__(self,_exchange, _exchange_type, _queue, _routing_key, amqp_url)
        threading.Thread.__init__(self,target=self.run)

    def run(self):
        QtsRMQReceiver.run(self)

    def start(self):
        threading.Thread.start(self)

    def stop(self):
        QtsRMQReceiver.stop(self)
        threading.Thread.join(self)