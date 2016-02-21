#coding=utf-8
from qtscommon import *

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#run program
if not IsCanRun(QTS_APP_SS) :
	PrintMessage('---------------------------------- begin load qtsss ----------------------------------------------')
	#//////////////////////////////////////////////////////////////////////////////
	#strategy manager log file
	QTS_SS_LOG_KEY='qts_sslog'
	QTS_SS_LOG_FILE='qtsss'
	QTS_SS_MANGER_ID_BASE=300
	#//////////////////////////////////////////////////////////////////////////////
	#create application cfg
	CreateApplication(QTS_SS_CFG_FILE,QTS_APP_SS,88830000,'2.0.0',QTS_APP_SS,'qts_ss',QTS_SS_LOG_KEY)
	AppendApplication(QTS_SS_CFG_FILE,QTS_DATA_TO_GW,QTS_TRUE)
	AppendApplication(QTS_SS_CFG_FILE,QTS_DATA_TO_GUI,QTS_TRUE)
	#//////////////////////////////////////////////////////////////////////////////
	#//////////////////////////////////////////////////////////////////////////////
	#create context cfg	
	CreateContext(QTS_SS_CFG_FILE,GetMultiThread(),30)
	#//////////////////////////////////////////////////////////////////////////////
	#//////////////////////////////////////////////////////////////////////////////
	#load share plugin
	if GetAppMode() == QTS_APP_MODE_SINGLE or GetAppMode() == QTS_APP_MODE_SERVER :
		LoadLogs(QTS_SS_CFG_FILE,QTS_LOG_DEFAULT_LIB,QTS_LOG_DEFAULT_FUN)		
		LoadParsers(QTS_SS_CFG_FILE,QTS_SS_MANGER_ID_BASE+1,QTS_SS_LOG_KEY,GetSharePath())
		LoadSecuInfoes(QTS_SS_CFG_FILE,QTS_SS_MANGER_ID_BASE+2,QTS_SS_LOG_KEY,qts_static=QTS_LOADER_FILE_INFO_S,qts_dynamic=QTS_LOADER_FILE_INFO_D)
		LoadBackups(QTS_SS_CFG_FILE,QTS_SS_MANGER_ID_BASE+3,QTS_SS_LOG_KEY,GetSharePath())
		LoadLoaders(QTS_SS_CFG_FILE,QTS_SS_MANGER_ID_BASE+4,QTS_SS_LOG_KEY,GetSharePath())
	AppendLog(QTS_SS_LOG_KEY,QTS_SS_LOG_FILE)
	#//////////////////////////////////////////////////////////////////////////////
	#//////////////////////////////////////////////////////////////////////////////
	#load business plugin
	LoadDSTransfers(QTS_SS_CFG_FILE,QTS_SS_MANGER_ID_BASE+5,QTS_SS_LOG_KEY,GetSSPath())
	#AppendPropertyForDSTransfers(QTS_SS_CFG_FILE,QTS_CFG_KEY_CHECKSECUID,QTS_FALSE)
	LoadGWTransfers(QTS_SS_CFG_FILE,QTS_SS_MANGER_ID_BASE+6,QTS_SS_LOG_KEY,GetSSPath())
	#AppendPropertyForGWTransfers(QTS_SS_CFG_FILE,QTS_CFG_KEY_CHECKSECUID,QTS_FALSE)
	LoadGUITransfers(QTS_SS_CFG_FILE,QTS_SS_MANGER_ID_BASE+7,QTS_SS_LOG_KEY,GetSSPath())
	LoadMonitors(QTS_SS_CFG_FILE,QTS_SS_MANGER_ID_BASE+8,QTS_SS_LOG_KEY,GetSSPath())
	LoadCalculates(QTS_SS_CFG_FILE,QTS_SS_MANGER_ID_BASE+9,QTS_SS_LOG_KEY,GetSSPath())
	LoadChecks(QTS_SS_CFG_FILE,QTS_SS_MANGER_ID_BASE+10,QTS_SS_LOG_KEY,GetSSPath())
	LoadAlgoes(QTS_SS_CFG_FILE,QTS_SS_MANGER_ID_BASE+11,QTS_SS_LOG_KEY,GetSSPath())
	LoadStrategies(QTS_SS_CFG_FILE,QTS_SS_MANGER_ID_BASE+12,QTS_SS_LOG_KEY,GetSSPath(),3)
	#QTS_CFG_KEY_BACKUP: index is 0 backup stratey,index is 1 backup parameter ,index is 2 backup ssworking,if no backup set BuildBackupFile(None)
	#[BuildBackupFile('strategy'),BuildBackupFile('parameter'),BuildBackupFile('ssworking')]
	#[BuildBackupFile(None),BuildBackupFile(None),BuildBackupFile(None)]
	AppendPropertyForStrategies(QTS_SS_CFG_FILE,QTS_CFG_KEY_BACKUP,[BuildBackupFile(QTS_BACKUP_SS_STRATEGY),BuildBackupFile(QTS_BACKUP_SS_PARAMETER),BuildBackupFile(QTS_BACKUP_SS_WORKING)])
	#//////////////////////////////////////////////////////////////////////////////
	PrintMessage('---------------------------------- end load qtsss ----------------------------------------------')
