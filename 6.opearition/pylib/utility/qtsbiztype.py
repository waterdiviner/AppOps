#coding=utf-8

###################################################################################
class QtsEnumItem(object) :
	def __init__(self,_key,_enum,_name,_display,_flag='',**kwargs) :
		self.key = _key
		self.enum = _enum
		self.name = _name
		self.display = _display
		self.flag = _flag
		self.items = dict()
		for kwarg in kwargs :
			self.items[kwarg] = kwargs[kwarg]

	@property
	def Key(self) :
		return self.key

	@property
	def Enum(self) :
		return self.enum

	@property
	def Name(self) :
		return self.name

	@property
	def Display(self) :
		return self.display

	@property
	def Flag(self) :
		return self.flag

	def Item(self,name) :
		try :
			return self.items[name]
		except Exception,e:
			return None

	def SetItem(self,**kwargs):
		for kwarg in kwargs :
			self.Insert(kwarg,kwargs[kwarg])

	def Insert(self,name,value) :
		if self.Item(name) == None :
			self.items[name] = value
		else :
			print('name={0} vlaue={1} is exist in QtsEnumItem'.format(name,value))

	def ToString(self) :
		msg = "key={0} enum={1} name={2} display={3} flag={4}".format(self.key,self.enum,self.name,self.display,self.flag)
		for key,value in self.items.items() :
			msg += ' ' + key + '=' + str(value)
		return msg

###################################################################################
class QtsEnum(object) :
	def __init__(self) :
		self.enums = dict()
		self._INVALID = self.add(-1,'INVALID','INVALID','未知')

	@property
	def INVALID(self):
		return self._INVALID

	@property
	def InvalidName(self):
		return self.get_by_key(self.INVALID).Name

	@property
	def InvalidDisplay(self):
		return self.get_by_key(self.INVALID).Display

	@property
	def InvalidFlag(self):
		return self.get_by_key(self.INVALID).Flag

	def buildkey(self,_key):
		return str(_key)

	def add(self,_key,_enum,_name,_display,_flag='',**kwargs) :
		if self.get_by_key(_key) == None :
			self.enums[self.buildkey(_key)] = QtsEnumItem(_key,_enum,_name,_display,_flag,**kwargs)
		else :
			print("key={0} enum={1} name={2} display={3} flag={4} is exist in QtsEnum".format(_key,_enum,_name,_display,_flag))
		return _key

	def get_by_key(self,_key) :
		try :
			return self.enums[self.buildkey(_key)]
		except Exception,e:
			return None

	def get_by_name(self,_name) :
		for value in self.enums.values() :
			if value.Name == _name :
				return value
		return None

	def get_by_display(self,_display) :
		for value in self.enums.values() :
			if value.Display == _display :
				return value
		return None

	def get_by_flag(self,_flag) :
		for value in self.enums.values() :
			if isinstance(value.Flag,list) :
				if _flag in value.Flag :
					return value
			else :
				if value.Flag == _flag :
					return value
		return None

	def get_by_item(self,_name,_value):
		for value in self.enums.values() :
			if isinstance(value.Item(_name),list) :
				if _value in value.Item(_name) :
					return value
			else :
				if value.Item(_name) == _value :
					return value
		return None

	def foreach_item(self,fun) :
		for value in self.enums.values() :
			if fun(value) == False :
				break;

	def ToString(self) :
		msg = ''
		for value in self.enums.values() :
			if msg == '' :
				msg = value.ToString() + '\r\n'
			else :
				msg += value.ToString() + '\r\n'
		return msg

	def setitem_by_key(self,_key,**kwargs):
		obj = self.get_by_key(_key)
		if obj != None :
			obj.SetItem(**kwargs)
			return True
		return False

#######################################################################################################################################
def GetPyTradeDate(timestamp) :
	return ((timestamp >> 32) & 0x00000000FFFFFFFF)

def GetPyTradeTime(timestamp) :
	return (timestamp & 0x00000000FFFFFFFF)

def CreatePyTradeTime(date,time) :
	return (((date << 32) & 0xFFFFFFFF00000000) | (time & 0x00000000FFFFFFFF))

#######################################################################################################################################
def GetMarketFromCode(code) :
	return ((code >> 48) & 0x000000000000FFFF)

def GetCategoryFromCode(code) :
	return ((code >> 32) & 0x000000000000FFFF)

def GetSecuCodeFromCode(code) :
	return (code & 0x00000000FFFFFFFF)

def GetSubCategoryFromCode(code) :
	return ((GetSecuCodeFromCode(code) >> 24) & 0x000000FF)

def GetSubCategoryFromSecuCode(secucode) :
	return ((secucode >> 24) & 0x000000FF)

def GetSubCodeFromSecuCode(secucode) :
	return (secucode& 0x00FFFFFF)

def GetRealPrice(price) :
	return float(float(price) / float(10000))

def GetSystemPrice(price) :
	return long((price + 0.00005) * 10000)

def CreateSecuCode(subcategory,num) :
	return (((subcategory << 24) & 0xFF000000) | (num & 0x00FFFFFF))

def CreateCode(market,category,secucode) :
	return (((market << 48) & 0xFFFF000000000000) | ((category << 32) & 0x0000FFFF00000000) | (secucode & 0x00000000FFFFFFFF))

#######################################################################################################################################