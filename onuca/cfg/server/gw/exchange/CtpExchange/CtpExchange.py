from qtscommon import *

if not GetIsMatch() :
	CreateUserPluginForExchange(6,[[ZJ_MARKET,IF_CATEGORY],[ZJ_MARKET,IC_CATEGORY],[ZJ_MARKET,IH_CATEGORY],[DL_MARKET,JD_CATEGORY]],'','','QtsCtpExchange','CreateCtpExchange')
	#AppendPropertyForExchange(6,QTS_CFG_KEY_LOGMESSAGE,QTS_TRUE)
	#AppendPropertyForExchange(6,QTS_CFG_KEY_LOGDEBUG,QTS_TRUE)
	#AppendPropertyForExchange(6,QTS_CFG_KEY_LOGERROR,QTS_TRUE)
	#AppendPropertyForExchange(6,QTS_CFG_KEY_LOGWARNING,QTS_TRUE)	
	AppendPropertyForExchange(6,'address','tcp://115.238.106.253:41205')
	AppendPropertyForExchange(6,'brokerid','1008')
	AppendPropertyForExchange(6,'userid','90089827')
	AppendPropertyForExchange(6,'password','081037')	
	AppendPropertyForExchange(6,QTS_CFG_KEY_CHECKS,[GetPluginIdForCheck(999)])
	AppendPropertyForExchange(6,QTS_CFG_KEY_ALGOES,[GetPluginIdForAlgo(1)])	
	AppendPropertyForExchange(6,"logpath",BuildLogFile(None))	
	AppendPropertyForExchange(6,"qts_backupfile",BuildBackupFile('ctpexchange'))
	AppendPropertyForExchange(6,"qts_backupflag",QTS_CSV_FLAG)