#coding=utf-8
import os
import sys
import string
import platform
import pika

################################################################################################
class QtsRMQInfo(object):
    def __init__(self, _exchange, _extype ,_queue, _routingkey, _url):
        self.m_url = _url
        self.m_exchange = _exchange
        self.m_extype = _extype
        self.m_queue = _queue
        self.m_routingkey = _routingkey

    def URL(self):
        return self.m_url;

    def Exchange(self):
        return self.m_exchange

    def ExType(self):
        return self.m_extype

    def Queue(self):
        return self.m_queue

    def RoutingKey(self):
        return self.m_routingkey

    def Compare(self,right):
        if (self.Exchange() == right.Exchange()) and (self.Queue() == right.Queue()) and (self.RoutingKey() == right.RoutingKey()) :
            return True
        else :
            return False

    def ToString(self):
        return 'url={0} \n exchange={1}\n type={2}\n queue={3}\n routing={4}'.format(self.m_url,self.m_exchange,self.m_extype,self.m_queue,self.m_routingkey)