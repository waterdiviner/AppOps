from qtscommon import *

QTS_USER_STRATEGY_MANGER_ID_BASE = 350
QTS_USER_STRATEGY_LOG_NAME = 'qts_sslog'

path = GetUserStrategyPath()
if path != '' :
	LoadUserStrategies(QTS_USER_STRATEGY_MANGER_ID_BASE+1,QTS_USER_STRATEGY_LOG_NAME,path)