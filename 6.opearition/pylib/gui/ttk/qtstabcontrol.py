#coding=utf-8
from Tkinter import *
import ttk

############################################################
class QtsTabPage(object) :
    def __init__(self,parent,page,control,title,tag = None) :
        self.parent = parent
        self.page = page
        self.title = title
        self.tag = tag
        self.control = control

    def Control(self) :
        return self.control

    def Tag(self) :
        return self.tag

    def TabControl(self) :
        return self.parent

    def Page(self) :
        return self.page

    def Title(self) :
        return self.title

    def Remove(self) :
        self.parent.forget(self.Page())

    def Hide(self) :
        self.parent.hide(self.Page())

    def Select(self) :
        self.parent.select(self.Page())

    def Options(self,option=None,**kw) :
        self.parent.tab(self.Page(),option,**kw)

    def Index(self) :
        return self.parent.index(self.Page())
		
############################################################
class QtsTabControl(Frame) :
    def __init__(self,master,h = 200,w =300) :
        Frame.__init__(self,master)
        self.master = master
        self.tb = None
        self.index = 0
        self.pages = dict()
        self.CreateWidgets(h,w)
		
    def CreateWidgets(self,h,w) :
        self.tb=ttk.Notebook(self,height=h,width=w)
        self.tb.grid(row=0,column=0)
		
    def Pages(self) :
        return self.pages

    def Add(self,page,title,tag = None) :
        newpage = None
        self.tb.add(page,text=title)
        for tab in self.tb.tabs() :
            if self.GetPageById(tab) == None :
                newpage = QtsTabPage(self.tb,tab,page,title,tag)
                self.pages[tab] = newpage
                break
        return newpage

    def Insert(self,pos,page,title,tag = None) :
        newpage = None
        self.tb.insert(pos,page,text=title)
        for tab in self.tb.tabs() :
            if self.GetPageById(tab) == None :
                newpage = QtsTabPage(self.tb,tab,page,title,tag)
                self.pages[tab] = newpage
                break
        return newpage

    def GetPageById(self,id) :
        page = None
        try:
            page = self.pages[id]
        except Exception,e:
            page = None
        return page

    def GetPageByTitle(self,title) :
        page = None
        for key in self.pages.keys() :
            if self.pages[key].Title() == title :
                page = self.pages[key]
                break
        return page

    def GetPageByIndex(self,index) :
        page = None
        for key in self.pages.keys() :
            if self.pages[key].Index() == index :
                page = self.pages[key]
                break
        return page

    def Selected(self) :
        return self.GetPageById(self.tb.select())

    def AddChangedEvent(self,fun) :
        self.tb.bind('<<NotebookTabChanged>>',fun)

############################################################
tabcontrol = None
def OnSelect(event) :
    print('hit me')
    item = tabcontrol.Selected()
    print(item.Title())

if __name__ == '__main__' :		
    root=Tk()
    tabcontrol=QtsTabControl(root)
    lable1=Label(text='欢迎登陆！',fg='black')
    page = tabcontrol.Add(lable1,'首页')
    lable2=Label(text='欢迎登陆2！',fg='black')
    page = tabcontrol.Add(lable2,'首页2')
    tabcontrol.AddChangedEvent(OnSelect)
    root.mainloop()