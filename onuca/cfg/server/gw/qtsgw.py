#coding=utf-8
from qtscommon import *

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#run program
if not IsCanRun(QTS_APP_GW) :
	PrintMessage('---------------------------------- begin load qtsgw ----------------------------------------------')
	#//////////////////////////////////////////////////////////////////////////////
	#strategy manager log file
	QTS_GW_LOG_KEY='qts_gwlog'
	QTS_GW_LOG_FILE='qtsgw'
	QTS_GW_MANGER_ID_BASE=100
	#//////////////////////////////////////////////////////////////////////////////
	#create application cfg
	CreateApplication(QTS_GW_CFG_FILE,QTS_APP_GW,88810000,'2.0.0',QTS_APP_GW,'qts_gw',QTS_GW_LOG_KEY)
	#//////////////////////////////////////////////////////////////////////////////
	#//////////////////////////////////////////////////////////////////////////////
	#create context cfg		
	CreateContext(QTS_GW_CFG_FILE,GetMultiThread(),30)
	#//////////////////////////////////////////////////////////////////////////////
	#//////////////////////////////////////////////////////////////////////////////
	#load share plugin
	if GetAppMode() == QTS_APP_MODE_SINGLE :
		LoadLogs(QTS_GW_CFG_FILE,QTS_LOG_DEFAULT_LIB,QTS_LOG_DEFAULT_FUN)
		LoadParsers(QTS_GW_CFG_FILE,QTS_GW_MANGER_ID_BASE+1,QTS_GW_LOG_KEY,GetSharePath())
		LoadSecuInfoes(QTS_GW_CFG_FILE,QTS_GW_MANGER_ID_BASE+2,QTS_GW_LOG_KEY,qts_static=QTS_LOADER_FILE_INFO_S,qts_dynamic=QTS_LOADER_FILE_INFO_D)
		LoadBackups(QTS_GW_CFG_FILE,QTS_GW_MANGER_ID_BASE+3,QTS_GW_LOG_KEY,GetSharePath())
		LoadLoaders(QTS_GW_CFG_FILE,QTS_GW_MANGER_ID_BASE+4,QTS_GW_LOG_KEY,GetSharePath())
	AppendLog(QTS_GW_LOG_KEY,QTS_GW_LOG_FILE)
	#//////////////////////////////////////////////////////////////////////////////
	#//////////////////////////////////////////////////////////////////////////////
	LoadAccounts(QTS_GW_CFG_FILE,QTS_GW_MANGER_ID_BASE+5,QTS_GW_LOG_KEY,qts_trade=QTS_LOADER_FILE_ACCOUNT_TRADE,qts_user=QTS_LOADER_FILE_ACCOUNT_USER,qts_exchange=QTS_LOADER_FILE_ACCOUNT_EXCHANGE)
	LoadPositions(QTS_GW_CFG_FILE,QTS_GW_MANGER_ID_BASE+6,QTS_GW_LOG_KEY,qts_trposition=QTS_LOADER_FILE_POSITION_TRADE,qts_exposition=QTS_LOADER_FILE_POSITION_EXCHANGE)
	#//////////////////////////////////////////////////////////////////////////////
	#//////////////////////////////////////////////////////////////////////////////
	#load business plugin
	LoadDSTransfers(QTS_GW_CFG_FILE,QTS_GW_MANGER_ID_BASE+7,QTS_GW_LOG_KEY,GetGWPath())
	LoadGWTransfers(QTS_GW_CFG_FILE,QTS_GW_MANGER_ID_BASE+8,QTS_GW_LOG_KEY,GetGWPath())
	LoadMonitors(QTS_GW_CFG_FILE,QTS_GW_MANGER_ID_BASE+9,QTS_GW_LOG_KEY,GetGWPath())
	LoadChecks(QTS_GW_CFG_FILE,QTS_GW_MANGER_ID_BASE+10,QTS_GW_LOG_KEY,GetGWPath())
	LoadAlgoes(QTS_GW_CFG_FILE,QTS_GW_MANGER_ID_BASE+11,QTS_GW_LOG_KEY,GetGWPath())
	LoadExchanges(QTS_GW_CFG_FILE,QTS_GW_MANGER_ID_BASE+12,QTS_GW_LOG_KEY,GetGWPath())
	#QTS_CFG_KEY_BACKUP: index is 0 backup trrecord,index is 1 backup trposition ,index is 2 backup traccount,index is 3 backup gwworking,if no backup set BuildBackupFile(None)
	#[BuildBackupFile('trrecord'),BuildBackupFile('trposition'),BuildBackupFile('traccount'),BuildBackupFile('gwworking')]
	#[BuildBackupFile(None),BuildBackupFile(None),BuildBackupFile(None),BuildBackupFile(None)]	
	AppendPropertyForExchanges(QTS_GW_CFG_FILE,QTS_CFG_KEY_BACKUP,[BuildBackupFile(QTS_BACKUP_GW_TRADE_RECORD),BuildBackupFile(QTS_BACKUP_GW_TRADE_POSITION),BuildBackupFile(QTS_BACKUP_GW_TRADE_ACCOUNT),BuildBackupFile(QTS_BACKUP_GW_TRADE_WORKING)])
	AppendPropertyForExchanges(QTS_GW_CFG_FILE,QTS_CFG_KEY_LOADER,[QTS_LOADER_GW_TRADE_POSITION])
	#AppendPropertyForExchanges(QTS_GW_CFG_FILE,QTS_CFG_KEY_CHECKSECUID,QTS_FALSE)
	#//////////////////////////////////////////////////////////////////////////////
	PrintMessage('---------------------------------- end load qtsgw ----------------------------------------------')