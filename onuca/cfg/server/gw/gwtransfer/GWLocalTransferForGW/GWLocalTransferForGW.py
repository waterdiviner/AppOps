from qtscommon import *

if GetAppMode() == QTS_APP_MODE_ALL or GetAppMode() == QTS_APP_MODE_SERVER :
	CreatePluginForGWTransfer(1,ALL_MARKET,'','QtsGW','CreateGWLocalForGW')