from qtscommon import *

if not GetIsMatch() :
	CreateUserPluginForExchange(7,[[SH_MARKET,EQUIT_CATEGORY],[SZ_MARKET,EQUIT_CATEGORY]],'','','QtsCtpSSEExchange','CreateCtpSSEExchange')
	#AppendPropertyForExchange(7,QTS_CFG_KEY_LOGMESSAGE,QTS_TRUE)
	#AppendPropertyForExchange(7,QTS_CFG_KEY_LOGDEBUG,QTS_TRUE)
	#AppendPropertyForExchange(7,QTS_CFG_KEY_LOGERROR,QTS_TRUE)
	#AppendPropertyForExchange(7,QTS_CFG_KEY_LOGWARNING,QTS_TRUE)		
	AppendPropertyForExchange(7,'address','tcp://180.166.11.40:41205')
	AppendPropertyForExchange(7,'brokerid','2011')
	AppendPropertyForExchange(7,'userid','20000510')
	AppendPropertyForExchange(7,'password','155001')	
	AppendPropertyForExchange(7,QTS_CFG_KEY_CHECKS,[GetPluginIdForCheck(999)])
	AppendPropertyForExchange(7,QTS_CFG_KEY_ALGOES,[GetPluginIdForAlgo(1)])	
	AppendPropertyForExchange(7,"logpath",BuildLogFile(None))	
	AppendPropertyForExchange(7,"qts_backupfile",BuildBackupFile('ctpsseexchange'))
	AppendPropertyForExchange(7,"qts_backupflag",QTS_CSV_FLAG)