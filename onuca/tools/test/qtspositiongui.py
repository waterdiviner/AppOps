#coding=utf-8
from Tkinter import *
import ttk

############################################################
class QtsPositionDlg(Toplevel) :
    def __init__(self,master,**kw) :
        Toplevel.__init__(self,master,**kw)
        self.CreateWidgets()

    def CreateWidgets(self) :
        l = Label(self,text='this is a simple').pack()
