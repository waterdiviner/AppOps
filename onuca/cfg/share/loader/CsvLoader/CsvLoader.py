from qtscommon import *

if GetLoaderType() == xfile :
	CreatePluginForLoader(999,ALL_MARKET,'','QtsFileLoader','CreateFileLoader')
	AppendPropertyForLoader(999,QTS_CFG_KEY_CSVFLAG,QTS_CSV_FLAG)