#coding=utf-8

########################################################
#操作系统类型
#EQtsSystemType
(
windows,		#windows操作系统
linux			#linux和unix操作系统
)=(0,1)

########################################################
#系统版本
#EQtsVersionType
(
release,			#非测试版
debug,				#测试版
publish				#发布版
)=(0,1,3)

########################################################
#加载器或备份器的类型
#EQtsLoaderType
#EQtsBackupType
(
qts_all_file,   #所有文件
xfile,			#文本文件
bfile,			#二进制文件
sqlite,			#sqlite 数据库
mysql,			#mysql 数据库
xml,			#xml 文件
json,			#json 文件
mixplugin,		#混合模式
sqlite_data		#market data
)=(0,1,2,3,4,5,6,7,8)

########################################################
#风控检查是否打开或关闭
#EQtsRiskSwitchType
(
check_off,			#关闭
check_on			#打开
)=(0,1)

########################################################
#配置的布尔值
#EQtsBoolType
(
QTS_FALSE,			#是
QTS_TRUE			#否
)=(0,1)

########################################################
#配置的布尔值
#EQtsReplayMode
(
QTS_REPLAY_MODE_COMMON,			#正常回放，检查时间，按时间回放
QTS_REPLAY_MODE_INDEX,			#不检查时间，按顺序回放
QTS_REPLAY_MODE_STEP			#一步一步回放
)=(0,1,2)

########################################################
#策略参数类型
#EQtsParameterType
(
PARA_INSTRUMENT,			#交易标的
PARA_PARAMETER,				#可变参数
PARA_COMMENT,				#静态参数
PARA_COMMAND				#命令参数
)=(0,1,2,3)

########################################################
#策略状态
#EQtsStrategyStatus
(
STRATEGY_STATUS_START,   #运行状态
STRATEGY_STATUS_PAUSE,   #暂停状态
STRATEGY_STATUS_WATCH,   #观察状态
STRATEGY_STATUS_STOP    #停止状态
)=(0,1,2,3)

########################################################
#交易标的类型
#EQtsTradeCodeType
(
QTS_TRADE_UNKONWN,			#未知
QTS_TRADE_CODE,				#交易代码
QTS_TRADE_SIGNAL,			#交易信息
QTS_TRADE_BASKET,			#交易篮子
QTS_TRADE_INDEX,			#指数
QTS_TRADE_OWNER				#自定义
)=(0,1,2,3,4,5)

########################################################
#策略参数控件类型	
#EQtsComponentType
(
QTS_COMPONENT_TEXTBOX,					#文本框
QTS_COMPONENT_COMBOX,					#下拉框
QTS_COMPONENT_COMMONTBUTTON,			#非确认按扭
QTS_COMPONENT_CONFIRMBUTTON,			#确认按钮
QTS_COMPONENT_LABEL						#标签
)=(0,1,2,3,4)

########################################################	
#控件状态	
#EQtsComponentStatus
(
QTS_DISABLE,			#禁止
QTS_ENABLE				#激活
)=(0,1)

########################################################
#交易标的对于终端的显示类型，这个主要来控制交易标的
#的盈亏、订单本和在途信息，策略服务是否发送给终端，
#以减轻网络压力
#EQtsInstrumentMode
(
QTS_INSTRUMENT_MODE_NONE,			#任何都不发送
QTS_INSTRUMENT_MODE_ALL,			#发送所有的信息
QTS_INSTRUMENT_MODE_PNL,			#仅发送盈亏数据
QTS_INSTRUMENT_MODE_BOOK,			#仅发送订单本数据
QTS_INSTRUMENT_MODE_WORKING,		#仅发送在途信息数据
QTS_INSTRUMENT_MODE_BP,				#发送订单本和盈亏数据
QTS_INSTRUMENT_MODE_BW,				#发送订单本和在途信息数据
QTS_INSTRUMENT_MODE_PW				#发送盈亏和在途信息数据
)=(
0,1,2,3,4,5,6,7
)

########################################################
#交易标的状态类型，是指交易标的，是否显示在策略监控面板上
#EQtsInstrumentStatus
(
QTS_INSTRUMENT_STATUS_HIDE,			#隐藏
QTS_INSTRUMENT_STATUS_DISPLAY		#显示
)=(0,1)

########################################################
#应用程序类型
#EQtsAppType
(
QTS_APP_GUI,			#终端类型
QTS_APP_DS,				#数据服务
QTS_APP_GW,				#通道服务
QTS_APP_SS,				#策略服务
QTS_APP_CONVERT,		#backup转换工具
QTS_APP_QUERY,			#查询工具
QTS_APP_DC				#数据落盘服务
)=(0,1,2,3,4,5,6)

########################################################
#应用程序部署类型
#EQtsAppMode
(
QTS_APP_MODE_ALL,			#全集成部署
QTS_APP_MODE_SERVER,		#服务集成部署
QTS_APP_MODE_SINGLE			#独立部署
)=(0,1,2)

########################################################
#撮合器类型
#EQtsMatchMode
(
qts_match_auto,				#线程撮合
qts_match_market,			#行情撮合
qts_match_immediately,		#立即撮合
qts_match_manual			#手动撮合
)=(0,1,2,3)


(
qts_match_mode_common,
qts_match_mode_noack,
qts_match_mode_ack,
qts_match_mode_part_dealed,
qts_match_mode_dealed,
qts_match_mode_part_denled
)=(0,1,2,3,4,5)
	
########################################################
#监控协议类型
#EQtsMonitorType
(
QTS_MONITOR_NONE,				#无监控
QTS_MONITOR_BINARY,				#仅自有协议
QTS_MONITOR_PROTOBUF,			#PROTO BUF协议
QTS_MONITOR_BOTH				#同时两种协议
)=(0,1,2,3)

########################################################
#下单价格类型
#EQtsPriceType
(
QTS_PRICE_TYPE_UNKNOWN,				#未知
QTS_PRICE_TYPE_PASSIVE,				#被动单
QTS_PRICE_TYPE_ACTIVE				#主动单
)=(0,1,2)

########################################################
#下单拆单类型
#EQtsSplitType
(
QTS_SPLIT_TYPE_NONE,				#无
QTS_SPLIT_TYPE_EQUAL,				#等量
QTS_SPLIT_TYPE_RANDOM				#随机
)=(0,1,2)

########################################################
QTS_NET_TYPE_BASE=10000
#消息事件主类型
#EQtsNetEventType
(
QTS_NET_TYPE_ACK_MESSAGE,			#消息事件
QTS_NET_TYPE_PUSH_DATA,				#数据事件
QTS_NET_TYPE_ACK_ERROR,				#错误事件
QTS_NET_TYPE_ACK_ACCOUNT,			#帐户事件
QTS_NET_TYPE_ACK_POSITION,			#仓位事件
QTS_NET_TYPE_ACK_RECORD,			#订单事件
QTS_NET_TYPE_ACK_PNL,				#盈亏事件
QTS_NET_TYPE_ACK_BOOK,				#订单本事件
QTS_NET_TYPE_ACK_PARAMETER,			#策略参数事件
QTS_NET_TYPE_ACK_CONTROL,			#策略控制事件
QTS_NET_TYPE_ACK_STRATEGY,			#策略事件
QTS_NET_TYPE_ACK_WORKING,			#在途信息事件
QTS_NET_TYPE_ACK_REMOTE,			#远程信息事件
QTS_NET_TYPE_ACK_EVENT,				#用户事件
QTS_NET_TYPE_ACK_MONITOR			#监控事件
)=(
QTS_NET_TYPE_BASE + 1000,
QTS_NET_TYPE_BASE + 1014,
QTS_NET_TYPE_BASE + 1015,
QTS_NET_TYPE_BASE + 1017,
QTS_NET_TYPE_BASE + 1018,
QTS_NET_TYPE_BASE + 1022,
QTS_NET_TYPE_BASE + 1024,
QTS_NET_TYPE_BASE + 1026,
QTS_NET_TYPE_BASE + 1029,
QTS_NET_TYPE_BASE + 1032,
QTS_NET_TYPE_BASE + 1034,
QTS_NET_TYPE_BASE + 1036,
QTS_NET_TYPE_BASE + 1038,
QTS_NET_TYPE_BASE + 1039,
QTS_NET_TYPE_BASE + 1043
)

########################################################
#消息事件子类型
#EQtsNetEventSubType
(
QTS_NET_SUB_TYPE_ACK_ACCOUNT_DATA,			#帐户数据事件
QTS_NET_SUB_TYPE_ACK_POSITION_DATA,			#仓位数据事件
QTS_NET_SUB_TYPE_ACK_PARAMETER_INIT,		#策略参数初始化事件
QTS_NET_SUB_TYPE_ACK_PARAMETER_VALUE,		#策略参数值更新事件
QTS_NET_SUB_TYPE_ACK_PARAMETER_STYLE		#策略参数状态更新事件
)=(
0,0,0,1,2
)


