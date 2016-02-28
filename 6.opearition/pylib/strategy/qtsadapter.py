#coding=utf-8
import os
import sys
import string
import platform
import traceback
from ctypes import *

adapterfile=''
if sys.platform == 'win32' :
	adapterfile = 'QtsAdapter.dll'
else:
	adapterfile = 'libQtsAdapter.so'
	
#////////////////////////////////////////////////////////////////////
QtsAdapter = cdll.LoadLibrary(adapterfile)

#////////////////////////////////////////////////////////////////////
#param 1 is return value,this is must be
#param 2 type
#param 3 subtype
#param 4 pro
#param 5 data
#param 6 size
#param 7 para
QTS_ADAPTER_EVENT_CALLBACK = CFUNCTYPE(c_uint,c_uint,c_uint,c_ushort,c_void_p,c_uint,c_uint)

#param 1 is return value,this is must be
#param 2 type
#param 3 data
#param 4 size
QTS_ADAPTER_CONFIG_CALLBACK = CFUNCTYPE(c_uint,c_uint,c_void_p,POINTER(c_uint))

def RegisterEvent(eventid,fun) :
	try:
		QtsAdapter.Adapter_RegisterEvent.restype = c_bool
		QtsAdapter.Adapter_RegisterEvent.argtype = [c_uint,QTS_ADAPTER_EVENT_CALLBACK]
		result = QtsAdapter.Adapter_RegisterEvent(c_uint(eventid),fun)
	except Exception,e:
		traceback.print_exc()
	return result
	
def UnRegisterEvent(eventid) :
	try:
		QtsAdapter.Adapter_UnRegisterEvent.restype = c_bool
		QtsAdapter.Adapter_UnRegisterEvent.argtype = [c_uint]
		result = QtsAdapter.Adapter_UnRegisterEvent(c_uint(eventid))
	except Exception,e:
		traceback.print_exc()
	return result

def RegisterConfig(eventid,fun) :
	try:
		QtsAdapter.Adapter_RegisterConfig.restype = c_bool
		QtsAdapter.Adapter_RegisterConfig.argtype = [c_uint,QTS_ADAPTER_CONFIG_CALLBACK]
		result = QtsAdapter.Adapter_RegisterConfig(c_uint(eventid),fun)
	except Exception,e:
		traceback.print_exc()
	return result
	
def UnRegisterConfig(eventid) :
	try:
		QtsAdapter.Adapter_UnRegisterConfig.restype = c_bool
		QtsAdapter.Adapter_UnRegisterConfig.argtype = [c_uint]
		result = QtsAdapter.Adapter_UnRegisterConfig(c_uint(eventid))
	except Exception,e:
		traceback.print_exc()
	return result
