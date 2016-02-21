from qtscommon import *

if GetIsMatch() :
	CreateUserPluginForExchange(2,[[ZJ_MARKET,IF_CATEGORY],[ZJ_MARKET,IC_CATEGORY],[ZJ_MARKET,IH_CATEGORY],[DL_MARKET,JD_CATEGORY]],'','','QtsFutureMatch','CreateFutureMatch')
	#AppendPropertyForExchange(2,QTS_CFG_KEY_LOGMESSAGE,QTS_TRUE)
	#AppendPropertyForExchange(2,QTS_CFG_KEY_LOGDEBUG,QTS_TRUE)
	#AppendPropertyForExchange(2,QTS_CFG_KEY_LOGERROR,QTS_TRUE)
	#AppendPropertyForExchange(2,QTS_CFG_KEY_LOGWARNING,QTS_TRUE)	
	AppendPropertyForExchange(2,QTS_CFG_KEY_MATCH_MODE,qts_match_market)
	#AppendPropertyForExchange(2,QTS_CFG_KEY_MATCH_MODE,qts_match_auto)	
	#AppendPropertyForExchange(2,QTS_CFG_KEY_MATCH_MODE,qts_match_immediately)		
	AppendPropertyForExchange(2,QTS_CFG_KEY_CHECKS,[GetPluginIdForCheck(999)])
	AppendPropertyForExchange(2,QTS_CFG_KEY_ALGOES,[GetPluginIdForAlgo(1)])	
	AppendPropertyForExchange(2,QTS_CFG_KEY_TESTMODE,qts_match_mode_common)
	AppendPropertyForExchange(2,QTS_CFG_KEY_TESTDELAY,1)
	AppendPropertyForExchange(2,QTS_CFG_KEY_TESTCOUNT,1)	