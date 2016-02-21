from qtscommon import *

if GetAppMode() == QTS_APP_MODE_SINGLE :
	CreatePluginForDSTransfer(1,ALL_MARKET,'','QtsGW','CreateDSRemoteForGW')
	SetRemoteInfoForDSTransfer(1,GetIPAddressForDS(1),GetIPPortForDS(1))