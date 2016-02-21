from qtscommon import *

if not GetIsReplay() :
	CreateUserPluginForMarket(6,[[ZJ_MARKET,IF_CATEGORY],[ZJ_MARKET,IC_CATEGORY],[ZJ_MARKET,IH_CATEGORY],[DL_MARKET,JD_CATEGORY]],'','','QtsCtpMarket','CreateCtpMarket')
	#AppendPropertyForMarket(6,QTS_CFG_KEY_LOGMESSAGE,QTS_TRUE)
	#AppendPropertyForMarket(6,QTS_CFG_KEY_LOGDEBUG,QTS_TRUE)
	#AppendPropertyForMarket(6,QTS_CFG_KEY_LOGERROR,QTS_TRUE)
	#AppendPropertyForMarket(6,QTS_CFG_KEY_LOGWARNING,QTS_TRUE)		
	AppendPropertyForMarket(6,'address','tcp://115.238.106.253:41213')
	AppendPropertyForMarket(6,'brokerid','1008')
	AppendPropertyForMarket(6,'userid','90089827')
	AppendPropertyForMarket(6,'password','081037')
	AppendPropertyForMarket(6,"logpath",BuildLogFile(None))