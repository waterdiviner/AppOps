from qtscommon import *

if GetAppMode() == QTS_APP_MODE_ALL or GetAppMode() == QTS_APP_MODE_SERVER :
	if GetRunVersion() == release :
		CreatePluginForGWTransfer(1,ALL_MARKET,BuildLocalCfg(QTS_GW_CFG_FILE,'CreateConfig','QtsPythonCfg',GetProtoPath(),GetProtoFile()),'QtsSS','CreateGWLocalForSS')
	else :
		CreatePluginForGWTransfer(1,ALL_MARKET,BuildLocalCfg(QTS_GW_CFG_FILE,'CreateConfig','QtsPythonDCfg',GetProtoPath(),GetProtoFile()),'QtsSS','CreateGWLocalForSS')