#coding=utf-8
#########################################################
#@brief  策略的基类，所有策略必须继承这个类
#@file qtsusertrade.py
#@note 所有的与结要参考qtsgoogleproto.proto文件
#########################################################

from qtstradeproto import *
from qtsmain import *
from qtsmaind import *

#/////////////////////////////////////////////////////////////////#		
class IQtsTrade(object) :
	def __init__(self) :
		RegisterTrade(self)
		
	##############################
	#@brief 设置父类管理器，用户不可用
	#@param parent 上层父管理器
	#@param strategyid 策略ID
	#@note 警告：用户一定不能使用此函数，会造成严重问题
	##############################	
	def SetParent(self,parent,srategyid) :
		self.parent=parent
		self.strategyid=srategyid
	
	##############################
	#@brief 得到主交易管理器
	#@return 主交易管理器
	#@note 警告：用户不可用
	##############################		
	def MainTrade(self) :
		return self.parent
		
	##############################
	#@brief 得到策略的ID
	#@return 策略的ID
	##############################
	def StrategyId(self) :
		return self.strategyid
		
	##############################
	#@brief 策略初始化事件，用户策略可继承
	##############################
	def Init(self) : pass
		
	##############################
	#@brief 策略一个循环的开始事件，用户策略可继承
	##############################		
	def OnCycling(self) : pass
			
	##############################
	#@brief 策略一个循环的结束事件，用户策略可继承
	##############################				
	def OnCycled(self) : pass
		
	##############################
	#@brief 策略事务的开始事件，用户策略可继承
	##############################		
	def OnUpdating(self) : pass	
		
	##############################
	#@brief 策略事务的结束事件，用户策略可继承
	##############################			
	def OnUpdated(self) : pass
	
	##############################
	#@brief 策略事务的开始事件，用户策略可继承
	##############################		
	def OnCommiting(self) : pass	
		
	##############################
	#@brief 策略事务的结束事件，用户策略可继承
	##############################			
	def OnCommited(self) : pass
			
	##############################
	#@brief 策略开始事件，用户策略可继承
	##############################			
	def OnStart(self) : pass
		
	##############################
	#@brief 策略暂停事件，用户策略可继承
	##############################	
	def OnPause(self) : pass
		
	##############################
	#@brief 策略观察事件，用户策略可继承
	##############################		
	def OnWatch(self) : pass
		
	##############################
	#@brief 策略停止事件，用户策略可继承
	##############################			
	def OnStop(self) : pass
		
	##############################
	#@brief 策略错误事件，用户策略可继承
	#@param errinfo 错误信息，QtsGProtoMessage结构，在qtsgoogleproto.proto文件中定义
	#@see QtsGProtoMessage
	##############################			
	def OnError(self,errinfo) : pass
		
	##############################
	#@brief 策略参数更新事件，用户策略可继承
	#@param parameter 参数信息，QtsGProtoParameter结构，在qtsgoogleproto.proto文件中定义
	#@see QtsGProtoParameter
	##############################			
	def OnParameter(self,parameter) : pass
		
	##############################
	#@brief 策略订单回报事件，用户策略可继承
	#@param result 订单回报信息，QtsGProtoReturn结构，在qtsgoogleproto.proto文件中定义
	#@see QtsGProtoReturn
	##############################			
	def OnReturn(self,result) : pass
		
	##############################
	#@brief 策略订单回报事件，用户策略可继承
	#@param result 订单回报信息，QtsGProtoReturn结构，在qtsgoogleproto.proto文件中定义
	#@see QtsGProtoReturn
	##############################			
	def OnReturns(self,results) : pass
	
	##############################
	#@brief 策略行情数据事件，用户策略可继承
	#@param market 行情数据信息，QtsGProtoData结构，在qtsgoogleproto.proto文件中定义
	#@see QtsGProtoData		
	def OnData(self,market) : pass

	##############################
	#@brief 策略行情数据事件，用户策略可继承
	#@param market 行情数据信息，QtsGProtoData结构，在qtsgoogleproto.proto文件中定义
	#@see QtsGProtoData		
	def OnDatas(self,markets) : pass
	
	##############################
	#@brief 策略收到GUI属性页事件会引发此事件，用户策略可继承
	#@param itype	用户命令
	#@param pro     协议
	#@param data    数据
	#@param size    大小
	#@see AckEvent
	#@note 每个策略都可以有一个或多个自定的属性页，属性页和策略之前可以通信，策略发属性页数据的函数是AckEvent
	##############################		
	def OnEvent(self,itype,pro,data,size) : pass
	
	##############################
	#@brief 得到市场值
	#@param icode 交易标的
	#@return 市场值
	##############################		
	def GetMarket(self,icode) :
		return qts_GetMarket(icode)
		
	##############################
	#@brief 得到品种值
	#@param icode 交易标的
	#@return 品种值
	##############################			
	def GetCategory(self,icode) :
		return qts_GetCategory(icode)
		
	##############################
	#@brief 得到证券代码
	#@param icode 交易标的
	#@return 证券代码
	##############################			
	def GetSecuCode(self,icode) :
		return qts_GetSecuCode(icode)
		
	##############################
	#@brief 创建交易标的
	#@param market 市场值
	#@param category 品种值
	#@param icode 证券代码
	#@return 交易标的
	##############################			
	def CreateCode(self,market,category,icode) :
		return qts_CreateCode(market,category,icode)
		
	##############################
	#@brief 设置是否支持手动下单
	#@param ismanual 是否支持手动下单，1是支持，0是不支持
	#@return 证券代码
	##############################			
	def SetManualTrade(self,ismanual) :	
		return qts_SetManualTrade(self.StrategyId(),ismanual)
		
	##############################
	#@brief 获得策略所支持帐户数目
	#@return 帐户数目
	##############################		
	def AccountSize(self) :
		return qts_AccountSize(self.StrategyId())
		
	##############################
	#@brief 获得指定的帐户
	#@param index 帐户序号
	#@return 帐户
	##############################			
	def Account(self,index = 0) :
		return qts_Account(self.StrategyId(),index)
		
	##############################
	#@brief 获得策略的循环周期
	#@return 循环周期
	##############################			
	def Cycle(self) :	
		return qts_Cycle(self.StrategyId())
		
	##############################
	#@brief 获得策略的交易周期
	#@return 循环周期
	#@note 暂不支持
	##############################			
	def TradeCycle(self) :
		return qts_TradeCycle(self.StrategyId())
		
	##############################
	#@brief 获得策略的状态
	#@return 策略的状态
	##############################			
	def Status(self) :
		return qts_Status(self.StrategyId())
		
	##############################
	#@brief 下一笔数据
	##############################			
	def NextData(self) :	
		qts_NextData(self.StrategyId())
		
	##############################
	#@brief 注册行情
	#@param market 市场值
	#@param category 品种值
	#@param icode 证券代码
	#@return 是否注册成功
	##############################				
	def RegisterData(self,market,category,icode) :
		return qts_RegisterData(self.StrategyId(),market,category,icode)
		
	##############################
	#@brief 注销行情
	#@param market 市场值
	#@param category 品种值
	#@param icode 证券代码
	#@return 是否注销成功
	##############################			
	def UnRegisterData(self,market,category,icode) :
		return qts_UnRegisterData(self.StrategyId(),market,category,icode)
		
	##############################
	#@brief 添加交易标的
	#@param itype 交易标的类型，QtsGProtoTradeCodeType的其中一个取值
	#@param key 键值，在一个策略内是唯一的
	#@param name 名称
	#@param icode 交易标的
	#@see  QtsGProtoTradeCodeType，具体字段参见qtsgoogleproto.proto文件
	#@return 添加是否成功
	##############################			
	def AddTradeCode(self,itype,key,name,icode) :
		return qts_AddTradeCode(self.StrategyId(),itype,key,name,icode)
	
	##############################
	#@brief 检查是否存在交易标的
	#@param itype 交易标的类型
	#@param icode 交易标的
	#@see QtsGProtoTradeCodeType，具体字段参见qtsgoogleproto.proto文件
	#@return 一个布尔值，是否存在
	##############################		
	def ExistTradeCode(self,itype,icode) :
		return qts_ExistTradeCode(self.StrategyId(),itype,icode)
		
	##############################
	#@brief 得到策略配置参数的整数值
	#@param key 参数的键值，一个策略内必须是唯一的
	#@return  整数值
	##############################			
	def GetParameterForInt64(self,key) :
		return qts_GetParameterForInt64(self.StrategyId(),key)[1]
		
	##############################
	#@brief 设置策略配置参数的整数值
	#@param key 参数的键值，一个策略内必须是唯一的
	#@param value  参数的整数值
	#@return 一个布尔值，是否成功
	##############################			
	def SetParameterForInt64(self,key,value) :
		return qts_SetParameterForInt64(self.StrategyId(),key,value)
		
	##############################
	#@brief 得到策略配置参数的双精度值
	#@param key 参数的键值，一个策略内必须是唯一的
	#@return  双精度值
	##############################			
	def GetParameterForDouble(self,key) :
		return qts_GetParameterForDouble(self.StrategyId(),key)[1]
		
	##############################
	#@brief 设置策略配置参数的双精度值
	#@param key 参数的键值，一个策略内必须是唯一的
	#@param value  双精度值
	#@return 一个布尔值，是否成功
	##############################			
	def SetParameterForDouble(self,key,value) :
		return qts_SetParameterForDouble(self.StrategyId(),key,value)

	##############################
	#@brief 得到策略配置参数的状态
	#@param key 参数的键值，一个策略内必须是唯一的
	#@return 状态
	##############################			
	def GetParameterForStatus(self,key) :
		return qts_GetParameterForStatus(self.StrategyId(),key)[1]
		
	##############################
	#@brief 设置策略配置参数的状态
	#@param key 参数的键值，一个策略内必须是唯一的
	#@param status  参数的状态
	#@return 一个布尔值，是否成功
	##############################		
	def SetParameterForStatus(self,key,value) :
		return qts_SetParameterForStatus(self.StrategyId(),key,value)
		
	##############################
	#@brief 得到策略所有的配置参数
	#@return 配置参数集，具体字段参见qtsgoogleproto.proto文件
	#@see QtsGProtoSecuInfoes
	##############################			
	def GetParameters(self) :
		values = QtsGProtoSecuInfoes()
		if qts_GetParameters(self.StrategyId(),values) :
			return values
		else :
			return None
		
	##############################
	#@brief 检查是否存在参籹
	#@param key 参数的键值，一个策略内必须是唯一的
	#@return 是否存在
	##############################			
	def ExistParameter(self,key) :
		return qts_GetParameterForInt64(self.StrategyId(),key)[0]
		
	##############################
	#@brief 得到配置
	#@param key 配置键值
	#@return 配置结构，具体字段参见qtsgoogleproto.proto文件
	#@see QtsGProtoConfig
	##############################			
	def GetConfig(self,key) :
		value = QtsGProtoConfig()
		if qts_GetConfig(self.StrategyId(),key,value) :
			return value
		else :
			return None
			
	##############################
	#@brief 检查配置是否存在
	#@param key 配置键值
	#@return 是否存在
	##############################				
	def ExistConfig(self,key) :
		value = QtsGProtoConfig()
		return qts_GetConfig(self.StrategyId(),key,value)
		
	##############################
	#@brief 得到所有的交易标的
	#@param type 交易标的类型
	#@return codes 返回值，交易标的集，具体字段参见qtsgoogleproto.proto文件
	#@see QtsGProtoCodes
	##############################				
	def GetCodes(self,type) :
		values = QtsGProtoCodes()
		if qts_GetCodes(self.StrategyId(),type,values) :
			return values
		else :
			return None
			
	##############################
	#@brief 启动策略
	#@return 一个布尔值，是否成功
	#@note 策略内部要慎用这个函数，一般由GUI的strategymonitor启动策略
	##############################				
	def Start(self) :
		return qts_Start(self.StrategyId())
		
	##############################
	#@brief 暂停策略
	#@return 一个布尔值，是否成功
	#@note 策略内部要慎用这个函数，一般由GUI的strategymonitor暂停策略
	##############################			
	def Pause(self) :
		return qts_Pause(self.StrategyId())
		
	##############################
	#@brief 观察策略
	#@return 一个布尔值，是否成功
	#@note 策略内部要慎用这个函数，一般由GUI的strategymonitor观察策略
	##############################			
	def Watch(self) :
		return qts_Watch(self.StrategyId())
		
	##############################
	#@brief 停止策略
	#@return 一个布尔值，是否成功
	#@note 策略内部要慎用这个函数，一般由GUI的strategymonitor停止策略
	##############################		
	def Stop(self) :
		return qts_Stop(self.StrategyId())
		
	##############################
	#@brief 得到时间戳中的日期
	#@param datetime 日期时间
	#@return 日期
	##############################		
	def GetDate(self,datetime) :
		return qts_GetData(datatime)
		
	##############################
	#@brief 得到时间戳中的时间
	#@param datetime 日期时间
	#@return 时间
	##############################			
	def GetTime(self,datetime) :
		return qts_GetTime(datetime)
		
	##############################
	#@brief 得到交易日期
	#@param market 市场
	#@return 交易日期
	##############################			
	def TradingDate(self,market) :
		return qts_TradingDate(market)
		
	##############################
	#@brief 得到交易时间
	#@param market 市场
	#@return 交易时间
	##############################		
	def TradingTime(self,market) :
		return qts_TradingTime(market)
		
	##############################
	#@brief 得到系统当前秒时间
	#@return 时间
	##############################			
	def GetSecond(self) :
		return qts_GetSecond()
		
	##############################
	#@brief 得到系统当前毫秒时间
	#@return 时间
	##############################			
	def GetMilliSecond(self) :
		return qts_GetMilliSecond()

	##############################
	#@brief 得到系统当前微秒时间
	#@return 时间
	##############################			
	def GetMicroSecond(self) :
		return qts_GetMicroSecond()
	
	##############################
	#@brief 回复策略属性页事件
	#@param userdata 用户数据，具体字段参见qtsgoogleproto.proto文件
	#@see QtsGProtoUserData
	#@return 一个布尔值
	##############################	
	def AckEvent(self,type,data) :
		return qts_AckEvent(self.StrategyId(),type,data)
		
	##############################
	#@brief 发送监控消息
	#@param userdata 用户数据，具体字段参见qtsgoogleproto.proto文件
	#@see QtsGProtoUserData
	#@return 一个布尔值，是否成功
	##############################
	def AckMonitor(self,type,data) :
		return qts_AckMonitor(self.StrategyId(),type,data)	

	##############################
	#@brief 在日志输出消息信息
	#@param msg  消息字符串
	#@return 是否成功
	##############################	
	def PrintMessageToLocal(self,msg) :
		return qts_PrintMessageToLocal(self.StrategyId(),msg)

	##############################
	#@brief 在日志输出调试信息
	#@param msg  消息字符串
	#@return 是否成功
	##############################	
	def PrintDebugToLocal(self,msg) :
		return qts_PrintDebugToLocal(self.StrategyId(),msg)
		
	##############################
	#@brief 在日志输出警告信息
	#@param msg  消息字符串
	#@return 是否成功
	##############################		
	def PrintWarningToLocal(self,msg) :
		return qts_PrintWarningToLocal(self.StrategyId(),msg)
		
	##############################
	#@brief 在日志输出错误信息
	#@param msg  消息字符串
	#@return 是否成功
	##############################		
	def PrintErrorToLocal(self,msg) :
		return qts_PrintErrorToLocal(self.StrategyId(),msg)
		
	##############################
	#@brief 在网络输出消息信息
	#@param msg  消息字符串
	#@return 是否成功
	##############################		
	def PrintMessageToNet(self,msg) :
		return qts_PrintMessageToNet(self.StrategyId(),msg)

	##############################
	#@brief 在网络输出主调试信息
	#@param msg  消息字符串
	#@return 是否成功
	##############################			
	def PrintDebugToNet(self,msg) :
		return qts_PrintDebugToNet(self.StrategyId(),msg)
		
	##############################
	#@brief 在网络输出警告信息
	#@param msg  消息字符串
	#@return 是否成功
	##############################			
	def PrintWarningToNet(self,msg) :
		return qts_PrintWarningToNet(self.StrategyId(),msg)
		
	##############################
	#@brief 在网络输出错误信息
	#@param msg  消息字符串
	#@return 是否成功
	##############################			
	def PrintErrorToNet(self,msg) :
		return qts_PrintErrorToNet(self.StrategyId(),msg)
		
	##############################
	#@brief 普通下单
	#@param algoid  算法ID
	#@param account 帐户
	#@param market 市场值
	#@param category 品种值
	#@param icode 证券代码
	#@param action 单行为
	#@param price 单价格
	#@param quantity 单量
	#@param iproperty 单属性
	#@return 订单id
	##############################			
	def Order(self,algoid,account,market,category,icode,action,price,quantity,iproperty) :	
		gorder = QtsGProtoOrder()
		gorder.strategyid = parent
		gorder.algoid = algoid
		gorder.market = market
		gorder.category = category
		gorder.code = icode
		gorder.account = account
		gorder.price = price
		gorder.quantity = quantity
		gorder.action = action
		gorder.property = iproperty
		gorder.sessionid = 0
		gorder.refid = 0
		gorder.direction = 0	
		gorder.channel = 0
		return qts_Order(self.StrategyId(),gorder)

	##############################
	#@brief 普通下单
	#@param order  单信息
	#@return 订单id
	##############################			
	def Order(self,order) :		
		return qts_Order(self.StrategyId(),order)
		
	##############################
	#@brief 算法下单
	#@param order 订单数据，具体字段参见qtsgoogleproto.proto文件
	#@see QtsGProtoAlgoOrder
	#@return 订单算法id
	##############################	
	def AlgoOrder(self,data) :
		return qts_AlgoOrder(self.StrategyId(),data)
		
	##############################
	#@brief 取消订单
	#@param orderid 订单数据id
	#@return 撤单量
	##############################		
	def Cancel(self,orderid) :
		return qts_Cancel(self.StrategyId(),orderid)
		
	##############################
	#@brief 取消所有订单
	#@return 撤单量
	##############################		
	def Cancels(self) :
		return qts_Cancels(self.StrategyId())
		
	##############################
	#@brief 取消算法订单
	#@param cancel 订单数据，具体字段参见qtsgoogleproto.proto文件
	#@see QtsGProtoAlgoCancel
	#@return 撤单量
	##############################
	def AlgoCancel(self,data) : 
		return qts_AlgoCancel(self.StrategyId(),data)

	##############################
	#@brief 取消所有算法订单
	#@return 撤单量
	##############################	
	def AlgoCancels(self) :  
		return qts_AlgoCancels(self.StrategyId())

	##############################
	#@brief 设置算法变量
	#@param value 变量
	#@return 一个布尔值，是否成功
	##############################			
	def AlgoSetCfg(self,value) : 
		return qts_AlgoSetCfg(self.StrategyId(),value)

	##############################
	#@brief 获得算法变量
	#@param value 变量键值
	#@return 数据
	##############################			
	def AlgoGetCfg(self,value) : 
		return qts_AlgoGetCfg(self.StrategyId(),value)

	##############################
	#@brief 对算法查寻
	#@param value 变量键值
	#@return 数据
	##############################			
	def AlgoQuery(self,value) : 
		return qts_AlgoQuery(self.StrategyId(),value)

	##############################
	#@brief 注册算法回调
	#@param key 键值
	#@param fun 回调函数
	#@param para 回调参数
	#@return 一个布尔值，是否成功
	##############################		
	def AlgoRegCallback(self,key,fun,para) : 
		return qts_AlgoRegCallback(self.StrategyId(),key,fun,para)

	##############################
	#@brief 注销算法回调
	#@param key 键值
	#@param fun 回调函数
	#@param para 回调参数
	#@return 一个布尔值，是否成功
	##############################			
	def AlgoUnRegCallback(self,key,fun,para) : 
		return qts_AlgoUnRegCallback(self.StrategyId(),key,fun,para)
		
	##############################
	#@brief 得到交易标的证券信息
	#@param icode 交易标的
	#@return 证券信息
	#@see QtsGProtoSecuInfo，具体字段参见qtsgoogleproto.proto文件
	##############################		
	def GetSecuInfo(self,icode) :
		value = QtsGProtoSecuInfo()
		if qts_GetSecuInfo(self.StrategyId(),icode,value) :
			return value
		else :
			return None
		
	##############################
	#@brief 得到交易标的证券信息
	#@param market 市场
	#@param category 品各
	#@param secucode 证券代码
	#@return 证券信息
	#@see QtsGProtoSecuInfo，具体字段参见qtsgoogleproto.proto文件
	##############################			
	def GetSecuInfoBySecuCode(self,market,category,secucode) :
		value = QtsGProtoSecuInfo()
		if qts_GetSecuInfoBySecuCode(self.StrategyId(),market,category,secucode,value) :
			return value
		else :
			return None
	
	##############################
	#@brief 得到交易标的证券信息
	#@param market 市场
	#@param category 品各
	#@param ordercode 交易代码
	#@return 证券信息
	#@see QtsGProtoSecuInfo，具体字段参见qtsgoogleproto.proto文件
	##############################		
	def GetSecuInfoByOrderCode(self,market,category,ordercode) :
		value = QtsGProtoSecuInfo()
		if qts_GetSecuInfoByOrderCode(self.StrategyId(),market,category,ordercode,value) :
			return value
		else :
			return None
		
	##############################
	#@brief 得到策略信息
	#@return 策略信息
	#@see QtsGProtoStrategyInfo，具体字段参见qtsgoogleproto.proto文件
	##############################		
	def GetStrategyInfo(self) :
		value = QtsGProtoStrategyInfo();
		if qts_GetStrategyInfo(self.StrategyId(),value) :
			return value
		else :
			return None
			
	##############################
	#@brief 得到帐户信息
	#@param market 市场
	#@param category 品种
	#@param account 帐户
	#@return 帐户信息
	#@see QtsGProtoAccount，具体字段参见qtsgoogleproto.proto文件
	##############################				
	def GetAccount(self,secuid,account) :
		value = QtsGProtoAccount()
		if qts_GetAccount(self.StrategyId(),secuid,account,value) :
			return value
		else :
			return None
	
	##############################
	#@brief 得到仓位集合
	#@param filter 过滤回调函数，参见QTSqts_FILTERqts_CALLBACK，在qtsprototradeapi.h中
	#@param para 参数，是过滤函数中的para参数
	#@return 仓位集合
	#@see QtsGProtoPositions，具体字段参见qtsgoogleproto.proto文件
	##############################
	def GetPositions(self,filter,para) :
		cfun = QTSqts_FILTERqts_CALLBACK(filter)
		values = QtsGProtoPositions()
		if qts_GetPositions(self.StrategyId(),cfun,para,values) :
			return values
		else :
			return None
			
	##############################
	#@brief 得到订单集合
	#@param type 指在活动单集合中查找，还是完结单集合中查找
	#@param filter 过滤回调函数，参见QTSqts_FILTERqts_CALLBACK，在qtsprototradeapi.h中
	#@param para 参数，是过滤函数中的para参数
	#@return 订单集合
	#@see QtsGProtoRecords，具体字段参见qtsgoogleproto.proto文件
	#@see QtsGProtoRecordMode，具体字段参见qtsgoogleproto.proto文件
	##############################			
	def GetRecords(self,filter,para) :
		cfun = QTSqts_FILTERqts_CALLBACK(filter)
		values = QtsGProtoRecords()
		if qts_GetRecords(self.StrategyId(),cfun,para,values) :
			return values
		else :
			return None	
			
	##############################
	#@brief 得到工作信息集
	#@param filter 过滤回调函数，参见QTSqts_FILTERqts_CALLBACK，在qtsprototradeapi.h中
	#@param para 参数，是过滤函数中的para参数
	#@return 工作信息集
	#@see QtsGProtoWorkings，具体字段参见qtsgoogleproto.proto文件
	##############################			
	def GetWorkings(self,filter,para) :	
		cfun = QTSqts_FILTERqts_CALLBACK(filter)
		values = QtsGProtoWorkings()
		if qts_GetWorkings(self.StrategyId(),cfun,para,values) :
			return values
		else :
			return None	
			
	##############################
	#@brief 得到盈亏集
	#@param filter 过滤回调函数，参见QTSqts_FILTERqts_CALLBACK，在qtsprototradeapi.h中
	#@param para 参数，是过滤函数中的para参数
	#@return 盈亏集
	#@see QtsGProtoPnls，具体字段参见qtsgoogleproto.proto文件
	##############################					
	def GetPnls(self,filter,para) :	
		cfun = QTSqts_FILTERqts_CALLBACK(filter)
		values = QtsGProtoPnls()
		if qts_GetPnls(self.StrategyId(),cfun,para,values) :
			return values
		else :
			return None	
	
	##############################
	#@brief 得到订单所在行情BOOK集
	#@param filter 过滤回调函数，参见QTSqts_FILTERqts_CALLBACK，在qtsprototradeapi.h中
	#@param para 参数，是过滤函数中的para参数
	#@return 行情BOOK集
	#@see QtsGProtoBooks，具体字段参见qtsgoogleproto.proto文件
	##############################
	def GetBooks(self,filter,para) :	
		cfun = QTSqts_FILTERqts_CALLBACK(filter)
		values = QtsGProtoBooks()
		if qts_GetBooks(self.StrategyId(),cfun,para,values) :
			return values
		else :
			return None	

	##############################
	#@brief 得到证券信息集
	#@param cmd 命令参数
	#@return 证券信息集
	#@see QtsGProtoSecuInfoes，具体字段参见qtsgoogleproto.proto文件
	##############################			
	def QuerySecuInfoes(self,cmd) :	
		values = QtsGProtoSecuInfoes()
		if qts_QuerySecuInfoes(self.StrategyId(),cmd,values) :
			return values
		else :
			return None

	##############################
	#@brief 得到账户集
	#@param cmd 命令参数
	#@return 账户集
	#@see QtsGProtoAccounts，具体字段参见qtsgoogleproto.proto文件
	##############################				
	def QueryAccounts(self,cmd) :
		values = QtsGProtoAccounts()
		if qts_QueryAccounts(self.StrategyId(),cmd,values) :
			return values
		else :
			return None
		
	##############################
	#@brief 得到仓位集
	#@param cmd 命令参数
	#@return 仓位集
	#@see QtsGProtoPositions，具体字段参见qtsgoogleproto.proto文件
	##############################			
	def QueryPositions(self,cmd) :
		values = QtsGProtoPositions()
		if qts_QueryPositions(self.StrategyId(),cmd,values) :
			return values
		else :
			return None
		
	##############################
	#@brief 得到订单集
	#@param cmd 命令参数
	#@return 订单集
	#@see QtsGProtoRecords，具体字段参见qtsgoogleproto.proto文件
	##############################		
	def QueryRecords(self,cmd) :
		values = QtsGProtoRecords()
		if qts_QueryRecords(self.StrategyId(),cmd,values) :
			return values
		else :
			return None
		
	##############################
	#@brief 得到在途信息集
	#@param cmd 命令参数
	#@return 在途信息集
	#@see QtsGProtoWorkings，具体字段参见qtsgoogleproto.proto文件
	##############################			
	def QueryWorkings(self,cmd) :
		values = QtsGProtoWorkings()
		if qts_QueryWorkings(self.StrategyId(),cmd,values) :
			return values
		else :
			return None
		
	##############################
	#@brief 得到盈亏信息集
	#@param cmd 命令参数
	#@return 盈亏息集
	#@see QtsGProtoPnls，具体字段参见qtsgoogleproto.proto文件
	##############################			
	def QueryPnls(self,cmd) :
		values = QtsGProtoPnls()
		if qts_QueryPnls(self.StrategyId(),cmd,values) :
			return values
		else :
			return None
		
	##############################
	#@brief 得到订单本信息集
	#@param cmd 命令参数
	#@return 订单本息集
	#@see QtsGProtoBooks，具体字段参见qtsgoogleproto.proto文件
	##############################			
	def QueryBooks(self,cmd) :
		values = QtsGProtoBooks()
		if qts_QueryBooks(self.StrategyId(),cmd,values) :
			return values
		else :
			return None
		
	##############################
	#@brief 得到仓位
	#@param account 帐户
	#@param icode 交易标的
	#@param itype 仓位类型
	#@return 仓位
	#@see QtsGProtoPosition，具体字段参见qtsgoogleproto.proto文件
	#@see EQtsGProtoPositionType，具体字段参见qtsgoogleproto.proto文件
	##############################			
	def GetPosition(self,account,icode,itype) :
		value = QtsGProtoPosition()
		if qts_GetPosition(self.StrategyId(),account,icode,itype,value) :
			return value
		else :
			return None
		
	##############################
	#@brief 得到订单
	#@param itype 指在活动单集合中查找，还是完结单集合中查找
	#@param orderid 订单ID
	#@return 订单
	#@see QtsGProtoRecord，具体字段参见qtsgoogleproto.proto文件
	#@see QtsGProtoRecordMode，具体字段参见qtsgoogleproto.proto文件
	##############################	
	def GetRecord(self,itype,orderid) :	
		value = QtsGProtoRecord()
		if qts_GetRecord(self.StrategyId(),itype,orderid,value) :
			return value
		else :
			return None
		
	##############################
	#@brief 得到工作信息
	#@param icode 交易标的
	#@param action 订单行为
	#@return 工作信息
	#@see QtsGProtoWorking，具体字段参见qtsgoogleproto.proto文件
	#@see EQtsGProtoOrderAction，具体字段参见qtsgoogleproto.proto文件
	##############################	
	def GetWorking(self,algoid,icode,action) :
		value = QtsGProtoWorking()
		if qts_GetWorking(self.StrategyId(),algoid,icode,action,value) :
			return value
		else :
			return None	
		
	##############################
	#@brief 得到盈亏
	#@param account 帐户
	#@param icode 交易标的
	#@return 盈亏
	#@see QtsGProtoPnl，具体字段参见qtsgoogleproto.proto文件
	##############################
	def GetPnl(self,account,icode) :
		value = QtsGProtoPnl()
		if qts_GetPnl(self.StrategyId(),account,icode,value) :
			return value
		else :
			return None	
		
	##############################
	#@brief 得到订单所在行情BOOK
	#@param icode 交易标的
	#@param price 交易价格
	#@return 行情BOOK
	#@see QtsGProtoBook，具体字段参见qtsgoogleproto.proto文件
	##############################	
	def GetBook(self,algoid,icode,price) :
		value = QtsGProtoBook()
		if qts_GetBook(self.StrategyId(),algoid,icode,price,value) :
			return value
		else :
			return None
		
	##############################
	#@brief 得到最新的行情
	#@param icode 交易标的
	#@return 最新的行情
	#@see QtsGProtoData，具体字段参见qtsgoogleproto.proto文件
	##############################			
	def GetLastData(self,icode) :
		value = QtsGProtoData()
		if qts_GetLastData(self.StrategyId(),icode,value) :
			return value
		else : 
			return None
		
	##############################
	#@brief 得到一个周期内的行情集
	#@param icode 交易标的
	#@return 行情集
	#@see QtsGProtoDatas，具体字段参见qtsgoogleproto.proto文件
	##############################		
	def GetCurrDatas(self,icode) :
		values = QtsGProtoDatas()
		if qts_GetCurrDatas(self.StrategyId(),icode,values) :
			return values
		else :
			return None
		
	##############################
	#@brief 得到订单所在行情BOOK
	#@param code 交易标的
	#@param price 交易价格
	#@return 行情BOOK
	#@see QtsGProtoBook，具体字段参见qtsgoogleproto.proto文件
	##############################		
	def EnoughAccount(self,secuid,account,amount) :
		return qts_EnoughAccount(self.StrategyId(),secuid,account,amount)
		
	##############################
	#@brief 根据基码，产生系统错误码
	#@note 基码
	#@return 实际的错误码
	##############################
	def BuildSysErrorCode(self,err) :
		return qts_GetSysErrorCode(err)
		
	##############################
	#@brief 根据基码，产生业务错误码
	#@note 基码
	#@return 实际的错误码
	##############################		
	def BuildBZErrorCode(self,err) :
		return qts_GetBZErrorCode(err)
		
	##############################
	#@brief 根据基码，产生风控错误码
	#@note 基码
	#@return 实际的错误码
	##############################		
	def BuildRiskErrorCode(self,err) :
		return qts_GetRiskErrorCode(err)
	
	##############################
	#@brief 设置公共变量
	#@param key 键值
	#@param name 名称
	#@param data 数据
	#@return 一个布尔值，QTSqts_TRUE成功，QTSqts_FALSE是不成功	
	##############################
	def SetVariable(self,key,name,value) :
		return qts_SetVariable(key,name,value)

	##############################
	#@brief 获得公共变量
	#@param key 键值
	#@param name 名称
	#@return 数据
	##############################
	def GetVariable(self,key,name) :
		return qts_GetVariable(key,name)

	##############################
	#@brief 设置是否向GUI发送行情，谨慎使用，对整个SS
	#@param bpush 是否发送
	##############################
	def SetPushDataToGUI(self,bpush) :
		qts_SetPushDataToGUI(bpush)
			
	##############################
	#@brief 设置是否向GW发送行情，谨慎使用，对整个SS
	#@param bpush 是否发送
	##############################
	def SetPushDataToGW(self,bpush) :
		qts_SetPushDataToGW(bpush)

	##############################
	#@brief 获得是否向GUI发送行情
	#@return 是否可发送	
	##############################	
	def GetPushDataToGUI(self) :
		return qts_GetPushDataToGUI()
		
	##############################
	#@brief 获得是否向GW发送行情
	#@return 是否可发送
	##############################
	def GetPushDataToGW(self) :
		return qts_GetPushDataToGW()
		
	##############################
	#@brief 获得是否向GUI发送订单
	#@return 是否可发送
	##############################
	def IsRecordToRemote(self,handle) :
		return qts_IsRecordToRemote(handle)
		
	##############################
	#@brief 获得是否向GUI发送仓位、BOOK和在途信息
	#@return 是否可发送
	##############################
	def IsPositionToRemote(self,handle) :
		return qts_IsPositionToRemote(handle)
		
	##############################
	#@brief 获得是否向GUI发送账户信息
	#@return 是否可发送
	##############################
	def IsAccountToRemote(self,handle) :
		return qts_IsAccountToRemote(handle)
		
	##############################
	#@brief 设置是否向GUI发送订单
	#@param bremote  是否可发送
	##############################
	def SetIsRecordToRemote(self,handle,bremote) :
		qts_SetIsRecordToRemote(handle,bremote)
		
	##############################
	#@brief 设置是否向GUI发送仓位
	#@param bremote  是否可发送
	##############################
	def SetIsPositionToRemote(self,handle,bremote) :
		qts_SetIsPositionToRemote(handle,bremote)
			
	##############################
	#@brief 设置是否向GUI发送账户
	#@param bremote  是否可发送
	##############################
	def SetIsAccountToRemote(self,handle,bremote) :
		qts_SetIsAccountToRemote(handle,bremote)

	##############################
	#@brief 返回是否可以在控制台输出消息信息，用户一般不会直接使用，如果要使用屏幕输出，
	#@return 一个布尔值，QTSqts_TRUE可以输出，QTSqts_FALSE是不可以输出	
	##############################	
	def IsTraceMessage(self) :
		return qts_IsTraceMessage
		
	##############################
	#@brief 返回是否可以在控制台输出调试信息，用户一般不会直接使用，如果要使用屏幕输出，
	#@return 一个布尔值，QTSqts_TRUE可以输出，QTSqts_FALSE是不可以输出		
	##############################
	def IsTraceDebug(self) :
		return qts_IsTraceDebug
		
	##############################
	#@brief 返回是否可以在控制台输出调试信息，用户一般不会直接使用，如果要使用屏幕输出，
	#@return 一个布尔值，QTSqts_TRUE可以输出，QTSqts_FALSE是不可以输出	
	##############################	
	def IsTraceWarning(self) :
		return qts_IsTraceWarning
		
	##############################
	#@brief 返回是否可以在控制台输出调试信息，用户一般不会直接使用，如果要使用屏幕输出，
	#@return 一个布尔值，QTSqts_TRUE可以输出，QTSqts_FALSE是不可以输出	
	##############################
	def IsTraceError(self) :
		return qts_IsTraceError

	##############################
	#@brief 返回是否可以在日志输出消息信息，用户一般不会直接使用，如果要使用日志输出，
	#@return 一个布尔值，QTSqts_TRUE可以输出，QTSqts_FALSE是不可以输出	
	##############################
	def IsLogMessage(self) :
		return qts_IsLogMessage
		
	##############################
	#@brief 返回是否可以在日志输出调试信息，用户一般不会直接使用，如果要使用日志输出，
	#@return 一个布尔值，QTSqts_TRUE可以输出，QTSqts_FALSE是不可以输出	
	##############################
	def IsLogDebug(self) :
		return qts_IsLogDebug
		
	##############################
	#@brief 返回是否可以在日志输出警告信息，用户一般不会直接使用，如果要使用日志输出，
	#@return 一个布尔值，QTSqts_TRUE可以输出，QTSqts_FALSE是不可以输出	
	##############################
	def IsLogWarning(self) :
		return qts_IsLogWarning
		
	##############################
	#@brief 返回是否可以在日志输出错误信息，用户一般不会直接使用，如果要使用日志输出，
	#@return 一个布尔值，QTSqts_TRUE可以输出，QTSqts_FALSE是不可以输出	
	##############################
	def IsLogError(self) :
		return qts_IsLogError()