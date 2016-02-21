from qtscommon import *

if GetAppMode() == QTS_APP_MODE_ALL or GetAppMode() == QTS_APP_MODE_SERVER :
	if GetRunVersion() == release :
		CreatePluginForDSTransfer(1,ALL_MARKET,BuildLocalCfg(QTS_DS_CFG_FILE,'CreateConfig','QtsPythonCfg',GetProtoPath(),GetProtoFile()),'QtsSS','CreateDSLocalForSS')
	else :
		CreatePluginForDSTransfer(1,ALL_MARKET,BuildLocalCfg(QTS_DS_CFG_FILE,'CreateConfig','QtsPythonDCfg',GetProtoPath(),GetProtoFile()),'QtsSS','CreateDSLocalForSS')