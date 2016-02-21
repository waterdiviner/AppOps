from qtscommon import *

if GetIsSSMonitor() == QTS_MONITOR_BINARY or  GetIsSSMonitor() == QTS_MONITOR_BOTH :
	CreatePluginForMonitor(1,ALL_MARKET,'','QtsRMQPublisher','CreateRMQPublisher')
	AppendPropertyForMonitor(1,QTS_CFG_KEY_ADDRESS,'127.0.0.1')
	AppendPropertyForMonitor(1,QTS_CFG_KEY_PORT,'5672')
	AppendPropertyForMonitor(1,QTS_CFG_KEY_VIRTUALHOST,'/')
	AppendPropertyForMonitor(1,QTS_CFG_KEY_EXCHANGE,'e.qts.ss')
	AppendPropertyForMonitor(1,QTS_CFG_KEY_QUEUE,'q.qts.ss.binary')
	AppendPropertyForMonitor(1,QTS_CFG_KEY_ROUTINGKEY,'r.qts.ss.binary')
	AppendPropertyForMonitor(1,QTS_CFG_KEY_EXTYPE,'fanout')
	AppendPropertyForMonitor(1,QTS_CFG_KEY_USR,'guest')
	AppendPropertyForMonitor(1,QTS_CFG_KEY_PSW,'guest')
	#AppendPropertyForMonitor(2,QTS_CFG_KEY_FILTERS,QTS_NET_TYPE_ACK_REMOTE)