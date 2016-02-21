from qtscommon import *

if GetIsReplay() and GetReplayType() == sqlite :
	CreateUserPluginForMarket(1,[[SH_MARKET,EQUIT_CATEGORY],[SZ_MARKET,EQUIT_CATEGORY]],'','','QtsEquitReplay','CreateEquitReplay')
	#AppendPropertyForMarket(1,QTS_CFG_KEY_LOGMESSAGE,QTS_TRUE)
	#AppendPropertyForMarket(1,QTS_CFG_KEY_LOGDEBUG,QTS_TRUE)
	#AppendPropertyForMarket(1,QTS_CFG_KEY_LOGERROR,QTS_TRUE)
	#AppendPropertyForMarket(1,QTS_CFG_KEY_LOGWARNING,QTS_TRUE)		
	AppendPropertyForMarket(1,QTS_CFG_KEY_DATA_PATH,GetReplayPath())
	AppendPropertyForMarket(1,QTS_CFG_KEY_BEGIN_DATE,GetMainDictForString(QTS_REPLAY_START_DATE))
	AppendPropertyForMarket(1,QTS_CFG_KEY_END_DATE,GetMainDictForString(QTS_REPLAY_END_DATE))
	AppendPropertyForMarket(1,QTS_CFG_KEY_BEGIN_TIME,GetMainDictForString(QTS_REPLAY_START_TIME))
	AppendPropertyForMarket(1,QTS_CFG_KEY_END_TIME,GetMainDictForString(QTS_REPLAY_END_TIME))
	AppendPropertyForMarket(1,'qts_speed',1)
	#AppendPropertyForMarket(1,'qts_waittime',3000)