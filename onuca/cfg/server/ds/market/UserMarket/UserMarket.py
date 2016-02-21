from qtscommon import *

QTS_USER_DS_MANGER_ID_BASE = 250
QTS_USER_DS_LOG_NAME = 'qts_ssds'

path = GetUserMarketPath()
if path != '' :
	LoadUserMarkets(QTS_USER_DS_MANGER_ID_BASE+1,QTS_USER_DS_LOG_NAME,path)