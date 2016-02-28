#coding=utf-8
from qtsxmltest import *

#########################################################################
(qts_secuinfo_s,
 qts_secuinfo_d,
 qts_trade_acc,
 qts_user_acc,
 qts_ex_acc,
 qts_trade_pos,
 qts_ex_pos,
 qts_data_market,
 qts_data_signal)=(0,1,2,3,4,5,6,7,8)

#########################################################################
class QtsTestXmlInput(QtsTestXml) :
	def LoadDefault(self) :
		self.ReadString('''<QTS><secuinfoes><qtsinfo_s_info/><qtsinfo_d_info/></secuinfoes>
								<accounts><qtstrade_acc/><qtsuser_acc/><qtsex_acc/></accounts>
								<positions><qtsexposition_pos/><qtstrposition_pos/></positions>
								<datas><market/></datas></QTS>''')

	def GetSecuInfoesNode(self,type) :
		child = None
		if type == qts_secuinfo_s :
			child = self.Root().find('./secuinfoes/qtsinfo_s_info')
		elif type == qts_secuinfo_d :
			child = self.Root().find('./secuinfoes/qtsinfo_d_info')
		return child
	
	def GetAccountsNode(self,type) :
		child = None
		if type == qts_trade_acc :
			child = self.Root().find('./accounts/qtstrade_acc')
		elif type == qts_user_acc :
			child = self.Root().find('./accounts/qtsuser_acc')
		elif type == qts_ex_acc :
			child = self.Root().find('./accounts/qtsex_acc')
		return child
		
	def GetPositionsNode(self,type) :
		child = None
		if type == qts_trade_pos :
			child = self.Root().find('./positions/qtsexposition_pos')
		elif type == qts_ex_pos :
			child = self.Root().find('./positions/qtstrposition_pos')
		return child
		
	def GetDatasNode(self,type) :
		child = None
		if type == qts_data_market :
			child = self.Root().find('./datas/market')
		elif type == qts_data_signal :
			child = self.Root().find('./datas/signal')
		return child

	def LoadSecuInfoes(self,type) :
		nodes = self.GetSecuInfoesNode(type)
		if nodes != None :
			childs = nodes.getchildren()
			for child in childs :
				self.index += 1
				item = QtsTestXmlItems(nodes,type,self.index)
				item.SetNode(child)
				item.LoadXml()
				self.items[self.index] = item

	def LoadPositions(self,type) :
		nodes = self.GetPositionsNode(type)
		if nodes != None :
			childs = nodes.getchildren()
			for child in childs :
				self.index += 1
				item = QtsTestXmlItems(nodes,type,self.index)
				item.SetNode(child)
				item.LoadXml()
				self.items[self.index] = item		
			
	def LoadAccounts(self,type) :
		nodes = self.GetAccountsNode(type)
		if nodes != None :
			childs = nodes.getchildren()
			for child in childs :
				self.index += 1
				item = QtsTestXmlItems(nodes,type,self.index)
				item.SetNode(child)
				item.LoadXml()
				self.items[self.index] = item	

	def LoadDatas(self,type) :
		nodes = self.GetDatasNode(type)
		if nodes != None :
			childs = nodes.getchildren()
			for child in childs :
				self.index += 1
				item = QtsTestXmlItems(nodes,type,self.index)
				item.SetNode(child)
				item.LoadXml()
				self.items[self.index] = item	

	def LoadXml(self,file) :
		self.ReadFile(file)
		self.LoadSecuInfoes(qts_secuinfo_s)
		self.LoadSecuInfoes(qts_secuinfo_d)
		self.LoadPositions(qts_trade_pos)
		self.LoadPositions(qts_ex_pos)
		self.LoadAccounts(qts_trade_acc)
		self.LoadAccounts(qts_user_acc)
		self.LoadAccounts(qts_ex_acc)
		self.LoadDatas(qts_data_market)
		
	def ToStringForSecuInfoes(self,type) :
		nodes = self.GetSecuInfoesNode(type)
		if nodes != None :
			return QTS_ET.tostring(nodes)
		return ''

	def ToStringForPositions(self,type) :
		nodes = self.GetPositionsNode(type)
		if nodes != None :
			return QTS_ET.tostring(nodes)
		return ''	
			
	def ToStringForAccounts(self,type) :
		nodes = self.GetAccountsNode(type)
		if nodes != None :
			return QTS_ET.tostring(nodes)
		return ''

	def ToStringForDatas(self,type) :
		nodes = self.GetDatasNode(type)
		if nodes != None :
			return QTS_ET.tostring(nodes)
		return ''	

	def AppendSecuInfo(self,type,**kwargs) :
		nodes = self.GetSecuInfoesNode(type)
		if nodes != None :
			return self.AppendItems(nodes,0,type,**kwargs)
		return 0

	def AppendPosition(self,type,**kwargs) :
		nodes = self.GetPositionsNode(type)
		if nodes != None :
			return self.AppendItems(nodes,0,type,**kwargs)
		return 0	
			
	def AppendAccount(self,type,**kwargs) :
		nodes = self.GetAccountsNode(type)
		if nodes != None :
			return self.AppendItems(nodes,0,type,**kwargs)
		return 0

	def AppendData(self,type,**kwargs) :
		nodes = self.GetDatasNode(type)
		if nodes != None :
			return self.AppendItems(nodes,0,type,**kwargs)
		return 0
		
#########################################################################

def TestDefaultXml() : 
	xml = QtsTestXmlInput()
	xml.LoadDefault()
	index = xml.AppendSecuInfo(qts_secuinfo_s,market=1,category=2)
	print(xml.ToString())
	xml.RemoveItem(index,'market')
	print(xml.ToString())
	xml.RemoveItems(index)
	print(xml.ToString())

def TestLoadXmlFile() :
    xml = QtsTestXmlInput()
    xml.LoadXml('e:/test/input.xml')
    print(xml.ToString())

if __name__ == '__main__' :
    TestDefaultXml()