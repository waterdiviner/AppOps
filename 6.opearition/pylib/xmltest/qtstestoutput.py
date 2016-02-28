#coding=utf-8
from qtsxmltest import *

#########################################################################
class QtsTestXmlOutput(object) : 
	def Compare(self,soure,target) :
		source_xml = QtsTestXml()
		target_xml = QtsTestXml()
		source_xml.ReadFile(soure)
		target_xml.ReadFile(target)
		return self.CompareXml(source_xml,target_xml) and self.CompareXml(target_xml,source_xml)
		
	def CompareXml(self,source_xml,target_xml) :
		source_ssnode = source_xml.Root().find('./SS')
		target_ssnode = target_xml.Root().find('./SS')
		if  source_ssnode == None and target_ssnode != None :
			return False
		elif source_ssnode != None and target_ssnode == None:
			return False
		source_gwnode = source_xml.Root().find('./GW')
		target_gwnode = target_xml.Root().find('./GW')
		if  source_gwnode == None and target_gwnode != None :
			return False
		elif source_gwnode != None and target_gwnode == None:
			return False
		return self.CompareSS(source_ssnode,target_ssnode) and self.CompareGW(source_gwnode,target_gwnode)
		
	def CompareSS(self,source_node,target_node) :
		if source_node == None and target_node == None :
			return True
		if len(source_node.getchildren()) != len(target_node.getchildren()) :
			return False
		breturn = True
		childs = source_node.getchildren()
		for child in childs :
			breturn = breturn and self.CompareIndex(child,target_node.find('./{}'.format(child.tag)))
			if not breturn :
				break
		return breturn
		
	def CompareGW(self,source_node,target_node) :
		if source_node == None and target_node == None :
			return True
		if len(source_node.getchildren()) != len(target_node.getchildren()) :
			return False
		breturn = True
		childs = source_node.getchildren()
		for child in childs :
			breturn = breturn and self.CompareIndex(child,target_node.find('./{}'.format(child.tag)))
			if not breturn :
				break
		return breturn		
		
	def CompareIndex(self,source_node,target_node) :
		if target_node == None :
			return False
		if len(source_node.getchildren()) != len(target_node.getchildren()) :
			return False
		breturn = True
		childs = source_node.getchildren()
		for child in childs :
			if child.tag == 'datas' :
				breturn = breturn and self.CompareDatas(child,target_node.find('./{}'.format(child.tag)))
			elif child.tag == 'records' :
				breturn = breturn and self.CompareDatas(child,target_node.find('./{}'.format(child.tag)))
			elif child.tag == 'positions' :
				breturn = breturn and self.CompareDatas(child,target_node.find('./{}'.format(child.tag)))
			elif child.tag == 'workings' :
				breturn = breturn and self.CompareDatas(child,target_node.find('./{}'.format(child.tag)))
			elif child.tag == 'books' :
				breturn = breturn and self.CompareDatas(child,target_node.find('./{}'.format(child.tag)))
			elif child.tag == 'accounts' :
				breturn = breturn and self.CompareAccount(child,target_node.find('./{}'.format(child.tag)))				
			if not breturn :
				break
		return breturn
		
	def CompareDatas(self,source_node,target_node) :
		if target_node == None :
			return False
		if len(source_node.getchildren()) != len(target_node.getchildren()) :
			return False
		breturn = True
		childs = source_node.getchildren()
		for child in childs :
			breturn = breturn and self.CompareData(child,target_node.find('./{}'.format(child.tag)))
			if not breturn :
				break
		return breturn
		
	def CompareArrtib(self,source_dict,target_dict) : 
		breturn = True
		try:
			for key in source_dict.keys() :
				if source_dict[key] != target_dict[key] :
					breturn = False
					break
			if not breturn :
				return breturn
			for key in target_dict.keys() :
				if source_dict[key] != target_dict[key] :
					breturn = False
					break
		except Exception,e:
			breturn = False
		return breturn

	def GetItemNode(self,item_node,target_node) :
		node = None
		childs = target_node.getchildren()
		for child in childs :
			if self.CompareArrtib(item_node.attrib,child.attrib) :
				node = child
				break
		return node
		
	def CompareData(self,source_node,target_node) :
		if target_node == None :
			return False
		if len(source_node.getchildren()) != len(target_node.getchildren()) :
			return False
		breturn = True
		childs = source_node.getchildren()
		for child in childs :
			breturn = breturn and self.CompareItems(child,self.GetItemNode(child,target_node))
			if not breturn :
				break
		return breturn
	
	def CompareAccount(self,source_node,target_node) : 
		if target_node == None :
			return False
		if len(source_node.getchildren()) != len(target_node.getchildren()) :
			return False
		breturn = True
		childs = source_node.getchildren()
		for child in childs :
			breturn = breturn and self.CompareItems(child,self.GetItemNode(child,target_node))
			if not breturn :
				break
		return breturn
	
	def CompareItems(self,source_node,target_node) : 
		if target_node == None :
			return False
		if len(source_node.getchildren()) != len(target_node.getchildren()) :
			return False
		breturn = True
		childs = source_node.getchildren()
		for child in childs :
			temp = target_node.find('./{}'.format(child.tag))
			if temp == None :
				breturn = False
				break
			else :
				if temp.text != child.text :
					breturn = False
					break			
		return breturn
	
#########################################################################

if __name__ == '__main__' :
    test = QtsTestXmlOutput()
    print('result:{}'.format(test.Compare('e:/test/output1.xml','e:/test/output2.xml')))
	