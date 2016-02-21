#coding=utf-8
from qtscommon import *

CreateUserPluginForCStrategy(5,ALL_MARKET,'','qtsfuturetestcfg','QtsFutureTest','CreateFutureTest',)
SetPluginNameForPyStrategy(5,'FutureTest')
AppendPropertyForStrategy(5,QTS_CFG_KEY_TASK,2)
AppendPropertyForStrategy(5,QTS_CFG_KEY_ACCOUNT,BuildAccount(55550000456))
AppendPropertyForStrategy(5,QTS_CFG_KEY_MINORDERID,BuildOrderId(5,0))
AppendPropertyForStrategy(5,QTS_CFG_KEY_MAXORDERID,BuildOrderId(5,99999999))
AppendPropertyForStrategy(5,QTS_CFG_KEY_ORDERIDSTEP,1)
AppendPropertyForStrategy(5,QTS_CFG_KEY_STATUS,3)
AppendPropertyForStrategy(5,QTS_CFG_KEY_PARAMETERSAVE,QTS_TRUE)
SetParameterForStrategy(5,'FutureTest')
AppendPropertyForStrategy(5,QTS_CFG_KEY_CHECKS,[GetPluginIdForCheck(999)])
AppendPropertyForStrategy(5,QTS_CFG_KEY_CALCULATES,[GetPluginIdForCalculate(1)])
