#coding=utf-8
from PyQt5.QtCore import (pyqtSignal, pyqtSlot, QObject, QAbstractTableModel, Qt, QVariant, QModelIndex)
from PyQt5.QtWidgets import (QApplication, QWidget, QTableView, QAbstractItemView)
from qtsreceiversqtbus import *
from qtsform import *

import sys
sys.path.append('../../utility')
from qtsutility import *

class PositionModel(QAbstractTableModel):
    def __init__(self):
        QAbstractTableModel.__init__(self)
        pyqtbus = QtsRMQReceiversPyQtBus()
        pyqtbus.EOnPosition.connect(self.on_position, Qt.QueuedConnection)
        self.items = dict()
        self.key_row_dict = dict()
        self.header_name = list()
        self.header_name.append('帐户')
        self.header_name.append('市场')
        self.header_name.append('品种')
        self.header_name.append('证券代码')
        self.header_name.append('类型')
        self.header_name.append('总仓位')
        self.header_name.append('可用仓位')
        self.header_name.append('冻结仓位')
        self.header_name.append('费用')
        self.header_name.append('仓位级别')
        self.header_name.append('可申赎仓位')
        self.header_name.append('今仓')
        self.header_name.append('日期')

    def rowCount(self, QModelIndex):
        return len(self.items)

    def columnCount(self, QModelIndex):
        return len(self.header_name)

    def headerData(self, p_int, Qt_Orientation, int_role=None):
        if int_role == Qt.DisplayRole and Qt_Orientation == Qt.Horizontal:
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
                return GetMarketStr(GetMarketFromCode(item.code))
            if col == 2:
                return GetCategoryStr(GetCategoryFromCode(item.code))
            if col == 3:
                return GetOrderCodeFromCode(item.code)
            if col == 4:
                return GetPosTypeStr(item.type)
            if col == 5:
                return str(item.totalvol)
            if col == 6:
                return str(item.avlvol)
            if col == 7:
                return str(item.workingvol)
            if col == 8:
                return str(item.totalcost)
            if col == 9:
                return GetPosLevelStr(item.level)
            if col == 10:
                return str(item.avlcredempvol)
            if col == 11:
                return str(item.todayvol)
            if col == 12:
                return str(item.date)
            return QVariant()

    def on_position(self, info, para):
        row = -1
        key = self.buildKey(para)
        if self.key_row_dict.has_key(key):
            row = self.key_row_dict[key]
            self.items[row] = para
            #self.dataChanged(self.index(row,0), self.index(row,11))
        else:
            row = len(self.items)
            self.beginInsertRows(QModelIndex(), row, row)
            self.key_row_dict[key] = row
            self.items[row] = para
            self.endInsertRows()

    def buildKey(self, para) :
        return '{0}-{1}-{2}'.format(para.account,para.code,para.type)

class PositionView(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.model = PositionModel()
        self.ui.tableView.setModel(self.model)