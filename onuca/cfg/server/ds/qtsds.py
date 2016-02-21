#coding=utf-8
from qtscommon import *
	
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#run program
if not IsCanRun(QTS_APP_DS) :	
	PrintMessage('---------------------------------- begin load qtsds ----------------------------------------------')	
	#//////////////////////////////////////////////////////////////////////////////
	#strategy manager log file
	QTS_DS_LOG_KEY='qts_dslog'
	QTS_DS_LOG_FILE='qtsds'
	QTS_DS_MANGER_ID_BASE=200
	#//////////////////////////////////////////////////////////////////////////////
	#create application cfg
	CreateApplication(QTS_DS_CFG_FILE,QTS_APP_DS,88820000,'2.0.0',QTS_APP_DS,'qts_ds',QTS_DS_LOG_KEY)
	#//////////////////////////////////////////////////////////////////////////////
	#//////////////////////////////////////////////////////////////////////////////
	#create context cfg		
	CreateContext(QTS_DS_CFG_FILE,GetMultiThread(),30)
	#//////////////////////////////////////////////////////////////////////////////
	#//////////////////////////////////////////////////////////////////////////////
	#load share plugin
	if GetAppMode() == QTS_APP_MODE_SINGLE :
		LoadLogs(QTS_DS_CFG_FILE,QTS_LOG_DEFAULT_LIB,QTS_LOG_DEFAULT_FUN)		
		LoadParsers(QTS_DS_CFG_FILE,QTS_DS_MANGER_ID_BASE+1,QTS_DS_LOG_KEY,GetSharePath())
		LoadSecuInfoes(QTS_DS_CFG_FILE,QTS_DS_MANGER_ID_BASE+2,QTS_DS_LOG_KEY,qts_static=QTS_LOADER_FILE_INFO_S,qts_dynamic=QTS_LOADER_FILE_INFO_D)
		LoadBackups(QTS_DS_CFG_FILE,QTS_DS_MANGER_ID_BASE+3,QTS_DS_LOG_KEY,GetSharePath())
		LoadLoaders(QTS_DS_CFG_FILE,QTS_DS_MANGER_ID_BASE+4,QTS_DS_LOG_KEY,GetSharePath())
	AppendLog(QTS_DS_LOG_KEY,QTS_DS_LOG_FILE)
	#//////////////////////////////////////////////////////////////////////////////
	#//////////////////////////////////////////////////////////////////////////////
	#load bz plugin
	LoadTransfers(QTS_DS_CFG_FILE,QTS_DS_MANGER_ID_BASE+5,QTS_DS_LOG_KEY,GetDSPath())
	LoadMonitors(QTS_DS_CFG_FILE,QTS_DS_MANGER_ID_BASE+6,QTS_DS_LOG_KEY,GetDSPath())
	LoadMarkets(QTS_DS_CFG_FILE,QTS_DS_MANGER_ID_BASE+7,QTS_DS_LOG_KEY,GetDSPath())
	#AppendPropertyForMarkets(QTS_DS_CFG_FILE,QTS_CFG_KEY_CHECKSECUID,QTS_FALSE)
	#//////////////////////////////////////////////////////////////////////////////
	PrintMessage('---------------------------------- end load qtsds ----------------------------------------------')