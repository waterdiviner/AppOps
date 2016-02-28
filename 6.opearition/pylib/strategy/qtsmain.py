#coding=utf-8
import platform
import traceback 
import string
from ctypes import * 
from qtsfun import *
from qtstradefun import *
from qtsgproto_pb2 import *
from qtsutility import *

#/////////////////////////////////////////////////////////////////#	
g_oUserTrade=None
def RegisterTrade(obj) :
	if QTS_RUN_VERSION == release :
		g_oUserTrade=obj
	else :
		global g_oUserTrade
		g_oUserTrade=obj
	
def GetTrade() :
	if QTS_RUN_VERSION == release :
		return g_oUserTrade
	else :
		global g_oUserTrade
		return g_oUserTrade

#/////////////////////////////////////////////////////////////////#		
class QtsMainTrade :
	def __init__(self,parent,eventmode) :
		self.parent=parent
		self.eventmode=eventmode
		oTrade = GetTrade()
		if oTrade != None :
			oTrade.SetParent(self,parent)
			oTrade.Init()
		if self.eventmode == release :
			qts_SetCallback(self.parent,'DoEvent',0)

	def DoEvent(self,itype,subtype,pro,data,size,para) :
		if self.eventmode == release :
			self.DoEventForPy(itype,subtype,pro,data,size,para)	
		else :
			self.DoEventForC(itype,subtype,pro,data,size,para)			

	def DoEventForPy(self,itype,subtype,pro,data,size,para) :
		if itype == QTS_GPROTO_EVENT_TYPE_DATA :
			market = QtsGProtoData()
			if ParseFromString(data,size,market) :			
				self.OnData(market)
		elif itype == QTS_GPROTO_EVENT_TYPE_DATAS :
			markets = QtsGProtoDatas()
			if ParseFromString(data,size,markets) :			
				self.OnDatas(markets)				
		elif itype == QTS_GPROTO_EVENT_TYPE_RETURN :
			result = QtsGProtoReturn()
			if ParseFromString(data,size,result) :				
				self.OnReturn(result)
		elif itype == QTS_GPROTO_EVENT_TYPE_RETURNS :
			results = QtsGProtoReturns()
			if ParseFromString(data,size,results) :				
				self.OnReturns(results)				
		elif itype == QTS_GPROTO_EVENT_TYPE_ERROR :
			errinfo = QtsGProtoMessage()
			if ParseFromString(data,size,errinfo) :	
				self.OnError(errinfo)
		elif itype == QTS_GPROTO_EVENT_TYPE_PARAMETER :
			parameter = QtsGProtoParameter()
			if ParseFromString(data,size,parameter) :	
				self.OnParameter(parameter)
		elif itype == QTS_GPROTO_EVENT_TYPE_STRATEGY_START :
			self.OnStart()
		elif itype == QTS_GPROTO_EVENT_TYPE_STRATEGY_PAUSE :
			self.OnPause()
		elif itype == QTS_GPROTO_EVENT_TYPE_STRATEGY_WATCH :
			self.OnWatch()
		elif itype == QTS_GPROTO_EVENT_TYPE_STRATEGY_STOP :
			self.OnStop()
		elif itype == QTS_GPROTO_EVENT_TYPE_CYCLING :
			self.OnCycling()
		elif itype == QTS_GPROTO_EVENT_TYPE_CYCLED :
			self.OnCycled()
		elif itype == QTS_GPROTO_EVENT_TYPE_UPDATING :
			self.OnUpdating()
		elif itype == QTS_GPROTO_EVENT_TYPE_UPDATED :
			self.OnUpdated()				
		elif itype == QTS_GPROTO_EVENT_TYPE_COMMITING :
			self.OnCommiting()
		elif itype == QTS_GPROTO_EVENT_TYPE_COMMITED :
			self.OnCommited()			
		elif itype == QTS_GPROTO_EVENT_TYPE_EVENT :	
			self.OnEvent(subtype,pro,data,size)
				
	def DoEventForC(self,itype,subtype,pro,data,size,para) :
		if itype == QTS_GPROTO_EVENT_TYPE_DATA :
			market = QtsGProtoData()
			if ParseFromPointer(data,size,market) :			
				self.OnData(market)
		elif itype == QTS_GPROTO_EVENT_TYPE_DATAS :
			markets = QtsGProtoDatas()
			if ParseFromPointer(data,size,markets) :			
				self.OnDatas(markets)				
		elif itype == QTS_GPROTO_EVENT_TYPE_RETURN :
			result = QtsGProtoReturn()
			if ParseFromPointer(data,size,result) :				
				self.OnReturn(result)
		elif itype == QTS_GPROTO_EVENT_TYPE_RETURNS :
			results = QtsGProtoReturns()
			if ParseFromPointer(data,size,results) :				
				self.OnReturns(results)				
		elif itype == QTS_GPROTO_EVENT_TYPE_ERROR :
			errinfo = QtsGProtoMessage()
			if ParseFromPointer(data,size,errinfo) :	
				self.OnError(errinfo)
		elif itype == QTS_GPROTO_EVENT_TYPE_PARAMETER :
			parameter = QtsGProtoParameter()
			if ParseFromPointer(data,size,parameter) :	
				self.OnParameter(parameter)
		elif itype == QTS_GPROTO_EVENT_TYPE_STRATEGY_START :
			self.OnStart()
		elif itype == QTS_GPROTO_EVENT_TYPE_STRATEGY_PAUSE :
			self.OnPause()
		elif itype == QTS_GPROTO_EVENT_TYPE_STRATEGY_WATCH :
			self.OnWatch()
		elif itype == QTS_GPROTO_EVENT_TYPE_STRATEGY_STOP :
			self.OnStop()
		elif itype == QTS_GPROTO_EVENT_TYPE_CYCLING :
			self.OnCycling()
		elif itype == QTS_GPROTO_EVENT_TYPE_CYCLED :
			self.OnCycled()
		elif itype == QTS_GPROTO_EVENT_TYPE_COMMITING :
			self.OnCommiting()
		elif itype == QTS_GPROTO_EVENT_TYPE_COMMITED :
			self.OnCommited()
		elif itype == QTS_GPROTO_EVENT_TYPE_UPDATING :
			self.OnUpdating()
		elif itype == QTS_GPROTO_EVENT_TYPE_UPDATED :
			self.OnUpdated()			
		elif itype == QTS_GPROTO_EVENT_TYPE_EVENT :	
			self.OnEvent(subtype,pro,data,size)
			
	def OnCycling(self) :
		oTrade = GetTrade()
		if oTrade != None :
			oTrade.OnCycling()
			
	def OnCycled(self) :
		oTrade = GetTrade()
		if oTrade != None :
			oTrade.OnCycled()	
		
	def OnUpdating(self) :
		oTrade = GetTrade()
		if oTrade != None :
			oTrade.OnUpdating()		
		
	def OnUpdated(self) : 
		oTrade = GetTrade()
		if oTrade != None :
			oTrade.OnUpdated()	
			
	def OnCommiting(self) :
		oTrade = GetTrade()
		if oTrade != None :
			oTrade.OnCommiting()		
		
	def OnCommited(self) : 
		oTrade = GetTrade()
		if oTrade != None :
			oTrade.OnCommited()	

	def OnStart(self) :
		oTrade = GetTrade()
		if oTrade != None :
			oTrade.OnStart()
			
	def OnPause(self) :
		oTrade = GetTrade()
		if oTrade != None :
			oTrade.OnPause()	
		
	def OnWatch(self) :
		oTrade = GetTrade()
		if oTrade != None :
			oTrade.OnWatch()		
		
	def OnStop(self) : 
		oTrade = GetTrade()
		if oTrade != None :
			oTrade.OnStop()	
		
	def OnError(self,errinfo) : 
		oTrade = GetTrade()
		if oTrade != None :
			oTrade.OnError(errinfo)		
		
	def OnParameter(self,parameter) : 
		oTrade = GetTrade()
		if oTrade != None :
			oTrade.OnParameter(parameter)			
		
	def OnReturn(self,result) :
		oTrade = GetTrade()
		if oTrade != None :
			oTrade.OnReturn(result)
		
	def OnReturns(self,results) :
		oTrade = GetTrade()
		if oTrade != None :
			oTrade.OnReturns(results)
			
	def OnData(self,market) :
		oTrade = GetTrade()
		if oTrade != None :
			oTrade.OnData(market)	
			
	def OnDatas(self,markets) :
		oTrade = GetTrade()
		if oTrade != None :
			oTrade.OnDatas(markets)
			
	def OnEvent(self,itype,pro,data,size) :
		oTrade = GetTrade()
		if oTrade != None :
			oTrade.OnEvent(itype,pro,data,size)
			