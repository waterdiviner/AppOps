#coding=utf-8
import os
import sys
import string
import platform
import traceback
from ctypes import *

sys.path.append(os.path.join(os.getenv('QTS_BASE_PATH','..'),'pylib/utility'))
try :
    from qtsgproto_pb2 import *
except :
    print('warning>> python lib no support protocol buffer')
from qtsutility import *
from qtsfun import *

dllfile=''
if sys.platform == 'win32' :
    dllfile = 'QtsProtoGuiApi.dll'
else:
    dllfile = 'libQtsProtoGuiApi.so'

#////////////////////////////////////////////////////////////////////
QtsGuiApi = cdll.LoadLibrary(dllfile)
QTS_FILTER_CALLBACK = CFUNCTYPE(c_void_p,c_uint)

#////////////////////////////////////////////////////////////////////
def qts_CreateAppcation(args) :
    result = c_bool(0)
    try:
        QtsGuiApi.Gui_CreateApplication1.restype = c_bool
        QtsGuiApi.Gui_CreateApplication1.argtype = [c_char_p,c_uint]
        carg = c_char_p()
        carg.value = args
        result = QtsGuiApi.Gui_CreateApplication1(carg,c_uint(1))
    except Exception,e:
        traceback.print_exc()
    return result

def qts_DestroyApplication() :
    try:
        QtsGuiApi.Gui_DistroyApplication()
    except Exception,e:
        traceback.print_exc()

def qts_RegisterCommands() :
    result = c_bool(0)
    try:
        QtsGuiApi.Gui_RegisterCommands.restype = c_bool
        result = QtsGuiApi.Gui_RegisterCommands()
    except Exception,e:
        traceback.print_exc()
    return result

def qts_RequestDatas() :
    result = c_bool(0)
    try:
        QtsGuiApi.Gui_RequestDatas.restype = c_bool
        QtsGuiApi.Gui_RequestDatas.argtype = [c_bool]
        result = QtsGuiApi.Gui_RequestDatas(c_bool(True))
    except Exception,e:
        traceback.print_exc()
    return result

def qts_RegisterCallbacks() :
    result = c_bool(0)
    try:
        QtsGuiApi.Gui_RegisterCallbacks.restype = c_bool
        result =  QtsGuiApi.Gui_RegisterCallbacks()
    except Exception,e:
        traceback.print_exc()
    return result

def qts_NextData() :
    try:
        QtsGuiApi.Gui_NextData()
    except Exception,e:
        traceback.print_exc()

def qts_Start(strategyid) :
    result = c_bool(0)
    try:
        QtsGuiApi.Gui_Start.restype = c_bool
        result = QtsGuiApi.Gui_Start()
    except Exception,e:
        traceback.print_exc()
    return result

def qts_Pause(strategyid) :
    result = c_bool(0)
    try:
        QtsGuiApi.Gui_Pause.restype = c_bool
        result = QtsGuiApi.Gui_Pause()
    except Exception,e:
        traceback.print_exc()
    return result

def qts_Watch(strategyid) :
    result = c_bool(0)
    try:
        QtsGuiApi.Gui_Watch.restype = c_bool
        result = QtsGuiApi.Gui_Watch()
    except Exception,e:
        traceback.print_exc()
    return result

def qts_Stop(strategyid) :
    result = c_bool(0)
    try:
        QtsGuiApi.Gui_Stop.restype = c_bool
        result = QtsGuiApi.Gui_Stop()
    except Exception,e:
        traceback.print_exc()
    return result

def qts_SetParameter(parameter) :
    result = c_bool(0)
    try:
        QtsGuiApi.Gui_SetParameter.restype = c_bool
        QtsGuiApi.Gui_SetParameter.argtype = [c_void_p,c_uint]
        unicode_str = SerializeToString(parameter)
        result = QtsGuiApi.Gui_SetParameter(c_char_p(unicode_str),c_uint(len(unicode_str)))
    except Exception,e:
        traceback.print_exc()
    return result

def qts_FreeData() :
    try:
        QtsGuiApi.Gui_FreeData()
    except Exception,e:
        traceback.print_exc()

def qts_GetSecuInfo(icode,value) :
    bresult = False
    try:
        QtsGuiApi.Gui_GetSecuInfo.restype = c_void_p
        QtsGuiApi.Gui_GetSecuInfo.argtype = [c_ulonglong,c_uint]
        size = c_uint()
        data = cast(QtsGuiApi.Gui_GetSecuInfo(c_ulonglong(icode),byref(size)),c_char_p)
        bresult = ParseFromPointer(data,size.value,value)
        qts_FreeData()
    except Exception,e:
        traceback.print_exc()
    return bresult

def qts_GetStrategyInfo(strategyid,value) :
    bresult = False
    try:
        QtsGuiApi.Gui_GetStrategyInfo.restype = c_void_p
        QtsGuiApi.Gui_GetStrategyInfo.argtype = [c_uint,c_uint]
        size = c_uint()
        data = QtsGuiApi.Gui_GetStrategyInfo(c_uint(strategyid),byref(size))
        bresult = ParseFromPointer(data,size.value,value)
        qts_FreeData()
    except Exception,e:
        traceback.print_exc()
    return bresult

def qts_QuerySecuInfoes(cmd,value) :
    bresult = False
    try:
        QtsGuiApi.Gui_QuerySecuInfoes.restype = c_void_p
        QtsGuiApi.Gui_QuerySecuInfoes.argtype = [c_char_p,c_uint]
        size = c_uint()
        data = QtsGuiApi.Gui_QuerySecuInfoes(c_char_p(cmd),byref(size))
        bresult = ParseFromPointer(data,size.value,value)
        qts_FreeData()
    except Exception,e:
        traceback.print_exc()
    return bresult

def qts_QueryAccounts(cmd,value) :
    bresult = False
    try:
        QtsGuiApi.Gui_QueryAccounts.restype = c_void_p
        QtsGuiApi.Gui_QueryAccounts.argtype = [c_uint,c_char_p,c_uint]
        size = c_uint()
        data = QtsGuiApi.Gui_QueryAccounts(c_char_p(cmd),byref(size))
        bresult = ParseFromPointer(data,size.value,value)
        qts_FreeData()
    except Exception,e:
        traceback.print_exc()
    return bresult

def qts_QueryPositions(cmd,value) :
    bresult = False
    try:
        QtsGuiApi.Gui_QueryPositions.restype = c_void_p
        QtsGuiApi.Gui_QueryPositions.argtype = [c_uint,c_char_p,c_uint]
        size = c_uint()
        data = QtsGuiApi.Gui_QueryPositions(c_char_p(cmd),byref(size))
        bresult = ParseFromPointer(data,size.value,value)
        qts_FreeData()
    except Exception,e:
        traceback.print_exc()
    return bresult

def qts_QueryRecords(cmd,value) :
    bresult = False
    try:
        QtsGuiApi.Gui_QueryRecords.restype = c_void_p
        QtsGuiApi.Gui_QueryRecords.argtype = [c_uint,c_char_p,c_uint]
        size = c_uint()
        data = QtsGuiApi.Gui_QueryRecords(c_char_p(cmd),byref(size))
        bresult = ParseFromPointer(data,size.value,value)
        qts_FreeData()
    except Exception,e:
        traceback.print_exc()
    return bresult

def qts_QueryWorkings(cmd,value) :
    bresult = False
    try:
        QtsGuiApi.Gui_QueryWorkings.restype = c_void_p
        QtsGuiApi.Gui_QueryWorkings.argtype = [c_uint,c_char_p,c_uint]
        size = c_uint()
        data = QtsGuiApi.Gui_QueryWorkings(c_char_p(cmd),byref(size))
        bresult = ParseFromPointer(data,size.value,value)
        qts_FreeData()
    except Exception,e:
        traceback.print_exc()
    return bresult

def qts_QueryPnls(cmd,value) :
    bresult = False
    try:
        QtsGuiApi.Gui_QueryPnls.restype = c_void_p
        QtsGuiApi.Gui_QueryPnls.argtype = [c_uint,c_char_p,c_uint]
        size = c_uint()
        data = QtsGuiApi.Gui_QueryPnls(c_char_p(cmd),byref(size))
        bresult = ParseFromPointer(data,size.value,value)
        qts_FreeData()
    except Exception,e:
        traceback.print_exc()
    return bresult

def qts_QueryBooks(cmd,value) :
    bresult = False
    try:
        QtsGuiApi.Gui_QueryBooks.restype = c_void_p
        QtsGuiApi.Gui_QueryBooks.argtype = [c_uint,c_char_p,c_uint]
        size = c_uint()
        data = QtsGuiApi.Gui_QueryBooks(c_char_p(cmd),byref(size))
        bresult = ParseFromPointer(data,size.value,value)
        qts_FreeData()
    except Exception,e:
        traceback.print_exc()
    return bresult

def qts_GetPosition(account,icode,itype,value) :
    bresult = False
    try:
        QtsGuiApi.Gui_GetPosition.restype = c_void_p
        QtsGuiApi.Gui_GetPosition.argtype = [c_uint,c_ulonglong,c_ulonglong,c_uint,c_uint]
        size = c_uint()
        data = QtsGuiApi.Gui_GetPosition(c_ulonglong(account),c_ulonglong(icode),c_uint(itype),byref(size))
        bresult = ParseFromPointer(data,size.value,value)
        qts_FreeData()
    except Exception,e:
        traceback.print_exc()
    return bresult

def qts_GetRecord(itype,orderid,value) :
    bresult = False
    try:
        QtsGuiApi.Gui_GetRecord.restype = c_void_p
        QtsGuiApi.Gui_GetRecord.argtype = [c_uint,c_uint,c_ulonglong,c_uint]
        size = c_uint()
        data = QtsGuiApi.Gui_GetRecord(c_uint(itype),c_ulonglong(orderid),byref(size))
        bresult = ParseFromPointer(data,size.value,value)
        qts_FreeData()
    except Exception,e:
        traceback.print_exc()
    return bresult

def qts_GetWorking(strategyid,icode,action,value) :
    bresult = False
    try:
        QtsGuiApi.Gui_GetWorking.restype = c_void_p
        QtsGuiApi.Gui_GetWorking.argtype = [c_uint,c_ulonglong,c_ulonglong,c_uint,c_uint]
        size = c_uint()
        data = QtsGuiApi.Gui_GetWorking(c_uint(strategyid),c_ulonglong(icode),c_uint(action),byref(size))
        bresult = ParseFromPointer(data,size.value,value)
        qts_FreeData()
    except Exception,e:
        traceback.print_exc()
    return bresult

def qts_GetPnl(account,icode,value) :
    bresult = False
    try:
        QtsGuiApi.Gui_GetPnl.restype = c_void_p
        QtsGuiApi.Gui_GetPnl.argtype = [c_uint,c_ulonglong,c_ulonglong,c_uint]
        size = c_uint()
        data = QtsGuiApi.Gui_GetPnl(c_ulonglong(account),c_ulonglong(icode),byref(size))
        bresult = ParseFromPointer(data,size.value,value)
        qts_FreeData()
    except Exception,e:
        traceback.print_exc()
    return bresult

def qts_GetBook(strategyid,icode,price,value) :
    bresult = False
    try:
        QtsGuiApi.Gui_GetBook.restype = c_void_p
        QtsGuiApi.Gui_GetBook.argtype = [c_uint,c_ulonglong,c_ulonglong,c_longlong,c_uint]
        size = c_uint()
        data = QtsGuiApi.Gui_GetBook(c_uint(strategyid),c_ulonglong(icode),c_longlong(price),byref(size))
        bresult = ParseFromPointer(data,size.value,value)
        qts_FreeData()
    except Exception,e:
        traceback.print_exc()
    return bresult
