#coding=utf-8
from qtsfun import *

#//////////////////////////////////////////////////////////////////////////////
####################################################
#@brief 工具操作配置文件需要
#@param module		应用模块名称
####################################################
def InitCfgEnv(module,tag) :
	if not ExistRootGlobals() :
		CreateRootGlobals()
		AppendMainDict(module,QTS_CFG_GROUP_APP)
		AppendItemForMainDict(module,QTS_CFG_GROUP_APP,QTS_CFG_GROUP_CFG,tag)
		SetAppPath(module)

#//////////////////////////////////////////////////////////////////////////////	
####################################################
#@brief 创建资源，一个进程只能有一个
#@param module		应用模块名称
#@param **kwargs	key=value参数
####################################################
def CreateResources(module,**kwargs):
	PrintMessage('*****************************' + QTS_CFG_GROUP_RESOURCES + '*********************************')		
	AppendMainDict(module,QTS_CFG_GROUP_RESOURCES)
	for kwarg in kwargs :
		AppendItemForMainDict(module,QTS_CFG_GROUP_RESOURCES,kwarg,kwargs[kwarg])	
	PrintMessageForMain(module,QTS_CFG_GROUP_RESOURCES)
	PrintMessage('*****************************' + QTS_CFG_GROUP_RESOURCES + '*********************************')

####################################################
#@brief 加载资源，一个进程只能有一个
#@param module		应用模块名称
#@param **kwargs	key=value参数
####################################################	
def LoadResources(module,path,**kwargs):
	CreateResources(module,**kwargs)
	appath = GetAppPath()
	SetAppPath(module)
	LoadPythonFileByPath( GetLanguagePath(path))
	LoadPythonFileByPath( GetMusicPath(path))
	LoadPythonFileByPath( GetQSSPath(path))
	SetAppPath(appath)

####################################################
#@brief 添加一个资源属性
#@param key			属性名称
#@param value		属性值
####################################################	
def AppendResource(key,value) :
	AppendItemForMainDict(GetAppPath(),QTS_CFG_GROUP_RESOURCES,key,value)

####################################################
#@brief 添加一个资源属性
#@param **kwargs	key=value参数
####################################################	
def AppendResources(**kwargs) :
	for kwarg in kwargs :
		AppendResource(kwarg,kwargs[kwarg])
		
#//////////////////////////////////////////////////////////////////////////////	
####################################################
#@brief 创建应用程序，一个进程只能有一个
#@param module		应用模块名称
#@param identity	进程身份
#@param objid		对象ID
#@param version		程序版本
#@param apptype		应用类型
#@param appname		应用名称
#@param applog		应用默认日志文件
#@param **kwargs	key=value参数
####################################################
def CreateApplication(module,identity,objid,version,apptype,appname,applog,**kwargs):
	PrintMessage('*****************************' + QTS_CFG_GROUP_APP + '*********************************')		
	AddAppIdentity(identity)
	AppendMainDict(module,QTS_CFG_GROUP_APP)
	AppendItemForMainDict(module,QTS_CFG_GROUP_APP,QTS_CFG_KEY_OBJID,objid)
	AppendItemForMainDict(module,QTS_CFG_GROUP_APP,QTS_CFG_KEY_VERSION,version)
	AppendItemForMainDict(module,QTS_CFG_GROUP_APP,QTS_CFG_KEY_TYPE,apptype)
	AppendItemForMainDict(module,QTS_CFG_GROUP_APP,QTS_CFG_KEY_NAME,appname)
	AppendItemForMainDict(module,QTS_CFG_GROUP_APP,QTS_CFG_KEY_LOG,applog)	
	for kwarg in kwargs :
		AppendItemForMainDict(module,QTS_CFG_GROUP_APP,kwarg,kwargs[kwarg])	
	PrintMessageForMain(module,QTS_CFG_GROUP_APP)
	PrintMessage('*****************************' + QTS_CFG_GROUP_APP + '*********************************')
	
####################################################
#@brief 添加一个应用属性
#@param module		应用模块名称
#@param key			属性名称
#@param value		属性值
####################################################	
def AppendApplication(module,key,value) :
	AppendItemForMainDict(module,QTS_CFG_GROUP_APP,key,value)

####################################################
#@brief 添加一个应用用户属性
#@param key			属性名称
#@param value		属性值
####################################################	
def AppendUserApplication(key,value) :
	AppendItemForMainDict(GetAppPath(),QTS_CFG_GROUP_APP,key,value)	

#//////////////////////////////////////////////////////////////////////////////
####################################################
#@brief 创建一个应用的上下文
#@param module			应用模块名称
#@param thdmulti		是否允许多线程，True：是，False：否
#@param monitortime		监控延时，以秒为单位
#@param **kwargs		key=value参数
####################################################
def CreateContext(module,thdmulti = True,monitortime = 0,**kwargs):
	PrintMessage('*****************************' + QTS_CFG_GROUP_CONTEXT + '*********************************')		
	AppendMainDict(module,QTS_CFG_GROUP_CONTEXT)
	AppendItemForMainDict(module,QTS_CFG_GROUP_CONTEXT,QTS_CFG_KEY_PROTOPATH,GetProtoPath())
	AppendItemForMainDict(module,QTS_CFG_GROUP_CONTEXT,QTS_CFG_KEY_PROTOFILE,GetProtoFile())	
	if monitortime <= 0 :
		AppendItemForMainDict(module,QTS_CFG_GROUP_CONTEXT,QTS_CFG_KEY_MONITOR_TIME,GetMonitorTime())
	else :
		AppendItemForMainDict(module,QTS_CFG_GROUP_CONTEXT,QTS_CFG_KEY_MONITOR_TIME,monitortime)
	if thdmulti :
		AppendItemForMainDict(module,QTS_CFG_GROUP_CONTEXT,QTS_CFG_KEY_THDMULTI,QTS_TRUE)
	else :
		AppendItemForMainDict(module,QTS_CFG_GROUP_CONTEXT,QTS_CFG_KEY_THDMULTI,QTS_FALSE)
	for kwarg in kwargs :
		AppendItemForMainDict(module,QTS_CFG_GROUP_CONTEXT,kwarg,kwargs[kwarg])			
	PrintMessageForMain(module,QTS_CFG_GROUP_CONTEXT)
	PrintMessage('*****************************' + QTS_CFG_GROUP_CONTEXT + '*********************************')

####################################################
#@brief 添加一个上下文属性
#@param key			属性名称
#@param value		属性值
####################################################	
def AppendContext(module,key,value) :
	AppendItemForMainDict(module,QTS_CFG_GROUP_CONTEXT,key,value)

####################################################
#@brief 添加一个上下文用户属性
#@param key			属性名称
#@param value		属性值
####################################################		
def AppendUserContext(key,value) :
	AppendItemForMainDict(GetAppPath(),QTS_CFG_GROUP_CONTEXT,key,value)

#//////////////////////////////////////////////////////////////////////////////
####################################################
#@brief 创建一个风控节点
#@param name	风控名称
####################################################
def CreateCheck(name):
	PrintMessage('*****************************' + name + '*********************************')		
	AppendMainDict(GetAppPath(),name)
	PrintMessageForMain(GetAppPath(),name)
	PrintMessage('*****************************' + name + '*********************************')

####################################################
#@brief 添加一个风控属性
#@param name		风控名称
#@param key			属性名称
#@param value		属性值
####################################################	
def AppendCheck(name,key,value) :
	AppendItemForMainDict(GetAppPath(),name,key,value)
	
#//////////////////////////////////////////////////////////////////////////////
####################################################
#@brief 添加一个日志文件
#@param key			日志键值
#@param logfile		日志文件
####################################################
def AppendLog(key,logfile) :
	AppendItemForMainDict(GetAppDefaultPath(),QTS_CFG_PLUGINS_LOGS,key,BuildLogFile(logfile))	
	
####################################################
#@brief 加载日志插件
#@param module 		应用模块名称
#@param lib			日志库
#@param fun			日志加载函数
####################################################		
def LoadLogs(module,lib,fun) :
	PrintMessage('*****************************' + QTS_CFG_GROUP_LOGS + '*********************************')
	AppendMainDict(module,QTS_CFG_GROUP_LOGS)
	AppendPropertyForPlugin(module,QTS_CFG_GROUP_LOGS,QTS_CFG_KEY_FILE,BuildLibraryFile(lib))
	AppendPropertyForPlugin(module,QTS_CFG_GROUP_LOGS,QTS_CFG_KEY_FUN,fun)
	AppendPropertyForPlugin(module,QTS_CFG_GROUP_LOGS,QTS_CFG_KEY_CFG,QTS_CFG_PLUGINS_LOGS)
	AppendPropertyForPlugin(module,QTS_CFG_GROUP_LOGS,QTS_CFG_KEY_PATH,GetLibPath())
	CreatePluginsForManager(module,QTS_CFG_PLUGINS_LOGS)
	AppendLog(QTS_LOG_DEFAULT_KEY,QTS_LOG_DEFAULT_NAME);
	PrintMessageForMain(module,QTS_CFG_PLUGINS_LOGS)
	PrintMessageForMain(module,QTS_CFG_GROUP_LOGS)	
	PrintMessage('*****************************' + QTS_CFG_GROUP_LOGS + '*********************************')	

####################################################
#@brief 加载资源插件
#@param module 		应用模块名称
#@param managerid	资源管理ID
#@param log			日志键值
#@param items		资源管理名称
#@param **kwargs	key=value参数
####################################################	
def LoadDatas(module,managerid,log,items,tag,**kwargs) :
	PrintMessage('*****************************' + items + '*********************************')
	if IsExistMainDict(module,items) :
		return
	CreatePluginManager(module,items,managerid,items,log,items)
	for kwarg in kwargs :
		AppendItemForMainDict(module,items,kwarg,BuildLoaderFile(kwargs[kwarg],tag))
	PrintMessageForMain(module,items)	
	PrintMessage('*****************************' + items + '*********************************')	

####################################################
#@brief 加载证券信息
#@param module 		应用模块名称
#@param managerid	资源管理ID
#@param log			日志键值
#@param **kwargs	key=value参数
####################################################	
def LoadSecuInfoes(module,managerid,log,**kwargs) :
	LoadDatas(module,managerid,log,QTS_CFG_GROUP_SECUINFOES,'info',**kwargs)

####################################################
#@brief 加载帐户信息
#@param module 		应用模块名称
#@param managerid	资源管理ID
#@param log			日志键值
#@param **kwargs	key=value参数
####################################################	
def LoadAccounts(module,managerid,log,**kwargs) :
	LoadDatas(module,managerid,log,QTS_CFG_GROUP_ACCOUNTS,'acc',**kwargs)
	
####################################################
#@brief 加载仓位信息
#@param module 		应用模块名称
#@param managerid	资源管理ID
#@param log			日志键值
#@param **kwargs	key=value参数
####################################################	
def LoadPositions(module,managerid,log,**kwargs) :
	LoadDatas(module,managerid,log,QTS_CFG_GROUP_POSITIONS,'pos',**kwargs)

####################################################
#@brief 加载业务插件
#@param module 		应用模块名称
#@param managername	管理器名称
#@param pluginname	插槽名称
#@param managerid	资源管理ID
#@param log			日志键值
#@param path		库路径
####################################################	
def LoadBizPlugins(module,managername,pluginname,managerid,log,path) :
	PrintMessage('*****************************' + managername + '*********************************')
	CreatePluginManager(module,managername,managerid,managername,log,pluginname)
	CreatePluginsForManager(module,pluginname)
	appath = GetAppPath()
	SetAppPath(module)
	plugins = LoadPlugins(path)
	for plugin in plugins :
		exec plugin
	SetAppPath(appath)
	PrintMessageForMain(module,pluginname)
	PrintMessageForMain(module,managername)
	PrintMessage('*****************************' + managername + '*********************************')
		
####################################################
#@brief 加载备份插件
#@param module 		应用模块名称
#@param managerid	资源管理ID
#@param log			日志键值
#@param path		库路径
#@param **kwargs	key=value参数
####################################################
def LoadBackups(module,managerid,log,path,**kwargs) : 
	LoadBizPlugins(module,QTS_CFG_GROUP_BACKUPS,QTS_CFG_PLUGINS_BACKUPS,managerid,log,GetBackupPath(path))
	for kwarg in kwargs :
		AppendItemForMainDict(module,QTS_CFG_GROUP_BACKUPS,kwarg,kwargs[kwarg])
		
####################################################
#@brief 加载加载插件
#@param module 		应用模块名称
#@param managerid	资源管理ID
#@param log			日志键值
#@param path		库路径
#@param **kwargs	key=value参数
####################################################		
def LoadLoaders(module,managerid,log,path,**kwargs) : 
	LoadBizPlugins(module,QTS_CFG_GROUP_LOADERS,QTS_CFG_PLUGINS_LOADERS,managerid,log,GetLoaderPath(path))
	for kwarg in kwargs :
		AppendItemForMainDict(module,QTS_CFG_GROUP_LOADERS,kwarg,kwargs[kwarg])	

####################################################
#@brief 加载解析插件
#@param module 		应用模块名称
#@param managerid	资源管理ID
#@param log			日志键值
#@param path		库路径
#@param **kwargs	key=value参数
####################################################		
def LoadParsers(module,managerid,log,path,**kwargs) :
	LoadBizPlugins(module,QTS_CFG_GROUP_PARSERS,QTS_CFG_PLUGINS_PARSERS,managerid,log,GetParserPath(path))
	for kwarg in kwargs :
		AppendItemForMainDict(module,QTS_CFG_GROUP_PARSERS,kwarg,kwargs[kwarg])	
	
####################################################
#@brief 加载风控插件
#@param module 		应用模块名称
#@param managerid	资源管理ID
#@param log			日志键值
#@param path		库路径
#@param **kwargs	key=value参数
####################################################		
def LoadChecks(module,managerid,log,path,**kwargs) :
	LoadBizPlugins(module,QTS_CFG_GROUP_CHECKS,QTS_CFG_PLUGINS_CHECKS,managerid,log,GetCheckPath(path))
	for kwarg in kwargs :
		AppendItemForMainDict(module,QTS_CFG_GROUP_CHECKS,kwarg,kwargs[kwarg])	
	
####################################################
#@brief 加载算法插件
#@param module 		应用模块名称
#@param managerid	资源管理ID
#@param log			日志键值
#@param path		库路径
#@param **kwargs	key=value参数
####################################################		
def LoadAlgoes(module,managerid,log,path,**kwargs) :
	LoadBizPlugins(module,QTS_CFG_GROUP_ALGOES,QTS_CFG_PLUGINS_ALGOES,managerid,log,GetAlgoPath(path))
	for kwarg in kwargs :
		AppendItemForMainDict(module,QTS_CFG_GROUP_ALGOES,kwarg,kwargs[kwarg])	
	
####################################################
#@brief 加载数据传输插件
#@param module 		应用模块名称
#@param managerid	资源管理ID
#@param log			日志键值
#@param path		库路径
#@param **kwargs	key=value参数
####################################################		
def LoadDSTransfers(module,managerid,log,path,**kwargs) :
	LoadBizPlugins(module,QTS_CFG_GROUP_DSTRANSFERS,QTS_CFG_PLUGINS_DSTRANSFERS,managerid,log,GetDSTransferPath(path))
	for kwarg in kwargs :
		AppendItemForMainDict(module,QTS_CFG_GROUP_DSTRANSFERS,kwarg,kwargs[kwarg])	

####################################################
#@brief 加载交易通道传输插件
#@param module 		应用模块名称
#@param managerid	资源管理ID
#@param log			日志键值
#@param path		库路径
#@param **kwargs	key=value参数
####################################################		
def LoadGWTransfers(module,managerid,log,path,**kwargs) :
	LoadBizPlugins(module,QTS_CFG_GROUP_GWTRANSFERS,QTS_CFG_PLUGINS_GWTRANSFERS,managerid,log,GetGWTransferPath(path))
	for kwarg in kwargs :
		AppendItemForMainDict(module,QTS_CFG_GROUP_GWTRANSFERS,kwarg,kwargs[kwarg])	

####################################################
#@brief 加载终端传输插件
#@param module 		应用模块名称
#@param managerid	资源管理ID
#@param log			日志键值
#@param path		库路径
#@param **kwargs	key=value参数
####################################################		
def LoadGUITransfers(module,managerid,log,path,**kwargs) :
	LoadBizPlugins(module,QTS_CFG_GROUP_GUITRANSFERS,QTS_CFG_PLUGINS_GUITRANSFERS,managerid,log,GetGUITransferPath(path))
	for kwarg in kwargs :
		AppendItemForMainDict(module,QTS_CFG_GROUP_GUITRANSFERS,kwarg,kwargs[kwarg])	

####################################################
#@brief 加载终端传输插件
#@param module 		应用模块名称
#@param managerid	资源管理ID
#@param log			日志键值
#@param path		库路径
#@param **kwargs	key=value参数
####################################################		
def LoadCKTransfers(module,managerid,log,path,**kwargs) :
	LoadBizPlugins(module,QTS_CFG_GROUP_CKTRANSFERS,QTS_CFG_PLUGINS_CKTRANSFERS,managerid,log,GetCKTransferPath(path))
	for kwarg in kwargs :
		AppendItemForMainDict(module,QTS_CFG_GROUP_CKTRANSFERS,kwarg,kwargs[kwarg])	
		
####################################################
#@brief 加载终端传输插件
#@param module 		应用模块名称
#@param managerid	资源管理ID
#@param log			日志键值
#@param path		库路径
#@param **kwargs	key=value参数
####################################################		
def LoadCPTransfers(module,managerid,log,path,**kwargs) :
	LoadBizPlugins(module,QTS_CFG_GROUP_CPTRANSFERS,QTS_CFG_PLUGINS_CPTRANSFERS,managerid,log,GetCPTransferPath(path))
	for kwarg in kwargs :
		AppendItemForMainDict(module,QTS_CFG_GROUP_CPTRANSFERS,kwarg,kwargs[kwarg])	
		
####################################################
#@brief 加载传输插件
#@param module 		应用模块名称
#@param managerid	资源管理ID
#@param log			日志键值
#@param path		库路径
#@param **kwargs	key=value参数
####################################################		
def LoadTransfers(module,managerid,log,path,**kwargs) :
	LoadBizPlugins(module,QTS_CFG_GROUP_TRANSFERS,QTS_CFG_PLUGINS_TRANSFERS,managerid,log,GetTransferPath(path))
	for kwarg in kwargs :
		AppendItemForMainDict(module,QTS_CFG_GROUP_TRANSFERS,kwarg,kwargs[kwarg])	

####################################################
#@brief 加载监控插件
#@param module 		应用模块名称
#@param managerid	资源管理ID
#@param log			日志键值
#@param path		库路径
#@param **kwargs	key=value参数
####################################################		
def LoadMonitors(module,managerid,log,path,**kwargs) :
	LoadBizPlugins(module,QTS_CFG_GROUP_MQTRANSFERS,QTS_CFG_PLUGINS_MQTRANSFERS,managerid,log,GetMonitorPath(path))	
	for kwarg in kwargs :
		AppendItemForMainDict(module,QTS_CFG_GROUP_MQTRANSFERS,kwarg,kwargs[kwarg])	
	
####################################################
#@brief 加载计算插件
#@param module 		应用模块名称
#@param managerid	资源管理ID
#@param log			日志键值
#@param path		库路径
#@param **kwargs	key=value参数
####################################################		
def LoadCalculates(module,managerid,log,path,**kwargs) :
	LoadBizPlugins(module,QTS_CFG_GROUP_CALCULATES,QTS_CFG_PLUGINS_CALCULATES,managerid,log,GetCalculatePath(path))
	for kwarg in kwargs :
		AppendItemForMainDict(module,QTS_CFG_GROUP_CALCULATES,kwarg,kwargs[kwarg])
		
####################################################
#@brief 加载数据插件
#@param module 		应用模块名称
#@param managerid	资源管理ID
#@param log			日志键值
#@param path		库路径
#@param **kwargs	key=value参数
####################################################		
def LoadMarkets(module,managerid,log,path,**kwargs) :
	LoadBizPlugins(module,QTS_CFG_GROUP_MARKETS,QTS_CFG_PLUGINS_MARKETS,managerid,log,GetMarketPath(path))	
	for kwarg in kwargs :
		AppendItemForMainDict(module,QTS_CFG_GROUP_MARKETS,kwarg,kwargs[kwarg])
		
####################################################
#@brief 加载交易通道插件
#@param module 		应用模块名称
#@param managerid	资源管理ID
#@param log			日志键值
#@param path		库路径
#@param **kwargs	key=value参数
####################################################		
def LoadExchanges(module,managerid,log,path,**kwargs) :
	LoadBizPlugins(module,QTS_CFG_GROUP_EXCHANGES,QTS_CFG_PLUGINS_EXCHANGES,managerid,log,GetExchangePath(path))
	for kwarg in kwargs :
		AppendItemForMainDict(module,QTS_CFG_GROUP_EXCHANGES,kwarg,kwargs[kwarg])
		
####################################################
#@brief 加载策略插件
#@param module 		应用模块名称
#@param managerid	资源管理ID
#@param log			日志键值
#@param path		库路径
#@param **kwargs	key=value参数
####################################################		
def LoadStrategies(module,managerid,log,path,count,**kwargs) :
	LoadBizPlugins(module,QTS_CFG_GROUP_STRATEGIES,QTS_CFG_PLUGINS_STRATEGIES,managerid,log,GetStrategyPath(path))	
	AppendItemForMainDict(module,QTS_CFG_GROUP_STRATEGIES,QTS_CFG_KEY_TASK,count)
	for kwarg in kwargs :
		AppendItemForMainDict(module,QTS_CFG_GROUP_STRATEGIES,kwarg,kwargs[kwarg])
		
####################################################
#@brief 加载逻辑插件
#@param module 		应用模块名称
#@param managerid	资源管理ID
#@param log			日志键值
#@param path		库路径
#@param **kwargs	key=value参数
####################################################		
def LoadLogics(module,managerid,log,path,**kwargs) :
	LoadBizPlugins(module,QTS_CFG_GROUP_LOGICS,QTS_CFG_PLUGINS_LOGICS,managerid,log,GetLogicPath(path))	
	for kwarg in kwargs :
		AppendItemForMainDict(module,QTS_CFG_GROUP_LOGICS,kwarg,kwargs[kwarg])
		
####################################################
#@brief 加载过滤插件
#@param module 		应用模块名称
#@param managerid	资源管理ID
#@param log			日志键值
#@param path		库路径
#@param **kwargs	key=value参数
####################################################		
def LoadFilters(module,managerid,log,path,**kwargs) :
	LoadBizPlugins(module,QTS_CFG_GROUP_FILTERS,QTS_CFG_PLUGINS_FILTERS,managerid,log,GetFilterPath(path))	
	for kwarg in kwargs :
		AppendItemForMainDict(module,QTS_CFG_GROUP_FILTERS,kwarg,kwargs[kwarg])

####################################################
#@brief 加载数据传输插件
#@param module 		应用模块名称
#@param managerid	资源管理ID
#@param path		库路径
#@param **kwargs	key=value参数
####################################################
def LoadPropertys(module,managerid,path,**kwargs) :
	LoadBizPlugins(module,QTS_CFG_GROUP_PROPERTYS,QTS_CFG_PLUGINS_PROPERTYS,managerid,'',GetPropertyPath(path))
	for kwarg in kwargs :
		AppendItemForMainDict(module,QTS_CFG_GROUP_DSTRANSFERS,kwarg,kwargs[kwarg])

####################################################
#@brief 加载用户数据插件
#@param module 		应用模块名称
#@param managerid	资源管理ID
#@param log			日志键值
#@param path		库路径
#@param **kwargs	key=value参数
####################################################		
def LoadUserMarkets(managerid,log,path,**kwargs) :
	LoadBizPlugins(GetAppPath(),QTS_CFG_GROUP_MARKETS,QTS_CFG_PLUGINS_MARKETS,managerid,log,path)	
	for kwarg in kwargs :
		AppendItemForMainDict(GetAppPath(),QTS_CFG_GROUP_MARKETS,kwarg,kwargs[kwarg])
		
####################################################
#@brief 加载用户交易通道插件
#@param module 		应用模块名称
#@param managerid	资源管理ID
#@param log			日志键值
#@param path		库路径
#@param **kwargs	key=value参数
####################################################		
def LoadUserExchanges(managerid,log,path,**kwargs) :
	LoadBizPlugins(GetAppPath(),QTS_CFG_GROUP_EXCHANGES,QTS_CFG_PLUGINS_EXCHANGES,managerid,log,path)	
	for kwarg in kwargs :
		AppendItemForMainDict(GetAppPath(),QTS_CFG_GROUP_EXCHANGES,kwarg,kwargs[kwarg])
		
####################################################
#@brief 加载用户策略插件
#@param module 		应用模块名称
#@param managerid	资源管理ID
#@param log			日志键值
#@param path		库路径
#@param **kwargs	key=value参数
####################################################		
def LoadUserStrategies(managerid,log,path,**kwargs) :
	LoadBizPlugins(GetAppPath(),QTS_CFG_GROUP_STRATEGIES,QTS_CFG_PLUGINS_STRATEGIES,managerid,log,path)	
	for kwarg in kwargs :
		AppendItemForMainDict(GetAppPath(),QTS_CFG_GROUP_STRATEGIES,kwarg,kwargs[kwarg])
		
######################################################################################################################

####################################################
#@brief 运行用户的策略
#@param strategy 	策略械块
####################################################	
def RunUserStrategy(strategy) :
	if GetRunVersion() == debug :
		exec 'from ' + strategy + ' import *'
		
####################################################
#@brief 加载用户的策略配置
#@param cfg 	策略配置
####################################################		
def LoadUserStrategyCfg(cfg) :
	exec 'from ' + cfg + ' import *'
	
####################################################
#@brief 加载解析插件
#@param objid 		插件ID
#@param secuid		支持证券ID
#@param dllfile		库文件
#@param dllfun		导出函数
#@param path		库路径
#@param **kwargs	key=value参数
####################################################		
def CreatePluginForParser(objid,secuid,cfg,dllfile,dllfun,dllpath=GetLibPath(),**kwargs) :
	CreatePlugin(GetAppPath(),QTS_CFG_GROUP_PARSERS,QTS_CFG_PLUGINS_PARSERS,GeneratorObjectName(QTS_CFG_PLUGINS_PARSERS,objid),objid,secuid,cfg,BuildLibraryFile(dllfile),dllfun,dllpath)
	for kwarg in kwargs :
		AppendItemForMainDict(GetAppPath(),GeneratorObjectName(QTS_CFG_PLUGINS_PARSERS,objid),kwarg,kwargs[kwarg])	
	PrintPlugin(GetAppPath(),GeneratorObjectName(QTS_CFG_PLUGINS_PARSERS,objid))

def PrintForParser(objid) :
	PrintPlugin(GetAppPath(),GeneratorObjectName(QTS_CFG_PLUGINS_PARSERS,objid))

####################################################
#@brief 加载解析插件
#@param objid 		插件ID
#@param secuid		支持证券ID
#@param dllfile		库文件
#@param dllfun		导出函数
#@param path		库路径
#@param **kwargs	key=value参数
####################################################		
def CreatePluginForBackup(objid,secuid,cfg,dllfile,dllfun,dllpath=GetLibPath(),**kwargs) :
	CreatePlugin(GetAppPath(),QTS_CFG_GROUP_BACKUPS,QTS_CFG_PLUGINS_BACKUPS,GeneratorObjectName(QTS_CFG_PLUGINS_BACKUPS,objid),objid,secuid,cfg,BuildLibraryFile(dllfile),dllfun,dllpath)	
	for kwarg in kwargs :
		AppendItemForMainDict(GetAppPath(),GeneratorObjectName(QTS_CFG_PLUGINS_BACKUPS,objid),kwarg,kwargs[kwarg])		
	PrintPlugin(GetAppPath(),GeneratorObjectName(QTS_CFG_PLUGINS_BACKUPS,objid))

def PrintForBackup(objid) :
	PrintPlugin(GetAppPath(),GeneratorObjectName(QTS_CFG_PLUGINS_BACKUPS,objid))

####################################################
#@brief 加载加载插件
#@param objid 		插件ID
#@param secuid		支持证券ID
#@param dllfile		库文件
#@param dllfun		导出函数
#@param path		库路径
#@param **kwargs	key=value参数
####################################################	
def CreatePluginForLoader(objid,secuid,cfg,dllfile,dllfun,dllpath=GetLibPath(),**kwargs) :
	CreatePlugin(GetAppPath(),QTS_CFG_GROUP_LOADERS,QTS_CFG_PLUGINS_LOADERS,GeneratorObjectName(QTS_CFG_PLUGINS_LOADERS,objid),objid,secuid,cfg,BuildLibraryFile(dllfile),dllfun,dllpath)	
	for kwarg in kwargs :
		AppendItemForMainDict(GetAppPath(),GeneratorObjectName(QTS_CFG_PLUGINS_LOADERS,objid),kwarg,kwargs[kwarg])	
	PrintPlugin(GetAppPath(),GeneratorObjectName(QTS_CFG_PLUGINS_LOADERS,objid))

def PrintForLoader(objid) :
	PrintPlugin(GetAppPath(),GeneratorObjectName(QTS_CFG_PLUGINS_LOADERS,objid))

####################################################
#@brief 加载风控插件
#@param objid 		插件ID
#@param secuid		支持证券ID
#@param dllfile		库文件
#@param dllfun		导出函数
#@param path		库路径
#@param **kwargs	key=value参数
####################################################	
def CreatePluginForCheck(objid,secuid,cfg,dllfile,dllfun,dllpath=GetLibPath(),**kwargs) :
	CreatePlugin(GetAppPath(),QTS_CFG_GROUP_CHECKS,QTS_CFG_PLUGINS_CHECKS,GeneratorObjectName(QTS_CFG_PLUGINS_CHECKS,objid),objid,secuid,cfg,BuildLibraryFile(dllfile),dllfun,dllpath)	
	for kwarg in kwargs :
		AppendItemForMainDict(GetAppPath(),GeneratorObjectName(QTS_CFG_PLUGINS_CHECKS,objid),kwarg,kwargs[kwarg])	
	PrintPlugin(GetAppPath(),GeneratorObjectName(QTS_CFG_PLUGINS_CHECKS,objid))

def PrintForCheck(objid) :
	PrintPlugin(GetAppPath(),GeneratorObjectName(QTS_CFG_PLUGINS_CHECKS,objid))

####################################################
#@brief 加载算法插件
#@param objid 		插件ID
#@param secuid		支持证券ID
#@param dllfile		库文件
#@param dllfun		导出函数
#@param path		库路径
#@param **kwargs	key=value参数
####################################################		
def CreatePluginForAlgo(objid,secuid,cfg,dllfile,dllfun,dllpath=GetLibPath(),**kwargs) :
	CreatePlugin(GetAppPath(),QTS_CFG_GROUP_ALGOES,QTS_CFG_PLUGINS_ALGOES,GeneratorObjectName(QTS_CFG_PLUGINS_ALGOES,objid),objid,secuid,cfg,BuildLibraryFile(dllfile),dllfun,dllpath)		
	for kwarg in kwargs :
		AppendItemForMainDict(GetAppPath(),GeneratorObjectName(QTS_CFG_PLUGINS_ALGOES,objid),kwarg,kwargs[kwarg])	
	PrintPlugin(GetAppPath(),GeneratorObjectName(QTS_CFG_PLUGINS_ALGOES,objid))

def PrintForAlgo(objid) :
	PrintPlugin(GetAppPath(),GeneratorObjectName(QTS_CFG_PLUGINS_ALGOES,objid))

####################################################
#@brief 加载数据传输插件
#@param objid 		插件ID
#@param secuid		支持证券ID
#@param dllfile		库文件
#@param dllfun		导出函数
#@param path		库路径
#@param **kwargs	key=value参数
####################################################		
def CreatePluginForDSTransfer(objid,secuid,cfg,dllfile,dllfun,dllpath=GetLibPath(),**kwargs) :
	CreatePlugin(GetAppPath(),QTS_CFG_GROUP_DSTRANSFERS,QTS_CFG_PLUGINS_DSTRANSFERS,GeneratorObjectName(QTS_CFG_PLUGINS_DSTRANSFERS,objid),objid,secuid,cfg,BuildLibraryFile(dllfile),dllfun,dllpath)		
	for kwarg in kwargs :
		AppendItemForMainDict(GetAppPath(),GeneratorObjectName(QTS_CFG_PLUGINS_DSTRANSFERS,objid),kwarg,kwargs[kwarg])	
	PrintPlugin(GetAppPath(),GeneratorObjectName(QTS_CFG_PLUGINS_DSTRANSFERS,objid))

def PrintForDSTransfer(objid) :
	PrintPlugin(GetAppPath(),GeneratorObjectName(QTS_CFG_PLUGINS_DSTRANSFERS,objid))

####################################################
#@brief 加载交易网关传输插件
#@param objid 		插件ID
#@param secuid		支持证券ID
#@param dllfile		库文件
#@param dllfun		导出函数
#@param path		库路径
#@param **kwargs	key=value参数
####################################################		
def CreatePluginForGWTransfer(objid,secuid,cfg,dllfile,dllfun,dllpath=GetLibPath(),**kwargs) :
	CreatePlugin(GetAppPath(),QTS_CFG_GROUP_GWTRANSFERS,QTS_CFG_PLUGINS_GWTRANSFERS,GeneratorObjectName(QTS_CFG_PLUGINS_GWTRANSFERS,objid),objid,secuid,cfg,BuildLibraryFile(dllfile),dllfun,dllpath)		
	for kwarg in kwargs :
		AppendItemForMainDict(GetAppPath(),GeneratorObjectName(QTS_CFG_PLUGINS_GWTRANSFERS,objid),kwarg,kwargs[kwarg])	
	PrintPlugin(GetAppPath(),GeneratorObjectName(QTS_CFG_PLUGINS_GWTRANSFERS,objid))

def PrintForGWTransfer(objid) :
	PrintPlugin(GetAppPath(),GeneratorObjectName(QTS_CFG_PLUGINS_GWTRANSFERS,objid))

####################################################
#@brief 加载终端传输插件
#@param objid 		插件ID
#@param secuid		支持证券ID
#@param dllfile		库文件
#@param dllfun		导出函数
#@param path		库路径
#@param **kwargs	key=value参数
####################################################		
def CreatePluginForGUITransfer(objid,secuid,cfg,dllfile,dllfun,dllpath=GetLibPath(),**kwargs) :
	CreatePlugin(GetAppPath(),QTS_CFG_GROUP_GUITRANSFERS,QTS_CFG_PLUGINS_GUITRANSFERS,GeneratorObjectName(QTS_CFG_PLUGINS_GUITRANSFERS,objid),objid,secuid,cfg,BuildLibraryFile(dllfile),dllfun,dllpath)		
	for kwarg in kwargs :
		AppendItemForMainDict(GetAppPath(),GeneratorObjectName(QTS_CFG_PLUGINS_GUITRANSFERS,objid),kwarg,kwargs[kwarg])	
	PrintPlugin(GetAppPath(),GeneratorObjectName(QTS_CFG_PLUGINS_GUITRANSFERS,objid))

def PrintForGUITransfer(objid) :
	PrintPlugin(GetAppPath(),GeneratorObjectName(QTS_CFG_PLUGINS_GUITRANSFERS,objid))

####################################################
#@brief 加载远程风控传输插件
#@param objid 		插件ID
#@param secuid		支持证券ID
#@param dllfile		库文件
#@param dllfun		导出函数
#@param path		库路径
#@param **kwargs	key=value参数
####################################################		
def CreatePluginForCKTransfer(objid,secuid,cfg,dllfile,dllfun,dllpath=GetLibPath(),**kwargs) :
	CreatePlugin(GetAppPath(),QTS_CFG_GROUP_CKTRANSFERS,QTS_CFG_PLUGINS_CKTRANSFERS,GeneratorObjectName(QTS_CFG_PLUGINS_CKTRANSFERS,objid),objid,secuid,cfg,BuildLibraryFile(dllfile),dllfun,dllpath)		
	for kwarg in kwargs :
		AppendItemForMainDict(GetAppPath(),GeneratorObjectName(QTS_CFG_PLUGINS_CKTRANSFERS,objid),kwarg,kwargs[kwarg])	
	PrintPlugin(GetAppPath(),GeneratorObjectName(QTS_CFG_PLUGINS_CKTRANSFERS,objid))

def PrintForCKTransfer(objid) :
	PrintPlugin(GetAppPath(),GeneratorObjectName(QTS_CFG_PLUGINS_CKTRANSFERS,objid))

####################################################
#@brief 加载远程风控传输插件
#@param objid 		插件ID
#@param secuid		支持证券ID
#@param dllfile		库文件
#@param dllfun		导出函数
#@param path		库路径
#@param **kwargs	key=value参数
####################################################		
def CreatePluginForCPTransfer(objid,secuid,cfg,dllfile,dllfun,dllpath=GetLibPath(),**kwargs) :
	CreatePlugin(GetAppPath(),QTS_CFG_GROUP_CPTRANSFERS,QTS_CFG_PLUGINS_CPTRANSFERS,GeneratorObjectName(QTS_CFG_PLUGINS_CPTRANSFERS,objid),objid,secuid,cfg,BuildLibraryFile(dllfile),dllfun,dllpath)		
	for kwarg in kwargs :
		AppendItemForMainDict(GetAppPath(),GeneratorObjectName(QTS_CFG_PLUGINS_CPTRANSFERS,objid),kwarg,kwargs[kwarg])	
	PrintPlugin(GetAppPath(),GeneratorObjectName(QTS_CFG_PLUGINS_CPTRANSFERS,objid))

def PrintForCPTransfer(objid) :
	PrintPlugin(GetAppPath(),GeneratorObjectName(QTS_CFG_PLUGINS_CPTRANSFERS,objid))

####################################################
#@brief 加载传输插件
#@param objid 		插件ID
#@param secuid		支持证券ID
#@param dllfile		库文件
#@param dllfun		导出函数
#@param path		库路径
#@param **kwargs	key=value参数
####################################################		
def CreatePluginForTransfer(objid,secuid,cfg,dllfile,dllfun,dllpath=GetLibPath(),**kwargs) :
	CreatePlugin(GetAppPath(),QTS_CFG_GROUP_TRANSFERS,QTS_CFG_PLUGINS_TRANSFERS,GeneratorObjectName(QTS_CFG_PLUGINS_TRANSFERS,objid),objid,secuid,cfg,BuildLibraryFile(dllfile),dllfun,dllpath)	
	for kwarg in kwargs :
		AppendItemForMainDict(GetAppPath(),GeneratorObjectName(QTS_CFG_PLUGINS_TRANSFERS,objid),kwarg,kwargs[kwarg])	
	PrintPlugin(GetAppPath(),GeneratorObjectName(QTS_CFG_PLUGINS_TRANSFERS,objid))

def PrintForTransfer(objid) :
	PrintPlugin(GetAppPath(),GeneratorObjectName(QTS_CFG_PLUGINS_TRANSFERS,objid))

####################################################
#@brief 加载监控插件
#@param objid 		插件ID
#@param secuid		支持证券ID
#@param dllfile		库文件
#@param dllfun		导出函数
#@param path		库路径
#@param **kwargs	key=value参数
####################################################	
def CreatePluginForMonitor(objid,secuid,cfg,dllfile,dllfun,dllpath=GetLibPath(),**kwargs) :
	CreatePlugin(GetAppPath(),QTS_CFG_GROUP_MONITORS,QTS_CFG_PLUGINS_MONITORS,GeneratorObjectName(QTS_CFG_PLUGINS_MONITORS,objid),objid,secuid,cfg,BuildLibraryFile(dllfile),dllfun,dllpath)		
	for kwarg in kwargs :
		AppendItemForMainDict(GetAppPath(),GeneratorObjectName(QTS_CFG_PLUGINS_MONITORS,objid),kwarg,kwargs[kwarg])	
	PrintPlugin(GetAppPath(),GeneratorObjectName(QTS_CFG_PLUGINS_MONITORS,objid))

def PrintForMonitor(objid) :
	PrintPlugin(GetAppPath(),GeneratorObjectName(QTS_CFG_PLUGINS_MONITORS,objid))

####################################################
#@brief 加载计算插件
#@param objid 		插件ID
#@param secuid		支持证券ID
#@param dllfile		库文件
#@param dllfun		导出函数
#@param path		库路径
#@param **kwargs	key=value参数
####################################################	
def CreatePluginForCalculate(objid,secuid,cfg,dllfile,dllfun,dllpath=GetLibPath(),**kwargs) :
	CreatePlugin(GetAppPath(),QTS_CFG_GROUP_CALCULATES,QTS_CFG_PLUGINS_CALCULATES,GeneratorObjectName(QTS_CFG_PLUGINS_CALCULATES,objid),objid,secuid,cfg,BuildLibraryFile(dllfile),dllfun,dllpath)		
	for kwarg in kwargs :
		AppendItemForMainDict(GetAppPath(),GeneratorObjectName(QTS_CFG_PLUGINS_CALCULATES,objid),kwarg,kwargs[kwarg])	
	PrintPlugin(GetAppPath(),GeneratorObjectName(QTS_CFG_PLUGINS_CALCULATES,objid))

def PrintForCalculate(objid) :
	PrintPlugin(GetAppPath(),GeneratorObjectName(QTS_CFG_PLUGINS_CALCULATES,objid))

####################################################
#@brief 加载策略插件
#@param objid 		插件ID
#@param secuid		支持证券ID
#@param dllfile		库文件
#@param dllfun		导出函数
#@param path		库路径
#@param **kwargs	key=value参数
####################################################	
def CreatePluginForStrategy(objid,secuid,cfg,dllfile,dllfun,dllpath=GetLibPath(),**kwargs) :
	CreatePlugin(GetAppPath(),QTS_CFG_GROUP_STRATEGIES,QTS_CFG_PLUGINS_STRATEGIES,GeneratorObjectName(QTS_CFG_PLUGINS_STRATEGIES,objid),objid,secuid,cfg,BuildLibraryFile(dllfile),dllfun,dllpath)		
	for kwarg in kwargs :
		AppendItemForMainDict(GetAppPath(),GeneratorObjectName(QTS_CFG_PLUGINS_STRATEGIES,objid),kwarg,kwargs[kwarg])	
	LoadUserStrategyCfg(cfg)	
	PrintPlugin(GetAppPath(),GeneratorObjectName(QTS_CFG_PLUGINS_STRATEGIES,objid))

def PrintForStrategy(objid) :
	PrintPlugin(GetAppPath(),GeneratorObjectName(QTS_CFG_PLUGINS_STRATEGIES,objid))

####################################################
#@brief 加载逻辑插件
#@param objid 		插件ID
#@param secuid		支持证券ID
#@param dllfile		库文件
#@param dllfun		导出函数
#@param path		库路径
#@param **kwargs	key=value参数
####################################################	
def CreatePluginForLogic(objid,secuid,cfg,dllfile,dllfun,dllpath=GetLibPath(),**kwargs) :
	CreatePlugin(GetAppPath(),QTS_CFG_GROUP_LOGICS,QTS_CFG_PLUGINS_LOGICS,GeneratorObjectName(QTS_CFG_PLUGINS_LOGICS,objid),objid,secuid,cfg,BuildLibraryFile(dllfile),dllfun,dllpath)		
	for kwarg in kwargs :
		AppendItemForMainDict(GetAppPath(),GeneratorObjectName(QTS_CFG_PLUGINS_LOGICS,objid),kwarg,kwargs[kwarg])	
	PrintPlugin(GetAppPath(),GeneratorObjectName(QTS_CFG_PLUGINS_LOGICS,objid))

def PrintForLogic(objid) :
	PrintPlugin(GetAppPath(),GeneratorObjectName(QTS_CFG_PLUGINS_LOGICS,objid))

####################################################
#@brief 加载过滤插件
#@param objid 		插件ID
#@param secuid		支持证券ID
#@param dllfile		库文件
#@param dllfun		导出函数
#@param path		库路径
#@param **kwargs	key=value参数
####################################################	
def CreatePluginForFilter(objid,secuid,cfg,dllfile,dllfun,dllpath=GetLibPath(),**kwargs) :
	CreatePlugin(GetAppPath(),QTS_CFG_GROUP_FILTERS,QTS_CFG_PLUGINS_FILTERS,GeneratorObjectName(QTS_CFG_PLUGINS_FILTERS,objid),objid,secuid,cfg,BuildLibraryFile(dllfile),dllfun,dllpath)		
	for kwarg in kwargs :
		AppendItemForMainDict(GetAppPath(),GeneratorObjectName(QTS_CFG_PLUGINS_FILTERS,objid),kwarg,kwargs[kwarg])	
	PrintPlugin(GetAppPath(),GeneratorObjectName(QTS_CFG_PLUGINS_FILTERS,objid))

def PrintForFilter(objid) :
	PrintPlugin(GetAppPath(),GeneratorObjectName(QTS_CFG_PLUGINS_FILTERS,objid))

####################################################
#@brief 加载市场插件
#@param objid 		插件ID
#@param secuid		支持证券ID
#@param dllfile		库文件
#@param dllfun		导出函数
#@param path		库路径
#@param **kwargs	key=value参数
####################################################	
def CreatePluginForMarket(objid,secuid,cfg,dllfile,dllfun,dllpath=GetLibPath(),**kwargs) :
	CreatePlugin(GetAppPath(),QTS_CFG_GROUP_MARKETS,QTS_CFG_PLUGINS_MARKETS,GeneratorObjectName(QTS_CFG_PLUGINS_MARKETS,objid),objid,secuid,cfg,BuildLibraryFile(dllfile),dllfun,dllpath)		
	for kwarg in kwargs :
		AppendItemForMainDict(GetAppPath(),GeneratorObjectName(QTS_CFG_PLUGINS_MARKETS,objid),kwarg,kwargs[kwarg])	
	PrintPlugin(GetAppPath(),GeneratorObjectName(QTS_CFG_PLUGINS_MARKETS,objid))

def PrintForMarket(objid) :
	PrintPlugin(GetAppPath(),GeneratorObjectName(QTS_CFG_PLUGINS_MARKETS,objid))

####################################################
#@brief 加载交易通道插件
#@param objid 		插件ID
#@param secuid		支持证券ID
#@param dllfile		库文件
#@param dllfun		导出函数
#@param path		库路径
#@param **kwargs	key=value参数
####################################################	
def CreatePluginForExchange(objid,secuid,cfg,dllfile,dllfun,dllpath=GetLibPath(),**kwargs) :
	CreatePlugin(GetAppPath(),QTS_CFG_GROUP_EXCHANGES,QTS_CFG_PLUGINS_EXCHANGES,GeneratorObjectName(QTS_CFG_PLUGINS_EXCHANGES,objid),objid,secuid,cfg,BuildLibraryFile(dllfile),dllfun,dllpath)		
	for kwarg in kwargs :
		AppendItemForMainDict(GetAppPath(),GeneratorObjectName(QTS_CFG_PLUGINS_EXCHANGES,objid),kwarg,kwargs[kwarg])	
	PrintPlugin(GetAppPath(),GeneratorObjectName(QTS_CFG_PLUGINS_EXCHANGES,objid))

def PrintForExchange(objid) :
	PrintPlugin(GetAppPath(),GeneratorObjectName(QTS_CFG_PLUGINS_EXCHANGES,objid))

####################################################
#@brief 加载传输插件
#@param objid 		插件ID
#@param secuid		支持证券ID
#@param **kwargs	key=value参数
####################################################
def CreatePluginForProperty(objid,secuid,name,**kwargs) :
	CreatePlugin(GetAppPath(),QTS_CFG_GROUP_PROPERTYS,QTS_CFG_PLUGINS_PROPERTYS,GeneratorObjectName(QTS_CFG_PLUGINS_PROPERTYS,objid),objid,secuid,'','','','')
	AppendItemForMainDict(GetAppPath(),GeneratorObjectName(QTS_CFG_PLUGINS_PROPERTYS,objid),QTS_CFG_KEY_NAME,name)
	for kwarg in kwargs :
		AppendItemForMainDict(GetAppPath(),GeneratorObjectName(QTS_CFG_PLUGINS_PROPERTYS,objid),kwarg,kwargs[kwarg])
	PrintPlugin(GetAppPath(),GeneratorObjectName(QTS_CFG_PLUGINS_PROPERTYS,objid))

####################################################
#@brief 加载用户数据插件
#@param objid 		插件ID
#@param secuid		支持证券ID
#@param dllfile		库文件
#@param dllfun		导出函数
#@param path		库路径
#@param **kwargs	key=value参数
####################################################		
def CreateUserPluginForMarket(objid,secuid,log,cfg,dllfile,dllfun,dllpath=GetLibPath(),**kwargs) :
	CreatePluginHasLog(GetAppPath(),QTS_CFG_GROUP_MARKETS,QTS_CFG_PLUGINS_MARKETS,GeneratorObjectName(QTS_CFG_PLUGINS_MARKETS,objid),objid,secuid,log,cfg,BuildLibraryFile('QtsProtoMarketApi'),'CreateMarketApi',GetLibPath())		
	AppendPropertyForMarket(objid,QTS_CFG_KEY_MKFILE,BuildLibraryFile(dllfile))
	AppendPropertyForMarket(objid,QTS_CFG_KEY_MKFUN,dllfun)	
	AppendPropertyForMarket(objid,QTS_CFG_KEY_SUBPATH,dllpath)	
	for kwarg in kwargs :
		AppendItemForMainDict(GetAppPath(),GeneratorObjectName(QTS_CFG_PLUGINS_MARKETS,objid),kwarg,kwargs[kwarg])	
	PrintPlugin(GetAppPath(),GeneratorObjectName(QTS_CFG_PLUGINS_MARKETS,objid))

####################################################
#@brief 加载用户交易通道插件
#@param objid 		插件ID
#@param secuid		支持证券ID
#@param dllfile		库文件
#@param dllfun		导出函数
#@param path		库路径
#@param **kwargs	key=value参数
####################################################		
def CreateUserPluginForExchange(objid,secuid,log,cfg,dllfile,dllfun,dllpath=GetLibPath(),**kwargs) :
	CreatePluginHasLog(GetAppPath(),QTS_CFG_GROUP_EXCHANGES,QTS_CFG_PLUGINS_EXCHANGES,GeneratorObjectName(QTS_CFG_PLUGINS_EXCHANGES,objid),objid,secuid,log,cfg,BuildLibraryFile('QtsProtoExchangeApi'),'CreateExchageApi',GetLibPath())		
	AppendPropertyForExchange(objid,QTS_CFG_KEY_EXFILE,BuildLibraryFile(dllfile))
	AppendPropertyForExchange(objid,QTS_CFG_KEY_EXFUN,dllfun)	
	AppendPropertyForExchange(objid,QTS_CFG_KEY_SUBPATH,dllpath)	
	for kwarg in kwargs :
		AppendItemForMainDict(GetAppPath(),GeneratorObjectName(QTS_CFG_PLUGINS_EXCHANGES,objid),kwarg,kwargs[kwarg])	
	PrintPlugin(GetAppPath(),GeneratorObjectName(QTS_CFG_PLUGINS_EXCHANGES,objid))
	
####################################################
#@brief 加载用户C++策略插件
#@param objid 		插件ID
#@param secuid		支持证券ID
#@param dllfile		库文件
#@param dllfun		导出函数
#@param path		库路径
#@param **kwargs	key=value参数
####################################################	
def CreateUserPluginForCStrategy(objid,secuid,log,cfg,dllfile,dllfun,dllpath=GetLibPath(),**kwargs) :
	CreatePluginHasLog(GetAppPath(),QTS_CFG_GROUP_STRATEGIES,QTS_CFG_PLUGINS_STRATEGIES,GeneratorObjectName(QTS_CFG_PLUGINS_STRATEGIES,objid),objid,secuid,log,cfg,BuildLibraryFile('QtsCPlusTrade'),'CreateCPlusTrade',GetLibPath())		
	AppendPropertyForStrategy(objid,QTS_CFG_KEY_TRADEFILE,BuildLibraryFile(dllfile))
	AppendPropertyForStrategy(objid,QTS_CFG_KEY_TRADEFUN,dllfun)	
	AppendPropertyForStrategy(objid,QTS_CFG_KEY_SUBPATH,dllpath)
	for kwarg in kwargs :
		AppendItemForMainDict(GetAppPath(),GeneratorObjectName(QTS_CFG_PLUGINS_STRATEGIES,objid),kwarg,kwargs[kwarg])	
	LoadUserStrategyCfg(cfg)
	PrintPlugin(GetAppPath(),GeneratorObjectName(QTS_CFG_PLUGINS_STRATEGIES,objid))	

####################################################
#@brief 加载用户Python策略插件
#@param objid 		插件ID
#@param secuid		支持证券ID
#@param dllfile		库文件
#@param dllfun		导出函数
#@param path		库路径
#@param **kwargs	key=value参数
####################################################		
def CreateUserPluginForPyStrategy(objid,secuid,log,cfg,dllfile,dllfun,dllpath=GetLibPath(),**kwargs) :
	if GetRunVersion() == release :
		CreatePluginHasLog(GetAppPath(),QTS_CFG_GROUP_STRATEGIES,QTS_CFG_PLUGINS_STRATEGIES,GeneratorObjectName(QTS_CFG_PLUGINS_STRATEGIES,objid),objid,secuid,log,cfg,BuildLibraryFile('QtsPythonTrade'),'CreatePythonTrade',GetLibPath())		
	else :
		CreatePluginHasLog(GetAppPath(),QTS_CFG_GROUP_STRATEGIES,QTS_CFG_PLUGINS_STRATEGIES,GeneratorObjectName(QTS_CFG_PLUGINS_STRATEGIES,objid),objid,secuid,log,cfg,BuildLibraryFile('QtsPythonDTrade'),'CreatePythonDTrade',GetLibPath())		
	AppendPropertyForStrategy(objid,QTS_CFG_KEY_TRADEFILE,dllfile)
	AppendPropertyForStrategy(objid,QTS_CFG_KEY_TRADEFUN,dllfun)	
	AppendPropertyForStrategy(objid,QTS_CFG_KEY_SUBPATH,dllpath)
	for kwarg in kwargs :
		AppendItemForMainDict(GetAppPath(),GeneratorObjectName(QTS_CFG_PLUGINS_STRATEGIES,objid),kwarg,kwargs[kwarg])	
	LoadUserStrategyCfg(cfg)
	RunUserStrategy(dllfile)
	PrintPlugin(GetAppPath(),GeneratorObjectName(QTS_CFG_PLUGINS_STRATEGIES,objid))
	
######################################################################################################	
####################################################
#@brief 设置策略名称
#@param objid 		策略插件ID
#@param name		策略名称
####################################################	
def SetPluginNameForPyStrategy(objid,name) :
	SetPluginName(GetAppPath(),GeneratorObjectName(QTS_CFG_PLUGINS_STRATEGIES,objid),name)
	
######################################################################################################
####################################################
#@brief 添加解析管理器属性
#@param module 		应用模块名称
#@param key 		属性键值
#@param value		属性值
####################################################
def AppendPropertyForPropertys(module,key,value) :
	AppendItemForMainDict(module,QTS_CFG_GROUP_PROPERTYS,key,value)

####################################################
#@brief 添加解析管理器属性
#@param module 		应用模块名称
#@param key 		属性键值
#@param value		属性值
####################################################	
def AppendPropertyForParsers(module,key,value) :
	AppendItemForMainDict(module,QTS_CFG_GROUP_PARSERS,key,value)
	
####################################################
#@brief 添加备份管理器属性
#@param module 		应用模块名称
#@param key 		属性键值
#@param value		属性值
####################################################		
def AppendPropertyForBackups(module,key,value) :
	AppendItemForMainDict(module,QTS_CFG_GROUP_BACKUPS,key,value)
	
####################################################
#@brief 添加加载管理器属性
#@param module 		应用模块名称
#@param key 		属性键值
#@param value		属性值
####################################################	
def AppendPropertyForLoaders(module,key,value) :
	AppendItemForMainDict(module,QTS_CFG_GROUP_LOADERS,key,value)
	
####################################################
#@brief 添加风控管理器属性
#@param module 		应用模块名称
#@param key 		属性键值
#@param value		属性值
####################################################		
def AppendPropertyForChecks(module,key,value) :
	AppendItemForMainDict(module,QTS_CFG_GROUP_CHECKS,key,value)
	
####################################################
#@brief 添加算法管理器属性
#@param module 		应用模块名称
#@param key 		属性键值
#@param value		属性值
####################################################	
def AppendPropertyForAlgoes(module,key,value) :
	AppendItemForMainDict(module,QTS_CFG_GROUP_ALGOES,key,value)	
	
####################################################
#@brief 添加数据传输管理器属性
#@param module 		应用模块名称
#@param key 		属性键值
#@param value		属性值
####################################################	
def AppendPropertyForDSTransfers(module,key,value) :
	AppendItemForMainDict(module,QTS_CFG_GROUP_DSTRANSFERS,key,value)
	
####################################################
#@brief 添加交易网关传输管理器属性
#@param module 		应用模块名称
#@param key 		属性键值
#@param value		属性值
####################################################	
def AppendPropertyForGWTransfers(module,key,value) :
	AppendItemForMainDict(module,QTS_CFG_GROUP_GWTRANSFERS,key,value)
	
####################################################
#@brief 添加终端传输管理器属性
#@param module 		应用模块名称
#@param key 		属性键值
#@param value		属性值
####################################################	
def AppendPropertyForGUITransfers(module,key,value) :
	AppendItemForMainDict(module,QTS_CFG_GROUP_GUITRANSFERS,key,value)
	
####################################################
#@brief 添加终端传输管理器属性
#@param module 		应用模块名称
#@param key 		属性键值
#@param value		属性值
####################################################	
def AppendPropertyForCKTransfers(module,key,value) :
	AppendItemForMainDict(module,QTS_CFG_GROUP_CKTRANSFERS,key,value)
	
####################################################
#@brief 添加终端传输管理器属性
#@param module 		应用模块名称
#@param key 		属性键值
#@param value		属性值
####################################################	
def AppendPropertyForCPTransfers(module,key,value) :
	AppendItemForMainDict(module,QTS_CFG_GROUP_CPTRANSFERS,key,value)
	
####################################################
#@brief 添加传输管理器属性
#@param module 		应用模块名称
#@param key 		属性键值
#@param value		属性值
####################################################	
def AppendPropertyForTransfers(module,key,value) :
	AppendItemForMainDict(module,QTS_CFG_GROUP_TRANSFERS,key,value)
	
####################################################
#@brief 添加监控管理器属性
#@param module 		应用模块名称
#@param key 		属性键值
#@param value		属性值
####################################################	
def AppendPropertyForMonitors(module,key,value) :
	AppendItemForMainDict(module,QTS_CFG_GROUP_MONITORS,key,value)	
	
####################################################
#@brief 添加计算管理器属性
#@param module 		应用模块名称
#@param key 		属性键值
#@param value		属性值
####################################################	
def AppendPropertyForCalculates(module,key,value) :
	AppendItemForMainDict(module,QTS_CFG_GROUP_CALCULATES,key,value)
	
####################################################
#@brief 添加策略管理器属性
#@param module 		应用模块名称
#@param key 		属性键值
#@param value		属性值
####################################################	
def AppendPropertyForStrategies(module,key,value) :
	AppendItemForMainDict(module,QTS_CFG_GROUP_STRATEGIES,key,value)	

####################################################
#@brief 添加逻辑管理器属性
#@param module 		应用模块名称
#@param key 		属性键值
#@param value		属性值
####################################################	
def AppendPropertyForLogics(module,key,value) :
	AppendItemForMainDict(module,QTS_CFG_GROUP_LOGICS,key,value)	

####################################################
#@brief 添加过滤管理器属性
#@param module 		应用模块名称
#@param key 		属性键值
#@param value		属性值
####################################################	
def AppendPropertyForFilters(module,key,value) :
	AppendItemForMainDict(module,QTS_CFG_GROUP_FILTERS,key,value)	

####################################################
#@brief 添加数据管理器属性
#@param module 		应用模块名称
#@param key 		属性键值
#@param value		属性值
####################################################	
def AppendPropertyForMarkets(module,key,value) :
	AppendItemForMainDict(module,QTS_CFG_GROUP_MARKETS,key,value)	

####################################################
#@brief 添加交易通道管理器属性
#@param module 		应用模块名称
#@param key 		属性键值
#@param value		属性值
####################################################	
def AppendPropertyForExchanges(module,key,value) :
	AppendItemForMainDict(module,QTS_CFG_GROUP_EXCHANGES,key,value)	
	
######################################################################################################
####################################################
#@brief 添加解析插件属性
#@param objid 		插件ID
#@param key 		属性键值
#@param value		属性值
####################################################
def AppendPropertyForParser(objid,key,value) :
	AppendItemForMainDict(GetAppPath(),GeneratorObjectName(QTS_CFG_PLUGINS_PARSERS,objid),key,value)
	
####################################################
#@brief 添加备份插件属性
#@param objid 		插件ID
#@param key 		属性键值
#@param value		属性值
####################################################	
def AppendPropertyForBackup(objid,key,value) :
	AppendItemForMainDict(GetAppPath(),GeneratorObjectName(QTS_CFG_PLUGINS_BACKUPS,objid),key,value)
	
####################################################
#@brief 添加加载插件属性
#@param objid 		插件ID
#@param key 		属性键值
#@param value		属性值
####################################################	
def AppendPropertyForLoader(objid,key,value) :
	AppendItemForMainDict(GetAppPath(),GeneratorObjectName(QTS_CFG_PLUGINS_LOADERS,objid),key,value)
	
####################################################
#@brief 添加风插件属性
#@param objid 		插件ID
#@param key 		属性键值
#@param value		属性值
####################################################	
def AppendPropertyForCheck(objid,key,value) :
	AppendItemForMainDict(GetAppPath(),GeneratorObjectName(QTS_CFG_PLUGINS_CHECKS,objid),key,value)
	
####################################################
#@brief 添加算法插件属性
#@param objid 		插件ID
#@param key 		属性键值
#@param value		属性值
####################################################	
def AppendPropertyForAlgo(objid,key,value) :
	AppendItemForMainDict(GetAppPath(),GeneratorObjectName(QTS_CFG_PLUGINS_ALGOES,objid),key,value)	
	
####################################################
#@brief 添加数据传输插件属性
#@param objid 		插件ID
#@param key 		属性键值
#@param value		属性值
####################################################	
def AppendPropertyForDSTransfer(objid,key,value) :
	AppendItemForMainDict(GetAppPath(),GeneratorObjectName(QTS_CFG_PLUGINS_DSTRANSFERS,objid),key,value)

####################################################
#@brief 添加数据传输插件属性
#@param objid 		插件ID
#@param key 		属性键值
#@param value		属性值
####################################################
def AppendPropertyForProperty(objid,key,value) :
	AppendItemForMainDict(GetAppPath(),GeneratorObjectName(QTS_CFG_PLUGINS_PROPERTYS,objid),key,value)

####################################################
#@brief 添加交易网关传输插件属性
#@param objid 		插件ID
#@param key 		属性键值
#@param value		属性值
####################################################	
def AppendPropertyForGWTransfer(objid,key,value) :
	AppendItemForMainDict(GetAppPath(),GeneratorObjectName(QTS_CFG_PLUGINS_GWTRANSFERS,objid),key,value)
	
####################################################
#@brief 添加终端传输插件属性
#@param objid 		插件ID
#@param key 		属性键值
#@param value		属性值
####################################################	
def AppendPropertyForGUITransfer(objid,key,value) :
	AppendItemForMainDict(GetAppPath(),GeneratorObjectName(QTS_CFG_PLUGINS_GUITRANSFERS,objid),key,value)
	
####################################################
#@brief 添加传输插件属性
#@param objid 		插件ID
#@param key 		属性键值
#@param value		属性值
####################################################	
def AppendPropertyForTransfer(objid,key,value) :
	AppendItemForMainDict(GetAppPath(),GeneratorObjectName(QTS_CFG_PLUGINS_TRANSFERS,objid),key,value)
	
####################################################
#@brief 添加监控插件属性
#@param objid 		插件ID
#@param key 		属性键值
#@param value		属性值
####################################################	
def AppendPropertyForMonitor(objid,key,value) :
	AppendItemForMainDict(GetAppPath(),GeneratorObjectName(QTS_CFG_PLUGINS_MONITORS,objid),key,value)	
	
####################################################
#@brief 添加计算插件属性
#@param objid 		插件ID
#@param key 		属性键值
#@param value		属性值
####################################################	
def AppendPropertyForCalculate(objid,key,value) :
	AppendItemForMainDict(GetAppPath(),GeneratorObjectName(QTS_CFG_PLUGINS_CALCULATES,objid),key,value)
	
####################################################
#@brief 添加策略插件属性
#@param objid 		插件ID
#@param key 		属性键值
#@param value		属性值
####################################################	
def AppendPropertyForStrategy(objid,key,value) :
	AppendItemForMainDict(GetAppPath(),GeneratorObjectName(QTS_CFG_PLUGINS_STRATEGIES,objid),key,value)	

####################################################
#@brief 添加逻辑插件属性
#@param objid 		插件ID
#@param key 		属性键值
#@param value		属性值
####################################################	
def AppendPropertyForLogic(objid,key,value) :
	AppendItemForMainDict(GetAppPath(),GeneratorObjectName(QTS_CFG_PLUGINS_LOGICS,objid),key,value)	

####################################################
#@brief 添加过滤插件属性
#@param objid 		插件ID
#@param key 		属性键值
#@param value		属性值
####################################################	
def AppendPropertyForFilter(objid,key,value) :
	AppendItemForMainDict(GetAppPath(),GeneratorObjectName(QTS_CFG_PLUGINS_FILTERS,objid),key,value)	

####################################################
#@brief 添加数据插件属性
#@param objid 		插件ID
#@param key 		属性键值
#@param value		属性值
####################################################	
def AppendPropertyForMarket(objid,key,value) :
	AppendItemForMainDict(GetAppPath(),GeneratorObjectName(QTS_CFG_PLUGINS_MARKETS,objid),key,value)	

####################################################
#@brief 添加交易通道插件属性
#@param objid 		插件ID
#@param key 		属性键值
#@param value		属性值
####################################################	
def AppendPropertyForExchange(objid,key,value) :
	AppendItemForMainDict(GetAppPath(),GeneratorObjectName(QTS_CFG_PLUGINS_EXCHANGES,objid),key,value)	
	
####################################################
#@brief 为策略添加参数配置
#@param objid 		插件ID
#@param name 		参数种子
####################################################	
def SetParameterForStrategy(objid,name) :
	AppendPropertyForStrategy(objid,QTS_CFG_KEY_INSTRUMENT, GetInstrumentNameForStrategy(name))
	AppendPropertyForStrategy(objid,QTS_CFG_KEY_PARAMETER, GetParameterNameForStrategy(name))
	AppendPropertyForStrategy(objid,QTS_CFG_KEY_COMMENT, GetCommentNameForStrategy(name))
	AppendPropertyForStrategy(objid,QTS_CFG_KEY_COMMAND, GetCommandNameForStrategy(name))
	
############################################################################################	
####################################################
#@brief 设置数据传输远程信息
#@param objid 		插件ID
#@param address 	IP地址
#@param port 		网络端口
#@param heart 		心跳延时
####################################################
def SetRemoteInfoForDSTransfer(objid,address='',port=0,heart=30) :
	SetRemoteInfo(GetAppPath(),GeneratorObjectName(QTS_CFG_PLUGINS_DSTRANSFERS,objid),address,port,heart)
	
####################################################
#@brief 设置交易网关传输远程信息
#@param objid 		插件ID
#@param address 	IP地址
#@param port 		网络端口
#@param heart 		心跳延时
####################################################	
def SetRemoteInfoForGWTransfer(objid,address='',port=0,heart=30) :
	SetRemoteInfo(GetAppPath(),GeneratorObjectName(QTS_CFG_PLUGINS_GWTRANSFERS,objid),address,port,heart)
	
####################################################
#@brief 设置终端传输远程信息
#@param objid 		插件ID
#@param address 	IP地址
#@param port 		网络端口
#@param heart 		心跳延时
####################################################	
def SetRemoteInfoForGUITransfer(objid,address='',port=0,heart=30) :
	SetRemoteInfo(GetAppPath(),GeneratorObjectName(QTS_CFG_PLUGINS_GUITRANSFERS,objid),address,port,heart)

####################################################
#@brief 设置传输远程信息
#@param objid 		插件ID
#@param address 	IP地址
#@param port 		网络端口
#@param heart 		心跳延时
####################################################	
def SetRemoteInfoForTransfer(objid,address='',port=0,heart=30) :
	SetRemoteInfo(GetAppPath(),GeneratorObjectName(QTS_CFG_PLUGINS_TRANSFERS,objid),address,port,heart)
	
####################################################
#@brief 设置数据远程信息
#@param objid 		插件ID
#@param address 	IP地址
#@param port 		网络端口
#@param heart 		心跳延时
####################################################	
def SetRemoteInfoForMarket(objid,address='',port=0,heart=30) :
	SetRemoteInfo(GetAppPath(),GeneratorObjectName(QTS_CFG_PLUGINS_MARKETS,objid),address,port,heart)

####################################################
#@brief 设置交易通道远程信息
#@param objid 		插件ID
#@param address 	IP地址
#@param port 		网络端口
#@param heart 		心跳延时
####################################################	
def SetRemoteInfoForExchange(objid,address='',port=0,heart=30) :
	SetRemoteInfo(GetAppPath(),GeneratorObjectName(QTS_CFG_PLUGINS_EXCHANGES,objid),address,port,heart)
	
############################################################################################
####################################################
#@brief 得到算法插件的ID
#@param objid 		插件ID
#@return 插件ID
####################################################
def GetPluginIdForAlgo(objid) :
	return GeneratorObjectIdByManager(GetAppPath(),QTS_CFG_GROUP_ALGOES,objid)
	
####################################################
#@brief 得到风控插件的ID
#@param objid 		插件ID
#@return 插件ID
####################################################	
def GetPluginIdForCheck(objid) :
	return GeneratorObjectIdByManager(GetAppPath(),QTS_CFG_GROUP_CHECKS,objid)

####################################################
#@brief 得到风控计算的ID
#@param objid 		插件ID
#@return 插件ID
####################################################	
def GetPluginIdForCalculate(objid) :
	return GeneratorObjectIdByManager(GetAppPath(),QTS_CFG_GROUP_CALCULATES,objid)

####################################################
#@brief 得到加载的ID
#@param objid 		插件ID
#@return 插件ID
####################################################	
def GetPluginIdForLoader(objid) :
	return GeneratorObjectIdByManager(GetAppPath(),QTS_CFG_GROUP_LOADERS,objid)
	
####################################################
#@brief 得到加载的ID
#@param objid 		插件ID
#@return 插件ID
####################################################	
def GetPluginIdForBackup(objid) :
	return GeneratorObjectIdByManager(GetAppPath(),QTS_CFG_GROUP_BACKUPS,objid)
	
############################################################################################
####################################################
#@brief 生成64位的帐号
#@param account 	帐号
#@return 64位的帐号
####################################################
def BuildAccount(account) :
	return ToInt64(account)
	
####################################################
#@brief 生成64位的帐号集
#@param *args 	帐号集
#@return 64位的帐号集
####################################################	
def BuildAccounts(*args) :
	accounts = list()
	for arg in args :
		accounts.append(BuildAccount(arg))
	return accounts

####################################################
#@brief 生成订单号
#@param objid 		插件ID
#@param orderid 	基础订单号
#@return 订单号
####################################################	
def BuildOrderId(objid,orderid) :
	return long(GeneratorObjectIdByManager(GetAppPath(),QTS_CFG_GROUP_STRATEGIES,objid) * 100000000 + orderid)

####################################################
#@brief 生成订单号
#@param objid 		插件ID
#@param orderid 	基础订单号
#@return 订单号
####################################################	
def BuildAlgoOrderId(objid,orderid) :
	return long(GeneratorObjectIdByManager(GetAppPath(),QTS_CFG_GROUP_ALGOES,objid) * 100000000 + orderid)

############################################################################################
############################################################################################
#对策略参数操作的函数
############################################################################################

####################################################
#@brief 创建策略参数的交易标的参数节点
#@param name 		参数节点名称
####################################################		
def CreateInstruments(name) :
	CreateInstrumentsForStrategy(name)
	
####################################################
#@brief 创建策略参数的动态参数节点
#@param name 		参数节点名称
####################################################		
def CreateParameters(name) :
	CreateParametersForStrategy(name)
	
####################################################
#@brief 创建策略参数的静态参数节点
#@param name 		参数节点名称
####################################################		
def CreateComments(name) :
	CreateCommentsForStrategy(name)
	
####################################################
#@brief 创建策略参数的命令参数节点
#@param name 		参数节点名称
####################################################		
def CreateCommands(name) :
	CreateCommandsForStrategy(name)
	
####################################################
#@brief 创建策略交易标的参数子节点
#@param 0  listname 字典名称
#@param 1  key		配置键值，在一个策略中必须唯一
#@param 2  name		配置变量的名称
#@param 3  codetype	代码类型，暂支持：QTS_TRADE_UNKONWN,QTS_TRADE_CODE,QTS_TRADE_SIGNAL,QTS_TRADE_BASKET,QTS_TRADE_INDEX,QTS_TRADE_OWNER
#@param 4  market 	市场
#@param 5  category 品种
#@param 6  secucode 证券代码
#@param 7  index   	控件的排例顺序，控制显示
#@param 8  level	控件的层级，控制显示
#@param 9  status   显示状态，是否显示在GUI上，暂支持：QTS_INSTRUMENT_STATUS_DISPLAY,QTS_INSTRUMENT_STATUS_HIDE
#@param 10 mode    	控制类型，是否服务端推送相应数据，暂支持：QTS_INSTRUMENT_MODE_NONE,QTS_INSTRUMENT_MODE_PNL,QTS_INSTRUMENT_MODE_BOOK,QTS_INSTRUMENT_MODE_BOOK_PNL
#@param 11 component	控件的填充内容格式(序号:文本,序号:文本,....)
#@param 12 style		控件样式
#@return 参数在表中所有的位置
####################################################
def CreateInstrument(*args,**kwargs) :
	return AppendInstrumentForStrategy(*args,**kwargs)
	
####################################################
#@brief 设置策略交易标参数的级别
#@param listname 	参数子节点名称
#@param pos 		参数位置
#@param level 		参数级别
####################################################	
def SetLevelForInstrument(listname,pos,level=0) :
	SetPropertyForInstrument(listname,pos,5,level)
	
####################################################
#@brief 设置策略交易标参数的状态
#@param listname 	参数子节点名称
#@param pos 		参数位置
#@param status 		参数状态
####################################################	
def SetStatusForInstrument(listname,pos,status=QTS_INSTRUMENT_STATUS_DISPLAY) :
	SetPropertyForInstrument(listname,pos,6,status)
	
####################################################
#@brief 设置策略交易标参数的模式
#@param listname 	参数子节点名称
#@param pos 		参数位置
#@param mode 		参数模式
####################################################	
def SetModeForInstrument(listname,pos,mode=QTS_INSTRUMENT_MODE_NONE) :
	SetPropertyForInstrument(listname,pos,7,mode)
	
####################################################
#@brief 设置策略交易标参数的组件
#@param listname 	参数子节点名称
#@param pos 		参数位置
#@param component	参数组件
####################################################	
def SetComponentForInstrument(listname,pos,component='') :
	SetPropertyForParameter(listname,pos,8,component)
	
####################################################
#@brief 设置策略交易标参数的样式
#@param listname 	参数子节点名称
#@param pos 		参数位置
#@param style 		参数样式
####################################################	
def SetStyleForInstrument(listname,pos,style='') :
	SetPropertyForParameter(listname,pos,9,style)	
	
####################################################
#@brief 创建策略可变参数的子节点
#@param 0  listname      	字典名称
#@param 1  key				配置键值，在一个策略中必须唯一
#@param 2  name				配置变量的名称
#@param 3  value			配置的值
#@param 4  verdecimal		配置的值小数位数
#@param 5  index			控件的排例顺序，控制显示
#@param 6  level			控件的层级，控制显示，暂支持：QTS_PARAMETER_STATUS_DISPLAY,QTS_PARAMETER_STATUS_HIDE
#@param 7  save				是否对值的改变进行备份,暂支持：True,False
#@param 8  status			控件状态，控制显示，是否可编译，暂支持：QTS_DISABLE,QTS_ENABLE
#@param 9  mode				控件类型，暂支持：QTS_COMPONENT_TEXTBOX和QTS_COMPONENT_COMBOX
#@param 10 component		控件的填充内容格式(序号:文本,序号:文本,....)
#@param 11 style			控件样式
#@return 参数在表中所有的位置
####################################################
def CreateParameter(*args,**kwargs) :
	return AppendParameterForStrategy(*args,**kwargs)
	
####################################################
#@brief 设置策略可变参数级别
#@param listname 	参数子节点名称
#@param pos 		参数位置
#@param level 		参数级别
####################################################	
def SetLevelForParameter(listname,pos,level=0) :
	SetPropertyForParameter(listname,pos,5,level)
	
####################################################
#@brief 设置策略可变参数是否可以备份
#@param listname 	参数子节点名称
#@param pos 		参数位置
#@param save 		是否可以备份
####################################################		
def SetSaveForParameter(listname,pos,save=QTS_FALSE) :
	SetPropertyForParameter(listname,pos,6,save)
	
####################################################
#@brief 设置策略可变参数状态
#@param listname 	参数子节点名称
#@param pos 		参数位置
#@param status 		参数状态
####################################################	
def SetStatusForParameter(listname,pos,status=QTS_ENABLE) :
	SetPropertyForParameter(listname,pos,7,status)
	
####################################################
#@brief 设置策略可变参数模式
#@param listname 	参数子节点名称
#@param pos 		参数位置
#@param mode 		参数模式
####################################################	
def SetModeForParameter(listname,pos,mode=QTS_COMPONENT_TEXTBOX) :
	SetPropertyForParameter(listname,pos,8,mode)
	
####################################################
#@brief 设置策略可变参数组件
#@param listname 	参数子节点名称
#@param pos 		参数位置
#@param component	参数组件
####################################################	
def SetComponentForParameter(listname,pos,component='') :
	SetPropertyForParameter(listname,pos,9,component)
	
####################################################
#@brief 设置策略可变参数样式
#@param listname 	参数子节点名称
#@param pos 		参数位置
#@param style 		参数样式
####################################################	
def SetStyleForParameter(listname,pos,style='') :
	SetPropertyForParameter(listname,pos,10,style)
	
####################################################
#@brief 创建策略静态参数子节点
#@param 0  listname			字典名称
#@param 1  key				配置键值，在一个策略中必须唯一
#@param 2  name				配置变量的名称
#@param 3  value			配置的值
#@param 4  verdecimal		配置的值小数位数
#@param 5  index			控件的排例顺序，控制显示
#@param 6  level			控件的层级，控制显示，暂支持：QTS_PARAMETER_STATUS_DISPLAY,QTS_PARAMETER_STATUS_HIDE
#@param 7  modify			是否改变可向远端发送，暂支持：QTS_FALSE,QTS_TRUE
#@param 8  status			控件状态，控制显示，是否由服务端推送给GUI，暂支持：QTS_DISABLE,QTS_ENABLE
#@param 9  mode				控件类型，暂支持QTS_COMPONENT_LABEL
#@param 10 component		控件的填充内容格式(序号:文本,序号:文本,....)
#@param 11 style			控件样式
#@return 参数在表中所有的位置
####################################################
def CreateComment(*args,**kwargs) :
	return AppendCommentForStrategy(*args,**kwargs)
	
####################################################
#@brief 设置策略静态参数级别
#@param listname 	参数子节点名称
#@param pos 		参数位置
#@param level 		参数级别
####################################################	
def SetLevelForComment(listname,pos,level=0) :
	SetPropertyForComment(listname,pos,5,level)
	
####################################################
#@brief 设置策略静态参数是否可以备份
#@param listname 	参数子节点名称
#@param pos 		参数位置
#@param modify 		是否可以备份
####################################################		
def SetModifyForComment(listname,pos,modify=QTS_TRUE) :
	SetPropertyForComment(listname,pos,6,modify)
	
####################################################
#@brief 设置策略静态参数状态
#@param listname 	参数子节点名称
#@param pos 		参数位置
#@param status 		参数状态
####################################################	
def SetStatusForComment(listname,pos,status=QTS_ENABLE) :
	SetPropertyForComment(listname,pos,7,status)
	
####################################################
#@brief 设置策略静态参数模式
#@param listname 	参数子节点名称
#@param pos 		参数位置
#@param mode 		参数模式
####################################################		
def SetModeForComment(listname,pos,mode=QTS_COMPONENT_LABEL) :
	SetPropertyForComment(listname,pos,8,mode)
	
####################################################
#@brief 设置策略静态参数组件
#@param listname 	参数子节点名称
#@param pos 		参数位置
#@param component	参数组件
####################################################		
def SetComponentForComment(listname,pos,component='') :
	SetPropertyForComment(listname,pos,9,component)
	
####################################################
#@brief 设置策略静态参数样式
#@param listname 	参数子节点名称
#@param pos 		参数位置
#@param style 		参数样式
####################################################	
def SetStyleForComment(listname,pos,style='') :
	SetPropertyForComment(listname,pos,10,style)

####################################################
#@brief 创建策略命令参数子节点
#@param 0  listname			字典名称
#@param 1  key				配置键值，在一个策略中必须唯一
#@param 2  name				配置变量的名称
#@param 3  index			控件的排例顺序，控制显示
#@param 4  level			控件的层级，控制显示，暂支持：QTS_PARAMETER_STATUS_DISPLAY,QTS_PARAMETER_STATUS_HIDE
#@param 5  status			控件状态，控制显示，是否可点击，暂支持：QTS_DISABLE,QTS_ENABLE
#@param 6  mode				控件类型，暂支持QTS_COMPONENT_COMMONTBUTTON和QTS_COMPONENT_CONFIRMBUTTON
#@param 7  component		控件的填充内容格式(序号:文本,序号:文本,....)
#@param 8  style			控件样式
#@return 参数在表中所有的位置
####################################################
def CreateCommand(*args,**kwargs) :
	return AppendCommandForStrategy(*args,**kwargs)
	
####################################################
#@brief 设置策略命令参数级别
#@param listname 	参数子节点名称
#@param pos 		参数位置
#@param level 		参数级别
####################################################		
def SetLevelForCommand(listname,pos,level=0) :
	SetPropertyForCommand(listname,pos,3,level)
	
####################################################
#@brief 设置策略命令参数状态
#@param listname 	参数子节点名称
#@param pos 		参数位置
#@param status 		参数状态
####################################################	
def SetStatusForCommand(listname,pos,status=QTS_ENABLE) :
	SetPropertyForCommand(listname,pos,4,status)
	
####################################################
#@brief 设置策略命令参数模式
#@param listname 	参数子节点名称
#@param pos 		参数位置
#@param mode 		参数模式
####################################################	
def SetModeForCommand(listname,pos,mode=QTS_COMPONENT_COMMONTBUTTON) :
	SetPropertyForCommand(listname,pos,5,mode)
	
####################################################
#@brief 设置策略命令参数组件
#@param listname 	参数子节点名称
#@param pos 		参数位置
#@param component	参数组件
####################################################	
def SetComponentForCommand(listname,pos,component='') :
	SetPropertyForCommand(listname,pos,6,component)
	
####################################################
#@brief 设置策略命令参数样式
#@param listname 	参数子节点名称
#@param pos 		参数位置
#@param style 		参数样式
####################################################		
def SetStyleForCommand(listname,pos,style='') :
	SetPropertyForCommand(listname,pos,7,style)	
