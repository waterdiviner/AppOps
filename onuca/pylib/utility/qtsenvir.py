#coding=utf-8
#define public var
import sys
import os
import string
try :
	import time
except :
	print('no support time')
try :
	import datetime
except :
	print('no support datetime')
import platform
from qtsvar import *
from qtssecurity import *


(SYS_LINUX,SYS_WINDOWS)=('Linux','Windows')

def TraceDebug(msg) :
	print("debug>>{0}".format(msg))

def TraceMessage(msg) :
	print("message>>{0}".format(msg))

def TraceWarning(msg) :
	print("warning>>{0}".format(msg))

def TraceError(msg) :
	print("error>>{0}".format(msg))