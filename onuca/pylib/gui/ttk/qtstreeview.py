#coding=utf-8
from Tkinter import *
import ttk

############################################################
class QtsTreeNode(object) :
    def __init__(self,tree,parent,node,index,tag = None) :
        self.tree = tree
        self.parent = parent
        self.node = node
        self.tag = tag
        self.index = index

    def TreeView(self) :
        return self.tree

    def Parent(self) :
        return self.parent

    def Node(self) :
        return self.node

    def Tag(self) :
        return self.tag

    def Id(self) :
        return self.tree.item(self.node)['tags'][0]

    def Index(self) :
        return self.index

    def Remove(self) :
        self.tree.delete(self.node)

    def Focus(self) :
        self.tree.focus(self.node)

    def Select(self) :
        self.tree.selection_set(self.node)

    def UnSelect(self) :
        self.tree.selection_remove(self.node)

    def Index(self) :
        return self.tree.index(self.node)

    def Open(self) :
        self.tree.item(self.node,open = True)

    def Close(self) :
        self.tree.item(self.node,open = False)

    def Move(self,parent,index) :
        self.tree.move(self.node,parent.Node(),index)

    def Text(self) :
        return self.tree.item(self.node)['text']

    def SetText(self,title) :
        self.tree.item(self.node,text = title)
		
############################################################
class QtsTreeView(Frame) :
    def __init__(self,master,title) :
        Frame.__init__(self,master)
        self.master = master
        self.tree = None
        self.index = 0
        self.items = dict()
        self.CreateWidgets(title)

    def CreateWidgets(self,title) :
        self.tree = ttk.Treeview(self)
        ysb = ttk.Scrollbar(self, orient='vertical', command=self.tree.yview)
        xsb = ttk.Scrollbar(self, orient='horizontal', command=self.tree.xview)
        self.tree.configure(yscroll=ysb.set, xscroll=xsb.set)
        self.SetHeadTitle(title)
        self.tree.grid(row=0, column=0,sticky='n')
        ysb.grid(row=0, column=1, sticky='ns')
        xsb.grid(row=1, column=0, sticky='ew')

    def Tree(self) :
        return self.tree

    def Master(self) :
        return self.master

    def Items(self) :
        return self.items

    def SetHeadTitle(self,title) :
        self.tree.heading('#0', text=title, anchor='w')

    def AddSelectEvent(self,fun) :
        self.tree.bind('<<TreeviewSelect>>',fun)

    def AddOpenEvent(self,fun) :
        self.tree.bind('<<TreeviewOpen>>',fun)

    def AddCloseEvent(self,fun) :
        self.tree.bind('<<TreeviewClose>>',fun)

    def AddDBClickEvent(self,type,fun) :
        self.tree.bind('<Double-1>',fun)

    def AddClickEvent(self,type,fun) :
        self.tree.bind('<Button-1>',fun)

    def InsertRoot(self,title,tag = None) :
        self.index += 1
        item = QtsTreeNode(self.tree,None,self.tree.insert('', 'end',self.index,text=title,tags=self.index),self.index,tag)
        self.items[self.index] = item
        return item

    def InsertItemByPos(self,parent,pos,title,tag = None) :
        self.index += 1
        item = QtsTreeNode(self.tree,parent.Node(),self.tree.insert(parent.Node(),pos,self.index,text=title,tags=self.index),self.index,tag)
        self.items[self.index] = item
        return item

    def InsertItemInEnd(self,parent,title,tag = None) :
        self.index += 1
        item = QtsTreeNode(self.tree,parent.Node(),self.tree.insert(parent.Node(),'end',self.index,text=title,tags=self.index),self.index,tag)
        self.items[self.index] = item
        return item
		
    def Id(self,node) :
        return self.tree.item(node)['tags'][0]

    def GetItem(self,id) :
        node = None
        try:
            node =self.items[id]
        except Exception,e:
            node = None
        return node
		
    def Remove(self,id) :
        item = self.GetItem(id)
        if item != None :
            item.Remove()
            self.items.pop(id)
        return item

    def Selected(self) :
        id = self.Id(self.tree.selection())
        return self.GetItem(id)

    def Focus(self,id) :
        item = self.GetItem(id)
        if item != None :
            item.Focus()

    def Select(self,id) :
        item = self.GetItem(id)
        if item != None :
            item.Select()

    def UnSelect(self,id) :
        item = self.GetItem(id)
        if item != None :
            item.UnSelect()
		
############################################################
treeview = None
def OnSelect(event) :
    print(treeview.Selected())

if __name__ == '__main__' :		
    root=Tk()
    treeview=QtsTreeView(root,'test')
    treeview.InsertRoot('QTS')
    treeview.AddSelectEvent(OnSelect)
    root.mainloop()