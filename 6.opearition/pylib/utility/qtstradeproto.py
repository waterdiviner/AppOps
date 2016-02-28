#coding=utf-8
import platform
import traceback 
import string
from ctypes import * 
from qtsenvir import *
from qtssecurity import *
from qtsfun import *
from qtstradefun import *
from qtsgproto_pb2 import *
from qtsutility import *

#/////////////////////////////////////////////////////////////////#	
#QtsGProtoVariable
class QtsVariable(object) :
	def __init__(self,var = None) :                
		if var == None :
			self.var = QtsGProtoVariable()
		else :
			self.var = var
	
	def Item(self) :
		return self.var
	
	def Type(self) :
		return self.var.type
		
	def Key(self) :
		return self.var.key
		
	def Name(self) :
		return self.var.name
		
	def Value_String(self) :
		return self.value_string
		
	def Value_Int32(self) :
		return self.value_int32
		
	def Value_UInt32(self) :
		return self.value_uint32
		
	def Value_Int64(self) :
		return self.value_int64
		
	def Value_UInt64(self) :
		return self.value_uint64
		
	def BuileVariableForString(self,key,name,value) :
		self.var.key = key
		self.var.name = name
		self.var.type = QTS_GPROTO_VARIABLE_TYPE_STRING
		self.var.value_string = value
	
	def BuileVariableForInt16(self,key,name,value) :
		self.var.key = key
		self.var.name = name
		self.var.type = QTS_GPROTO_VARIABLE_TYPE_INT16
		self.var.value_int16 = value	
		
	def BuileVariableForUInt16(self,key,name,value) :
		self.var.key = key
		self.var.name = name
		self.var.type = QTS_GPROTO_VARIABLE_TYPE_UINT16
		self.var.value_uint16 = value	
		
	def BuileVariableForInt32(self,key,name,value) :
		self.var.key = key
		self.var.name = name
		self.var.type = QTS_GPROTO_VARIABLE_TYPE_INT32
		self.var.value_int32 = value	

	def BuileVariableForUInt32(self,key,name,value) :
		self.var.key = key
		self.var.name = name
		self.var.type = QTS_GPROTO_VARIABLE_TYPE_UINT32
		self.var.value_uint32 = value		
		
	def BuileVariableForInt64(self,key,name,value) :
		self.var.key = key
		self.var.name = name
		self.var.type = QTS_GPROTO_VARIABLE_TYPE_INT64
		self.var.value_int64 = value
		
	def BuileVariableForUInt64(self,key,name,value) :
		self.var.key = key
		self.var.name = name
		self.var.type = QTS_GPROTO_VARIABLE_TYPE_UINT64
		self.var.value_uint64 = value		
			
	def BuileVariableForDouble(self,key,name,value) :
		self.var.key = key
		self.var.name = name
		self.var.type = QTS_GPROTO_VARIABLE_TYPE_DOUBLE
		self.var.value_double = value		
		
	def BuileVariableForFloat(self,key,name,value) :
		self.var.key = key
		self.var.name = name
		self.var.type = QTS_GPROTO_VARIABLE_TYPE_FLOAT
		self.var.value_float = value		
		
	def BuileVariableForBool(self,key,name,value) :
		self.var.key = key
		self.var.name = name
		self.var.type = QTS_GPROTO_VARIABLE_TYPE_BOOL
		self.var.value_bool = value	
		
	def BuildVariable(self,itype,key,name,value) :
		if itype == QTS_GPROTO_VARIABLE_TYPE_INT16 :
			self.BuileVariableForInt16(key,name,value)
		elif itype == QTS_GPROTO_VARIABLE_TYPE_UINT16 :
			self.BuileVariableForUInt16(key,name,value)
		elif itype == QTS_GPROTO_VARIABLE_TYPE_INT32 :
			self.BuileVariableForInt32(key,name,value)
		elif itype == QTS_GPROTO_VARIABLE_TYPE_UINT32 :
			self.BuileVariableForUInt32(key,name,value)
		elif itype == QTS_GPROTO_VARIABLE_TYPE_INT64 :
			self.BuileVariableForInt64(key,name,value)
		elif itype == QTS_GPROTO_VARIABLE_TYPE_UINT64 :
			self.BuileVariableForUInt64(key,name,value)	
		elif itype == QTS_GPROTO_VARIABLE_TYPE_DOUBLE :
			self.BuileVariableForDouble(key,name,value)
		elif itype == QTS_GPROTO_VARIABLE_TYPE_FLOAT :
			self.BuileVariableForFloat(key,name,value)	
		elif itype == QTS_GPROTO_VARIABLE_TYPE_STRING :
			self.BuileVariableForString(key,name,value)	
	
	def Print(self) :
		print(self.var)
		
#/////////////////////////////////////////////////////////////////#			
#QtsGProtoVariables
class QtsVariables(object) :
	def __init__(self,var = None) :
		if var == None :
			self.var = QtsGProtoVariables()
		else :
			self.var = var
	
	def Items(self) :
		return self.var
		
	def Add(self) :
		return QtsVariable(self.var.items.add())
		
	def AddItem(self,itype,key,name,value) :
		item = self.Add()
		item.BuildVariable(itype,key,name,value)
		return item

	def Type(self) :
		return self.var.type
		
	def SetType(self,itype) :
		self.var.type = itype
		
	def Print(self) :
		for item in self.var.items :
			QtsVariable(item).Print()
			
#/////////////////////////////////////////////////////////////////#			
#QtsGProtoUserData
class QtsUserData(object) :
	def __init__(self,var = None) :
		if var == None :
			self.var = QtsGProtoUserData()
		else :
			self.var = var
	
	def Items(self) :
		return self.var
		
	def Add(self) :
		return QtsVariables(self.var.items.add())	

	def Type(self) :
		return self.var.type
		
	def SetType(self,itype) :
		self.var.type = itype
		
	def Name(self) :
		return self.var.name
		
	def SetName(self,name) :
		self.var.name = name

	def Print(self) :
		for item in self.var.items :
			QtsVariables(item).Print()
			
#/////////////////////////////////////////////////////////////////#			
#QtsGProtoAlgoOrder
class QtsAlgoOrder(object) :
	def __init__(self,var = None) :
		if var == None :
			self.var = QtsGProtoAlgoOrder()
		else :
			self.var = var
	
	def Items(self) :
		return self.var
		
	def Add(self) :
		return QtsVariables(self.var.items.add())
		
	def SetAlgoId(self,algoid) :
		self.var.algoid = algoid
		
	def AlgoId(self) :
		return self.var.algoid
		
	def SetAlgoIndex(self,algoindex) :
		self.var.algoindex = algoindex
		
	def AlgoIndex(self) :
		return self.var.algoindex	
		
	def Print(self) :
		for item in self.var.items :
			QtsVariables(item).Print()
			
#/////////////////////////////////////////////////////////////////#			
#QtsGProtoAlgoCancel
class QtsAlgoCancel(object) :
	def __init__(self,var = None) :
		if var == None :
			self.var = QtsGProtoAlgoCancel()
		else :
			self.var = var
	
	def Items(self) :
		return self.var
		
	def Add(self) :
		return QtsVariables(self.var.items.add())
		
	def SetAlgoId(self,algoid) :
		self.var.algoid = algoid
		
	def AlgoId(self) :
		return self.var.algoid
		
	def SetAlgoIndex(self,algoindex) :
		self.var.algoindex = algoindex
		
	def AlgoIndex(self) :
		return self.var.algoindex		

	def Print(self) :
		for item in self.var.items :
			QtsVariables(item).Print()
			