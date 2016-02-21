#coding=utf-8
############################################
#本文件是行情系统的入口置文件，用QGOnuca应用程序起动，
#通过相同名称的后缀名为.qts的配置导入，配置节点是
#QTS_ENTRY_CFG，请参看main_*.qts
#这个文件能由QGOnuca应用程序起动
############################################
from entry import *

#*******************************************************************************
#初始化运行环境，参数是入口配置模块
#参数1：设置缺省的主模块
#参数2：设置应用程序的类型，参看qts_security.py中的定义
#参数3：设置应用程序的版本，release、debug和publish,定义参看qts_security.py中的定义
#参数4：设置程序运行的版本，release和debug，定义参看qts_security.py中的定义，
#		这个主要是用来指定python策略的启动方式，如果是QGOnuca应用程序起动时，
#		则设为release，如果是由python启动，则设为debug
#参数5：设置是否支持回放
#参数6：设置是否支持撮合
#参数7：设置是否支持行情服务的监控,QTS_MONITOR_NONE,QTS_MONITOR_BINARY,QTS_MONITOR_PROTOBUF,QTS_MONITOR_BOTH,定义参看qts_security.py中的定义
#参数8：设置是否支持下单通道服服的监控,QTS_MONITOR_NONE,QTS_MONITOR_BINARY,QTS_MONITOR_PROTOBUF,QTS_MONITOR_BOTH,定义参看qts_security.py中的定义
#参数9：设置是否支持策略服务的监控,QTS_MONITOR_NONE,QTS_MONITOR_BINARY,QTS_MONITOR_PROTOBUF,QTS_MONITOR_BOTH,定义参看qts_security.py中的定义
#参数9：设置是否支持GUI的监控,QTS_MONITOR_NONE,QTS_MONITOR_BINARY,QTS_MONITOR_PROTOBUF,QTS_MONITOR_BOTH,定义参看qts_security.py中的定义
#参数10：如果是python启动的环境，则要先设置程序的配置的根目录
#参数11：如果是python启动的环境，则要回放数据的根目录
InitRunEnv(QTS_GW_CFG_FILE,QTS_APP_MODE_SINGLE,QTS_APP_PY_VERSION,release,True,False,QTS_MONITOR_NONE,QTS_MONITOR_NONE,QTS_MONITOR_NONE,
		QTS_MONITOR_NONE,loadertype=QTS_LOADER_TYPE,backuptype=QTS_BACKUP_TYPE,replaytype=QTS_REPLAY_TYPE)
#设置是否打印所有的python输出
SetIsPrint(False)
#初始化测试环境，这个仅用在用vs编译的程序，因vs会主动增加Debug和Release目录，
#这个仅对平台测试用，用户不应打开这个
InitTestEnv()
#设置用户通道插件的根目录，如果用户通道没有放到server/gw/exchange下面。
SetUserExchangePath('')
#*******************************************************************************

#*******************************************************************************
#用户变量自定义区，回放时间定义

#终端网络联结信息
SetIPAddressForDS(1,'127.0.0.1')
SetIPPortForDS(1,10000)

SetIPAddressForGW(1,'127.0.0.1')
SetIPPortForGW(1,12000)
#*******************************************************************************

#*******************************************************************************
#模块导入
sys.path.append('{0}/cfg/server/gw'.format(GetBasePath()))
from qtsgw import *
#*******************************************************************************
