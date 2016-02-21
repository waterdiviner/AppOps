#coding=utf-8
from Tkinter import *
import ttk

############################################################
class QtsListItem(object) :
    def __init__(self,tree,node,index,tag = None) :
        self.tree = tree
        self.node = node
        self.tag = tag
        self.index = index

    def ListView(self) :
        return self.tree

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

    def Values(self) :
        return self.tree.item(self.node)['values']

    def SetValues(self,units) :
        self.tree.item(self.node,values = units)
		
############################################################
class QtsListView(Frame) :
    def __init__(self,master,heads) :
        Frame.__init__(self,master)
        self.master = master
        self.tree = None
        self.items = dict()
        self.index = 0
        self.CreateWidgets(heads)

    def CreateWidgets(self,heads) :
        self.tree = ttk.Treeview(self,columns=heads)
        ysb = ttk.Scrollbar(self, orient='vertical', command=self.tree.yview)
        xsb = ttk.Scrollbar(self, orient='horizontal', command=self.tree.xview)
        self.tree.configure(yscroll=ysb.set, xscroll=xsb.set)
        self.tree.grid(row=0, column=0,sticky='n')
        ysb.grid(row=0, column=1, sticky='ns')
        xsb.grid(row=1, column=0, sticky='ew')
        for head in heads :
            self.SetColumnText(head,head)

    def Tree(self) :
        return self.tree

    def Master(self) :
        return self.master

    def SetColumnProperty(self,head,**kw) :
        self.tree.column(head,**kw)

    def SetHeadProperty(self,head,**kw) :
        self.tree.heading(head,**kw)

    def SetColumnText(self,head,title) :
        self.tree.heading(head,text=title)

    def SetHeadTitle(self,title) :
        self.tree.heading('#0', text=title, anchor='w')

    def SetColumnWidth(self,head,w) :
        self.tree.column(head,width=w)

    def SetHeadWidth(self,w) :
        self.tree.column('#0', width=w)

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

    def InsertByPos(self,pos,units,tag = None) :
        self.index += 1
        item = QtsListItem(self.tree,self.tree.insert('', pos,self.index,values = units,tags=self.index),self.index,tag)
        self.items[self.index] = item
        return item

    def InsertInEnd(self,units,tag = None) :
        self.index += 1
        item = QtsListItem(self.tree,self.tree.insert('', 'end',self.index,values = units,tags=self.index),self.index,tag)
        self.items[self.index] = item
        return item

    def InsertFull(self,units,tag = None) :
        head = None
        values = list()
        for value in units :
            if head == None :
                head = value
            else :
                values.append(value)
        self.InsertInEnd(values,tag).SetText(head)

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

    def Clear(self) :
        for key in self.items.keys() :
            self.items[key].Remove()
        self.items.clear()

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
if __name__ == '__main__' :		
    root=Tk()
    treeview=QtsListView(root,('col1','col2','col3'))
    treeview.SetHeadTitle('col0')
    treeview.InsertInEnd(('a','b','c')).SetText('d')
    root.mainloop()