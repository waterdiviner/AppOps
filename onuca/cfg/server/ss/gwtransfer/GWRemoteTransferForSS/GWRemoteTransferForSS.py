from qtscommon import *

if GetAppMode() == QTS_APP_MODE_SINGLE :
	CreatePluginForGWTransfer(2,ALL_MARKET,'','QtsSS','CreateGWRemoteForSS')
	SetRemoteInfoForGWTransfer(2,GetIPAddressForGW(1),GetIPPortForGW(1))