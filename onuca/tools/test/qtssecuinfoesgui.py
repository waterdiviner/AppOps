#coding=utf-8
from Tkinter import *
import ttk
from SimpleDialog import *
from tkCommonDialog import *

############################################################
class QtsSecuInfoesStaticDlg(Toplevel) :
    def __init__(self,master,**kw) :
        Toplevel.__init__(self,master,**kw)
        self.CreateWidgets()

    def CreateWidgets(self) :
        l = Label(self,text='this is a simple').pack()

