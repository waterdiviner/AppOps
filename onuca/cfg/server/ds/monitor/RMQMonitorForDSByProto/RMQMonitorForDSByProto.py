from qtscommon import *

if GetIsDSMonitor() == QTS_MONITOR_PROTOBUF or GetIsDSMonitor() == QTS_MONITOR_BOTH :
	CreatePluginForMonitor(2,ALL_MARKET,'','QtsRMQProPublisher','CreateRMQProPublisher')
	AppendPropertyForMonitor(2,QTS_CFG_KEY_ADDRESS,'127.0.0.2')
	AppendPropertyForMonitor(2,QTS_CFG_KEY_PORT,'5672')
	AppendPropertyForMonitor(2,QTS_CFG_KEY_VIRTUALHOST,'/')
	AppendPropertyForMonitor(2,QTS_CFG_KEY_EXCHANGE,'e.qts.ds')
	AppendPropertyForMonitor(2,QTS_CFG_KEY_QUEUE,'q.qts.ds.proto')
	AppendPropertyForMonitor(2,QTS_CFG_KEY_ROUTINGKEY,'r.qts.ds.proto')
	AppendPropertyForMonitor(2,QTS_CFG_KEY_EXTYPE,'fanout')
	AppendPropertyForMonitor(2,QTS_CFG_KEY_USR,'guest')
	AppendPropertyForMonitor(2,QTS_CFG_KEY_PSW,'guest')
	AppendPropertyForMonitor(2,QTS_CFG_KEY_PROTOPATH,GetProtoPath())
	AppendPropertyForMonitor(2,QTS_CFG_KEY_PROTOFILE,GetProtoFile())	
	#AppendPropertyForMonitor(2,QTS_CFG_KEY_FILTERS,QTS_NET_TYPE_ACK_REMOTE)
	