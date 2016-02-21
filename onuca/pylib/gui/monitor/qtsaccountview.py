#coding=utf-8
from PyQt5.QtCore import (pyqtSignal, pyqtSlot, QObject, QAbstractTableModel, Qt, QVariant, QModelIndex)
from PyQt5.QtWidgets import (QApplication, QWidget, QTableView, QAbstractItemView)
from qtsreceiversqtbus import *
from qtsform import *

import sys
sys.path.append('../../utility')
from qtsutility import *

class AccountModel(QAbstractTableModel):
    def __init__(self):
        QAbstractTableModel.__init__(self)
        pyqtbus = QtsRMQReceiversPyQtBus()
        pyqtbus.EOnAccount.connect(self.on_account, Qt.QueuedConnection)
        self.items = dict()
        self.key_row_dict = dict()
        self.header_name = list()
        self.header_name.append('市场')
        self.header_name.append('品种')
        self.header_name.append('帐户')
        self.header_name.append('总资金')
        self.header_name.append('可用资金')
        self.header_name.append('冻结资金')
        self.header_name.append('日期')
        self.header_name.append('货币类型')

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
                return GetMarketStr(GetMarketFromCode(item.secuid))
            if col == 1:
                return GetCategoryStr(GetCategoryFromCode(item.secuid))
            if col == 2:
                return str(item.account)
            if col == 3:
                return str(GetRealPrice(item.totalamount))
            if col == 4:
                return str(GetRealPrice(item.avlamount))
            if col == 5:
                return str(GetRealPrice(item.freezeamount))
            if col == 6:
                return str(item.date)
            if col == 7:
                return str(item.currency)
            return QVariant()

    def on_account(self, info, para):
        row = -1
        key = self.buildKey(para)
        if self.key_row_dict.has_key(key):
            row = self.key_row_dict[key]
            self.items[row] = para
            #self.dataChanged(self.index(row,0), self.index(row,6))
        else:
            row = len(self.items)
            self.beginInsertRows(QModelIndex(), row, row)
            self.key_row_dict[key] = row
            self.items[row] = para
            self.endInsertRows()

    def buildKey(self, para):
        return '{0}-{1}'.format(para.secuid, para.account)

class AccountView(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.mode = AccountModel()
        self.ui.tableView.setModel(self.mode)