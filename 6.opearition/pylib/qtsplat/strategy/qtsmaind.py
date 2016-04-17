#coding=utf-8
#////////////////////////////////////////////////////////////////////
import os
import sys
import string
import platform
import traceback 
from ctypes import *

sys.path.append(os.path.join(os.getenv('QTS_BASE_PATH','../..'),'pylib/utility'))
sys.path.append(os.path.join(os.getenv('QTS_BASE_PATH','../..'),'pylib/qtsplat/share'))
from qtsfun import *
from qtstradefun import *
try :
	from qtsgproto_pb2 import *
except :
	print('warning>> python lib no support protocol buffer')
from qtsonuca import *
from qtsadapter import *
from qtspycfg import *
from qtsmain import *

#////////////////////////////////////////////////////////////////////
g_oDebugTrade = None

def OnEvent(itype,subtype,pro,data,size,para) :
	global g_oDebugTrade
	if itype == QTS_GPROTO_EVENT_TYPE_INIT :
		g_oDebugTrade = QtsMainTrade(para,debug)
	else :
		g_oDebugTrade.DoEvent(itype,subtype,pro,data,size,para)
	return 1

QtsAdapter_OnEvent=QTS_ADAPTER_EVENT_CALLBACK(OnEvent)
def RegisterStrategyEvent() :
	RegisterEvent(QTS_GPROTO_EVENT_TYPE_INIT,QtsAdapter_OnEvent)
	RegisterEvent(QTS_GPROTO_EVENT_TYPE_DATA,QtsAdapter_OnEvent)
	RegisterEvent(QTS_GPROTO_EVENT_TYPE_PARAMETER,QtsAdapter_OnEvent)
	RegisterEvent(QTS_GPROTO_EVENT_TYPE_STRATEGY_START,QtsAdapter_OnEvent)
	RegisterEvent(QTS_GPROTO_EVENT_TYPE_STRATEGY_PAUSE,QtsAdapter_OnEvent)
	RegisterEvent(QTS_GPROTO_EVENT_TYPE_STRATEGY_WATCH,QtsAdapter_OnEvent)
	RegisterEvent(QTS_GPROTO_EVENT_TYPE_STRATEGY_STOP,QtsAdapter_OnEvent)
	RegisterEvent(QTS_GPROTO_EVENT_TYPE_RETURN,QtsAdapter_OnEvent)
	RegisterEvent(QTS_GPROTO_EVENT_TYPE_ERROR,QtsAdapter_OnEvent)
	RegisterEvent(QTS_GPROTO_EVENT_TYPE_CYCLING,QtsAdapter_OnEvent)
	RegisterEvent(QTS_GPROTO_EVENT_TYPE_CYCLED,QtsAdapter_OnEvent)
	RegisterEvent(QTS_GPROTO_EVENT_TYPE_COMMITING,QtsAdapter_OnEvent)
	RegisterEvent(QTS_GPROTO_EVENT_TYPE_COMMITED,QtsAdapter_OnEvent)

def RegisterAllEvent() :
	RegisterStrategyEvent()
	RegisterCfgEvent()

def RunMain(argv) :
	print("Start Application from python main")	
	RegisterAllEvent()
	print('RunMain input argv is {0}'.format(argv))
	RunPlat(argv)
	print("End Application from python main")
	
def RunDebug(path) :
	if GetRunVersion() == debug :
		if GetAppMode() == QTS_APP_MODE_ALL :
			RunMain('{0} {1}={2} {3}={4} {5}={6}'.format(BuildLocalCfg('qtsgui','CreateConfig','QtsPythonDCfg',GetProtoPath(),GetProtoFile()),QTS_EVN_FILE_KEY,CombinePath(path,'main_all.qts'),QTS_TRACE_MESSAGE_KEY,GetTraceMessage(),QTS_TRACE_DEBUG_KEY,GetTraceDebug()))
		elif GetAppMode() == QTS_APP_MODE_SERVER :
			RunMain('{0} {1}={2} {3}={4} {5}={6}'.format(BuildLocalCfg('qtsss','CreateConfig','QtsPythonDCfg',GetProtoPath(),GetProtoFile()),QTS_EVN_FILE_KEY,CombinePath(path,'main_server.qts'),QTS_TRACE_MESSAGE_KEY,GetTraceMessage(),QTS_TRACE_DEBUG_KEY,GetTraceDebug()))
		elif GetAppMode() == QTS_APP_MODE_SINGLE :
			if GetStartApp() == QTS_CFG_APP_SS_NAME :
				RunMain('{0} {1}={2} {3}={4} {5}={6}'.format(BuildLocalCfg('qtsss','CreateConfig','QtsPythonDCfg',GetProtoPath(),GetProtoFile()),QTS_EVN_FILE_KEY,CombinePath(path,'main_ss.qts'),QTS_TRACE_MESSAGE_KEY,GetTraceMessage(),QTS_TRACE_DEBUG_KEY,GetTraceDebug()))
			elif GetStartApp() == QTS_CFG_APP_DS_NAME :
				RunMain('{0} {1}={2} {3}={4} {5}={6}'.format(BuildLocalCfg('qtsds','CreateConfig','QtsPythonDCfg',GetProtoPath(),GetProtoFile()),QTS_EVN_FILE_KEY,CombinePath(path,'main_ds.qts'),QTS_TRACE_MESSAGE_KEY,GetTraceMessage(),QTS_TRACE_DEBUG_KEY,GetTraceDebug()))
			elif GetStartApp() == QTS_CFG_APP_GW_NAME :
				RunMain('{0} {1}={2} {3}={4} {5}={6}'.format(BuildLocalCfg('qtsgw','CreateConfig','QtsPythonDCfg',GetProtoPath(),GetProtoFile()),QTS_EVN_FILE_KEY,CombinePath(path,'main_gw.qts'),QTS_TRACE_MESSAGE_KEY,GetTraceMessage(),QTS_TRACE_DEBUG_KEY,GetTraceDebug()))
			elif GetStartApp() == QTS_CFG_APP_GUI_NAME :
				RunMain('{0} {1}={2} {3}={4} {5}={6}'.format(BuildLocalCfg('qtsgui','CreateConfig','QtsPythonDCfg',GetProtoPath(),GetProtoFile()),QTS_EVN_FILE_KEY,CombinePath(path,'main_gui.qts'),QTS_TRACE_MESSAGE_KEY,GetTraceMessage(),QTS_TRACE_DEBUG_KEY,GetTraceDebug()))
			else :
				print('error:>>unknow system start')
		else :
			print('error:>>unknow app mode')