#coding=utf-8
import os
import sys
import string
import platform
import traceback 
from ctypes import *  
try :
	from qtsgproto_pb2 import *
except :
	print('warning>> python lib no support protocol buffer')
from qtsutility import *

dllfile=''
if sys.platform == 'win32' :
	dllfile = 'QtsProtoTradeApi.dll'
else:
	dllfile = 'libQtsProtoTradeApi.so'
	
#////////////////////////////////////////////////////////////////////
QtsTradeApi = cdll.LoadLibrary(dllfile)

#////////////////////////////////////////////////////////////////////
QTS_STRATEGY_CALLBACK = CFUNCTYPE(c_uint,c_uint,c_ushort,c_void_p,c_uint,c_uint)
QTS_FILTER_CALLBACK = CFUNCTYPE(c_uint,c_uint,c_uint,c_void_p,c_uint,c_void_p)

#////////////////////////////////////////////////////////////////////
def qts_GetMarket(icode) :
	market = c_ushort(0)
	try:
		QtsTradeApi.Trade_GetMarket.restype = c_ushort
		QtsTradeApi.Trade_GetMarket.argtype = [c_ulonglong]
		market = QtsTradeApi.Trade_GetMarket(c_ulonglong(icode))
	except Exception,e:
		traceback.print_exc()
	return market

def qts_GetCategory(icode) :
	category = c_ushort(0)
	try:
		QtsTradeApi.Trade_GetCategory.restype = c_ushort
		QtsTradeApi.Trade_GetCategory.argtype = [c_ulonglong]
		category = QtsTradeApi.Trade_GetCategory(c_ulonglong(icode))
	except Exception,e:
		traceback.print_exc()
	return category

def qts_GetSecuCode(icode) :
	secucode = c_uint(0)
	try:
		QtsTradeApi.Trade_GetSecuCode.restype = c_uint
		QtsTradeApi.Trade_GetSecuCode.argtype = [c_ulonglong]
		secucode = QtsTradeApi.Trade_GetSecuCode(c_ulonglong(icode))
	except Exception,e:
		traceback.print_exc()
	return secucode

def qts_CreateCode(market,category,icode) :
	innercode = c_ulonglong(0)
	try:
		QtsTradeApi.Trade_CreateCode.restype = c_ulonglong
		QtsTradeApi.Trade_CreateCode.argtype = [c_ushort,c_ushort,c_uint]
		innercode = QtsTradeApi.Trade_CreateCode(c_ushort(market),c_ushort(category),c_uint(icode))
	except Exception,e:
		traceback.print_exc()
	return innercode

def qts_SetManualTrade(parent,ismanual) :
	bresult = False
	try:		
		QtsTradeApi.Trade_SetCallback.argtype = [c_uint,c_bool]
		QtsTradeApi.Trade_SetManualTrade(c_uint(parent),c_bool(ismanual))
		bresult = True
	except Exception,e:
		traceback.print_exc()
	return bresult
	
def qts_SetCallback(parent,fun,para) :
	bresult = c_bool(0)
	try:
		QtsTradeApi.Trade_SetCallback.restype = c_bool
		QtsTradeApi.Trade_SetCallback.argtype = [c_uint,QTS_STRATEGY_CALLBACK,c_void_p]
		bresult = QtsTradeApi.Trade_SetCallback(c_uint(parent),fun,c_void_p(para))
	except Exception,e:
		traceback.print_exc()
	return bresult

def qts_StrategyId(parent) :
	id = c_ulonglong(0)
	try:
		QtsTradeApi.Trade_StrategyId.restype = c_ulonglong
		QtsTradeApi.Trade_StrategyId.argtype = [c_uint]
		id = QtsTradeApi.Trade_StrategyId(c_uint(parent))
	except Exception,e:
		traceback.print_exc()
	return id
	
def qts_AccountSize(parent) :
	size = c_uint(0)
	try:
		QtsTradeApi.Trade_AccountSize.restype = c_uint
		QtsTradeApi.Trade_AccountSize.argtype = [c_uint]
		size = QtsTradeApi.Trade_AccountSize(c_uint(parent))
	except Exception,e:
		traceback.print_exc()
	return size
	
def qts_Account(parent,index = 0) :
	accid = c_ulonglong(0)
	try:
		QtsTradeApi.Trade_Account.restype = c_ulonglong
		QtsTradeApi.Trade_Account.argtype = [c_uint,c_uint]
		accid = QtsTradeApi.Trade_Account(c_uint(parent),c_uint(index))
	except Exception,e:
		traceback.print_exc()
	return accid
	
def qts_Cycle(parent) :
	cycle = c_ulonglong(0)
	try:
		QtsTradeApi.Trade_Cycle.restype = c_ulonglong
		QtsTradeApi.Trade_Cycle.argtype = [c_uint]
		cycle = QtsTradeApi.Trade_Cycle(c_uint(parent))
	except Exception,e:
		traceback.print_exc()
	return cycle

def qts_TradeCycle(parent) :
	tradecycle = c_ulonglong(0)
	try:
		QtsTradeApi.Trade_TradeCycle.restype = c_ulonglong
		QtsTradeApi.Trade_TradeCycle.argtype = [c_uint]
		tradecycle = QtsTradeApi.Trade_TradeCycle(c_uint(parent))
	except Exception,e:
		traceback.print_exc()
	return tradecycle

def qts_Status(parent) :
	status = c_ushort(0)
	try:
		QtsTradeApi.Trade_Status.restype = c_ushort
		QtsTradeApi.Trade_Status.argtype = [c_uint]
		status = QtsTradeApi.Trade_Status(c_uint(parent))
	except Exception,e:
		traceback.print_exc()
	return status
	
def qts_NextData(parent) :
	try:
		QtsTradeApi.Trade_NextData.argtype = [c_uint]
		QtsTradeApi.Trade_NextData(c_uint(parent))
	except Exception,e:
		traceback.print_exc()
	
def qts_RegisterData(parent,market,category,icode,itype = 0,imode = QTS_GOROTO_REG_DATA_MODE_CODE) :
	bresult = c_bool(0)
	try:
		regdata = QtsGProtoRegisterData()		
		regdata.strategyid = parent
		regdata.type = itype
		regdata.code = CreateCode(market,category,icode)
		regdata.secuid = regdata.code
		regdata.mode = imode
		regdata.channel = 0
		unicode_str = SerializeToString(regdata)
		QtsTradeApi.Trade_RegisterData.restype = c_bool
		QtsTradeApi.Trade_RegisterData.argtype = [c_uint,c_void_p,c_uint]
		bresult = QtsTradeApi.Trade_RegisterData(c_uint(parent),c_char_p(unicode_str),c_uint(len(unicode_str)))
	except Exception,e:
		traceback.print_exc()
	return bresult

def qts_UnRegisterData(parent,market,category,icode,itype = 0,imode = QTS_GOROTO_REG_DATA_MODE_CODE) :
	bresult = c_bool(0)
	try:
		regdata = QtsGProtoRegisterData()		
		regdata.strategyid = parent
		regdata.type = itype
		regdata.code = CreateCode(market,category,icode)
		regdata.secuid = regdata.code	
		regdata.mode = imode
		unicode_str = SerializeToString(regdata)
		QtsTradeApi.Trade_UnRegisterData.restype = c_bool
		QtsTradeApi.Trade_UnRegisterData.argtype = [c_uint,c_char_p,c_uint]
		bresult = QtsTradeApi.Trade_UnRegisterData(c_uint(parent),c_char_p(unicode_str),c_uint(len(unicode_str)))
	except Exception,e:
		traceback.print_exc()
	return bresult

def qts_AddTradeCode(parent,itype,key,name,icode) :
	bresult = c_bool(0)
	try:
		parameter = QtsGProtoParameter()		
		parameter.strategyid = parent
		parameter.value = icode
		parameter.key = key
		parameter.name = name	
		unicode_str = SerializeToString(parameter)
		QtsTradeApi.Trade_AddTradeCode.restype = c_bool
		QtsTradeApi.Trade_AddTradeCode.argtype = [c_uint,c_char_p,c_uint]
		bresult = QtsTradeApi.Trade_AddTradeCode(c_uint(parent),c_uint(itype),c_char_p(unicode_str),c_uint(len(unicode_str)))
	except Exception,e:
		traceback.print_exc()
	return bresult

def qts_ExistTradeCode(parent,itype,icode) :
	bresult = c_bool(0)
	try:
		QtsTradeApi.Trade_ExistTradeCode.restype = c_bool
		QtsTradeApi.Trade_ExistTradeCode.argtype = [c_uint,c_uint,c_ulonglong]	
		breturn = QtsTradeApi.Trade_ExistTradeCode(c_uint(parent),c_uint(itype),c_ulonglong(icode))
	except Exception,e:
		traceback.print_exc()
	return bresult
	
def qts_GetParameterForInt64(parent,key) :
	bresult = c_bool(0)
	value = c_longlong(0)
	try:
		QtsTradeApi.Trade_GetParameterForInt64.restype = c_bool
		QtsTradeApi.Trade_GetParameterForInt64.argtype = [c_uint,c_uint,c_longlong]	
		breturn = QtsTradeApi.Trade_GetParameterForInt64(c_uint(parent),c_uint(key),byref(value))
	except Exception,e:
		traceback.print_exc()
	return (bresult,value.value)

def qts_SetParameterForInt64(parent,key,value) :
	bresult = c_bool(0)
	try:
		QtsTradeApi.Trade_SetParameterForInt64.restype = c_bool
		QtsTradeApi.Trade_SetParameterForInt64.argtype = [c_uint,c_uint,c_longlong]	
		bresult = QtsTradeApi.Trade_SetParameterForInt64(c_uint(parent),c_uint(key),c_longlong(value))
	except Exception,e:
		traceback.print_exc()
	return bresult

def qts_GetParameterForDouble(parent,key) :
	bresult = c_bool(0)
	value = c_double(0)
	try:
		QtsTradeApi.Trade_GetParameterForDouble.restype = c_double
		QtsTradeApi.Trade_GetParameterForDouble.argtype = [c_uint,c_uint,c_double]
		bresult = QtsTradeApi.Trade_GetParameterForDouble(c_uint(parent),c_uint(key),byref(value))
	except Exception,e:
		traceback.print_exc()
	return (bresult,value.value)

def qts_SetParameterForDouble(parent,key,value) :
	bresult = c_bool(0)
	try:
		QtsTradeApi.Trade_SetParameterForDouble.restype = c_bool
		QtsTradeApi.Trade_SetParameterForDouble.argtype = [c_uint,c_uint,c_double]
		bresult = QtsTradeApi.Trade_SetParameterForDouble(c_uint(parent),c_uint(key),c_double(value))
	except Exception,e:
		traceback.print_exc()
	return bresult

def GetParameterForStatus(parent,key) :
	bresult = c_bool(0)
	value = c_short(0)
	try:
		QtsTradeApi.Trade_GetParameterForDouble.restype = c_double
		QtsTradeApi.Trade_GetParameterForDouble.argtype = [c_uint,c_uint,c_short]
		bresult = QtsTradeApi.Trade_GetParameterForStatus(c_uint(parent),c_uint(key),byref(value))
	except Exception,e:
		traceback.print_exc()
	return (bresult,value.value)

def qts_SetParameterForStatus(parent,key,value) :
	bresult = c_bool(0)
	try:
		QtsTradeApi.Trade_SetParameterForDouble.restype = c_bool
		QtsTradeApi.Trade_SetParameterForDouble.argtype = [c_uint,c_uint,c_short]
		bresult = QtsTradeApi.Trade_SetParameterForStatus(c_uint(parent),c_uint(key),c_short(value))
	except Exception,e:
		traceback.print_exc()
	return bresult
	
def qts_GetParameters(parent,values) :
	bresult = False
	try:
		QtsTradeApi.Trade_GetParameters.restype = c_void_p
		QtsTradeApi.Trade_GetParameters.argtype = [c_uint,c_uint]
		size = c_uint()
		data = QtsTradeApi.Trade_GetParameters(c_uint(parent),byref(size))
		bresult = ParseFromPointer(data,size.value,values)
		qts_FreeData(parent)
	except Exception,e:
		traceback.print_exc()
	return bresult
	
def qts_GetConfig(parent,key,value) :
	bresult = False
	try:
		QtsTradeApi.Trade_GetConfig.restype = c_void_p
		QtsTradeApi.Trade_GetConfig.argtype = [c_uint,c_uint,c_uint]
		size = c_uint()
		data = QtsTradeApi.Trade_GetConfig(c_uint(parent),c_uint(key),byref(size))
		bresult = ParseFromPointer(data,size.value,value)
		qts_FreeData(parent)
	except Exception,e:
		traceback.print_exc()
	return bresult

def qts_GetCodes(parent,type,values) :
	bresult = False
	try:
		QtsTradeApi.Trade_GetCodes.restype = c_void_p
		QtsTradeApi.Trade_GetCodes.argtype = [c_uint,c_uint,c_uint]
		size = c_uint()
		data = QtsTradeApi.Trade_GetCodes(c_uint(parent),c_uint(type),byref(size))
		bresult = ParseFromPointer(data,size.value,values)
		qts_FreeData(parent)
	except Exception,e:
		traceback.print_exc()
	return bresult

def qts_Start(parent) :
	bresult = c_bool(0)
	try:
		QtsTradeApi.Trade_Start.restype = c_bool
		QtsTradeApi.Trade_Start.argtype = [c_uint]
		bresult = QtsTradeApi.Trade_Start(c_uint(parent))
	except Exception,e:
		traceback.print_exc()
	return bresult

def qts_Pause(parent) :
	bresult = c_bool(0)
	try:
		QtsTradeApi.Trade_Pause.restype = c_bool
		QtsTradeApi.Trade_Pause.argtype = [c_uint]
		bresult = QtsTradeApi.Trade_Pause(c_uint(parent))
	except Exception,e:
		traceback.print_exc()
	return bresult

def qts_Watch(parent) :
	bresult = c_bool(0)
	try:
		QtsTradeApi.Trade_Watch.restype = c_bool
		QtsTradeApi.Trade_Watch.argtype = [c_uint]
		bresult = QtsTradeApi.Trade_Watch(c_uint(parent))
	except Exception,e:
		traceback.print_exc()
	return bresult

def qts_Stop(parent) :
	bresult = c_bool(0)
	try:
		QtsTradeApi.Trade_Stop.restype = c_bool
		QtsTradeApi.Trade_Stop.argtype = [c_uint]
		bresult = QtsTradeApi.Trade_Stop(c_uint(parent))
	except Exception,e:
		traceback.print_exc()
	return bresult

def qts_GetDate(datetime) :
	date = c_ulonglong(0)
	try:
		QtsTradeApi.Trade_GetDate.restype = c_ulonglong
		QtsTradeApi.Trade_GetDate.argtype = [c_ulonglong]
		date = QtsTradeApi.Trade_GetDate(c_ulonglong(datetime))
	except Exception,e:
		traceback.print_exc()
	return date
	
def qts_GetTime(datetime) :
	time = c_ulonglong(0)
	try:
		QtsTradeApi.Trade_GetTime.restype = c_ulonglong
		QtsTradeApi.Trade_GetTime.argtype = [c_ulonglong]
		time = QtsTradeApi.Trade_GetTime(c_ulonglong(datetime))
	except Exception,e:
		traceback.print_exc()
	return time
	
def qts_TradingDate(market) :
	date = c_ulonglong(0)
	try:
		QtsTradeApi.Trade_TradingDate.restype = c_ulonglong
		QtsTradeApi.Trade_TradingDate.argtype = [c_uint]
		date = QtsTradeApi.Trade_TradingDate(market)
	except Exception,e:
		traceback.print_exc()
	return date
	
def qts_TradingTime(market) :
	time = c_ulonglong(0)
	try:
		QtsTradeApi.Trade_TradingTime.restype = c_ulonglong
		QtsTradeApi.Trade_TradingTime.argtype = [c_uint]
		time = QtsTradeApi.Trade_TradingTime(market)
	except Exception,e:
		traceback.print_exc()
	return time
	
def qts_GetSecond() :
	time = c_ulonglong(0)
	try:
		QtsTradeApi.Trade_GetSecond.restype = c_ulonglong
		time = QtsTradeApi.Trade_GetSecond()
	except Exception,e:
		traceback.print_exc()
	return time	
	
def qts_GetMilliSecond() :
	time = c_ulonglong(0)
	try:
		QtsTradeApi.Trade_GetMilliSecond.restype = c_ulonglong
		time = QtsTradeApi.Trade_GetMilliSecond()
	except Exception,e:
		traceback.print_exc()
	return time	

def qts_GetMicroSecond() :
	time = c_ulonglong(0)
	try:
		QtsTradeApi.Trade_GetMicroSecond.restype = c_ulonglong
		time = QtsTradeApi.Trade_GetMicroSecond()
	except Exception,e:
		traceback.print_exc()
	return time	
	
def qts_AckEvent(parent,type,data,size) :
	bresult = c_bool(0)
	try:
		QtsTradeApi.Trade_AckEvent.restype = c_bool
		QtsTradeApi.Trade_AckEvent.argtype = [c_uint,c_uint,c_char_p,c_uint]
		bresult = QtsTradeApi.Trade_AckEvent(c_uint(parent),c_uint(type),c_char_p(data),c_uint(size))
	except Exception,e:
		traceback.print_exc()
	return bresult
	
def qts_AckMonitor(parent,type,data,size) :
	bresult = c_bool(0)
	try:
		QtsTradeApi.Trade_AckMonitor.restype = c_bool
		QtsTradeApi.Trade_AckMonitor.argtype = [c_uint,c_uint,c_char_p,c_uint]
		bresult = QtsTradeApi.Trade_AckMonitor(c_uint(parent),c_uint(type),c_char_p(data),c_uint(size))
	except Exception,e:
		traceback.print_exc()
	return bresult
	
def qts_PrintLog(parent,itype,level,msg,net) :
	bresult = c_bool(0)
	try:
		gmsg = QtsGProtoLog()
		gmsg.key = ''
		gmsg.type = itype
		gmsg.level = level
		gmsg.msg = msg
		gmsg.net = net		
		print(gmsg)
		unicode_str = SerializeToString(gmsg)
		QtsTradeApi.Trade_PrintLog.restype = c_bool
		QtsTradeApi.Trade_PrintLog.argtype = [c_uint,c_char_p,c_uint]
		bresult = QtsTradeApi.Trade_PrintLog(c_uint(parent),c_char_p(unicode_str),c_uint(len(unicode_str)))
	except Exception,e:
		traceback.print_exc()
	return bresult

def qts_PrintMessageToLocal(parent,msg) :
	return PrintLog(parent,QTS_GPROTO_LOG_TYPE_MESSAGE,QTS_GPROTO_LOG_LEVEL_0,msg,False)

def qts_PrintDebugToLocal(parent,msg) :
	return PrintLog(parent,QTS_GPROTO_LOG_TYPE_DEBUG,QTS_GPROTO_LOG_LEVEL_0,msg,False)
	
def qts_PrintWarningToLocal(parent,msg) :
	return PrintLog(parent,QTS_GPROTO_LOG_TYPE_WARNING,QTS_GPROTO_LOG_LEVEL_0,msg,False)
	
def qts_PrintErrorToLocal(parent,msg) :
	return PrintLog(parent,QTS_GPROTO_LOG_TYPE_ERROR,QTS_GPROTO_LOG_LEVEL_0,msg,False)
	
def qts_PrintMessageToNet(parent,msg) :
	return PrintLog(parent,QTS_GPROTO_LOG_TYPE_MESSAGE,QTS_GPROTO_LOG_LEVEL_0,msg,True)

def qts_PrintDebugToNet(parent,msg) :
	return PrintLog(parent,QTS_GPROTO_LOG_TYPE_DEBUG,QTS_GPROTO_LOG_LEVEL_0,msg,True)
	
def qts_PrintWarningToNet(parent,msg) :
	return PrintLog(parent,QTS_GPROTO_LOG_TYPE_WARNING,QTS_GPROTO_LOG_LEVEL_0,msg,True)
	
def qts_PrintErrorToNet(parent,msg) :
	return PrintLog(parent,QTS_GPROTO_LOG_TYPE_ERROR,QTS_GPROTO_LOG_LEVEL_0,msg,True)
	
def qts_Order(parent,order) :
	bresult = c_ulonglong(0)
	try:
		unicode_str = SerializeToString(order)
		QtsTradeApi.Trade_Order.restype = c_ulonglong
		QtsTradeApi.Trade_Order.argtype = [c_uint,c_char_p,c_uint]
		bresult = QtsTradeApi.Trade_Order(c_uint(parent),c_char_p(unicode_str),c_uint(len(unicode_str)))
	except Exception,e:
		traceback.print_exc()
	return bresult

def qts_AlgoOrder(parent,order) :
	bresult = c_ulonglong(0)
	try:
		unicode_str = SerializeToString(order)
		QtsTradeApi.Trade_AlgoOrder.restype = c_ulonglong
		QtsTradeApi.Trade_AlgoOrder.argtype = [c_uint,c_char_p,c_uint]
		bresult = QtsTradeApi.Trade_AlgoOrder(c_uint(parent),c_char_p(unicode_str),c_uint(len(unicode_str)))
	except Exception,e:
		traceback.print_exc()
	return bresult
	
def qts_Cancel(parent,orderid,force=False) :
	bresult = c_longlong(0)
	try:
		gcancel = QtsGProtoCancel()
		gcancel.strategyid = parent
		gcancel.orderid = orderid
		unicode_str = SerializeToString(gcancel)
		QtsTradeApi.Trade_Cancel.restype = c_longlong
		QtsTradeApi.Trade_Cancel.argtype = [c_uint,c_char_p,c_uint,c_bool]
		bresult = QtsTradeApi.Trade_Cancel(c_uint(parent),c_char_p(unicode_str),c_uint(len(unicode_str)),c_bool(force))
	except Exception,e:
		traceback.print_exc()
	return bresult

def qts_Cancels(parent,force=False) :
	bresult = c_longlong(0)
	try:
		QtsTradeApi.Trade_Cancels.restype = c_longlong
		QtsTradeApi.Trade_Cancels.argtype = [c_uint,c_bool]
		bresult = QtsTradeApi.Trade_Cancels(c_uint(parent),c_bool(force))
	except Exception,e:
		traceback.print_exc()
	return bresult

def qts_AlgoCancel(parent,algoid,algoindex,force=False) :
	bresult = c_longlong(0)
	try:
		gcancel = QtsGProtoAlgoCancel()
		gcancel.algoid = algoid
		gcancel.algoindex = algoindex
		unicode_str = SerializeToString(gcancel)
		QtsTradeApi.Trade_AlgoCancel.restype = c_longlong
		QtsTradeApi.Trade_AlgoCancel.argtype = [c_uint,c_char_p,c_uint,c_bool]
		bresult = QtsTradeApi.Trade_AlgoCancel(c_uint(parent),c_char_p(unicode_str),c_uint(len(unicode_str)),c_bool(force))
	except Exception,e:
		traceback.print_exc()
	return bresult
	
def qts_AlgoCancels(parent,force=False) :
	bresult = c_longlong(0)
	try:
		QtsTradeApi.Trade_AlgoCancels.restype = c_longlong
		QtsTradeApi.Trade_AlgoCancels.argtype = [c_uint,c_bool]
		bresult = QtsTradeApi.Trade_AlgoCancels(c_uint(parent),c_bool(force))
	except Exception,e:
		traceback.print_exc()
	return bresult
	
def qts_AlgoSetCfg(parent,value) :
	bresult = c_bool(0)
	try:
		unicode_str = SerializeToString(value)
		QtsTradeApi.Trade_AlgoSetCfg.restype = c_bool
		QtsTradeApi.Trade_AlgoSetCfg.argtype = [c_uint,c_char_p,c_uint]
		bresult = QtsTradeApi.Trade_AlgoSetCfg(c_uint(parent),c_char_p(unicode_str),c_uint(len(unicode_str)))
	except Exception,e:
		traceback.print_exc()
	return bresult
	
def qts_AlgoGetCfg(parent,key,value) : 
	bresult = False
	try:
		unicode_str = SerializeToString(key)
		QtsTradeApi.Trade_AlgoGetCfg.restype = c_void_p
		QtsTradeApi.Trade_AlgoGetCfg.argtype = [c_uint,c_char_p,c_uint]
		size = c_uint(len(unicode_str))
		data = QtsTradeApi.Trade_AlgoGetCfg(c_uint(parent),c_char_p(unicode_str),size)
		bresult = ParseFromPointer(data,size.value,value)
		qts_FreeData(parent)		
	except Exception,e:
		traceback.print_exc()
	return bresult
	
def qts_AlgoQuery(parent,key,value) :
	bresult = False
	try:
		unicode_str = SerializeToString(key)
		QtsTradeApi.Trade_AlgoQuery.restype = c_void_p
		QtsTradeApi.Trade_AlgoQuery.argtype = [c_uint,c_char_p,c_uint]
		size = c_uint(len(unicode_str))
		data = QtsTradeApi.Trade_AlgoQuery(c_uint(parent),c_char_p(unicode_str),size)
		bresult = ParseFromPointer(data,size.value,value)
		qts_FreeData(parent)	
	except Exception,e:
		traceback.print_exc()
	return bresult
	
def qts_AlgoRegCallback(parent,key,fun,para) :
	bresult = c_bool(0)
	try:
		unicode_str = SerializeToString(key)
		QtsTradeApi.Trade_AlgoRegCallback.restype = c_bool
		QtsTradeApi.Trade_AlgoRegCallback.argtype = [c_uint,c_char_p,c_uint,QTS_FILTER_CALLBACK,c_void_p]
		bresult = QtsTradeApi.Trade_AlgoRegCallback(c_uint(parent),c_char_p(unicode_str),c_uint(len(unicode_str)),fun,c_void_p(para))
	except Exception,e:
		traceback.print_exc()
	return bresult
	
def qts_AlgoUnRegCallback(parent,key) :	
	bresult = c_bool(0)
	try:
		unicode_str = SerializeToString(key)
		QtsTradeApi.Trade_AlgoUnRegCallback.restype = c_bool
		QtsTradeApi.Trade_AlgoUnRegCallback.argtype = [c_uint,c_char_p,c_uint]
		bresult = QtsTradeApi.Trade_AlgoUnRegCallback(c_uint(parent),c_char_p(unicode_str),c_uint(len(unicode_str)))
	except Exception,e:
		traceback.print_exc()
	return bresult
	
def qts_GetSecuInfo(parent,icode,value) :
	bresult = False
	try:
		QtsTradeApi.Trade_GetSecuInfo.restype = c_void_p
		QtsTradeApi.Trade_GetSecuInfo.argtype = [c_uint,c_ulonglong,c_uint]
		size = c_uint()
		data = cast(QtsTradeApi.Trade_GetSecuInfo(c_uint(parent),c_ulonglong(icode),byref(size)),c_char_p)
		bresult = ParseFromPointer(data,size.value,value)
		qts_FreeData(parent)
	except Exception,e:
		traceback.print_exc()
	return bresult

def qts_GetSecuInfoBySecuCode(parent,market,category,secucode,value) :
	bresult = False
	try:
		QtsTradeApi.Trade_GetSecuInfo.restype = c_void_p
		QtsTradeApi.Trade_GetSecuInfo.argtype = [c_uint,c_ushort,c_ushort,c_uint,c_uint]
		size = c_uint()
		data = cast(QtsTradeApi.Trade_GetSecuInfo(c_uint(parent),c_ushort(market),c_ushort(category),c_uint(secucode),byref(size)),c_char_p)
		bresult = ParseFromPointer(data,size.value,value)
		qts_FreeData(parent)
	except Exception,e:
		traceback.print_exc()
	return bresult

def qts_GetSecuInfoByOrderCode(parent,market,category,ordercode,value) :
	bresult = False
	try:
		QtsTradeApi.Trade_GetSecuInfo.restype = c_void_p
		QtsTradeApi.Trade_GetSecuInfo.argtype = [c_uint,c_ushort,c_ushort,c_char_p,c_uint]
		size = c_uint()
		data = cast(QtsTradeApi.Trade_GetSecuInfo(c_uint(parent),c_ushort(market),c_ushort(category),c_char_p(ordercode),byref(size)),c_char_p)
		bresult = ParseFromPointer(data,size.value,value)
		qts_FreeData(parent)
	except Exception,e:
		traceback.print_exc()
	return bresult
	
def qts_GetStrategyInfo(parent,value) :
	bresult = False
	try:
		QtsTradeApi.Trade_GetStrategyInfo.restype = c_void_p
		QtsTradeApi.Trade_GetStrategyInfo.argtype = [c_uint,c_uint]
		size = c_uint()
		data = QtsTradeApi.Trade_GetStrategyInfo(c_uint(parent),byref(size))
		bresult = ParseFromPointer(data,size.value,value)
		qts_FreeData(parent)
	except Exception,e:
		traceback.print_exc()
	return bresult

def qts_GetAccount(parent,secuid,account,value) :
	bresult = False
	try:
		QtsTradeApi.Trade_GetAccount.restype = c_void_p
		QtsTradeApi.Trade_GetAccount.argtype = [c_uint,c_ulonglong,c_ulonglong,c_uint]
		size = c_uint()
		data = QtsTradeApi.Trade_GetAccount(c_uint(parent),c_ulonglong(secuid),c_ulonglong(account),byref(size))
		bresult = ParseFromPointer(data,size.value,value)
		qts_FreeData(parent)
	except Exception,e:
		traceback.print_exc()
	return bresult

def qts_GetPositions(parent,fun,para,value) :
	bresult = False
	try:
		QtsTradeApi.Trade_GetPositions.restype = c_void_p
		QtsTradeApi.Trade_GetPositions.argtype = [c_uint,QTS_FILTER_CALLBACK,c_void_p,c_uint]
		size = c_uint()
		data = QtsTradeApi.Trade_GetPositions(c_uint(parent),fun,c_void_p(para),byref(size))
		bresult = ParseFromPointer(data,size.value,value)
		qts_FreeData(parent)
	except Exception,e:
		traceback.print_exc()
	return bresult

def qts_GetRecords(parent,fun,para,value) :
	bresult = False
	try:
		QtsTradeApi.Trade_GetRecords.restype = c_void_p
		QtsTradeApi.Trade_GetRecords.argtype = [c_uint,QTS_FILTER_CALLBACK,c_void_p,c_uint]
		size = c_uint()
		data = QtsTradeApi.Trade_GetRecords(c_uint(parent),fun,c_void_p(para),byref(size))
		bresult = ParseFromPointer(data,size.value,value)
		qts_FreeData(parent)
	except Exception,e:
		traceback.print_exc()
	return bresult

def qts_GetWorkings(parent,fun,para,value) :
	bresult = False
	try:
		QtsTradeApi.Trade_GetWorkings.restype = c_void_p
		QtsTradeApi.Trade_GetWorkings.argtype = [c_uint,QTS_FILTER_CALLBACK,c_void_p,c_uint]
		size = c_uint()
		data = QtsTradeApi.Trade_GetWorkings(c_uint(parent),fun,c_void_p(para),byref(size))
		bresult = ParseFromPointer(data,size.value,value)
		qts_FreeData(parent)
	except Exception,e:
		traceback.print_exc()
	return bresult

def qts_GetPnls(parent,fun,para,value) :
	bresult = False
	try:
		QtsTradeApi.Trade_GetPnls.restype = c_void_p
		QtsTradeApi.Trade_GetPnls.argtype = [c_uint,QTS_FILTER_CALLBACK,c_void_p,c_uint]
		size = c_uint()
		data = QtsTradeApi.Trade_GetPnls(c_uint(parent),fun,c_void_p(para),byref(size))
		bresult = ParseFromPointer(data,size.value,value)
		qts_FreeData(parent)
	except Exception,e:
		traceback.print_exc()
	return bresult

def qts_GetBooks(parent,fun,para,value) :
	bresult = False
	try:
		QtsTradeApi.Trade_GetBooks.restype = c_void_p
		QtsTradeApi.Trade_GetBooks.argtype = [c_uint,QTS_FILTER_CALLBACK,c_void_p,c_uint]
		size = c_uint()
		data = QtsTradeApi.Trade_GetBooks(c_uint(parent),fun,c_void_p(para),byref(size))
		bresult = ParseFromPointer(data,size.value,value)
		qts_FreeData(parent)
	except Exception,e:
		traceback.print_exc()
	return bresult
	
def qts_QuerySecuInfoes(parent,cmd,value) :
	bresult = False
	try:
		QtsTradeApi.Trade_QuerySecuInfoes.restype = c_void_p
		QtsTradeApi.Trade_QuerySecuInfoes.argtype = [c_uint,c_char_p,c_uint]
		size = c_uint()
		data = QtsTradeApi.Trade_QuerySecuInfoes(c_uint(parent),c_char_p(cmd),byref(size))
		bresult = ParseFromPointer(data,size.value,value)
		qts_FreeData(parent)
	except Exception,e:
		traceback.print_exc()
	return bresult
	
def qts_QueryAccounts(parent,cmd,value) :
	bresult = False
	try:
		QtsTradeApi.Trade_QueryAccounts.restype = c_void_p
		QtsTradeApi.Trade_QueryAccounts.argtype = [c_uint,c_char_p,c_uint]
		size = c_uint()
		data = QtsTradeApi.Trade_QueryAccounts(c_uint(parent),c_char_p(cmd),byref(size))
		bresult = ParseFromPointer(data,size.value,value)
		qts_FreeData(parent)
	except Exception,e:
		traceback.print_exc()
	return bresult

def qts_QueryPositions(parent,cmd,value) :
	bresult = False
	try:
		QtsTradeApi.Trade_QueryPositions.restype = c_void_p
		QtsTradeApi.Trade_QueryPositions.argtype = [c_uint,c_char_p,c_uint]
		size = c_uint()
		data = QtsTradeApi.Trade_QueryPositions(c_uint(parent),c_char_p(cmd),byref(size))
		bresult = ParseFromPointer(data,size.value,value)
		qts_FreeData(parent)
	except Exception,e:
		traceback.print_exc()
	return bresult

def qts_QueryRecords(parent,cmd,value) :
	bresult = False
	try:
		QtsTradeApi.Trade_QueryRecords.restype = c_void_p
		QtsTradeApi.Trade_QueryRecords.argtype = [c_uint,c_char_p,c_uint]
		size = c_uint()
		data = QtsTradeApi.Trade_QueryRecords(c_uint(parent),c_char_p(cmd),byref(size))
		bresult = ParseFromPointer(data,size.value,value)
		qts_FreeData(parent)
	except Exception,e:
		traceback.print_exc()
	return bresult

def qts_QueryWorkings(parent,cmd,value) :
	bresult = False
	try:
		QtsTradeApi.Trade_QueryWorkings.restype = c_void_p
		QtsTradeApi.Trade_QueryWorkings.argtype = [c_uint,c_char_p,c_uint]
		size = c_uint()
		data = QtsTradeApi.Trade_QueryWorkings(c_uint(parent),c_char_p(cmd),byref(size))
		bresult = ParseFromPointer(data,size.value,value)
		qts_FreeData(parent)
	except Exception,e:
		traceback.print_exc()
	return bresult

def qts_QueryPnls(parent,cmd,value) :
	bresult = False
	try:
		QtsTradeApi.Trade_QueryPnls.restype = c_void_p
		QtsTradeApi.Trade_QueryPnls.argtype = [c_uint,c_char_p,c_uint]
		size = c_uint()
		data = QtsTradeApi.Trade_QueryPnls(c_uint(parent),c_char_p(cmd),byref(size))
		bresult = ParseFromPointer(data,size.value,value)
		qts_FreeData(parent)
	except Exception,e:
		traceback.print_exc()
	return bresult

def qts_QueryBooks(parent,cmd,value) :
	bresult = False
	try:
		QtsTradeApi.Trade_QueryBooks.restype = c_void_p
		QtsTradeApi.Trade_QueryBooks.argtype = [c_uint,c_char_p,c_uint]
		size = c_uint()
		data = QtsTradeApi.Trade_QueryBooks(c_uint(parent),c_char_p(cmd),byref(size))
		bresult = ParseFromPointer(data,size.value,value)
		qts_FreeData(parent)
	except Exception,e:
		traceback.print_exc()
	return bresult
	
def qts_GetPosition(parent,account,icode,itype,value) :
	bresult = False
	try:
		QtsTradeApi.Trade_GetPosition.restype = c_void_p
		QtsTradeApi.Trade_GetPosition.argtype = [c_uint,c_ulonglong,c_ulonglong,c_uint,c_uint]
		size = c_uint()		
		data = QtsTradeApi.Trade_GetPosition(c_uint(parent),c_ulonglong(account),c_ulonglong(icode),c_uint(itype),byref(size))
		bresult = ParseFromPointer(data,size.value,value)
		qts_FreeData(parent)
	except Exception,e:
		traceback.print_exc()
	return bresult	

def qts_GetRecord(parent,itype,orderid,value) :
	bresult = False
	try:
		QtsTradeApi.Trade_GetRecord.restype = c_void_p
		QtsTradeApi.Trade_GetRecord.argtype = [c_uint,c_uint,c_ulonglong,c_uint]
		size = c_uint()
		data = QtsTradeApi.Trade_GetRecord(c_uint(parent),c_uint(itype),c_ulonglong(orderid),byref(size))
		bresult = ParseFromPointer(data,size.value,value)
		qts_FreeData(parent)
	except Exception,e:
		traceback.print_exc()
	return bresult
	
def qts_GetWorking(parent,algoid,icode,action,value) :
	bresult = False
	try:
		QtsTradeApi.Trade_GetWorking.restype = c_void_p
		QtsTradeApi.Trade_GetWorking.argtype = [c_uint,c_ulonglong,c_ulonglong,c_uint,c_uint]
		size = c_uint()
		data = QtsTradeApi.Trade_GetWorking(c_uint(parent),c_ulonglong(algoid),c_ulonglong(icode),c_uint(action),byref(size))
		bresult = ParseFromPointer(data,size.value,value)
		qts_FreeData(parent)
	except Exception,e:
		traceback.print_exc()
	return bresult
	
def qts_GetPnl(parent,account,icode,value) :
	bresult = False
	try:
		QtsTradeApi.Trade_GetPnl.restype = c_void_p
		QtsTradeApi.Trade_GetPnl.argtype = [c_uint,c_ulonglong,c_ulonglong,c_uint]
		size = c_uint()
		data = QtsTradeApi.Trade_GetPnl(c_uint(parent),c_ulonglong(account),c_ulonglong(icode),byref(size))
		bresult = ParseFromPointer(data,size.value,value)
		qts_FreeData(parent)
	except Exception,e:
		traceback.print_exc()
	return bresult
	
def qts_GetBook(parent,algoid,icode,price,value) :
	bresult = False
	try:
		QtsTradeApi.Trade_GetBook.restype = c_void_p
		QtsTradeApi.Trade_GetBook.argtype = [c_uint,c_ulonglong,c_ulonglong,c_longlong,c_uint]
		size = c_uint()
		data = QtsTradeApi.Trade_GetBook(c_uint(parent),c_ulonglong(algoid),c_ulonglong(icode),c_longlong(price),byref(size))
		bresult = ParseFromPointer(data,size.value,value)
		qts_FreeData(parent)
	except Exception,e:
		traceback.print_exc()
	return bresult	
			
def qts_GetLastData(parent,icode,value) :
	bresult = False
	try:
		QtsTradeApi.Trade_GetLastData.restype = c_void_p
		QtsTradeApi.Trade_GetLastData.argtype = [c_uint,c_ulonglong,c_uint]
		size = c_uint()
		data = QtsTradeApi.Trade_GetLastData(c_uint(parent),c_ulonglong(icode),byref(size))
		bresult = ParseFromPointer(data,size.value,value)
		qts_FreeData(parent)
	except Exception,e:
		traceback.print_exc()
	return bresult	

def qts_GetCurrDatas(parent,icode,value) :
	bresult = False
	try:
		QtsTradeApi.Trade_GetCurrDatas.restype = c_void_p
		QtsTradeApi.Trade_GetCurrDatas.argtype = [c_uint,c_ulonglong,c_uint]
		size = c_uint()
		data = QtsTradeApi.Trade_GetCurrDatas(c_uint(parent),c_ulonglong(icode),byref(size))
		bresult = ParseFromPointer(data,size.value,value)
		qts_FreeData(parent)
	except Exception,e:
		traceback.print_exc()
	return bresult	
	
def qts_EnoughAccount(parent,secuid,account,amount) :
	bresult = c_bool(0)
	try:
		QtsTradeApi.Trade_EnoughAccount.restype = c_bool
		QtsTradeApi.Trade_EnoughAccount.argtype = [c_uint,c_ulonglong,c_ulonglong,c_longlong]
		bresult = QtsTradeApi.Trade_EnoughAccount(c_uint(parent),c_ulonglong(secuid),c_ulonglong(account),c_longlong(amount))
	except Exception,e:
		traceback.print_exc()
	return bresult
	
def qts_FreeData(parent) :
	try:
		QtsTradeApi.Trade_FreeData.argtype = [c_uint]
		QtsTradeApi.Trade_FreeData(c_uint(parent))
	except Exception,e:
		traceback.print_exc()
		
def qts_SetVariable(key,name,value) :
	bresult = c_bool(0)
	try:
		QtsTradeApi.Trade_EnoughAccount.restype = c_bool
		QtsTradeApi.Trade_EnoughAccount.argtype = [c_uint,c_char_p,c_void_p]
		bresult = QtsTradeApi.Trade_SetVariable(c_uint(key),c_char_p(name),c_void_p(value))
	except Exception,e:
		traceback.print_exc()
	return bresult	

def qts_GetVariable(key,name) :
	bresult = c_void_p(0)
	try:
		QtsTradeApi.Trade_EnoughAccount.restype = c_void_p
		QtsTradeApi.Trade_EnoughAccount.argtype = [c_uint,c_char_p]
		bresult = QtsTradeApi.Trade_GetVariable(c_uint(key),c_char_p(name))
	except Exception,e:
		traceback.print_exc()
	return bresult	

def qts_SetPushDataToGUI(bpush) :
	try:
		QtsTradeApi.Trade_SetPushDataToGUI.argtype = [c_bool]
		QtsTradeApi.Trade_SetPushDataToGUI(c_bool(bpush))
	except Exception,e:
		traceback.print_exc()
		
def qts_SetPushDataToGW(bpush) :
	try:
		QtsTradeApi.Trade_SetPushDataToGW.argtype = [c_bool]
		QtsTradeApi.Trade_SetPushDataToGW(c_bool(bpush))
	except Exception,e:
		traceback.print_exc()
		
def qts_GetPushDataToGUI() :
	bresult = c_bool(0)
	try:
		QtsTradeApi.Trade_GetPushDataToGUI.restype = c_bool
		bresult = QtsTradeApi.Trade_GetPushDataToGUI()
	except Exception,e:
		traceback.print_exc()
	return bresult
	
def qts_GetPushDataToGW() :
	bresult = c_bool(0)
	try:
		QtsTradeApi.Trade_GetPushDataToGW.restype = c_bool
		bresult = QtsTradeApi.Trade_GetPushDataToGW()
	except Exception,e:
		traceback.print_exc()
	return bresult
	
def qts_IsRecordToRemote(handle) :
	bresult = c_bool(0)
	try:
		QtsTradeApi.Trade_IsRecordToRemote.restype = c_bool
		QtsTradeApi.Trade_IsRecordToRemote.argtype = [c_uint]
		bresult = QtsTradeApi.Trade_IsRecordToRemote(c_uint(handle))
	except Exception,e:
		traceback.print_exc()
	return bresult
	
def qts_IsPositionToRemote(handle) :
	bresult = c_bool(0)
	try:
		QtsTradeApi.Trade_IsPositionToRemote.restype = c_bool
		QtsTradeApi.Trade_IsPositionToRemote.argtype = [c_uint]
		bresult = QtsTradeApi.Trade_IsPositionToRemote(c_uint(handle))
	except Exception,e:
		traceback.print_exc()
	return bresult
	
def qts_IsAccountToRemote(handle) :
	bresult = c_bool(0)
	try:
		QtsTradeApi.Trade_IsAccountToRemote.restype = c_bool
		QtsTradeApi.Trade_IsAccountToRemote.argtype = [c_uint]
		bresult = QtsTradeApi.Trade_IsAccountToRemote(c_uint(handle))
	except Exception,e:
		traceback.print_exc()
	return bresult
	
def qts_SetIsRecordToRemote(handle,bremote) :
	try:
		QtsTradeApi.Trade_SetIsRecordToRemote.argtype = [c_uint,c_bool]
		bresult = QtsTradeApi.Trade_SetIsRecordToRemote(c_uint(handle),c_bool(bremote))
	except Exception,e:
		traceback.print_exc()
	
def qts_SetIsPositionToRemote(handle,bremote) :
	try:
		QtsTradeApi.Trade_SetIsPositionToRemote.argtype = [c_uint,c_bool]
		bresult = QtsTradeApi.Trade_SetIsPositionToRemote(c_uint(handle),c_bool(bremote))
	except Exception,e:
		traceback.print_exc()
		
def qts_SetIsAccountToRemote(handle,bremote) :
	try:
		QtsTradeApi.Trade_SetIsAccountToRemote.argtype = [c_uint,c_bool]
		bresult = QtsTradeApi.Trade_SetIsAccountToRemote(c_uint(handle),c_bool(bremote))
	except Exception,e:
		traceback.print_exc()

def qts_IsTraceMessage() :
	bresult = c_bool(0)
	try:
		QtsTradeApi.Trade_IsTraceMessage.restype = c_bool
		bresult = QtsTradeApi.Trade_IsTraceMessage()
	except Exception,e:
		traceback.print_exc()
	return bresult
	
def qts_IsTraceDebug() :
	bresult = c_bool(0)
	try:
		QtsTradeApi.Trade_IsTraceDebug.restype = c_bool
		bresult = QtsTradeApi.Trade_IsTraceDebug()
	except Exception,e:
		traceback.print_exc()
	return bresult
	
def qts_IsTraceWarning() :
	bresult = c_bool(0)
	try:
		QtsTradeApi.Trade_IsTraceWarning.restype = c_bool
		bresult = QtsTradeApi.Trade_IsTraceWarning()
	except Exception,e:
		traceback.print_exc()
	return bresult
	
def qts_IsTraceError() :
	bresult = c_bool(0)
	try:
		QtsTradeApi.Trade_IsTraceError.restype = c_bool
		bresult = QtsTradeApi.Trade_IsTraceError()
	except Exception,e:
		traceback.print_exc()
	return bresult

def qts_IsLogMessage() :
	bresult = c_bool(0)
	try:
		QtsTradeApi.Trade_IsLogMessage.restype = c_bool
		bresult = QtsTradeApi.Trade_IsLogMessage()
	except Exception,e:
		traceback.print_exc()
	return bresult
	
def qts_IsLogDebug() :
	bresult = c_bool(0)
	try:
		QtsTradeApi.Trade_IsLogDebug.restype = c_bool
		bresult = QtsTradeApi.Trade_IsLogDebug()
	except Exception,e:
		traceback.print_exc()
	return bresult
	
def qts_IsLogWarning() :
	bresult = c_bool(0)
	try:
		QtsTradeApi.Trade_IsLogWarning.restype = c_bool
		bresult = QtsTradeApi.Trade_IsLogWarning()
	except Exception,e:
		traceback.print_exc()
	return bresult
	
def qts_IsLogError() :
	bresult = c_bool(0)
	try:
		QtsTradeApi.Trade_IsLogError.restype = c_bool
		bresult = QtsTradeApi.Trade_IsLogError()
	except Exception,e:
		traceback.print_exc()
	return bresult
