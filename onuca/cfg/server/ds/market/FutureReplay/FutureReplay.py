from qtscommon import *

if GetIsReplay() and GetReplayType() == sqlite :
	CreateUserPluginForMarket(2,[[ZJ_MARKET,IF_CATEGORY],[ZJ_MARKET,IC_CATEGORY],[ZJ_MARKET,IH_CATEGORY],[DL_MARKET,JD_CATEGORY]],'','','QtsFutureReplay','CreateFutureReplay')
	#AppendPropertyForMarket(2,QTS_CFG_KEY_LOGMESSAGE,QTS_TRUE)
	#AppendPropertyForMarket(2,QTS_CFG_KEY_LOGDEBUG,QTS_TRUE)
	#AppendPropertyForMarket(2,QTS_CFG_KEY_LOGERROR,QTS_TRUE)
	#AppendPropertyForMarket(2,QTS_CFG_KEY_LOGWARNING,QTS_TRUE)			
	AppendPropertyForMarket(2,QTS_CFG_KEY_DATA_PATH,GetReplayPath())
	AppendPropertyForMarket(2,QTS_CFG_KEY_BEGIN_DATE,GetMainDictForString(QTS_REPLAY_START_DATE))
	AppendPropertyForMarket(2,QTS_CFG_KEY_END_DATE,GetMainDictForString(QTS_REPLAY_END_DATE))
	AppendPropertyForMarket(2,QTS_CFG_KEY_BEGIN_TIME,GetMainDictForString(QTS_REPLAY_START_TIME))
	AppendPropertyForMarket(2,QTS_CFG_KEY_END_TIME,GetMainDictForString(QTS_REPLAY_END_TIME))
	AppendPropertyForMarket(2,'qts_speed',1)
	#AppendPropertyForMarket(2,'qts_waittime',500)