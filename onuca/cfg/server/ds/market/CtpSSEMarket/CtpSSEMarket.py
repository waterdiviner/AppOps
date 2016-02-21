from qtscommon import *

if not GetIsReplay() :
	CreateUserPluginForMarket(7,[[SH_MARKET,EQUIT_CATEGORY],[SZ_MARKET,EQUIT_CATEGORY]],'','','QtsCtpSSEMarket','CreateCtpSSEMarket')
	#AppendPropertyForMarket(7,QTS_CFG_KEY_LOGMESSAGE,QTS_TRUE)
	#AppendPropertyForMarket(7,QTS_CFG_KEY_LOGDEBUG,QTS_TRUE)
	#AppendPropertyForMarket(7,QTS_CFG_KEY_LOGERROR,QTS_TRUE)
	#AppendPropertyForMarket(7,QTS_CFG_KEY_LOGWARNING,QTS_TRUE)			
	AppendPropertyForMarket(7,'address','tcp://180.166.11.40:41213')
	AppendPropertyForMarket(7,'brokerid','2011')
	AppendPropertyForMarket(7,'userid','20000510')
	AppendPropertyForMarket(7,'password','155001')
	AppendPropertyForMarket(7,"logpath",BuildLogFile(None))