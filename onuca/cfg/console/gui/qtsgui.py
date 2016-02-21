#coding=utf-8
from qtscommon import *

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#run program
if not IsCanRun(QTS_APP_GUI) :
	PrintMessage('---------------------------------- begin load qtsgui ----------------------------------------------')
	#//////////////////////////////////////////////////////////////////////////////
	#strategy manager log file
	QTS_GUI_LOG_KEY='qts_guilog'
	QTS_GUI_LOG_FILE='qtsgui'
	QTS_GUI_MANGER_ID_BASE=400
	#//////////////////////////////////////////////////////////////////////////////
	#create application cfg
	CreateApplication(QTS_GUI_CFG_FILE,QTS_APP_GUI,88840000,'2.0.0',QTS_APP_GUI,'qts_gui',QTS_GUI_LOG_KEY)
	#//////////////////////////////////////////////////////////////////////////////
	#//////////////////////////////////////////////////////////////////////////////
	#create context cfg		
	CreateContext(QTS_GUI_CFG_FILE,True,30)
	#//////////////////////////////////////////////////////////////////////////////
	#//////////////////////////////////////////////////////////////////////////////
	#load share plugin
	LoadLogs(QTS_GUI_CFG_FILE,QTS_LOG_DEFAULT_LIB,QTS_LOG_DEFAULT_FUN)
	AppendLog(QTS_GUI_LOG_KEY,QTS_GUI_LOG_FILE)
	LoadParsers(QTS_GUI_CFG_FILE,QTS_GUI_MANGER_ID_BASE+1,QTS_GUI_LOG_KEY,GetSharePath())
	LoadSecuInfoes(QTS_GUI_CFG_FILE,QTS_GUI_MANGER_ID_BASE+2,QTS_GUI_LOG_KEY,qts_static=QTS_LOADER_FILE_INFO_S,qts_dynamic=QTS_LOADER_FILE_INFO_D)
	LoadBackups(QTS_GUI_CFG_FILE,QTS_GUI_MANGER_ID_BASE+3,QTS_GUI_LOG_KEY,GetSharePath())
	LoadLoaders(QTS_GUI_CFG_FILE,QTS_GUI_MANGER_ID_BASE+4,QTS_GUI_LOG_KEY,GetSharePath())
	#//////////////////////////////////////////////////////////////////////////////
	#//////////////////////////////////////////////////////////////////////////////
	#load business plugin
	LoadMonitors(QTS_GUI_CFG_FILE,QTS_GUI_MANGER_ID_BASE+5,QTS_GUI_LOG_KEY,GetGuiPath())
	LoadDSTransfers(QTS_GUI_CFG_FILE,QTS_GUI_MANGER_ID_BASE+6,QTS_GUI_LOG_KEY,GetGuiPath())
	LoadGUITransfers(QTS_GUI_CFG_FILE,QTS_GUI_MANGER_ID_BASE+7,QTS_GUI_LOG_KEY,GetGuiPath())
	#//////////////////////////////////////////////////////////////////////////////
	PrintMessage('---------------------------------- end load qtsgui ----------------------------------------------')