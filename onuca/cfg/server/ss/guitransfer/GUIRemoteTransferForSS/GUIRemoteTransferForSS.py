from qtscommon import *

if GetAppMode() == QTS_APP_MODE_SINGLE or GetAppMode() == QTS_APP_MODE_SERVER:
	CreatePluginForGUITransfer(2,ALL_MARKET,'','QtsSS','CreateGUIRemoteForSS')
	SetRemoteInfoForGUITransfer(2,GetIPAddressForGUI(1),GetIPPortForGUI(1))