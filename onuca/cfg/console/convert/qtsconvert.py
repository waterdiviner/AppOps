#coding=utf-8
from qtscommon import *

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#run program
if not IsCanRun(QTS_APP_CONVERT) :
	PrintMessage('---------------------------------- begin load qtsconvert ----------------------------------------------')
	#//////////////////////////////////////////////////////////////////////////////
	#strategy manager log file
	QTS_CONVERT_LOG_KEY='qts_convertlog'
	QTS_CONVERT_LOG_FILE='qtsconvert'
	QTS_CONVERT_MANGER_ID_BASE=500
	#//////////////////////////////////////////////////////////////////////////////
	#create application cfg
	CreateApplication(QTS_CONVERT_CFG_FILE,QTS_APP_CONVERT,88850000,'2.0.0',QTS_APP_CONVERT,'qts_convert',QTS_CONVERT_LOG_KEY)
	AppendApplication(QTS_CONVERT_CFG_FILE,'qts_bfile_key',CreateObjectId(503,999))
	AppendApplication(QTS_CONVERT_CFG_FILE,'qts_xfile_key',CreateObjectId(503,995))
	#//////////////////////////////////////////////////////////////////////////////
	#//////////////////////////////////////////////////////////////////////////////
	#create context cfg		
	CreateContext(QTS_CONVERT_CFG_FILE,True,30)
	#//////////////////////////////////////////////////////////////////////////////
	#//////////////////////////////////////////////////////////////////////////////
	#load share plugin
	LoadLogs(QTS_CONVERT_CFG_FILE,QTS_LOG_DEFAULT_LIB,QTS_LOG_DEFAULT_FUN)
	AppendLog(QTS_CONVERT_LOG_KEY,QTS_CONVERT_LOG_FILE)
	LoadParsers(QTS_CONVERT_CFG_FILE,QTS_CONVERT_MANGER_ID_BASE+1,QTS_CONVERT_LOG_KEY,GetSharePath())
	LoadSecuInfoes(QTS_CONVERT_CFG_FILE,QTS_CONVERT_MANGER_ID_BASE+2,QTS_CONVERT_LOG_KEY,qts_static=QTS_LOADER_FILE_INFO_S,qts_dynamic=QTS_LOADER_FILE_INFO_D)
	LoadBackups(QTS_CONVERT_CFG_FILE,QTS_CONVERT_MANGER_ID_BASE+3,QTS_CONVERT_LOG_KEY,GetSharePath())
	LoadLoaders(QTS_CONVERT_CFG_FILE,QTS_CONVERT_MANGER_ID_BASE+4,QTS_CONVERT_LOG_KEY,GetSharePath())
	#//////////////////////////////////////////////////////////////////////////////
	PrintMessage('---------------------------------- end load qtsconvert ----------------------------------------------')