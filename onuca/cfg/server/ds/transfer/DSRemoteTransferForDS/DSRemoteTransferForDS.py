from qtscommon import *

if GetAppMode() == QTS_APP_MODE_SINGLE :
	CreatePluginForTransfer(1,ALL_MARKET,'','QtsDS','CreateDSRemoteForDS')
	SetRemoteInfoForTransfer(1,GetIPAddressForDS(1),GetIPPortForDS(1))