from qtscommon import *
	
if GetIsMatch() :
	CreateUserPluginForExchange(1,[[SZ_MARKET,EQUIT_CATEGORY],[SH_MARKET,EQUIT_CATEGORY]],'','','QtsEquitMatch','CreateEquitMatch')
	#AppendPropertyForExchange(1,QTS_CFG_KEY_LOGMESSAGE,QTS_TRUE)
	#AppendPropertyForExchange(1,QTS_CFG_KEY_LOGDEBUG,QTS_TRUE)
	#AppendPropertyForExchange(1,QTS_CFG_KEY_LOGERROR,QTS_TRUE)
	#AppendPropertyForExchange(1,QTS_CFG_KEY_LOGWARNING,QTS_TRUE)		
	AppendPropertyForExchange(1,QTS_CFG_KEY_MATCH_MODE,qts_match_market)
	#AppendPropertyForExchange(1,QTS_CFG_KEY_MATCH_MODE,qts_match_auto)	
	#AppendPropertyForExchange(1,QTS_CFG_KEY_MATCH_MODE,qts_match_immediately)	
	AppendPropertyForExchange(1,QTS_CFG_KEY_CHECKS,[GetPluginIdForCheck(999)])	
	AppendPropertyForExchange(1,QTS_CFG_KEY_TESTMODE,qts_match_mode_common)
	AppendPropertyForExchange(1,QTS_CFG_KEY_TESTDELAY,1)
	AppendPropertyForExchange(1,QTS_CFG_KEY_TESTCOUNT,1)