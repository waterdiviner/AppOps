from qtscommon import *

if GetAppMode() == QTS_APP_MODE_SINGLE :
	CreatePluginForGUITransfer(2,ALL_MARKET,'','QtsGUI','CreateGUIRemoteForGUI')
	SetRemoteInfoForGUITransfer(2,GetIPAddressForGUI(1),GetIPPortForGUI(1))