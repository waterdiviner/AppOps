#coding=utf-8
from qtscommon import *
#///////////////////////////////////////////////////////////////////////////////////
QTS_CONFIG_TRADE_PREFIX = 'FutureTest'
InitCfgEnv(QTS_SS_CFG_FILE,QTS_CONFIG_TRADE_PREFIX)
#///////////////////////////////////////////////////////////////////////////////////
CreateInstruments(QTS_CONFIG_TRADE_PREFIX)
CreateParameters(QTS_CONFIG_TRADE_PREFIX)
CreateComments(QTS_CONFIG_TRADE_PREFIX)
CreateCommands(QTS_CONFIG_TRADE_PREFIX)
#///////////////////////////////////////////////////////////////////////////////////

#///////////////////////////////////////////////////////////////////////////////////
#add code
#要交易的标的，现暂时支持一个交易代码
CreateInstrument(QTS_CONFIG_TRADE_PREFIX,100,'TradeCode',QTS_TRADE_CODE,ZJ_MARKET,IF_CATEGORY,1509,0,mode=QTS_INSTRUMENT_MODE_BP)

#///////////////////////////////////////////////////////////////////////////////////
#可修改参数
#///////////////////////////////////////////////////////////////////////////////////
#最大亏损
CreateParameter(QTS_CONFIG_TRADE_PREFIX,200,'下单量',1,0,1,save=QTS_TRUE)
#最大亏损
CreateParameter(QTS_CONFIG_TRADE_PREFIX,201,'最大亏损',10000,2,2,save=QTS_TRUE)
#最大回撤
CreateParameter(QTS_CONFIG_TRADE_PREFIX,202,'最大回撤',5000,2,3,save=QTS_TRUE)
#清仓时间
CreateParameter(QTS_CONFIG_TRADE_PREFIX,203,'清仓时间',150000,0,4,save=QTS_TRUE)
#主动单多少层
CreateParameter(QTS_CONFIG_TRADE_PREFIX,204,'是否自动',1,0,5,save=QTS_TRUE,mode=QTS_COMPONENT_COMBOX,component='0:手工,1:自动')
#///////////////////////////////////////////////////////////////////////////////////
#不可修改参数
#///////////////////////////////////////////////////////////////////////////////////
CreateComment(QTS_CONFIG_TRADE_PREFIX,300,'当前盈亏',0,2,1)
CreateComment(QTS_CONFIG_TRADE_PREFIX,301,'最大盈利',0,2,2)
CreateComment(QTS_CONFIG_TRADE_PREFIX,302,'当前回撤',0,2,3)
CreateComment(QTS_CONFIG_TRADE_PREFIX,303,'当前市价',0,2,4)
CreateComment(QTS_CONFIG_TRADE_PREFIX,304,'交易均价',0,2,5)
CreateComment(QTS_CONFIG_TRADE_PREFIX,305,'当前仓位',0,0,6)
CreateComment(QTS_CONFIG_TRADE_PREFIX,306,'盈亏资金',0,0,7)

#///////////////////////////////////////////////////////////////////////////////////
#命令参数
#///////////////////////////////////////////////////////////////////////////////////
#买入交易标的
CreateCommand(QTS_CONFIG_TRADE_PREFIX,400,'买入',1,mode=QTS_COMPONENT_CONFIRMBUTTON,component='是否买入')
#卖出交易标的
CreateCommand(QTS_CONFIG_TRADE_PREFIX,401,'卖出',2,mode=QTS_COMPONENT_CONFIRMBUTTON,component='是否卖出')
#清仓交易标的
CreateCommand(QTS_CONFIG_TRADE_PREFIX,402,'清空',3,mode=QTS_COMPONENT_CONFIRMBUTTON,component='是否清仓')
#重置清仓状态
CreateCommand(QTS_CONFIG_TRADE_PREFIX,403,'重置',4,mode=QTS_COMPONENT_CONFIRMBUTTON,component='是否重置')
#///////////////////////////////////////////////////////////////////////////////////