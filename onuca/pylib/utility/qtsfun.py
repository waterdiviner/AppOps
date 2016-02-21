#coding=utf-8
from qtsenvir import *

#######################################################################
#######################################################################	
#系统操作函数
#######################################################################
####################################################
#@brief 得到命令行参数
#@param index  	序号
#@return  命令行参数
####################################################
def GetArgv(index,defvalue = '') :
	try :
		if index >= len(sys.argv) :
			return defvalue
		else :
			return sys.argv[index]
	except :
		return defvalue

####################################################
#@brief 得到命令行参数
#@param index  	序号
#@return  命令行参数
####################################################
def GetArgvInt(index,defvalue = 0) :
	try :
		if index >= len(sys.argv) :
			return defvalue
		else :
			return int(sys.argv[index])
	except :
		return defvalue

####################################################
#@brief 得到环境变量
#@param key  	环境变量键值
#@param defvalue  缺省的环境变量的值
#@return  环境变量
####################################################
def GetEnv(key,defvalue) :
	return os.getenv(key,defvalue)

####################################################
#@brief 设置环境变量
#@param key  	环境变量键值
#@param value  环境变量的值
####################################################	
def SetEnv(key,value) :
	os.environ[key] = value
	
####################################################
#@brief 追加环境变量
#@param key  	环境变量键值
#@param value  环境变量的值
####################################################	
def AppendEnv(key,value) :
	if platform.system() == SYS_LINUX :
		os.environ[key] += ":{0}".format(value)
	else :
		os.environ[key] += ";{0}".format(value)

####################################################
#@brief 得到交易日期
#@return  交易日期
####################################################
def GetTradeDate() :
	tradedate = GetEnv('QTS_TRADE_DATE','')
	try :
		if tradedate == '' :
			tradedate = time.strftime('%Y%m%d',time.localtime(time.time()))
	except :
		TraceWarning('if you want to use date folder,please open QTS_TRADE_DATE in script file!')
	return tradedate

####################################################
#@brief 日期加月
#@return  日期
####################################################	
def AddMonth(dt,months) :
	tdate = dt
	tmonth = months + tdate.month
	try :
		tdate = tdate.replace(year=dt.year + int(tmonth/12),month=(tmonth%12))
	except :
		tdate = tdate.replace(year=dt.year + int((tmonth + 1)/12),month=((tmonth + 1)%12),day=1)
		tdate += datetime.timedelta(days=-1)
	return tdate
	
#######################################################################
#######################################################################	
#函数参数操作函数
#######################################################################

####################################################
#@brief 检查指定的序号的参数是否有参数
#@param index		参数序号
#@param *args		序号参数集
#@return  是否存在
####################################################
def IsExistArgByIndex(index,*args) :
	if index < len(args) :
		return True
	else :
		return False
	
####################################################
#@brief 检查指定的参数名称的参数是否有参数
#@param name		参数名称
#@param **kwargs	名称参数集
#@return  是否存在
####################################################
def IsExistArgByName(name,**kwargs) :
	for kwarg in kwargs :
		if kwarg == name :
			return True
	return False
	
####################################################
#@brief 检查指定的参数序号或参数名称的参数是否有参数
#@param index		参数序号
#@param name		参数名称
#@param *args		序号参数集
#@param **kwargs	名称参数集
#@return  是否存在
####################################################	
def IsExistArgByIndexAndName(index,name,*args,**kwargs) :
	return IsExistArgByIndex(index,*args) or IsExistArgByName(name,**kwargs)
	
####################################################
#@brief 得到指定序号的参数的值
#@param index		参数序号
#@param defvalue	缺省的值
#@param *args		序号参数集
#@return  参数指定的值
####################################################	
def GetArgByIndex(index,defvalue,*args) :
	if index < len(args) :
		return args[index]
	return defvalue
	
####################################################
#@brief 得到指名称的参数的值
#@param name		参数名称
#@param defvalue	缺省的值
#@param **kwargs	名称参数集
#@return  参数指定的值
####################################################	
def GetArgByName(name,defvalue,**kwargs) :
	for kwarg in kwargs :
		if kwarg == name :
			return kwargs[name]
	return defvalue
	
####################################################
#@brief 得到指定序号的参数的值
#@param index		参数序号
#@param name		参数名称
#@param defvalue	缺省的值
#@param *args		序号参数集
#@param **kwargs	名称参数集
#@return  参数指定的值
####################################################	
def GetArgByIndexAndName(index,name,defvalue,*args,**kwargs) :
	if index < len(args) :
		return args[index]
	for kwarg in kwargs :
		if kwarg == name :
			return kwargs[name]		
	return defvalue	

#######################################################################
#######################################################################	
#数据转换函数
#######################################################################

####################################################
#@brief 将给定的数值转换成64数值
#@param num		任意数字
#@return  64数值
####################################################	
def ToInt64(num) :
	return long(num)
	
#######################################################################
#######################################################################	
#路径操作的函数
#######################################################################

####################################################
#@brief 得到日期目录
#@return  目录
####################################################
def GetPathByDate() :
	return time.strftime('%Y-%m-%d',time.localtime(time.time()))
	
####################################################
#@brief 得到执行目录
#@return  目录
####################################################	
def GetExecutePath() :
	return os.getcwd()
	
####################################################
#@brief 得到当前的PY文件目录
#@return  目录
####################################################
def GetCurrPyPath() :
	return os.path.dirname(os.path.realpath(__file__))
		
####################################################
#@brief 得到当前的PY文件目录
#@return  目录
####################################################		
def GetCurrFolder() :
	currdir = GetCurrPyPath()
	dir_list=currdir.split('/')
	str_len=len(dir_list)
	return dir_list[str_len-1]
	
####################################################
#@brief 得到时间目录
#@return  目录
####################################################	
def GetTimeFolder() :
	return GetTradeDate()
	
####################################################
#@brief 合并目录
#@param parent  父目录
#@param path    子目录
#@return  目录
####################################################	
def CombinePath(parent,path) :
	strparent = parent.replace('\\','/')
	strpath = path.replace('\\','/')
	if strparent == '' or strpath == '' :
		return strparent + strpath;
	elif (strparent[len(strparent) - 1] == '/') and (strpath[0] == '/') :
		return strparent[0:len(strparent) - 1] + strpath
	elif strpath[0] == '/' :
		return strparent + strpath;
	elif strparent[len(strparent) - 1] == '/' :
		return strparent + strpath;
	else :
		return strparent + '/' + strpath
	
#######################################################################
#######################################################################	
#字典操作函数
#######################################################################	

####################################################
#@brief 得到全局字典对象
#@param name  字典名称
#@return  字典对象
####################################################
def GetGlobals(name) :
	qtsglobals = None
	try:
		qtsglobals = globals()[name]
	except Exception,e:
		globals()[name] = dict()
		qtsglobals = globals()[name]
	return 	qtsglobals

####################################################
#@brief 是否存在全局字典对象
#@param name  字典名称
#@return  是否存在
####################################################
def ExistGlobals(name) :
	qtsglobals = None
	try:
		qtsglobals = globals()[name]
	except Exception,e:
		qtsglobals = None
	return 	qtsglobals != None
	
####################################################
#@brief 得到PY变量根字典对象
#@return  字典对象
####################################################	
def GetPyGlobals() :
	return GetGlobals(QTS_Py_Variables)	
	
####################################################
#@brief 是否存在PY变量根字典对象
#@return  是否存在
####################################################	
def ExistPyGlobals() :
	return ExistGlobals(QTS_Py_Variables)	
	
####################################################
#@brief 得到应用配置根字典对象
#@return  字典对象
####################################################	
def GetRootGlobals() :
	return GetGlobals(QTS_App_Variables)
	
####################################################
#@brief 是否存在应用配置根字典对象
#@return  是否存在
####################################################	
def ExistRootGlobals() :
	return ExistGlobals(QTS_App_Variables)
	
####################################################
#@brief 创建应用配置根字典对象
####################################################		
def CreateRootGlobals() :
	GetRootGlobals()
	
####################################################
#@brief 得到对象的属性
#@param name  属性名称
#@return  属性对象
####################################################	
def GetAttr(obj,name) :
	value = None
	try:
		value = obj[name]
	except Exception,e:
		value = None
	return value
	
####################################################
#@brief 检查指定的属性是在对象中
#@param name  属性名称
#@return  True是在，False是不在
####################################################		
def HasAttr(obj,name) :
	if GetAttr(obj,name) == None :
		return False
	else :
		return True	
		
####################################################
#@brief 设置指定的属性的值
#@param name  属性名称
#@param value 属性的值
####################################################			
def SetAttr(obj,name,value) :
	obj[name]=value
	
####################################################
#@brief 得到指定的路径的属性对象
#@param obj  父属性
#@param path 路径，格式XX/XXX/XX
#@return  属性对象
####################################################		
def GetDictByPath(obj,path) :
	qtsdict = obj
	names = path.split('/')
	for name in names :
		if HasAttr(qtsdict,name) == True :
			qtsdict = GetAttr(qtsdict,name)
		else :
			qtsdict = None
			break
	return qtsdict
	
####################################################
#@brief 从应用根对象中得到指定的路径的属性对象
#@param path 路径，格式XX/XXX/XX
#@return  属性对象
####################################################	
def GetDictFromRootByPath(path) :
	return GetDictByPath(GetRootGlobals(),path)
	
####################################################
#@brief 从应用根字典
#@param name 应用名称
#@return  字典对象
####################################################	
def GetAppGlobals(name) :
	appglobals = None
	if name == '' :
		appglobals = GetRootGlobals()
	else :
		try:
			appglobals = GetRootGlobals()[name]
		except Exception,e:
			GetRootGlobals()[name] = dict()
			appglobals = GetRootGlobals()[name]
	return 	appglobals

####################################################
#@brief 为字典添加属性
#@param obj  字典
#@param name 属性名称
####################################################
def AppendDict(obj,name) :
	obj[name] = dict()
	
####################################################
#@brief 为应用字典添加属性
#@param module  应用模块
#@param name 属性名称
####################################################	
def AppendMainDict(module,name) :
	GetAppGlobals(module)[name] = dict()
	
####################################################
#@brief 从字典中得到属性
#@param obj  字典
#@param name 属性名称
#@return  字典对象
####################################################	
def GetDict(obj,name) :
	return GetAttr(obj,name)

####################################################
#@brief 由应用字典中得到属性
#@param module  应用模块
#@param name 属性名称
#@return  字典对象
####################################################	
def GetMainDict(module,name) :
	value = None
	try:
		value = GetAppGlobals(module)[name]
	except Exception,e:
		value = None
	return value	
	
####################################################
#@brief 在字典中是否存在指定的属性
#@param obj  字典
#@param name 属性名称
#@return  True是存在，False不存在
####################################################		
def IsExistDict(obj,name) :
	return HasAttr(obj,name)
	
####################################################
#@brief 在应用字典中是否存在指定的属性
#@param module  应用模块
#@param name 属性名称
#@return  True是存在，False不存在
####################################################	
def IsExistMainDict(module,name) :
	if GetMainDict(module,name) == None :
		return False
	else :
		return True

####################################################
#@brief 为字典添加属性
#@param obj  字典
#@param name 属性名称
#@param value 属性值
####################################################	
def AppendItemForDict(obj,name,value):
	SetAttr(obj,name,value)

####################################################
#@brief 为应用字典添加属性
#@param module  应用模块
#@param dictname 字典名称
#@param name 属性名称
#@param value 属性值
####################################################		
def AppendItemForMainDict(module,dictname,name,value) :
	GetAppGlobals(module)[dictname][name]=value
	
####################################################
#@brief 设置变量在PY根字典中
#@param name  变量名称
#@param value 变量值
####################################################		
def SetVarInMainDict(name,value) :
	GetPyGlobals()[name]=value

####################################################
#@brief 获得变量从PY根字典中
#@param name  变量名称
#@return 变量值
####################################################	
def GetVarInMainDict(name) :
	obj = GetPyGlobals()
	if obj == None :
		return None
	else :
		return GetDict(obj,name)
	
####################################################
#@brief 获得字符串变量从PY根字典中
#@param name  变量名称
#@return 字符串变量值
####################################################	
def GetMainDictForString(name) :
	value = GetVarInMainDict(name)
	if value == None :
		return ''
	else :
		return value
		
####################################################
#@brief 获得整数变量从PY根字典中
#@param name  变量名称
#@return 整数变量值
####################################################		
def GetMainDictForInt(name) :
	value = GetVarInMainDict(name)
	if value == None :
		return 0
	else :
		return value

####################################################
#@brief 获得双精度变量从PY根字典中
#@param name  变量名称
#@return 双精度变量值
####################################################			
def GetMainDictForDouble(name) :
	value = GetVarInMainDict(name)
	if value == None :
		return 0.0
	else :
		return value
	
####################################################
#@brief 获得布尔变量从PY根字典中
#@param name  变量名称
#@return 布尔变量值
####################################################	
def GetMainDictForBool(name) :
	value = GetVarInMainDict(name)
	if value == None :
		return False
	else :
		return value

####################################################
#@brief 为字典添加链表属性
#@param obj 字典对象
#@param name  变量名称
####################################################
def AppendList(obj,name) :
	obj[name] = list()
	
####################################################
#@brief 为应用字典添加链表属性
#@param obj 字典对象
#@param name  变量名称
####################################################	
def AppendMainList(module,name) :
	GetAppGlobals(module)[name] = list()

####################################################
#@brief 从字典得到链表属性
#@param obj 字典对象
#@param name  变量名称
#@return 链表对象
####################################################	
def GetList(obj,name) :
	return GetAttr(obj,name)
	
####################################################
#@brief 从应用字典得到链表属性
#@param obj 字典对象
#@param name  变量名称
#@return 链表对象
####################################################	
def GetMainList(module,name) :
	value = None
	try:
		value = GetAppGlobals(module)[name]
	except Exception,e:
		value = None
	return value

####################################################
#@brief 得到字典中链表指定位置的值
#@param obj 字典对象
#@param name  链表名称
#@param pos 链表数据位置
#@return 数据
####################################################		
def GetListValue(obj,name,pos) :
	value = GetList(obj,name)
	if value == None :
		return False
	else :
		return value[pos]
	
####################################################
#@brief 得到应用字典中链表指定位置的值
#@param obj 字典对象
#@param name  链表名称
#@param pos 链表数据位置
#@return 数据
####################################################	
def GetMainListValue(module,name,pos) :
	value = GetMainList(module,name)
	if value == None :
		return False
	else :
		return value[pos]
	
####################################################
#@brief 检查字典中链表是否存在
#@param obj 字典对象
#@param name  链表名称
#@return True是存在，False不存在
####################################################	
def IsExistList(obj,name) :
	return HasAttr(obj,name)
	
####################################################
#@brief 检查应用字典中链表是否存在
#@param obj 字典对象
#@param name  链表名称
#@return True是存在，False不存在
####################################################		
def IsExistMainList(module,name) :
	if GetMainList(module,name) == None :
		return False
	else :
		return True
		
####################################################
#@brief 得到链表的大小
#@param obj 链表对象
#@return 大小
####################################################		
def GetListSize(obj) :
	return len(obj)
	
####################################################
#@brief 得到应用中链表的大小
#@param module 应用模块名称
#@param name 链表名称
#@return 大小
####################################################	
def GetMainListSize(module,name) :
	return len(GetAppGlobals(module)[name])
	
####################################################
#@brief 为链表在指定位置充置值
#@param obj 链表对象
#@param pos 位置
#@param value 值
####################################################	
def AppendItemForListByPos(obj,pos,value) :
	obj[pos].append(value)

####################################################
#@brief 为应用中的链表在指定位置充置值
#@param module 应用模块名称
#@param obj 链表对象
#@param pos 位置
#@param value 值
####################################################		
def AppendItemForMainListByPos(module,name,pos,value) :
	GetAppGlobals(module)[name][pos].append(value)
	
####################################################
#@brief 为链表添加数据
#@param obj 链表对象
#@param value 数据
#@return 数据所在的位置
####################################################
def AppendItemForList(obj,value) :
	obj.append(value)
	return len(obj) - 1

####################################################
#@brief 为应用中的链表添加数据
#@param module 应用模块名称
#@param name 链表名称
#@param value 数据
#@return 数据所在的位置
####################################################
def AppendItemForMainList(module,name,value) :
	GetAppGlobals(module)[name].append(value)
	return len(GetAppGlobals(module)[name]) - 1

####################################################
#@brief 检查数据是否在应用链表中
#@param module 应用模块名称
#@param name 链表名称
#@param value 数据
#@return True是成功，False是失败
####################################################	
def IsExistInList(module,name,value) :
	values = GetMainList(module,name)
	if values == None :
		return False
	for exist_value in values :
		if value == exist_value :
			return True
	return False
	
####################################################
#@brief 添加数据到应用链表中
#@param module 应用模块名称
#@param name 链表名称
#@param value 数据
####################################################	
def AddVarInList(module,name,value) :
	if not IsExistMainList(module,name) :
		AppendMainList(module,name)
	if not IsExistInList(module,name,value) :
		AppendItemForMainList(module,name,value)

#######################################################################
#######################################################################	
#应用变量操作函数
#######################################################################

####################################################
#@brief 检查是否存在应用身份标示
#@param identity 身份标示
#@return True是存在，False不存在
####################################################
def IsExistAppIdentity(identity) :
	return IsExistInList('',QTS_APP_IDENTITY_KEY,identity)
	
####################################################
#@brief 为应用添加身份标示
#@param identity 身份标示
####################################################	
def AddAppIdentity(identity) :
	AddVarInList('',QTS_APP_IDENTITY_KEY,identity)
	
####################################################
#@brief 检查应用是否可运行
#@param identity 身份标示
#@return True可运行，False不可运行
####################################################	
def IsCanRun(identity) :
	return IsExistInList('',QTS_APP_IDENTITY_KEY,identity)
		
####################################################
#@brief 设置应用部署模式
#@param mode 应用模式，值是QTS_APP_MODE_ALL or QTS_APP_MODE_SERVER or QTS_APP_MODE_SINGLE
#			参考EQtsAppMode枚举，在qtssecurity.py中
####################################################		
def SetAppMode(mode) :
	SetVarInMainDict(QTS_APP_MODE_KEY,mode)

####################################################
#@brief 得到应用部署模式
#@return 部署模式
####################################################	
def GetAppMode() :
	return GetMainDictForInt(QTS_APP_MODE_KEY)
		
####################################################
#@brief 设置应用的根路径
#@param path 根路径
####################################################		
def SetAppPath(path) :
	SetVarInMainDict(QTS_APP_PATH,path)

####################################################
#@brief 得到应用的根路径
#@return 根路径
####################################################	
def GetAppPath() :
	return GetMainDictForString(QTS_APP_PATH)
	
####################################################
#@brief 设置应用的缺省根路径
#@param path 根路径
####################################################	
def SetAppDefaultPath(path) :
	SetVarInMainDict(QTS_APP_DEFAULT_PATH,path)

####################################################
#@brief 得到应用的缺省根路径
#@return 根路径
####################################################	
def GetAppDefaultPath() :
	return GetMainDictForString(QTS_APP_DEFAULT_PATH)
	
####################################################
#@brief 设置应用的用户策略插件根路径
#@param path 根路径
####################################################		
def SetUserStrategyPath(path) :
	SetVarInMainDict(QTS_USER_STRATEGY_PATH,path)

####################################################
#@brief 得到应用的用户策略插件根路径
#@return 根路径
####################################################	
def GetUserStrategyPath() :
	return GetMainDictForString(QTS_USER_STRATEGY_PATH)	

####################################################
#@brief 设置应用的用户数据插件根路径
#@param path 根路径
####################################################	
def SetUserMarketPath(path) :
	SetVarInMainDict(QTS_USER_MARKET_PATH,path)

####################################################
#@brief 得到应用的用户数据插件根路径
#@return 根路径
####################################################	
def GetUserMarketPath() :
	return GetMainDictForString(QTS_USER_MARKET_PATH)

####################################################
#@brief 设置应用的用户交易通道插件根路径
#@param path 根路径
####################################################	
def SetUserExchangePath(path) :
	SetVarInMainDict(QTS_USER_EXCHANGE_PATH,path)

####################################################
#@brief 得到应用的用户交易通道插件根路径
#@return 根路径
####################################################	
def GetUserExchangePath() :
	return GetMainDictForString(QTS_USER_EXCHANGE_PATH)
	
####################################################
#@brief 设置应用的加载插件类型
#@param itype 插件类型，参考EQtsLoaderType枚举，在qtssecurity.py中
####################################################
def SetLoaderType(itype) :
	SetVarInMainDict(QTS_LOADER_TYPE,itype)

####################################################
#@brief 得到应用的加载插件类型
#@return 插件类型
####################################################		
def GetLoaderType() :
	return GetMainDictForInt(QTS_LOADER_TYPE)

####################################################
#@brief 设置应用的备份插件类型
#@param itype 插件类型，参考EQtsBackupType枚举，在qtssecurity.py中
####################################################
def SetBackupType(itype) :
	SetVarInMainDict(QTS_BACKUP_TYPE,itype)

####################################################
#@brief 得到应用的备份插件类型
#@return 插件类型
####################################################	
def GetBackupType() :
	return GetMainDictForInt(QTS_BACKUP_TYPE)
	
####################################################
#@brief 设置应用的回放插件类型
#@param itype 插件类型，参考EQtsBackupType枚举，在qtssecurity.py中
####################################################
def SetReplayType(itype) :
	SetVarInMainDict(QTS_REPLAY_TYPE,itype)

####################################################
#@brief 得到应用的回放插件类型
#@return 插件类型
####################################################	
def GetReplayType() :
	return GetMainDictForInt(QTS_REPLAY_TYPE)
	
####################################################
#@brief 设置应用的是否是多线程
#@param multi 是否是多线程
####################################################
def SetMultiThread(multi) :
	SetVarInMainDict(QTS_MULTI_THREAD,multi)

####################################################
#@brief 得到应用是否是多线程
#@return 是否是多线程
####################################################	
def GetMultiThread() :
	return GetMainDictForBool(QTS_MULTI_THREAD)
	
####################################################
#@brief 设置系统是否支持回放
#@param breplay True是支持，False不支持
####################################################
def SetIsReplay(breplay) :
	SetVarInMainDict(QTS_IS_REPLAY,breplay)

####################################################
#@brief 得到系统是否支持回放
#@return True是支持，False不支持
####################################################	
def GetIsReplay() :
	return GetMainDictForBool(QTS_IS_REPLAY)

####################################################
#@brief 设置系统是否支持模拟撮合
#@param bmatch True是支持，False不支持
####################################################
def SetIsMatch(bmatch) :
	SetVarInMainDict(QTS_IS_MATCH,bmatch)

####################################################
#@brief 得到系统是否支持模拟撮合
#@return True是支持，False不支持
####################################################	
def GetIsMatch() :
	return GetMainDictForBool(QTS_IS_MATCH)
	
####################################################
#@brief 设置系统是否支持监控数据插件
#@param bmonitor True是支持，False不支持
####################################################
def SetIsDSMonitor(bmonitor) :
	SetVarInMainDict(QTS_IS_DS_MONITOR,bmonitor)

####################################################
#@brief 得到系统是否支持监控数据插件
#@return True是支持，False不支持
####################################################	
def GetIsDSMonitor() :
	return GetMainDictForBool(QTS_IS_DS_MONITOR)

####################################################
#@brief 设置系统是否支持监控交易插件
#@param bmonitor True是支持，False不支持
####################################################		
def SetIsGWMonitor(bmonitor) :
	SetVarInMainDict(QTS_IS_GW_MONITOR,bmonitor)

####################################################
#@brief 得到系统是否支持监控交易插件
#@return True是支持，False不支持
####################################################	
def GetIsGWMonitor() :
	return GetMainDictForBool(QTS_IS_GW_MONITOR)
	
####################################################
#@brief 设置系统是否支持监控策略插件
#@param bmonitor True是支持，False不支持
####################################################		
def SetIsSSMonitor(bmonitor) :
	SetVarInMainDict(QTS_IS_SS_MONITOR,bmonitor)

####################################################
#@brief 得到系统是否支持监控策略插件
#@return True是支持，False不支持
####################################################	
def GetIsSSMonitor() :
	return GetMainDictForBool(QTS_IS_SS_MONITOR)	
	
####################################################
#@brief 设置系统是否支持监控终端插件
#@param bmonitor True是支持，False不支持
####################################################		
def SetIsGUIMonitor(bmonitor) :
	SetVarInMainDict(QTS_IS_GUI_MONITOR,bmonitor)

####################################################
#@brief 得到系统是否支持监控终端插件
#@return True是支持，False不支持
####################################################	
def GetIsGUIMonitor() :
	return GetMainDictForBool(QTS_IS_GUI_MONITOR)
	
####################################################
#@brief 设置系统监控延时
#@param time 延时时间
####################################################
def SetMonitorTime(time) :
	SetVarInMainDict(QTS_MONITOR_WAIT_TIME,time * 1000 * 1000)

####################################################
#@brief 获得系统监控延时
#@return 延时时间
####################################################	
def GetMonitorTime() :
	return GetMainDictForInt(QTS_MONITOR_WAIT_TIME)
	
####################################################
#@brief 设置系统是否允许打印
#@param bprint True是允许，False不允许
####################################################	
def SetIsPrint(bprint) :
	SetVarInMainDict(QTS_IS_PRINT,bprint)

####################################################
#@brief 获得系统是否允许打印
#@return True是允许，False不允许
####################################################		
def GetIsPrint() :
	return GetMainDictForBool(QTS_IS_PRINT)	
	
####################################################
#@brief 设置系统所在的操作系统
#@param isystem  操作系统，参考EQtsSystemType枚举，在qtssecurity.py中
####################################################	
def SetAppSystem(isystem) :
	SetVarInMainDict(QTS_APP_SYSTEM,isystem)

####################################################
#@brief 获得系统所在的操作系统
#@return 操作系统
####################################################	
def GetAppSystem() :
	return GetMainDictForInt(QTS_APP_SYSTEM)
	
####################################################
#@brief 设置系统版本
#@param iversion 系统版本，参考EQtsVersionType枚举，在qtssecurity.py中
####################################################		
def SetAppVersion(iversion) :
	SetVarInMainDict(QTS_APP_VERSION,iversion)

####################################################
#@brief 获得系统版本
#@return 系统版本
####################################################	
def GetAppVersion() :
	return GetMainDictForInt(QTS_APP_VERSION)

####################################################
#@brief 设置系统版本字符串
#@param iversion   版本字符串
####################################################	
def SetAppVersionStr(iversion) :
	SetVarInMainDict(QTS_APP_VERSION_STR,iversion)

####################################################
#@brief 获得系统版本字符串
#@return  版本字符串
####################################################	
def GetAppVersionStr() :
	return GetMainDictForString(QTS_APP_VERSION_STR)
	
####################################################
#@brief 设置运行系统版本
#@param iversion  系统版本，参考EQtsVersionType枚举，在qtssecurity.py中
####################################################
def SetRunVersion(iversion) :
	SetVarInMainDict(QTS_RUN_VERSION,iversion)

####################################################
#@brief 获得运行系统版本
#@return  运行系统版本
####################################################	
def GetRunVersion() :
	return GetMainDictForInt(QTS_RUN_VERSION)
	
####################################################
#@brief 设置系统的根路径
#@param path 路径
####################################################	
def SetBasePath(path) :
	SetVarInMainDict(QTS_BASE_PATH,path)
	
####################################################
#@brief 设置回放数据的路径
#@param path 路径
####################################################		
def SetReplayPath(path) :
	SetVarInMainDict(QTS_REPLAY_PATH,path)
	
####################################################
#@brief 设置启动的应用
#@param app 应用名称
####################################################	
def SetStartApp(app) :
	SetVarInMainDict(QTS_CFG_START_SINGLE_APP,app)

####################################################
#@brief 获得启动的应用
#@return 应用名称
####################################################	
def GetStartApp() :
	return GetMainDictForInt(QTS_CFG_START_SINGLE_APP)
	
####################################################
#@brief 设置指定应用的指定标示的IP地址
#@param app 应用名称
#@param flag 标示
#@param address IP地址
####################################################		
def SetIPAddress(app,flag,address) :
	SetVarInMainDict(QTS_CFG_APP_IP_ADDR.format(app,flag),address)

####################################################
#@brief 获得指定应用的指定标示的IP地址
#@param app 应用名称
#@param flag 标示
#@return IP地址
####################################################	
def GetIPAddress(app,flag) :
	ipaddress = GetMainDictForString(QTS_CFG_APP_IP_ADDR.format(app,flag))
	if ipaddress == '' :
		ipaddress = '127.0.0.1'
	return ipaddress
	
####################################################
#@brief 设置指定应用的指定标示的端口
#@param app 应用名称
#@param flag 标示
#@param port 端口
####################################################	
def SetIPPort(app,flag,port) :
	SetVarInMainDict(QTS_CFG_APP_IP_PORT.format(app,flag),port)

####################################################
#@brief 获得指定应用的指定标示的端口
#@param app 应用名称
#@param flag 标示
#@return 端口
####################################################	
def GetIPPort(app,flag) :
	ipport = GetMainDictForInt(QTS_CFG_APP_IP_PORT.format(app,flag))
	if ipport == 0 :
		ipport = 10000
	return ipport
	
####################################################
#@brief 设置是否支持屏幕输出信息消息
#@param bprint True是支持，False不支持
####################################################		
def SetTraceMessage(bprint) :
	SetVarInMainDict(QTS_TRACE_MESSAGE,bprint)
	
####################################################
#@brief 获得是否支持屏幕输出信息消息
#@return True是支持，False不支持
####################################################	
def GetTraceMessage() :
	value = GetVarInMainDict(QTS_TRACE_MESSAGE)
	if value == None :
		return QTS_TRUE_STR
	else :
		return value
	
####################################################
#@brief 设置是否支持屏幕调试输出
#@param bprint True是支持，False不支持
####################################################	
def SetTraceDebug(bprint) :
	SetVarInMainDict(QTS_TRACE_DEBUG,bprint)
	
####################################################
#@brief 获得是否支持屏幕输出调试消息
#@return True是支持，False不支持
####################################################	
def GetTraceDebug() :
	value = GetVarInMainDict(QTS_TRACE_DEBUG)
	if value == None :
		return QTS_TRUE_STR
	else :
		return value	

####################################################
#@brief 设置是否支持屏幕警告输出
#@param bprint True是支持，False不支持
####################################################	
def SetTraceWarning(bprint) :
	SetVarInMainDict(QTS_TRACE_WARNING,bprint)
	
####################################################
#@brief 获得是否支持屏幕输出警告消息
#@return True是支持，False不支持
####################################################	
def GetTraceWarning() :
	value = GetVarInMainDict(QTS_TRACE_WARNING)
	if value == None :
		return QTS_TRUE_STR
	else :
		return value	

####################################################
#@brief 设置是否支持屏幕错误输出
#@param bprint True是支持，False不支持
####################################################		
def SetTraceError(bprint) :
	SetVarInMainDict(QTS_TRACE_ERROR,bprint)
	
####################################################
#@brief 获得是否支持屏幕输出错误消息
#@return True是支持，False不支持
####################################################		
def GetTraceError() :
	value = GetVarInMainDict(QTS_TRACE_ERROR)
	if value == None :
		return QTS_TRUE_STR
	else :
		return value	
	
####################################################
#@brief 设置是否支持日志信息消息输出
#@param bprint True是支持，False不支持
####################################################	
def SetLogMessage(bprint) :
	SetVarInMainDict(QTS_LOG_MESSAGE,bprint)
	
####################################################
#@brief 获得是否支持日志输出信息消息
#@return True是支持，False不支持
####################################################	
def GetLogMessage() :
	value = GetVarInMainDict(QTS_LOG_MESSAGE)
	if value == None :
		return QTS_TRUE_STR
	else :
		return value		
	
####################################################
#@brief 设置是否支持日志调试消息输出
#@param bprint True是支持，False不支持
####################################################		
def SetLogDebug(bprint) :
	SetVarInMainDict(QTS_LOG_DEBUG,bprint)
	
####################################################
#@brief 获得是否支持日志输出调试消息
#@return True是支持，False不支持
####################################################	
def GetLogDebug() :
	value = GetVarInMainDict(QTS_LOG_DEBUG)
	if value == None :
		return QTS_TRUE_STR
	else :
		return value	

####################################################
#@brief 设置是否支持日志警告消息输出
#@param bprint True是支持，False不支持
####################################################			
def SetLogWarning(bprint) :
	SetVarInMainDict(QTS_LOG_WARNING,bprint)
	
####################################################
#@brief 获得是否支持日志输出警告消息
#@return True是支持，False不支持
####################################################	
def GetLogWarning() :
	value = GetVarInMainDict(QTS_LOG_WARNING)
	if value == None :
		return QTS_TRUE_STR
	else :
		return value	

####################################################
#@brief 设置是否支持日志信息错误输出
#@param bprint True是支持，False不支持
####################################################			
def SetLogError(bprint) :
	SetVarInMainDict(QTS_LOG_ERROR,bprint)
	
####################################################
#@brief 获得是否支持日志输出错误消息
#@return True是支持，False不支持
####################################################	
def GetLogError() :
	value = GetVarInMainDict(QTS_LOG_ERROR)
	if value == None :
		return QTS_TRUE_STR
	else :
		return value	
	
####################################################
#@brief 设置配置目录名称
#@param folder 目录名称
####################################################	
def SetCfgFolder(folder) :
	SetVarInMainDict(QTS_CFG_APP_FOLDER,folder)
		
####################################################
#@brief 得到应用的配置文件夹名称
#@return 文件夹名称
####################################################		
def GetCfgFolder() :
	name = GetMainDictForString(QTS_CFG_APP_FOLDER)
	if name=='' :
		name = GetEnv(QTS_CFG_APP_FOLDER,'')
	return name
	
####################################################
#@brief 设置指定应用的语言
#@param language 语言
####################################################	
def SetLanguage(language) :
	SetVarInMainDict(QTS_CFG_LANGUAGE,language)

####################################################
#@brief 获得指定应用的语言
#@return 语言
####################################################	
def GetLanguage() :
	language = GetMainDictForString(QTS_CFG_LANGUAGE)
	if language == '' :
		language = GetEnv(QTS_CFG_LANGUAGE,'zh')
	return language

####################################################
#@brief 设置数据目录名称
#@param folder 目录名称
####################################################			
def SetDataFolder(folder) :
	SetVarInMainDict(QTS_DATA_APP_FOLDER,folder)
	
####################################################
#@brief 得到应用的数据文件夹名称
#@return 文件夹名称
####################################################		
def GetDataFolder() :
	name = GetMainDictForString(QTS_DATA_APP_FOLDER)
	if name=='' :
		name = GetEnv(QTS_DATA_APP_FOLDER,'')
	return name
		
#######################################################################	
#打印操作函数
#######################################################################

####################################################
#@brief 向屏幕打印消息
#@param msg 消息字符串
####################################################
def PrintMessage(msg) :
	if GetIsPrint() :
		print(msg)

####################################################
#@brief 向屏幕打印字典
#@param obj 字典对象
#@param name 字典名称
####################################################		
def PrintMessageForObj(obj,name) :
	PrintMessage('{0}={1}'.format(name,obj[name]))
		
####################################################
#@brief 向屏幕打印应用字典
#@param module 应用模块名称
#@param name 字典名称
####################################################		
def PrintMessageForMain(module,name) :
	PrintMessage('{0}={1}'.format(name,GetAppGlobals(module)[name]))
		
####################################################
#@brief 向屏幕打印应用插槽
#@param module 应用模块名称
#@param name 插槽名称
####################################################			
def PrintManager(module,name) :
	PrintMessageForMain(module,name)

####################################################
#@brief 向屏幕打印应用插件
#@param module 应用模块名称
#@param name 插件名称
####################################################		
def PrintPlugin(module,name) :
	PrintMessageForMain(module,name)
	
####################################################
#@brief 向屏幕打印根变量
####################################################	
def PrintRootVariables() :
	for item in GetRootGlobals().items() :
		print(str(item[0]) + ' = ' + str(item[1]))

####################################################
#@brief 向屏幕打印指定路径字典
#@param path 字典路径
####################################################		
def PrintDict(path) :
	obj = GetDictFromRootByPath(path)
	if obj == None :
		return
	for item in obj.items() :
		print(str(item[0]) + ' = ' + str(item[1]))
		
####################################################
#@brief 向屏幕打印PY所有的变量
####################################################		
def PrintPyVariables() :
	print(GetPyGlobals())
	
#######################################################################
#######################################################################	
#系统路径操作函数
#######################################################################	
	
####################################################
#@brief 得到应用的根路径
#@return 应用的根路径
####################################################		
def GetBasePath() :
	path = GetMainDictForString(QTS_BASE_PATH)
	if path=='' :
		path = GetEnv(QTS_BASE_PATH_KEY,'')
	return path
	
####################################################
#@brief 得到应用可执行程序路径
#@return 可执行程序路径
####################################################		
def GetBinPath() :
	path = GetAppVersionStr()
	if path == '' :
		return CombinePath(GetBasePath(),'/bin/')
	else :
		return CombinePath(CombinePath(GetBasePath(),'/bin/'),path)

####################################################
#@brief 得到应用库路径
#@return 库路径
####################################################		
def GetLibPath() :
	path = GetAppVersionStr()
	if path == '' :
		return CombinePath(GetBasePath(),'/lib/')
	else :
		return CombinePath(CombinePath(GetBasePath(),'/lib/'),path)

####################################################
#@brief 得到应用插件路径
#@return 插件路径
####################################################		
def GetPluginPath() :
	path = GetAppVersionStr()
	if path == '' :
		return CombinePath(GetBasePath(),'/plugin/')
	else :
		return CombinePath(CombinePath(GetBasePath(),'/plugin/'),path)	
	
####################################################
#@brief 生成库文件名称
#@param name 库名称
#@return 库文件名称
####################################################	
def BuildLibraryFile(name) :
	if GetAppSystem() == windows :
		return name + '.dll'
	else :
		return 'lib' + name + '.so'
	
####################################################
#@brief 得到配置文件路径
#@param path 路径
#@return 配置文件路径
####################################################
def GetCfgPath(path=GetCfgFolder()) :
	if path == '' :
		return CombinePath(GetBasePath(),'/cfg/')	
	else :
		return CombinePath(CombinePath(GetBasePath(),'/cfg/'),path)

####################################################
#@brief 生成日志文件名称
#@param path 路径
#@return 日志文件名称
####################################################
def BuildLogFile(file,folder=GetCfgFolder()) :
	path = ''
	log = CombinePath('/log/',GetTimeFolder())
	if folder == '' :
		path = CombinePath(GetBasePath(),log)
	else :
		path = CombinePath(CombinePath(GetBasePath(),log),folder)
		
	if file == None :
		return path
	else :
		return CombinePath(path,file + ".log")

####################################################
#@brief 得到数据路径
#@param path 路径
#@return 数据路径
####################################################
def GetDataPath(file,folder=GetDataFolder()) :
	path = ''
	data = CombinePath('/data/',GetTimeFolder())
	if folder == '' :
		path = CombinePath(GetBasePath(),data)
	else :
		path = CombinePath(CombinePath(GetBasePath(),data),folder)
	
	if file == None :
		return path
	else :
		return CombinePath(path,file)
		
####################################################
#@brief 得到数据路径
#@param path 路径
#@return 数据路径
####################################################
def GetTestPath(folder=GetDataFolder()) :
	path = ''
	if folder == '' :
		path = CombinePath(GetBasePath(),'/test/')
	else :
		path = CombinePath(CombinePath(GetBasePath(),'/test/'),folder)
	return path

####################################################
#@brief 生成本地置配参数
#@param cfg 配置
#@param fun 函数
#@param lib 库名称
#@return 本地置配参数
####################################################
def BuildLocalCfg(cfg,fun,lib,protopath='',protofile='') :
	return QTS_CMD_CFG_KEY + "=" + cfg + ',' + fun + ',' + BuildLibraryFile(lib) + ',' + protopath + ',' + protofile

####################################################
#@brief 生成备份文件名称
#@param file 文件名称
#@return 文件名称
####################################################	
def BuildBackupFile(file=None,folder=GetCfgFolder()) :
	if file == None or file == '' :
		return ''
	path = ''
	backup = CombinePath('/backup/',GetTimeFolder())
	if folder == '' :
		path = CombinePath(GetBasePath(),backup)
	else :
		path = CombinePath(CombinePath(GetBasePath(),backup),folder)
	backupfile = ''
	if GetBackupType() == xfile :			
		backupfile = CombinePath(path,file + '.bup')
	elif GetBackupType() == bfile :
		backupfile = CombinePath(path,file + '.dat')
	elif GetBackupType() == sqlite :
		backupfile = file
	elif GetBackupType() == mysql :
		backupfile = file
	elif GetBackupType() == xml :
		backupfile = file
	return backupfile
	
####################################################
#@brief 生成测试输入文件路径
#@param file 文件名称
#@return 文件路径
####################################################	
def BuildTestInputFile(file) :	
	return CombinePath(GetTestPath('input'),file)
	
####################################################
#@brief 生成测输出试文件路径
#@param file 文件名称
#@return 文件路径
####################################################	
def BuildTestOutputFile(file) :	
	return CombinePath(GetTestPath('output'),file)

####################################################
#@brief 生成备份文件名称
#@param file 文件名称
#@return 文件名称
####################################################	
def BuildLoaderFile(file=None,tag='') :	
	if file == None or file == '' :
		return ''
	loaderfile = ''
	if GetLoaderType() == xfile :			
		loaderfile = GetDataPath(file + '.' + tag)
	elif GetLoaderType() == bfile :
		loaderfile = GetDataPath(file + '.' + tag)
	elif GetLoaderType() == sqlite :
		loaderfile = file + '_' + tag
	elif GetLoaderType() == mysql :
		loaderfile = file + '_' + tag
	elif GetLoaderType() == xml :
		loaderfile = file + '_' + tag
	return loaderfile
	
####################################################
#@brief 得到策略服务的路径
#@return 策略服务的路径
####################################################		
def GetSSPath() :
	return CombinePath(GetCfgPath(),'server/ss/')
	
####################################################
#@brief 得到数据服务的路径
#@return 数据服务的路径
####################################################	
def GetDSPath() :
	return CombinePath(GetCfgPath(),'server/ds/')
	
####################################################
#@brief 得到交易通道服务的路径
#@return 交易通道服务的路径
####################################################	
def GetGWPath() :
	return CombinePath(GetCfgPath(),'server/gw/')

####################################################
#@brief 得到控制服务的路径
#@return 控制服务的路径
####################################################	
def GetCSPath() :
	return CombinePath(GetCfgPath(),'server/cs/')

####################################################
#@brief 得到监控服务的路径
#@return 监控服务的路径
####################################################	
def GetGVPath() :
	return CombinePath(GetCfgPath(),'server/gv/')

####################################################
#@brief 得到记录服务的路径
#@return 记录服务的路径
####################################################	
def GetRCPath() :
	return CombinePath(GetCfgPath(),'server/rc/')

####################################################
#@brief 得到共享插件的路径
#@return 共享插件的路径
####################################################	
def GetSharePath() :
	return CombinePath(GetCfgPath(),'share/')

####################################################
#@brief 得到属性页的路径
#@return 资源的路径
####################################################
def GetPropertyPath(path) :
	return CombinePath(path,'property/')

####################################################
#@brief 得到资源的路径
#@return 资源的路径
####################################################	
def GetResourcePath(path) :
	return CombinePath(path,'res/')

####################################################
#@brief 得到资源的路径
#@return 资源的路径
####################################################
def GetLanguagePath(path) :
	return CombinePath(GetResourcePath(path),'language/{0}/'.format(GetLanguage()))

####################################################
#@brief 得到资源的路径
#@return 资源的路径
####################################################
def GetMusicPath(path) :
	return CombinePath(GetResourcePath(path),'music/')

####################################################
#@brief 得到资源的路径
#@return 资源的路径
####################################################
def GetQSSPath(path) :
	return CombinePath(GetResourcePath(path),'qss/')

####################################################
#@brief 得到终端的路径
#@return 终端的路径
####################################################	
def GetConsolePath() :
	return CombinePath(GetCfgPath(),'console/')
	
####################################################
#@brief 得到终端插件的路径
#@return 终端插件的路径
####################################################	
def GetGuiPath() :
	return CombinePath(GetConsolePath(),'gui/')
	
####################################################
#@brief 得到配置入口的路径
#@return 配置入口的路径
####################################################	
def GetEntryPath() :
	return CombinePath(GetCfgPath(),'entry/')
	
####################################################
#@brief 得到回放数据的路径
#@return 回放数据的路径
####################################################	
def GetReplayPath() :
	path = GetMainDictForString(QTS_REPLAY_PATH)
	if path=='' :
		path = GetEnv(QTS_REPLAY_PATH_KEY,'')
	return path	
	
####################################################
#@brief 得到策略插件的路径
#@param parent 父目录
#@return 策略插件的路径
####################################################	
def GetStrategyPath(parent) :
	return CombinePath(parent,'strategy')
	
####################################################
#@brief 得到算法插件的路径
#@param parent 父目录
#@return 算法插件的路径
####################################################	
def GetAlgoPath(parent) :
	return CombinePath(parent,'algo')
	
####################################################
#@brief 得到计算插件的路径
#@param parent 父目录
#@return 计算插件的路径
####################################################	
def GetCalculatePath(parent) :
	return CombinePath(parent,'calculate')

####################################################
#@brief 得到解析插件的路径
#@param parent 父目录
#@return 解析插件的路径
####################################################	
def GetParserPath(parent) :
	return CombinePath(parent,'parser')

####################################################
#@brief 得到数据插件的路径
#@param parent 父目录
#@return 数据插件的路径
####################################################	
def GetMarketPath(parent) :
	return CombinePath(parent,'market')
	
####################################################
#@brief 得到交易通道插件的路径
#@param parent 父目录
#@return 交易通道插件的路径
####################################################	
def GetExchangePath(parent) :
	return CombinePath(parent,'exchange')

####################################################
#@brief 得到备份插件的路径
#@param parent 父目录
#@return 备份插件的路径
####################################################	
def GetBackupPath(parent) :
	return CombinePath(parent,'backup')

####################################################
#@brief 得到加载插件的路径
#@param parent 父目录
#@return 加载插件的路径
####################################################	
def GetLoaderPath(parent) :
	return CombinePath(parent,'loader') 

####################################################
#@brief 得到风控插件的路径径
#@param parent 父目录
#@return 风控插件的路径
####################################################	
def GetCheckPath(parent) :
	return CombinePath(parent,'check')
		
####################################################
#@brief 得到传输插件的路径
#@param parent 父目录
#@return 传输插件的路径
####################################################		
def GetTransferPath(parent) :
	return CombinePath(parent,'transfer')		
		
####################################################
#@brief 得到数据传输插件的路径
#@param parent 父目录
#@return 数据传输插件的路径
####################################################	
def GetDSTransferPath(parent) :
	return CombinePath(parent,'dstransfer')		

####################################################
#@brief 得到交易传输插件的路径
#@param parent 父目录
#@return 交易传输插件的路径
####################################################	
def GetGWTransferPath(parent) :
	return CombinePath(parent,'gwtransfer')	

####################################################
#@brief 得到终端传输插件的路径
#@param parent 父目录
#@return 终端传输插件的路径
####################################################		
def GetGUITransferPath(parent) :
	return CombinePath(parent,'guitransfer')	
	
####################################################
#@brief 得到远程风控传输插件的路径
#@param parent 父目录
#@return 终端传输插件的路径
####################################################		
def GetCKTransferPath(parent) :
	return CombinePath(parent,'cktransfer')	
	
####################################################
#@brief 得到远程风控传输插件的路径
#@param parent 父目录
#@return 终端传输插件的路径
####################################################		
def GetCPTransferPath(parent) :
	return CombinePath(parent,'cptransfer')	
	
####################################################
#@brief 得到监控插件的路径
#@param parent 父目录
#@return 监控插件的路径
####################################################	
def GetMonitorPath(parent) :
	return CombinePath(parent,'monitor')	
	
####################################################
#@brief 得到过滤插件的路径
#@param parent 父目录
#@return 过滤插件的路径
####################################################		
def GetFilterPath(parent) :
	return CombinePath(parent,'filter')
	
####################################################
#@brief 得到逻辑插件的路径
#@param parent 父目录
#@return 逻辑插件的路径
####################################################		
def GetLogicPath(parent) :
	return CombinePath(parent,'logic')

####################################################
#@brief 得到协议文件的路径
#@return 协议文件的路径
####################################################		
def GetProtoPath() :
	return GetCfgPath()
	
####################################################
#@brief 得到协议文件
#@return 协议文件
####################################################	
def GetProtoFile() :
	return QTS_PROTO_FILE
	
#######################################################################	
#######################################################################	
#应用初始化操作函数
#######################################################################

####################################################
#@brief 初始化测试运行环境
####################################################
def InitTestEnv() :
	if GetAppVersion() == release :
		if GetAppSystem() == windows :
			SetAppVersionStr(QTS_APP_WINDOWS_RELEASE)
		else :
			SetAppVersionStr(QTS_APP_LINUX_RELEASE)
	elif GetAppVersion() == debug :
		if GetAppSystem() == windows :
			SetAppVersionStr(QTS_APP_WINDOWS_DEBUG)
		else :
			SetAppVersionStr(QTS_APP_LINUX_DEBUG)
	else :
		SetAppVersionStr('')

####################################################
#@brief 初始化运行环境，参数是入口配置模块
#@param 0  module：设置缺省的主模块
#@param 1  appmode：设置应用程序的类型，QTS_APP_MODE_ALL,QTS_APP_MODE_SERVER,QTS_APP_MODE_SINGLE,参看qts_security.py中的定义
#@param 2  appver：设置应用程序的版本，release、debug和publish,定义参看qts_security.py中的定义
#@param 3  runver：设置程序运行的版本，release和debug，定义参看qts_security.py中的定义，
#		这个主要是用来指定python策略的启动方式，如果是QGOnuca应用程序起动时，
#		则设为release，如果是由python启动，则设为debug
#@param 4  breplay：设置是否支持回放
#@param 5  bmatch：设置是否支持撮合
#@param 6  bdsmonitor：设置是否支持行情服务的监控,QTS_MONITOR_NONE,QTS_MONITOR_BINARY,QTS_MONITOR_PROTOBUF,QTS_MONITOR_BOTH,定义参看qts_security.py中的定义
#@param 7  bgwmonitor：设置是否支持下单通道服服的监控,QTS_MONITOR_NONE,QTS_MONITOR_BINARY,QTS_MONITOR_PROTOBUF,QTS_MONITOR_BOTH,定义参看qts_security.py中的定义
#@param 8  bssmonitor：设置是否支持策略服务的监控,QTS_MONITOR_NONE,QTS_MONITOR_BINARY,QTS_MONITOR_PROTOBUF,QTS_MONITOR_BOTH,定义参看qts_security.py中的定义
#@param 9  bguimonitor：设置是否支持GUI的监控,QTS_MONITOR_NONE,QTS_MONITOR_BINARY,QTS_MONITOR_PROTOBUF,QTS_MONITOR_BOTH,定义参看qts_security.py中的定义
#@param 10 basepath：如果是python启动的环境，则要先设置程序的配置的根目录
#@param 11 replaypath：如果是python启动的环境，则要回放数据的根目录
#@param 12 loadertype: 加载器类型,xfile,sqlite,mysql,mixplugin,定义参看qts_security.py中的定义
#@param 13 backuptype: 备份器类型,xfile,sqlite,mysql,mixplugin,定义参看qts_security.py中的定义
#@param 14 replaytype: 备份器类型,xfile,sqlite,mysql,mixplugin,定义参看qts_security.py中的定义
####################################################
def InitRunEnv(*args,**kwargs) :
	#创建主节点
	CreateRootGlobals()
	#设置缺省的主模块
	SetAppDefaultPath(GetArgByIndexAndName(0,'module','',*args,**kwargs))
	#设置应用程序的类型，参看qts_security.py中的定义
	SetAppMode(GetArgByIndexAndName(1,'appmode',QTS_APP_MODE_ALL,*args,**kwargs))
	#设置应用程序的版本，release和debug,定义参看qts_security.py中的定义
	SetAppVersion(GetArgByIndexAndName(2,'appver',debug,*args,**kwargs))
	#设置程序运行的版本，release和debug，定义参看qts_security.py中的定义
	#这个主要是用来指定python策略的启动方式，如果是QGOnuca应用程序起动时，
	#则设为release，如果是由python启动，则设为debug
	SetRunVersion(GetArgByIndexAndName(3,'runver',debug,*args,**kwargs))	
	#设置操作系统的类型，参看qts_security.py中的定义
	if sys.platform == QTS_SYSTEM_WINDOWS_STR :
		SetAppSystem(windows)
	else:
		SetAppSystem(linux)	
	#设置是否支持回放
	SetIsReplay(GetArgByIndexAndName(4,'breplay',False,*args,**kwargs))
	#设置是否支持撮合
	SetIsMatch(GetArgByIndexAndName(5,'bmatch',False,*args,**kwargs))
	#设置是否支持行情服务的监控
	SetIsDSMonitor(GetArgByIndexAndName(6,'bdsmonitor',QTS_MONITOR_NONE,*args,**kwargs))
	#设置是否支持下单通道服服的监控
	SetIsGWMonitor(GetArgByIndexAndName(7,'bgwmonitor',QTS_MONITOR_NONE,*args,**kwargs))
	#设置是否支持策略服务的监控
	SetIsSSMonitor(GetArgByIndexAndName(8,'bssmonitor',QTS_MONITOR_NONE,*args,**kwargs))
	#设置是否支持GUI的监控
	SetIsGUIMonitor(GetArgByIndexAndName(9,'bguimonitor',QTS_MONITOR_NONE,*args,**kwargs))	
	#如果是python启动的环境，则要先设置程序的配置的根目录，还要回放数据的根目录
	if GetRunVersion() == debug :
		SetBasePath(GetArgByIndexAndName(10,'basepath','',*args,**kwargs))	
		if GetIsReplay() :
			SetReplayPath(GetArgByIndexAndName(11,'replaypath','',*args,**kwargs))
	#设置加载器的类型，参看qts_security.py中的定义
	SetLoaderType(GetArgByIndexAndName(12,'loadertype',xfile,*args,**kwargs))
	#设置备份器的类型，参看qts_security.py中的定义
	SetBackupType(GetArgByIndexAndName(13,'backuptype',xfile,*args,**kwargs))	
	#设置回放器的类型，参看qts_security.py中的定义
	SetReplayType(GetArgByIndexAndName(14,'replaytype',sqlite,*args,**kwargs))	
	
#######################################################################
#######################################################################
#插件管理与操作函数
#######################################################################

####################################################
#@brief 创建管理插件
#@param module  			应用模块名称
#@param managername  		管理器名称
#@param key  				管理器ID
#@param name  				管理器名称
#@param log  				日志
#@param plugins  			插件槽名称
####################################################
def CreatePluginManager(module,managername,key,name,log,plugins) :
	if IsExistMainDict(module,managername) :
		return
	AppendMainDict(module,managername)
	AppendItemForMainDict(module,managername,QTS_CFG_KEY_OBJID,key)
	AppendItemForMainDict(module,managername,QTS_CFG_KEY_NAME,name)
	AppendItemForMainDict(module,managername,QTS_CFG_KEY_LOG,log)
	AppendItemForMainDict(module,managername,QTS_CFG_KEY_CFG,plugins)

####################################################
#@brief 为管理插件创建插件槽
#@param module  		应用模块名称
#@param pluginsname  	插件槽名称
####################################################	
def CreatePluginsForManager(module,pluginsname) :
	if IsExistMainDict(module,pluginsname) :
		return
	AppendMainDict(module,pluginsname)	

####################################################
#@brief 向插件槽添加插件
#@param module  		应用模块名称
#@param pluginsname  	插件槽名称
#@param key  			插件名称
#@param value  			插件值
####################################################
def AppendPluginForManager(module,pluginsname,key,value) :
	AppendItemForMainDict(module,pluginsname,key,value)
	
####################################################
#@brief 生成插件的ID
#@param pluginsid  	插件槽ID
#@param pluginid  	插件ID种子
#@return  插件ID
####################################################	
def CreateObjectId(pluginsid,pluginid) :
	return pluginsid * 1000 + pluginid;
	
####################################################
#@brief 通过名称得到插件管理者
#@param module  应用模块名称
#@param managername  管理器名称
#@return  管理器对象
####################################################	
def GetManagerByName(module,managername) :
	return GetAppGlobals(module)[managername]
	
####################################################
#@brief 通过名称得到插件
#@param module  		应用模块名称
#@param pluginname  	插件名称
#@return	插件
####################################################	
def GetPluginByName(module,pluginname) :
	return GetAppGlobals(module)[pluginname]
	
####################################################
#@brief 通过名称得到插件管理者
#@param module  			应用模块名称
#@param managername 		管理器名称 
#@return	管理器ID
####################################################	
def GetManagerId(module,managername) :
	return GetManagerByName(module,managername)[QTS_CFG_KEY_OBJID]
	
####################################################
#@brief 通过名称得到插件ID
#@param module  		应用模块名称	
#@param pluginname  	插件名称
#@return	插件ID
####################################################	
def GetPluginId(module,pluginname) :
	return GetPluginByName(module,pluginname)[QTS_CFG_KEY_OBJID]
	
####################################################
#@brief 产生插件ID
#@param plugins  		插槽名称
#@param pluginid  		插槽ID
#@return	插件ID
####################################################		
def GeneratorObjectId(plugins,pluginid) :
	return CreateObjectId(plugins[QTS_CFG_KEY_OBJID], pluginid)

####################################################
#@brief 通过插件管理器产生插件ID
#@param module			应用模块名称
#@param managername  	管理器名称
#@param pluginid  		插件ID种子
#@return	插件ID
####################################################	
def GeneratorObjectIdByManager(module,managername,pluginid) :
	return GeneratorObjectId(GetAppGlobals(module)[managername], pluginid)
	
####################################################
#@brief 产生插名槽称
#@param pluginsname 	插槽名称 
#@param pluginid  		插槽ID
#@return
####################################################		
def GeneratorObjectName(pluginsname,pluginid) :
	return pluginsname + '_{0}'.format(pluginid)

####################################################
#@brief 为插件添加属性
#@param module 		  应用模块名称	
#@param pluginname    插件名称
#@param key  		  属性名称
#@param value  		  属性值
####################################################	
def AppendPropertyForPlugin(module,pluginname,key,value) :
	AppendItemForMainDict(module,pluginname,key,value)

####################################################
#@brief 执行目录下的所有的PY文件
#@param path 		  目录
####################################################
def LoadPythonFileByPath(path) :
	sys.path.append(path)
	files = os.listdir(path)
	entrys = list()
	for file in files :
		if os.path.isfile('{0}/{1}'.format(path,file)) :
			sufix = os.path.splitext(file)[1][1:]
			entry = os.path.splitext(file)[0]
			if (sufix == 'py') and  (not entry in entrys) :
				entrys.append(entry)
		else :
			LoadPythonFileByPath('{0}/{1}'.format(path,file))
	for entry in entrys :
		try :
			exec 'from ' + entry + ' import *'
		except :
			print('import error resource file:{0}'.format(entry))

####################################################	
#@brief 创建插件
#@param 0  module :插件所在的模块
#@param 1  managername :插件管理者的名称
#@param 2  pluginsname :插槽的名称
#@param 3  pluginname :插件的名称
#@param 4  objid :插件的ID
#@param 5  secuid :插件所支持的市场和品种
#@param 6  cfg :插件的配置
#@param 7  dllfile :插件的文件
#@param 8  dllfun :插件的入口函数
#@param 9  dllpath :插件文件的路径
####################################################
def CreatePlugin(*args,**kwargs) :
	if IsExistMainDict(GetArgByIndexAndName(0,'module','',*args,**kwargs),GetArgByIndexAndName(3,'pluginname','',*args,**kwargs)) :
		raise StandardError('exist plugin name=' + GetArgByIndexAndName(3,'pluginname','',*args,**kwargs))
	AppendPluginForManager(GetArgByIndexAndName(0,'module','',*args,**kwargs),GetArgByIndexAndName(2,'pluginsname','',*args,**kwargs),
						'plugin_'+GetArgByIndexAndName(3,'pluginname','',*args,**kwargs),GetArgByIndexAndName(3,'pluginname','',*args,**kwargs))
	AppendMainDict(GetArgByIndexAndName(0,'module','',*args,**kwargs),GetArgByIndexAndName(3,'pluginname','',*args,**kwargs))
	AppendPropertyForPlugin(GetArgByIndexAndName(0,'module','',*args,**kwargs),GetArgByIndexAndName(3,'pluginname','',*args,**kwargs),QTS_CFG_KEY_SECUID,GetArgByIndexAndName(5,'secuid',ALL_MARKET,*args,**kwargs))
	AppendPropertyForPlugin(GetArgByIndexAndName(0,'module','',*args,**kwargs),GetArgByIndexAndName(3,'pluginname','',*args,**kwargs),QTS_CFG_KEY_OBJID,GeneratorObjectIdByManager(GetArgByIndexAndName(0,'module','',*args,**kwargs),GetArgByIndexAndName(1,'managername','',*args,**kwargs),GetArgByIndexAndName(4,'objid',0,*args,**kwargs)))
	AppendPropertyForPlugin(GetArgByIndexAndName(0,'module','',*args,**kwargs),GetArgByIndexAndName(3,'pluginname','',*args,**kwargs),QTS_CFG_KEY_NAME,GetArgByIndexAndName(3,'pluginname','',*args,**kwargs))
	AppendPropertyForPlugin(GetArgByIndexAndName(0,'module','',*args,**kwargs),GetArgByIndexAndName(3,'pluginname','',*args,**kwargs),QTS_CFG_KEY_LOG,GetAppGlobals(GetArgByIndexAndName(0,'module','',*args,**kwargs))[GetArgByIndexAndName(1,'managername','',*args,**kwargs)][QTS_CFG_KEY_LOG])
	AppendPropertyForPlugin(GetArgByIndexAndName(0,'module','',*args,**kwargs),GetArgByIndexAndName(3,'pluginname','',*args,**kwargs),QTS_CFG_KEY_CFG,GetArgByIndexAndName(6,'cfg','',*args,**kwargs))
	AppendPropertyForPlugin(GetArgByIndexAndName(0,'module','',*args,**kwargs),GetArgByIndexAndName(3,'pluginname','',*args,**kwargs),QTS_CFG_KEY_FILE,GetArgByIndexAndName(7,'dllfile','',*args,**kwargs))
	AppendPropertyForPlugin(GetArgByIndexAndName(0,'module','',*args,**kwargs),GetArgByIndexAndName(3,'pluginname','',*args,**kwargs),QTS_CFG_KEY_FUN,GetArgByIndexAndName(8,'dllfun','',*args,**kwargs))
	AppendPropertyForPlugin(GetArgByIndexAndName(0,'module','',*args,**kwargs),GetArgByIndexAndName(3,'pluginname','',*args,**kwargs),QTS_CFG_KEY_PATH,GetArgByIndexAndName(9,'dllpath',GetLibPath(),*args,**kwargs))
	
####################################################	
#@brief 创建自由日志的插件
#@param 0  module :插件所在的模块
#@param 1  managername :插件管理者的名称
#@param 2  pluginsname :插槽的名称
#@param 3  pluginname :插件的名称
#@param 4  objid :插件的ID
#@param 5  secuid :插件所支持的市场和品种
#@param 6  log :自定义的日志
#@param 7  cfg :插件的配置
#@param 8  dllfile :插件的文件
#@param 9  dllfun :插件的入口函数
#@param 10  dllpath :插件文件的路径
####################################################
def CreatePluginHasLog(*args,**kwargs) :
	if IsExistMainDict(GetArgByIndexAndName(0,'module','',*args,**kwargs),GetArgByIndexAndName(3,'pluginname','',*args,**kwargs)) :
		raise StandardError('exist plugin name=' + GetArgByIndexAndName(3,'pluginname','',*args,**kwargs))
	AppendPluginForManager(GetArgByIndexAndName(0,'module','',*args,**kwargs),GetArgByIndexAndName(2,'pluginsname','',*args,**kwargs),
						'plugin_'+GetArgByIndexAndName(3,'pluginname','',*args,**kwargs),GetArgByIndexAndName(3,'pluginname','',*args,**kwargs))
	AppendMainDict(GetArgByIndexAndName(0,'module','',*args,**kwargs),GetArgByIndexAndName(3,'pluginname','',*args,**kwargs))
	AppendPropertyForPlugin(GetArgByIndexAndName(0,'module','',*args,**kwargs),GetArgByIndexAndName(3,'pluginname','',*args,**kwargs),QTS_CFG_KEY_SECUID,GetArgByIndexAndName(5,'secuid',ALL_MARKET,*args,**kwargs))
	AppendPropertyForPlugin(GetArgByIndexAndName(0,'module','',*args,**kwargs),GetArgByIndexAndName(3,'pluginname','',*args,**kwargs),QTS_CFG_KEY_OBJID,GeneratorObjectIdByManager(GetArgByIndexAndName(0,'module','',*args,**kwargs),GetArgByIndexAndName(1,'managername','',*args,**kwargs),GetArgByIndexAndName(4,'objid',0,*args,**kwargs)))
	AppendPropertyForPlugin(GetArgByIndexAndName(0,'module','',*args,**kwargs),GetArgByIndexAndName(3,'pluginname','',*args,**kwargs),QTS_CFG_KEY_NAME,GetArgByIndexAndName(3,'pluginname','',*args,**kwargs))
	AppendPropertyForPlugin(GetArgByIndexAndName(0,'module','',*args,**kwargs),GetArgByIndexAndName(3,'pluginname','',*args,**kwargs),QTS_CFG_KEY_LOG,GetArgByIndexAndName(6,'log',GetAppGlobals(GetArgByIndexAndName(0,'module','',*args,**kwargs))[GetArgByIndexAndName(1,'managername','',*args,**kwargs)][QTS_CFG_KEY_LOG],*args,**kwargs))
	AppendPropertyForPlugin(GetArgByIndexAndName(0,'module','',*args,**kwargs),GetArgByIndexAndName(3,'pluginname','',*args,**kwargs),QTS_CFG_KEY_CFG,GetArgByIndexAndName(7,'cfg','',*args,**kwargs))
	AppendPropertyForPlugin(GetArgByIndexAndName(0,'module','',*args,**kwargs),GetArgByIndexAndName(3,'pluginname','',*args,**kwargs),QTS_CFG_KEY_FILE,GetArgByIndexAndName(8,'dllfile','',*args,**kwargs))
	AppendPropertyForPlugin(GetArgByIndexAndName(0,'module','',*args,**kwargs),GetArgByIndexAndName(3,'pluginname','',*args,**kwargs),QTS_CFG_KEY_FUN,GetArgByIndexAndName(9,'dllfun','',*args,**kwargs))
	AppendPropertyForPlugin(GetArgByIndexAndName(0,'module','',*args,**kwargs),GetArgByIndexAndName(3,'pluginname','',*args,**kwargs),QTS_CFG_KEY_PATH,GetArgByIndexAndName(10,'dllpath',GetLibPath(),*args,**kwargs))
	
####################################################
#@brief 设置插件名称
#@param module 
#@param pluginsname  
#@param name  
####################################################	
def SetPluginName(module,pluginname,name) :
	AppendPropertyForPlugin(module,pluginname,QTS_CFG_KEY_NAME,name)
	
####################################################
#@brief 设置插件远程信息
#@param module 
#@param pluginsname  
#@param address  
#@param port
#@param heart
####################################################
def SetRemoteInfo(module,pluginname,address='',port=0,heart=30) :
	AppendPropertyForPlugin(module,pluginname,QTS_CFG_KEY_ADDRESS,address)
	AppendPropertyForPlugin(module,pluginname,QTS_CFG_KEY_PORT,port)
	AppendPropertyForPlugin(module,pluginname,QTS_CFG_KEY_HEART,heart)
	
####################################################
#@brief 检查是否存在入口文件
#@param path 
#@return
####################################################	
def IsExistEntryFile(path) :
	entryfile = path + '/' + QTS_ENTRY_PYFILE + '.py'
	if os.path.exists(entryfile) and os.path.isfile(entryfile) :
		return True
	return False
	
####################################################
#@brief 检查是否存在入口文件
#@param parent  父目录
#@param path 子目录
#@return 文件路径
####################################################	
def FindPlugin(parent,path) :
	filepath = parent + '/' + path + '/' + path + '.py'
	if os.path.exists(filepath) and os.path.isfile(filepath) :
		return (parent + '/' + path,path)
	else :
		raise StandardError('no find file=' + filepath)

####################################################
#@brief 获得所有的插件集
#@param path  插件目录
#@return 插件集
####################################################		
def FindPlugins(path) :
	result = list()
	stragegy_floders = os.listdir(path)
	for subpath in stragegy_floders :
		result.append(FindPlugin(path,subpath))
	return result
	
####################################################
#@brief 加载目录下的所有的插件
#@param path 插件目录
#@return 所有的命令集
####################################################	
def LoadPlugins(path) :
	commands = list()
	if IsExistEntryFile(path) :
		importstring = 'from ' + QTS_ENTRY_PYFILE + ' import *'
		commands.append(importstring)
		sys.path.append(path)
	else :
		plugins = FindPlugins(path)
		for plugin in plugins :
			importstring = 'from ' + plugin[1] + ' import *'
			commands.append(importstring)
			sys.path.append(plugin[0])					
	return commands
	
#######################################################################	
#######################################################################	
#策略参数配置的操作函数
#######################################################################

####################################################
#@brief 产生策略交易标的集名称
#@param name 种子名称
#@return 策略交易标的集名称
####################################################	
def GetInstrumentNameForStrategy(name) :
	return name + '_' + QTS_CFG_SUFIX_INSTRUMENT
	
####################################################
#@brief 产生策略可变参数集名称
#@param name 种子名称
#@return 策略可变参数名称
####################################################
def GetParameterNameForStrategy(name) :
	return name + '_' + QTS_CFG_SUFIX_PARAMETER

####################################################
#@brief 产生策略静态参数名称
#@param name 种子名称
#@return 策略静态参数名称
####################################################	
def GetCommentNameForStrategy(name) :
	return name + '_' + QTS_CFG_SUFIX_COMMENT

####################################################
#@brief 产生策略命令参数名称
#@param name 种子名称
#@return 策略命令参数名称
####################################################	
def GetCommandNameForStrategy(name) :
	return name + '_' + QTS_CFG_SUFIX_COMMAND

####################################################
#@brief 创建策略标的配置
#@param name 种子名称
####################################################	
def CreateInstrumentsForStrategy(name) :
	if IsExistMainList(GetAppPath(),GetInstrumentNameForStrategy(name)) :
		raise StandardError('exist instrument name=' + name)	
	AppendMainList(GetAppPath(),GetInstrumentNameForStrategy(name))
	
####################################################
#@brief 创建策略可变参数配置
#@param name 种子名称
####################################################		
def CreateParametersForStrategy(name) :
	if IsExistMainList(GetAppPath(),GetParameterNameForStrategy(name)) :
		raise StandardError('exist parameter name=' + name)	
	AppendMainList(GetAppPath(),GetParameterNameForStrategy(name))
	
####################################################
#@brief 创建策略静态参数配置
#@param name 种子名称
####################################################		
def CreateCommentsForStrategy(name) :
	if IsExistMainList(GetAppPath(),GetCommentNameForStrategy(name)) :
		raise StandardError('exist comment name=' + name)	
	AppendMainList(GetAppPath(),GetCommentNameForStrategy(name))
	
####################################################
#@brief 创建策略命令参数配置
#@param name 种子名称
####################################################		
def CreateCommandsForStrategy(name) :
	if IsExistMainList(GetAppPath(),GetCommandNameForStrategy(name)) :
		raise StandardError('exist command name=' + name)	
	AppendMainList(GetAppPath(),GetCommandNameForStrategy(name))
	
####################################################
#@brief 得到参数序号
#@param pos 参数位置
#@return 参数序号
####################################################
def GetParameterIndex(pos,*args,**kwargs) :
	index = GetArgByIndexAndName(pos,'index',-1,*args,**kwargs)
	if index < 0 :
		index = GetMainDictForInt(GetInstrumentNameForStrategy(GetArgByIndexAndName(0,'listname','',*args,**kwargs)))
		index += 1
		SetVarInMainDict(GetInstrumentNameForStrategy(GetArgByIndexAndName(0,'listname','',*args,**kwargs)),index)
	return index

####################################################
#@brief 添加策略标的参数属性
#@param 0  listname      		字典名称
#@param 1  key		配置键值，在一个策略中必须唯一
#@param 2  name		配置变量的名称
#@param 3  codetype	代码类型，暂支持：QTS_TRADE_UNKONWN,QTS_TRADE_CODE,QTS_TRADE_SIGNAL,QTS_TRADE_BASKET,QTS_TRADE_INDEX,QTS_TRADE_OWNER
#@param 4  market 	市场
#@param 5  category   品种
#@param 6  secucode   证券代码
#@param 7  index   	控件的排例顺序，控制显示
#@param 8  level		控件的层级，控制显示
#@param 9  status     显示状态，是否显示在GUI上，暂支持：QTS_INSTRUMENT_STATUS_DISPLAY,QTS_INSTRUMENT_STATUS_HIDE
#@param 10 mode    	控制类型，是否服务端推送相应数据，暂支持：QTS_INSTRUMENT_MODE_NONE,QTS_INSTRUMENT_MODE_PNL,QTS_INSTRUMENT_MODE_BOOK,QTS_INSTRUMENT_MODE_BOOK_PNL
#@param 11 component	控件的填充内容格式(序号:文本,序号:文本,....)
#@param 12 style		控件样式
#return  	例表中所有的位置
####################################################
def AppendInstrumentForStrategy(*args,**kwargs) :
	lists=list()
	lists.append(GetArgByIndexAndName(1,'key',0,*args,**kwargs))
	lists.append(GetArgByIndexAndName(2,'name','',*args,**kwargs))
	lists.append(GetArgByIndexAndName(3,'codetype',QTS_TRADE_UNKONWN,*args,**kwargs))
	lists.append([GetArgByIndexAndName(4,'market',0,*args,**kwargs),GetArgByIndexAndName(5,'category',0,*args,**kwargs),GetArgByIndexAndName(6,'secucode',0,*args,**kwargs)])
	lists.append(GetParameterIndex(7,*args,**kwargs))
	lists.append(GetArgByIndexAndName(8,'level',1,*args,**kwargs))
	lists.append(GetArgByIndexAndName(9,'status',QTS_INSTRUMENT_STATUS_DISPLAY,*args,**kwargs))
	lists.append(GetArgByIndexAndName(10,'mode',QTS_INSTRUMENT_MODE_NONE,*args,**kwargs))
	lists.append(GetArgByIndexAndName(11,'component','',*args,**kwargs))
	lists.append(GetArgByIndexAndName(12,'style','',*args,**kwargs))
	return AppendItemForMainList(GetAppPath(),GetInstrumentNameForStrategy(GetArgByIndexAndName(0,'listname','',*args,**kwargs)),lists)

####################################################
#@brief 设置策略标的参数属性
#@param listname 	 策略标的参数名称
#@param parentpos 	 参数所在位置
#@param childpos 	 子参数位置
#@param data 		 数据
####################################################	
def SetPropertyForInstrument(listname,parentpos,childpos,data) :
	value = GetMainListValue(GetAppPath(),GetInstrumentNameForStrategy(listname),parentpos)
	if value != None :
		if childpos < len(value) :
			value[childpos] = data
		else :
			raise StandardError('pos larger len,pos={0}'.format(childpos))	

####################################################			
#@brief 添加可变参数
#@param 0  listname      		字典名称
#@param 1  key				配置键值，在一个策略中必须唯一
#@param 2  name				配置变量的名称
#@param 3  value				配置的值
#@param 4  verdecimal			配置的值小数位数
#@param 5  index				控件的排例顺序，控制显示
#@param 6  level				控件的层级，控制显示，暂支持：QTS_PARAMETER_STATUS_DISPLAY,QTS_PARAMETER_STATUS_HIDE
#@param 7  save				是否对值的改变进行备份,暂支持：True,False
#@param 8  status				控件状态，控制显示，是否可编译，暂支持：QTS_DISABLE,QTS_ENABLE
#@param 9  mode				控件类型，暂支持：QTS_COMPONENT_TEXTBOX和QTS_COMPONENT_COMBOX
#@param 10 component			控件的填充内容格式(序号:文本,序号:文本,....)
#@param 11 style				控件样式
#@return 例表中所有的位置
####################################################
def AppendParameterForStrategy(*args,**kwargs):
	lists=list()
	lists.append(GetArgByIndexAndName(1,'key',0,*args,**kwargs))
	lists.append(GetArgByIndexAndName(2,'name','',*args,**kwargs))
	lists.append(ToInt64(GetArgByIndexAndName(3,'value',0,*args,**kwargs)))
	lists.append(GetArgByIndexAndName(4,'vardecimal',0,*args,**kwargs))
	lists.append(GetParameterIndex(5,*args,**kwargs))
	lists.append(GetArgByIndexAndName(6,'level',1,*args,**kwargs))
	lists.append(GetArgByIndexAndName(7,'save',False,*args,**kwargs))
	lists.append(GetArgByIndexAndName(8,'status',QTS_ENABLE,*args,**kwargs))
	lists.append(GetArgByIndexAndName(9,'mode',QTS_COMPONENT_TEXTBOX,*args,**kwargs))	
	lists.append(GetArgByIndexAndName(10,'component','',*args,**kwargs))
	lists.append(GetArgByIndexAndName(11,'style','',*args,**kwargs))
	return AppendItemForMainList(GetAppPath(),GetParameterNameForStrategy(GetArgByIndexAndName(0,'listname','',*args,**kwargs)),lists)
	
####################################################
#@brief 设置策略可变参数属性
#@param listname 	 策略标的参数名称
#@param parentpos 	 参数所在位置
#@param childpos 	 子参数位置
#@param data 		 数据
####################################################		
def SetPropertyForParameter(listname,parentpos,childpos,data) :
	value = GetMainListValue(GetAppPath(),GetParameterNameForStrategy(listname),parentpos)
	if value != None :
		if childpos < len(value) :
			value[childpos] = data
		else :
			raise StandardError('pos larger len,pos={0}'.format(childpos))	
		
####################################################
#@brief 添加静态参数
#@param 0  listname			字典名称
#@param 1  key				配置键值，在一个策略中必须唯一
#@param 2  name				配置变量的名称
#@param 3  value				配置的值
#@param 4  verdecimal			配置的值小数位数
#@param 5  index				控件的排例顺序，控制显示
#@param 6  level				控件的层级，控制显示，暂支持：QTS_PARAMETER_STATUS_DISPLAY,QTS_PARAMETER_STATUS_HIDE
#@param 7  modify				是否改变可向远端发送，暂支持：QTS_FALSE,QTS_TRUE
#@param 8  status				控件状态，控制显示，是否由服务端推送给GUI，暂支持：QTS_DISABLE,QTS_ENABLE
#@param 9  mode				控件类型，暂支持QTS_COMPONENT_LABEL
#@param 10 component			控件的填充内容格式(序号:文本,序号:文本,....)
#@param 11 style				控件样式
#@return 例表中所有的位置
####################################################
def AppendCommentForStrategy(*args,**kwargs):
	lists=list()
	lists.append(GetArgByIndexAndName(1,'key',0,*args,**kwargs))
	lists.append(GetArgByIndexAndName(2,'name','',*args,**kwargs))
	lists.append(ToInt64(GetArgByIndexAndName(3,'value',0,*args,**kwargs)))
	lists.append(GetArgByIndexAndName(4,'vardecimal',0,*args,**kwargs))
	lists.append(GetParameterIndex(5,*args,**kwargs))
	lists.append(GetArgByIndexAndName(6,'level',1,*args,**kwargs))
	lists.append(GetArgByIndexAndName(7,'modify',True,*args,**kwargs))
	lists.append(GetArgByIndexAndName(8,'status',QTS_ENABLE,*args,**kwargs))
	lists.append(GetArgByIndexAndName(9,'mode',QTS_COMPONENT_LABEL,*args,**kwargs))	
	lists.append(GetArgByIndexAndName(10,'component','',*args,**kwargs))
	lists.append(GetArgByIndexAndName(11,'style','',*args,**kwargs))
	return AppendItemForMainList(GetAppPath(),GetCommentNameForStrategy(GetArgByIndexAndName(0,'listname','',*args,**kwargs)),lists)

####################################################
#@brief 设置策略静态参数属性
#@param listname 	 策略标的参数名称
#@param parentpos 	 参数所在位置
#@param childpos 	 子参数位置
#@param data 		 数据
####################################################		
def SetPropertyForComment(listname,parentpos,childpos,data) :
	value = GetMainListValue(GetAppPath(),GetCommentNameForStrategy(listname),parentpos)
	if value != None :
		if childpos < len(value) :
			value[childpos] = data
		else :
			raise StandardError('pos larger len,pos={0}'.format(childpos))	
		
####################################################
#@brief 添加命令参数
#@param 0  listname			字典名称
#@param 1  key				配置键值，在一个策略中必须唯一
#@param 2  name				配置变量的名称
#@param 3  index				控件的排例顺序，控制显示
#@param 4  level				控件的层级，控制显示，暂支持：QTS_PARAMETER_STATUS_DISPLAY,QTS_PARAMETER_STATUS_HIDE
#@param 5  status				控件状态，控制显示，是否可点击，暂支持：QTS_DISABLE,QTS_ENABLE
#@param 6  mode				控件类型，暂支持QTS_COMPONENT_COMMONTBUTTON和QTS_COMPONENT_CONFIRMBUTTON
#@param 7  component			控件的填充内容格式(序号:文本,序号:文本,....)
#@param 8  style				控件样式
#@return 例表中所有的位置
####################################################
def AppendCommandForStrategy(*args,**kwargs):
	lists=list()
	lists.append(GetArgByIndexAndName(1,'key',0,*args,**kwargs))
	lists.append(GetArgByIndexAndName(2,'name','',*args,**kwargs))
	lists.append(GetParameterIndex(3,*args,**kwargs))
	lists.append(GetArgByIndexAndName(4,'level',1,*args,**kwargs))
	lists.append(GetArgByIndexAndName(5,'status',QTS_ENABLE,*args,**kwargs))
	lists.append(GetArgByIndexAndName(6,'mode',QTS_COMPONENT_COMMONTBUTTON,*args,**kwargs))	
	lists.append(GetArgByIndexAndName(7,'component','',*args,**kwargs))
	lists.append(GetArgByIndexAndName(8,'style','',*args,**kwargs))
	return AppendItemForMainList(GetAppPath(),GetCommandNameForStrategy(GetArgByIndexAndName(0,'listname','',*args,**kwargs)),lists)
	
####################################################
#@brief 设置策略命令参数属性
#@param listname 	 策略标的参数名称
#@param parentpos 	 参数所在位置
#@param childpos 	 子参数位置
#@param data 		 数据
####################################################		
def SetPropertyForCommand(listname,parentpos,childpos,data) :
	value = GetMainListValue(GetAppPath(),GetCommandNameForStrategy(listname),parentpos)
	if value != None :
		if childpos < len(value) :
			value[childpos] = data
		else :
			raise StandardError('pos larger len,pos={0}'.format(childpos))		
		
#######################################################################	
#######################################################################	
#远程连接的IP与端口操作函数
#######################################################################

####################################################
#@brief 设置数据服务IP地址
#@param flag 	   标示
#@param address    IP地址
####################################################	
def SetIPAddressForDS(flag,address) :
	SetIPAddress(QTS_CFG_APP_DS_IP_NAME,flag,address)

####################################################
#@brief 得到数据服务IP地址
#@param flag 	   标示
#@return   IP地址
####################################################		
def GetIPAddressForDS(flag) :
	return GetIPAddress(QTS_CFG_APP_DS_IP_NAME,flag)
	
####################################################
#@brief 设置数据服务网络端口
#@param flag 	   标示
#@param port       网络端口
####################################################		
def SetIPPortForDS(flag,port) :
	SetIPPort(QTS_CFG_APP_DS_IP_NAME,flag,port)

####################################################
#@brief 得到数据服务网络端口
#@param flag 	   标示
#@return   网络端口
####################################################		
def GetIPPortForDS(flag) :
	return GetIPPort(QTS_CFG_APP_DS_IP_NAME,flag)

####################################################
#@brief 设置交易通道服务IP地址
#@param flag 	   标示
#@param address    IP地址
####################################################		
def SetIPAddressForGW(flag,address) :
	SetIPAddress(QTS_CFG_APP_GW_IP_NAME,flag,address)

####################################################
#@brief 得到交易通道服务IP地址
#@param flag 	   标示
#@return   IP地址
####################################################		
def GetIPAddressForGW(flag) :
	return GetIPAddress(QTS_CFG_APP_GW_IP_NAME,flag)
	
####################################################
#@brief 设置交易通道服务端口
#@param flag 	   标示
#@param port       网络端口
####################################################		
def SetIPPortForGW(flag,port) :
	SetIPPort(QTS_CFG_APP_GW_IP_NAME,flag,port)

####################################################
#@brief 得到交易通道服务端口
#@param flag 	   标示
#@return    网络端口
####################################################	
def GetIPPortForGW(flag) :
	return GetIPPort(QTS_CFG_APP_GW_IP_NAME,flag)
	
####################################################
#@brief 设置策略服务IP地址
#@param flag 	   标示
#@param address    IP地址
####################################################	
def SetIPAddressForSS(flag,address) :
	SetIPAddress(QTS_CFG_APP_SS_IP_NAME,flag,address)

####################################################
#@brief 得到策略服务IP地址
#@param flag 	   标示
#@return   IP地址
####################################################	
def GetIPAddressForSS(flag) :
	return GetIPAddress(QTS_CFG_APP_SS_IP_NAME,flag)
	
####################################################
#@brief 设置策略服务端口
#@param flag 	   标示
#@param port       网络端口
####################################################	
def SetIPPortForSS(flag,port) :
	SetIPPort(QTS_CFG_APP_SS_IP_NAME,flag,port)

####################################################
#@brief 得到策略服务端口
#@param flag 	   标示
#@return    网络端口
####################################################	
def GetIPPortForSS(flag) :
	return GetIPPort(QTS_CFG_APP_SS_IP_NAME,flag)

####################################################
#@brief 设置终端IP地址
#@param flag 	   标示
#@param address    IP地址
####################################################	
def SetIPAddressForGUI(flag,address) :
	SetIPAddress(QTS_CFG_APP_GUI_IP_NAME,flag,address)

####################################################
#@brief 得到终端IP地址
#@param flag 	   标示
#@return   IP地址
####################################################	
def GetIPAddressForGUI(flag) :
	return GetIPAddress(QTS_CFG_APP_GUI_IP_NAME,flag)
	
####################################################
#@brief 设置终端端口
#@param flag 	   标示
#@param port       网络端口
####################################################		
def SetIPPortForGUI(flag,port) :
	SetIPPort(QTS_CFG_APP_GUI_IP_NAME,flag,port)

####################################################
#@brief 得到终端端口
#@param flag 	   标示
#@return    网络端口
####################################################		
def GetIPPortForGUI(flag) :
	return GetIPPort(QTS_CFG_APP_GUI_IP_NAME,flag)	
	
#######################################################################	
#######################################################################	
#错误码合成函数
#######################################################################	

####################################################
#@brief 产生业务错误码
#@param error 	错误码种子
#@return    错误码
####################################################
def GetBZErrorCode(error) :
	return -5000 - error;
	
####################################################
#@brief 产生风控错误码
#@param error 	错误码种子
#@return    错误码
####################################################	
def GetRiskErrorCode(error) :
	return -100000 - error;
	
####################################################
#@brief 产生系统错误码
#@param error 	错误码种子
#@return    错误码
####################################################	
def GetSysErrorCode(error) :
	return -1 - error;
