#coding=utf-8
from PyQt5.QtCore import (pyqtSignal, pyqtSlot, QObject, QAbstractTableModel, Qt, QVariant, QModelIndex)
from PyQt5.QtWidgets import (QApplication, QWidget, QTableView, QAbstractItemView)
from qtsreceiversqtbus import *
from qtsform import *

import sys
import os
sys.path.append(os.path.join(os.getenv('QTS_BASE_PATH','../..'),'pylib/utility'))
from qtsutility import *

class RecordModel(QAbstractTableModel):
    def __init__(self):
        QAbstractTableModel.__init__(self)
        pyqtbus = QtsRMQReceiversPyQtBus()
        pyqtbus.EOnRecord.connect(self.on_record, Qt.QueuedConnection)
        self.items = dict()
        self.key_row_dict = dict()
        self.header_name = list()
        self.header_name.append('帐户')
        self.header_name.append('策略ID')
        self.header_name.append('父订单ID')
        self.header_name.append('订单ID')
        self.header_name.append('算法ID')
        self.header_name.append('算法订单ID')
        self.header_name.append('市场')
        self.header_name.append('品种')
        self.header_name.append('证券代码')
        self.header_name.append('交易行为')
        self.header_name.append('状态')
        self.header_name.append('下单价格')
        self.header_name.append('成交价格')
        self.header_name.append('下单量')
        self.header_name.append('成交量')
        self.header_name.append('下单时间')
        self.header_name.append('成交时间')
        self.header_name.append('属性')
        self.header_name.append('是否撤单')
        self.header_name.append('用户ID')
        self.header_name.append('父交易行为')
        self.header_name.append('前状态')
        self.header_name.append('方向')

    def rowCount(self, QModelIndex):
        return len(self.items)

    def columnCount(self, QModelIndex):
        return len(self.header_name)

    def headerData(self, p_int, Qt_Orientation, int_role=None):
        if (int_role == Qt.DisplayRole) and (Qt_Orientation == Qt.Horizontal) :
            return self.header_name[p_int]
        return QVariant()

    def data(self, index, role):
     if role == Qt.DisplayRole :
        row = index.row()
        col = index.column()
        item = self.items[row]
        if col == 0:
            return str(item.account)
        if col == 1:
            return str(item.strategyid)
        if col == 2:
            return str(item.parentid)
        if col == 3:
            return str(item.orderid)
        if col == 4:
            return str(item.algoid)
        if col == 5:
            return str(item.algoindex)
        if col == 6:
            return GetMarketStr(GetMarketFromCode(item.code))
        if col == 7:
            return GetCategoryStr(GetCategoryFromCode(item.code))
        if col == 8:
            return GetOrderCodeFromCode(item.code)
        if col == 9:
            return GetActionStr(item.action)
        if col == 10:
            return GetStatusStr(item.status)
        if col == 11:
            return str(GetRealPrice(item.oprice))
        if col == 12:
            return str(GetRealPrice(item.iprice))
        if col == 13:
            return str(item.ovolume)
        if col == 14:
            return str(item.ivolume)
        if col == 15:
            return str(item.otime)
        if col == 16:
            return str(item.itime)
        if col == 17:
            return str(item.property)
        if col == 18:
            return str(item.canceled)
        if col == 19:
            return str(item.userid)
        if col == 20:
            return GetActionStr(item.paction)
        if col == 21:
            return GetStatusStr(item.prevstatus)	
        if col == 22:
            return GetDirectionStr(item.direction)			
        return QVariant()

    def on_record(self, info, para):
        row = -1
        key = self.buildKey(para)
        if self.key_row_dict.has_key(key):
            row = self.key_row_dict[key]
            self.items[row] = para
            #self.dataChanged(self.index(row,0), self.index(row,20))
        else:
            row = len(self.items)
            self.beginInsertRows(QModelIndex(), row, row)
            self.key_row_dict[key] = row
            self.items[row] = para
            self.endInsertRows()

    def buildKey(self, para):
        return '{0}-{1}-{2}'.format(para.account,para.parentid,para.orderid)

class RecordView(QWidget):
   def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.model = RecordModel()
        self.ui.tableView.setModel(self.model)

