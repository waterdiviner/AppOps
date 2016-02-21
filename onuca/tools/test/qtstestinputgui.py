#coding=utf-8
from Tkinter import *
from FileDialog import *
from tkMessageBox import *
import ttk
import sys

sys.path.append('../../pylib/xmltest')
sys.path.append('../../pylib/gui')

from qtstestinput import QtsTestXmlInput
from qtstreeview import QtsTreeView,QtsTreeNode
from qtslistview import QtsListView,QtsListItem
from qtstabcontrol import QtsTabControl,QtsTabPage
from qtssecuinfoesgui import QtsSecuInfoesStaticDlg
#########################################################################
(qts_secuinfo_s,qts_secuinfo_d,qts_trade_acc,qts_user_acc,qts_ex_acc,qts_trade_pos,qts_ex_pos,qts_data_market,qts_data_signal)=(0,1,2,3,4,5,6,7,8)

#################################################################################################
class QtsTestInputMainWindow(object) :
    def __init__(self) :
        self.master = Tk()
        self.xml = QtsTestXmlInput()
        self.CreateMenu()
        self.CreateWidgets()
        self.CreatePages()
        self.FillNodes()

    def CreateWidgets(self) :
        self.panel = Frame(self.master)
        self.panel.grid(row=0,column=0)
        self.tree = QtsTreeView(self.panel,'TestInput')
        self.tree.AddSelectEvent(self.OnTreeSelect)
        self.tree.grid(row=0,column=0)
        self.tabctl = QtsTabControl(self.panel,400,1000)
        self.tabctl.grid(row=0,column=1)

    def CreatePages(self) :
        self.CreatePageForSecuInfoes_s()
        self.CreatePageForSecuInfoes_d()
        self.CreatePageForTradeAcc()
        self.CreatePageForUserAcc()
        self.CreatePageForExAcc()
        self.CreatePageForTradePos()
        self.CreatePageForExPos()
        self.CreatePageForMarket()

    def CreateMenu(self) :
        self.mainmenu = Menu(self.master)
        filemenu = Menu(self.mainmenu,tearoff = 0)
        self.mainmenu.add_cascade(label='File',menu=filemenu)
        filemenu.add_command(label='Open',command=self.OnOpen)
        filemenu.add_command(label='Save',command=self.OnSave)
        filemenu.add_command(label='SaveAs',command=self.OnSaveAs)
        toolsmenu = Menu(self.mainmenu,tearoff = 0)
        self.mainmenu.add_cascade(label='Tools',menu=toolsmenu)
        toolsmenu.add_command(label='Add',command=self.OnAddListItem)
        toolsmenu.add_command(label='Modify',command=self.OnModifyItem)
        toolsmenu.add_command(label='Delete',command=self.OnDelListitem)
        self.master['menu'] = self.mainmenu

    def CreatePageForSecuInfoes_s(self) :
        self.secuinfoes_s_view = QtsListView(self.panel,('category','secucode','ordercode','marketname','categoryname','secuname','minorderqty','maxorderqty','pricetick','tradetn','posmode','multipler','margin'))
        self.secuinfoes_s_view.SetHeadTitle('market')
        self.secuinfoes_s_view.AddSelectEvent(self.OnListSelect)
        self.secuinfoes_s_page = self.tabctl.Add(self.secuinfoes_s_view,'secuinfoes_s')
        self.secuinfoes_s_view.SetHeadWidth(50)
        self.secuinfoes_s_view.SetColumnWidth(0,60)
        self.secuinfoes_s_view.SetColumnWidth(1,60)
        self.secuinfoes_s_view.SetColumnWidth(2,60)
        self.secuinfoes_s_view.SetColumnWidth(3,80)
        self.secuinfoes_s_view.SetColumnWidth(4,80)
        self.secuinfoes_s_view.SetColumnWidth(5,80)
        self.secuinfoes_s_view.SetColumnWidth(6,70)
        self.secuinfoes_s_view.SetColumnWidth(7,70)
        self.secuinfoes_s_view.SetColumnWidth(8,60)
        self.secuinfoes_s_view.SetColumnWidth(9,60)
        self.secuinfoes_s_view.SetColumnWidth(10,60)
        self.secuinfoes_s_view.SetColumnWidth(11,60)
        self.secuinfoes_s_view.SetColumnWidth(12,60)

    def CreatePageForSecuInfoes_d(self) :
        self.secuinfoes_d_view = QtsListView(self.panel,('category','secucode','lastprice','lolimitedprice','uplimitedprice','suspension','tradingfee'))
        self.secuinfoes_d_view.SetHeadTitle('market')
        self.secuinfoes_d_view.AddSelectEvent(self.OnListSelect)
        self.secuinfoes_d_page = self.tabctl.Add(self.secuinfoes_d_view,'secuinfoes_d')
        self.secuinfoes_d_view.SetHeadWidth(50)
        self.secuinfoes_d_view.SetColumnWidth(0,60)
        self.secuinfoes_d_view.SetColumnWidth(1,60)
        self.secuinfoes_d_view.SetColumnWidth(2,60)
        self.secuinfoes_d_view.SetColumnWidth(3,60)
        self.secuinfoes_d_view.SetColumnWidth(4,60)
        self.secuinfoes_d_view.SetColumnWidth(5,60)
        self.secuinfoes_d_view.SetColumnWidth(6,200)

    def CreatePageForTradeAcc(self) :
        self.tradeacc_view = QtsListView(self.panel,('category','account','totalamoumt','avlamount','freezeamount','currency','qtsdate'))
        self.tradeacc_view.SetHeadTitle('market')
        self.tradeacc_view.AddSelectEvent(self.OnListSelect)
        self.tradeacc_page = self.tabctl.Add(self.tradeacc_view,'tradeacc')
        self.tradeacc_view.SetHeadWidth(50)
        self.tradeacc_view.SetColumnWidth(0,60)
        self.tradeacc_view.SetColumnWidth(1,60)
        self.tradeacc_view.SetColumnWidth(2,60)
        self.tradeacc_view.SetColumnWidth(3,60)
        self.tradeacc_view.SetColumnWidth(4,60)
        self.tradeacc_view.SetColumnWidth(5,60)
        self.tradeacc_view.SetColumnWidth(6,200)

    def CreatePageForUserAcc(self) :
        self.useracc_view = QtsListView(self.panel,('subaccount','viraccount'))
        self.useracc_view.SetHeadTitle('qtsuser')
        self.useracc_view.AddSelectEvent(self.OnListSelect)
        self.useracc_page = self.tabctl.Add(self.useracc_view,'useracc')
        self.useracc_view.SetHeadWidth(50)
        self.useracc_view.SetColumnWidth(0,60)
        self.useracc_view.SetColumnWidth(1,60)

    def CreatePageForExAcc(self) :
        self.exacc_view = QtsListView(self.panel,('category','viraccount','relaccount','sharetag','totalamoumt','avlamount','freezeamount'))
        self.exacc_view.SetHeadTitle('market')
        self.exacc_view.AddSelectEvent(self.OnListSelect)
        self.exacc_page = self.tabctl.Add(self.exacc_view,'exacc')
        self.exacc_view.SetHeadWidth(50)
        self.exacc_view.SetColumnWidth(0,60)
        self.exacc_view.SetColumnWidth(1,60)
        self.exacc_view.SetColumnWidth(2,60)
        self.exacc_view.SetColumnWidth(3,60)
        self.exacc_view.SetColumnWidth(4,60)
        self.exacc_view.SetColumnWidth(5,60)
        self.exacc_view.SetColumnWidth(6,200)

    def CreatePageForTradePos(self) :
        self.tradepos_view = QtsListView(self.panel,('market','category','code','qtstype','qtslevel','totalvol','avlvol','workingvol','totalcost','qtsdate','avlcredempvol','todayvol'))
        self.tradepos_view.SetHeadTitle('account')
        self.tradepos_view.AddSelectEvent(self.OnListSelect)
        self.tradepos_page = self.tabctl.Add(self.tradepos_view,'tradepos')
        self.tradepos_view.SetHeadWidth(50)
        self.tradepos_view.SetColumnWidth(0,60)
        self.tradepos_view.SetColumnWidth(1,60)
        self.tradepos_view.SetColumnWidth(2,60)
        self.tradepos_view.SetColumnWidth(3,60)
        self.tradepos_view.SetColumnWidth(4,60)
        self.tradepos_view.SetColumnWidth(5,60)
        self.tradepos_view.SetColumnWidth(6,60)
        self.tradepos_view.SetColumnWidth(7,60)
        self.tradepos_view.SetColumnWidth(8,60)
        self.tradepos_view.SetColumnWidth(9,60)
        self.tradepos_view.SetColumnWidth(10,60)
        self.tradepos_view.SetColumnWidth(11,60)

    def CreatePageForExPos(self) :
        self.expos_view = QtsListView(self.panel,('market','category','code','qtstype','qtslevel','totalvol','avlvol','workingvol','totalcost','qtsdate','avlcredempvol','todayvol'))
        self.expos_view.SetHeadTitle('account')
        self.expos_view.AddSelectEvent(self.OnListSelect)
        self.expos_page = self.tabctl.Add(self.expos_view,'tradepos')
        self.expos_view.SetHeadWidth(50)
        self.expos_view.SetColumnWidth(0,60)
        self.expos_view.SetColumnWidth(1,60)
        self.expos_view.SetColumnWidth(2,60)
        self.expos_view.SetColumnWidth(3,60)
        self.expos_view.SetColumnWidth(4,60)
        self.expos_view.SetColumnWidth(5,60)
        self.expos_view.SetColumnWidth(6,60)
        self.expos_view.SetColumnWidth(7,60)
        self.expos_view.SetColumnWidth(8,60)
        self.expos_view.SetColumnWidth(9,60)
        self.expos_view.SetColumnWidth(10,60)
        self.expos_view.SetColumnWidth(11,60)

    def CreatePageForMarket(self) :
        self.market_view = QtsListView(self.panel,('market','category','secucode','level','askprice0','askprice1','askprice2',
                                                   'askprice3','askprice4','askvol0','askvol1','askvol2','askvol3','askvol4',
                                                   'asklevel','bidprice0','bidprice1','bidprice2','bidprice3','bidprice4','bidvol0',
                                                   'bidvol1','bidvol2','bidvol3','bidvol4','bidlevel','lolimitprice','uplimitprice',
                                                   'lastprice','openprice','presettlementprice','precloseprice','marketprice','marketvol',
                                                   'totalvol','totalamount','timestamp','suspension'))
        self.market_view.SetHeadTitle('index')
        self.market_view.AddSelectEvent(self.OnListSelect)
        self.market_page = self.tabctl.Add(self.market_view,'market')
        self.market_view.SetHeadWidth(50)
        self.market_view.SetColumnWidth(0,60)
        self.market_view.SetColumnWidth(1,60)
        self.market_view.SetColumnWidth(2,60)
        self.market_view.SetColumnWidth(3,60)
        self.market_view.SetColumnWidth(4,60)
        self.market_view.SetColumnWidth(5,60)
        self.market_view.SetColumnWidth(6,60)
        self.market_view.SetColumnWidth(7,60)
        self.market_view.SetColumnWidth(8,60)
        self.market_view.SetColumnWidth(9,60)
        self.market_view.SetColumnWidth(10,60)
        self.market_view.SetColumnWidth(11,60)
        self.market_view.SetColumnWidth(12,60)
        self.market_view.SetColumnWidth(13,60)
        self.market_view.SetColumnWidth(14,60)
        self.market_view.SetColumnWidth(15,60)
        self.market_view.SetColumnWidth(16,60)
        self.market_view.SetColumnWidth(17,60)
        self.market_view.SetColumnWidth(18,60)
        self.market_view.SetColumnWidth(19,60)
        self.market_view.SetColumnWidth(20,60)
        self.market_view.SetColumnWidth(21,60)
        self.market_view.SetColumnWidth(22,60)
        self.market_view.SetColumnWidth(23,60)
        self.market_view.SetColumnWidth(24,60)
        self.market_view.SetColumnWidth(25,60)
        self.market_view.SetColumnWidth(26,60)
        self.market_view.SetColumnWidth(27,60)
        self.market_view.SetColumnWidth(28,60)
        self.market_view.SetColumnWidth(29,60)
        self.market_view.SetColumnWidth(30,60)
        self.market_view.SetColumnWidth(31,60)
        self.market_view.SetColumnWidth(32,60)
        self.market_view.SetColumnWidth(33,60)
        self.market_view.SetColumnWidth(34,60)
        self.market_view.SetColumnWidth(35,60)
        self.market_view.SetColumnWidth(36,60)
        self.market_view.SetColumnWidth(37,60)

    def FillNodes(self) :
        self.root = self.tree.InsertRoot('QTS')
        self.root.Open()
        secuinfoes = self.tree.InsertItemInEnd(self.root,'secuinfoes')
        self.secuinfoes_s = self.tree.InsertItemInEnd(secuinfoes,'qtsinfo_s_info',self.secuinfoes_s_page)
        self.secuinfoes_d = self.tree.InsertItemInEnd(secuinfoes,'qtsinfo_d_info',self.secuinfoes_d_page)
        positions = self.tree.InsertItemInEnd(self.root,'positions')
        self.exposition = self.tree.InsertItemInEnd(positions,'qtsexposition_pos',self.tradepos_page)
        self.trposition = self.tree.InsertItemInEnd(positions,'qtstrposition_pos',self.expos_page)
        accounts = self.tree.InsertItemInEnd(self.root,'accounts')
        self.tradeacc = self.tree.InsertItemInEnd(accounts,'qtstrade_acc',self.tradeacc_page)
        self.useracc = self.tree.InsertItemInEnd(accounts,'qtsuser_acc',self.useracc_page)
        self.exacc = self.tree.InsertItemInEnd(accounts,'qtsex_acc',self.exacc_page)
        datas = self.tree.InsertItemInEnd(self.root, 'datas')
        self.market = self.tree.InsertItemInEnd(datas,'market',self.market_page)

    def RunApp(self) :
        self.master.mainloop()

    def TestXml(self) :
        return self.xml

    def NewTest(self) :
        self.xml.Clear()
        self.xml.LoadDefault()

    def LoadFile(self,file) :
        self.xml.Clear()
        self.xml.LoadXml(file)
        self.LoadItems()

    def Save(self) :
        self.xml.Write()

    def SaveAs(self,file) :
        self.xml.WriteAs(file)

    def LoadItems(self) :
        self.LoadItem(qts_secuinfo_s,self.secuinfoes_s_view,('market','category','secucode','ordercode','marketname','categoryname','secuname','minorderqty','maxorderqty','pricetick','tradetn','posmode','multipler','margin'))
        self.LoadItem(qts_secuinfo_d,self.secuinfoes_d_view,('market','category','secucode','lastprice','lolimitedprice','uplimitedprice','suspension','tradingfee'))
        self.LoadItem(qts_trade_acc,self.tradeacc_view,('market','category','account','totalamoumt','avlamount','freezeamount','currency','qtsdate'))
        self.LoadItem(qts_user_acc,self.useracc_view,('qtsuser','subaccount','viraccount'))
        self.LoadItem(qts_ex_acc,self.exacc_view,('market','category','viraccount','relaccount','sharetag','totalamoumt','avlamount','freezeamount'))
        self.LoadItem(qts_trade_pos,self.tradepos_view,('account','market','category','code','qtstype','qtslevel','totalvol','avlvol','workingvol','totalcost','qtsdate','avlcredempvol','todayvol'))
        self.LoadItem(qts_ex_pos,self.expos_view,('account','market','category','code','qtstype','qtslevel','totalvol','avlvol','workingvol','totalcost','qtsdate','avlcredempvol','todayvol'))
        self.LoadItem(qts_data_market,self.market_view,('index','market','category','secucode','level','askprice0','askprice1','askprice2',
                                                   'askprice3','askprice4','askvol0','askvol1','askvol2','askvol3','askvol4',
                                                   'asklevel','bidprice0','bidprice1','bidprice2','bidprice3','bidprice4','bidvol0',
                                                   'bidvol1','bidvol2','bidvol3','bidvol4','bidlevel','lolimitprice','uplimitprice',
                                                   'lastprice','openprice','presettlementprice','precloseprice','marketprice','marketvol',
                                                   'totalvol','totalamount','timestamp','suspension'))

    def LoadItem(self,type,listview,heads) :
        items = self.xml.GetItemsByType(type)
        for item in items :
            values = item.Values(heads)
            listview.InsertFull(values,item)

    def OnTreeSelect(self,event) :
        item = self.tree.Selected()
        if item == None :
            return
        if item.Tag() != None :
            item.Tag().Select()

    def OnListSelect(self,event) :
        item = self.tabctl.Selected()
        if item == None :
            return
        if item.Control().Selected() == None :
            return
        #if item.Control().Selected().Tag() != None :
        #    print(item.Control().Selected().Tag())

    def OnOpen(self) :
        fd = LoadFileDialog(self.master)
        self.LoadFile(fd.go())

    def OnSave(self) :
        if askokcancel(title='save file',message='Do you save file?',default=CANCEL) :
            self.Save()

    def OnSaveAs(self) :
        fd = SaveFileDialog(self.master)
        self.SaveAs(fd.go())

    def OnAddListItem(self) :
        print(QtsSecuInfoesStaticDlg(self.master))

    def OnModifyItem(self) : pass
    def OnDelListitem(self) :
        item = self.tabctl.Selected()
        if item == None :
            return
        if item.Control().Selected() == None :
            return
        if item.Control().Selected().Tag() != None :
            self.xml.RemoveItems(item.Control().Selected().Tag().Index())
            item.Control().Remove(item.Control().Selected().Id())

############################################################
if __name__ == '__main__' :
	mainwindow=QtsTestInputMainWindow()
	mainwindow.RunApp()