from qtscommon import *

if GetAppMode() == QTS_APP_MODE_ALL :
	if GetRunVersion() == release :
		CreatePluginForGUITransfer(1,ALL_MARKET,BuildLocalCfg(QTS_SS_CFG_FILE,'CreateConfig','QtsPythonCfg',GetProtoPath(),GetProtoFile()),'QtsGUI','CreateGUILocalForGUI')
	else :
		CreatePluginForGUITransfer(1,ALL_MARKET,BuildLocalCfg(QTS_SS_CFG_FILE,'CreateConfig','QtsPythonDCfg',GetProtoPath(),GetProtoFile()),'QtsGUI','CreateGUILocalForGUI')	