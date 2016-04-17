#coding=utf-8
import os
import sys
import string
import platform
import traceback 
from ctypes import *

sys.path.append(os.path.join(os.getenv('QTS_BASE_PATH','../..'),'pylib/utility'))
try :
	from qtsgproto_pb2 import *
except :
	print('warning>> python lib no support protocol buffer')
from qtsfun import *
from qtsutility import *
from qtsadapter import *

#////////////////////////////////////////////////////////////////////
def PrintVariable(var) :
	if var.type == QTS_GPROTO_VARIABLE_TYPE_LIST :
		for subvar in var.value_list :
			PrintVariable(subvar)
	elif var.type == QTS_GPROTO_VARIABLE_TYPE_INT32 :
		print(var.value_int32)
	elif var.type == QTS_GPROTO_VARIABLE_TYPE_INT64 :		
		print(var.value_int64)
	elif var.type == QTS_GPROTO_VARIABLE_TYPE_FLOAT :
		print(var.value_float)	
	elif var.type == QTS_GPROTO_VARIABLE_TYPE_BOOL :
		print(var.value_bool)
	elif var.type == QTS_GPROTO_VARIABLE_TYPE_STRING :
		print(var.value_string)
		
def PrintVariables(vars,msg) :
	print("*********************** entry " + msg + "*************************")
	for var in vars.items :
		PrintVariable(var)
	print("*********************** exit " + msg + "*************************")
	
def ParserVariables(data,size) :
	vars = QtsGProtoVariables()	
	vars.ParseFromString(data)
	PrintVariables(vars,'ParserVariables')

def ReadAnyValue(qtsvalue,var) :
	breturn = True
	if isinstance(qtsvalue,list) :
		var.type = QTS_GPROTO_VARIABLE_TYPE_LIST
		for qtsitem in qtsvalue :
			subvar = var.value_list.add()
			ReadAnyValue(qtsitem,subvar)
	elif isinstance(qtsvalue,int) :			
		var.type = QTS_GPROTO_VARIABLE_TYPE_INT32
		var.value_int32 = qtsvalue
	elif isinstance(qtsvalue,long) :			
		var.type = QTS_GPROTO_VARIABLE_TYPE_INT64
		var.value_int64 = qtsvalue
	elif isinstance(qtsvalue,float) :
		var.type = QTS_GPROTO_VARIABLE_TYPE_FLOAT
		var.value_float = qtsvalue	
	elif isinstance(qtsvalue,bool) :
		var.type = QTS_GPROTO_VARIABLE_TYPE_BOOL
		var.value_bool = qtsvalue
	elif isinstance(qtsvalue,str) :
		var.type = QTS_GPROTO_VARIABLE_TYPE_STRING
		var.value_string = unicode(qtsvalue,'utf8')
	else :
		print('ReadAnyValue: error data type;',qtsvalue)
		breturn = False
	return breturn

def ReadAllKey(qtsdict) :	
	vars = QtsGProtoVariables()
	qtskeys = qtsdict.keys()
	for qtskey in qtskeys :
		var = vars.items.add()
		var.type = QTS_GPROTO_VARIABLE_TYPE_STRING
		var.value_string = qtskey
	return SerializeToString(vars)
	
def ReadKey(cfgfile,cfgdict) :
	qtsdict = GetDictFromRootByPath(cfgfile + '/' + cfgdict)
	if qtsdict == None :
		return None
	return ReadAllKey(qtsdict)
	
def ReadAnyByKey(cfgfile,cfgdict,cfgkey) : 
	qtsdict = GetDictFromRootByPath(cfgfile + '/' + cfgdict)
	if qtsdict == None :
		return None	
	qtskey = GetAttr(qtsdict,cfgkey)
	if qtskey == None :
		return None	
	vars = QtsGProtoVariables()
	var = vars.items.add()
	if ReadAnyValue(qtskey,var) :
		return SerializeToString(vars)
	else :
		return None

def ReadAnyByDict(cfgfile,cfgdict) : 
	qtsdict = GetDictFromRootByPath(cfgfile + '/' + cfgdict)
	if qtsdict == None :
		return None		
	vars = QtsGProtoVariables()
	var = vars.items.add()	
	if ReadAnyValue(qtsdict,var) :
		return SerializeToString(vars)
	else :
		return None

def OnReadCfg(itype,data,size) :
	qtscfg_data = None
	vars = QtsGProtoVariables()	
	if ParseFromPointer(data,size[0],vars) :
		if itype == QTS_GPROTO_EVENT_TYPE_READKEY :
			qtscfg_data = ReadKey(vars.items[0].value_string,vars.items[1].value_string)
		elif itype == QTS_GPROTO_EVENT_TYPE_READANY_BYKEY :
			qtscfg_data = ReadAnyByKey(vars.items[0].value_string,vars.items[1].value_string,vars.items[2].value_string)	
		elif itype == QTS_GPROTO_EVENT_TYPE_READANY_BYDICT :
			qtscfg_data = ReadAnyByDict(vars.items[0].value_string,vars.items[1].value_string)
	if qtscfg_data == None :
		return QTS_FALSE
	else :
		memset(data,0,size[0])
		size[0]=len(qtscfg_data)
		if size[0] < (1024 * 1024) :
			memmove(data,c_char_p(qtscfg_data),size[0])
		else :
			raise StandardError('cfg buff size is large,real size={0},set size=1024 * 1024'.format(size[0]))
		return QTS_TRUE

QtsAdapter_OnReadCfg=QTS_ADAPTER_CONFIG_CALLBACK(OnReadCfg)
def RegisterCfgEvent() :
	RegisterConfig(QTS_GPROTO_EVENT_TYPE_READKEY,QtsAdapter_OnReadCfg)
	RegisterConfig(QTS_GPROTO_EVENT_TYPE_READANY_BYKEY,QtsAdapter_OnReadCfg)
	RegisterConfig(QTS_GPROTO_EVENT_TYPE_READANY_BYDICT,QtsAdapter_OnReadCfg)