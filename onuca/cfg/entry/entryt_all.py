#coding=utf-8
############################################
#本文件是合体版系统的入口置文件，有两种途径应用本入口，
#如果是用QGOnuca应用程序起动，则是通过相同名称的后缀名为
#.qts的配置导入，配置节点是QTS_ENTRY_CFG，请参看main_*.qts
#文件，这个文件由QGOnuca应用程序起动时参数传入。另一程方式
#是通过python应用程序直接执行，但这种模式是用来调试python
#策略，当用这种方式启动时，SetRunVersion，参数是debug模式。
#这个文件能由QGOnuca应用程序起动
############################################
from entryt import *

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
InitRunEnv(QTS_GUI_CFG_FILE,QTS_APP_MODE_ALL,QTS_APP_PY_VERSION,release,True,True,QTS_MONITOR_NONE,QTS_MONITOR_NONE,QTS_MONITOR_NONE,
	QTS_MONITOR_NONE,loadertype=QTS_LOADER_TYPE,backuptype=QTS_BACKUP_TYPE,replaytype=QTS_REPLAY_TYPE)
#设置是否打印所有的python输出
SetIsPrint(False)
#初始化测试环境，这个仅用在用vs编译的程序，因vs会主动增加Debug和Release目录，
#这个仅对平台测试用，用户不应打开这个
InitTestEnv()
#设置用户策略的根目录，如果用户策略没有放到server/ss/strategy下面。
SetUserStrategyPath('')
#设置用户行情插件的根目录，如果用户插件没有放到server/ds/market下面。
SetUserMarketPath('')
#设置用户通道插件的根目录，如果用户通道没有放到server/gw/exchange下面。
SetUserExchangePath('')
#*******************************************************************************

#*******************************************************************************
#用户变量自定义区，回放时间定义
SetVarInMainDict(QTS_REPLAY_START_DATE,'20150630')
SetVarInMainDict(QTS_REPLAY_END_DATE,'20150630')
SetVarInMainDict(QTS_REPLAY_START_TIME,'093000000')
SetVarInMainDict(QTS_REPLAY_END_TIME,'150000000')
#*******************************************************************************

#*******************************************************************************
#模块导入
sys.path.append('{0}/console/gui'.format(GetCfgPath()))
sys.path.append('{0}/server/ds'.format(GetCfgPath()))
sys.path.append('{0}/server/gw'.format(GetCfgPath()))
sys.path.append('{0}/server/ss'.format(GetCfgPath()))
from qtsgui import *
from qtsss import *
from qtsgw import *
from qtsds import *
#******************************************************************************



