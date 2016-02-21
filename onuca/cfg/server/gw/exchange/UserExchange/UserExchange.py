from qtscommon import *

QTS_USER_GW_MANGER_ID_BASE = 150
QTS_USER_GW_LOG_NAME = 'qts_gwlog'

path = GetUserExchangePath()
if path != '' :
	LoadUserExchanges(QTS_USER_GW_MANGER_ID_BASE+1,QTS_USER_GW_LOG_NAME,path)