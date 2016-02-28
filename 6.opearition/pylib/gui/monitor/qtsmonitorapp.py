#coding=utf-8
import os
import sys
import threading
import string
import platform
import pika

################################################################################################
class QtsMonitorApp(object) :
    def start(self):pass
    def stop(self):pass
    def Pages(self):
        return None

    def AddPage(self,name,page):
        return (name,page)