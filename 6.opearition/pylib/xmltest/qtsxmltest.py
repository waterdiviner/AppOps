#coding=utf-8
from xml.etree import ElementTree as QTS_ET

#########################################################################
class QtsTestXmlItem(object) : 
	def __init__(self,parent) :
		self.parent = parent
		self.node = None
		
	def Clear(self) :
		if self.node != None :
			self.node.clear()
		
	def SetNode(self,node):
		self.node = node
		
	def CreateNode(self,tag) :
		self.node = QTS_ET.Element(tag)
		self.parent.append(self.node)
		
	def RemoveNode(self) :
		self.parent.remove(self.node)
		
	def SetText(self,text) :
		self.node.text = '{}'.format(text)
		
	def Parent(self) :
		return self.parent
		
	def Node(self) :
		return self.node
		
	def Tag(self) :
		return self.node.tag
		
	def Text(self) :
		return self.node.text

	def ToString(self) :
		return QTS_ET.tostring(self.node)		
		
#########################################################################
class QtsTestXmlItems(object) :
    def __init__(self,parent,type,index) :
        self.parent = parent
        self.type = type
        self.index = index
        self.node = None
        self.items = dict()

    def Clear(self) :
        if self.node != None :
            self.node.clear()
        self.items.clear()

    def SetNode(self,node) :
        self.node = node

    def CreateNode(self,tag='item') :
        self.node = QTS_ET.Element(tag)
        self.parent.append(self.node)

    def RemoveNode(self) :
        self.parent.remove(self.node)

    def RemoveItem(self,tag) :
        item = self.GetChild(tag)
        if item != None :
            item.RemoveNode()
            self.items.pop(tag)

    def Parent(self) :
        return self.parent

    def Node(self) :
        return self.node

    def Tag(self) :
        return self.node.tag

    def Type(self) :
        return self.type

    def Index(self) :
        return self.index

    def Items(self) :
        return self.items

    def GetChild(self,tag) :
        item = None
        try:
            item =self.items[tag]
        except Exception,e:
            item = None
        return item

    def AddChild(self,tag,text) :
        item = QtsTestXmlItem(self.node)
        item.CreateNode(tag)
        item.SetText(text)
        self.items[tag] = item

    def UpdateChild(self,tag,text) :
        item = self.GetChild(tag)
        if item != None :
            item.SetText(text)
        else :
            self.AddChild(tag,text)

    def AddChilds(self,**kwargs) :
        for kwarg in kwargs :
            self.AddChild(kwarg,kwargs[kwarg])

    def UpdateChilds(self,**kwargs) :
        for kwarg in kwargs :
            self.UpdateChild(kwarg,kwargs[kwarg])

    def LoadXml(self) :
        childs = self.node.getchildren()
        for child in childs :
            item = QtsTestXmlItem(self.node)
            item.SetNode(child)
            self.items[child.tag] = item

    def Values(self,heads) :
        values = list()
        for i in range(0,len(heads)) :
            values.append(0)
        index = 0
        for key in self.items.keys() :
            index = 0
            for head in heads :
                if head == key :
                    values[index] = self.items[key].Text()
                index += 1
        return values

    def ToString(self) :
        return QTS_ET.tostring(self.node)
		
#########################################################################
class QtsTestXml(object) :
    def __init__(self) :
        self.tree = None
        self.root = None
        self.file = None
        self.index = 0
        self.items = dict()

    def Items(self) :
        return self.items

    def Tree(self) :
        return self.tree

    def Root(self) :
        return self.root

    def File(self) :
        return self.file

    def Clear(self) :
        if self.root != None :
            self.root.clear()
        self.items.clear()

    def ReadFile(self,file) :
        self.file = file
        self.tree = QTS_ET.parse(file)
        self.root = self.tree.getroot()

    def ReadString(self,text) :
        self.tree = QTS_ET.ElementTree()
        self.root = QTS_ET.fromstring(text)
        self.tree._setroot(self.root)

    def Write(self) :
        self.tree.write(self.file)

    def WriteAs(self,file) :
        self.file = file
        self.tree.write(file)

    def ToString(self) :
        return QTS_ET.tostring(self.root)

    def GetChild(self,index) :
        item = None
        try:
            item =self.items[index]
        except Exception,e:
            item = None
        return item

    def RemoveItems(self,index) :
        item = self.GetChild(index)
        if item != None :
            item.RemoveNode()
            self.items.pop(index)

    def RemoveItem(self,index,tag) :
        item = self.GetChild(index)
        if item != None :
            item.RemoveItem(tag)

    def AppendItem(self,parent,index,type,tag,text) :
        itemindex = index
        item = self.GetChild(index)
        if item == None :
            self.index += 1
            item = QtsTestXmlItems(parent,self.index,type)
            item.CreateNode()
            item.AddChild(tag,text)
            self.items[self.index] = item
            itemindex = self.index
        else :
            item.UpdateChild(tag,text)
        return itemindex

    def AppendItems(self,parent,index,type,**kwargs) :
        itemindex = index
        for kwarg in kwargs :
            itemindex = self.AppendItem(parent,itemindex,type,kwarg,kwargs[kwarg])
        return itemindex

    def GetItemsByType(self,type) :
        items = list()
        for key in self.items.keys() :
            if self.items[key].Type() == type :
                items.append(self.items[key])
        return items

#########################################################################		