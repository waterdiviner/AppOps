#coding=utf-8
import sys
import time
################################################################################################
#py库的路径
sys.path.append('../../pylib/utility')
sys.path.append('../../pylib/monitor')
sys.path.append('../../pylib/database')
sys.path.append('../../pylib/gui/monitor')

from qtssingleton import singleton
from qtsdelegate import delegate
from qtsreceiversmsgbus import *
from qtsmonitorreceivers import *
from qtsmonitorapp import *
from qtsmonitor import *
from qtsmysqlrecorder import QtsMySqlRecorder

from qtsaccountview import *
from qtspositionview import *
from qtsrecordview import *
from qtsdeployview import *
################################################################################################

@singleton
class QtsSSReceiver(QtsComponentReceiver):
    def __init__(self):
        QtsComponentReceiver.__init__(self,'e.qts.ss', 'fanout', 'q.qts.ss.proto', 'r.qts.ss.proto', 'amqp://guest:guest@localhost:5672/%2F')

@singleton
class QtsGWReceiver(QtsComponentReceiver):
    def __init__(self):
        QtsComponentReceiver.__init__(self,'e.qts.gw', 'fanout', 'q.qts.gw.proto', 'r.qts.gw.proto', 'amqp://guest:guest@localhost:5672/%2F')

@singleton
class QtsDSReceiver(QtsComponentReceiver):
    def __init__(self):
        QtsComponentReceiver.__init__(self,'e.qts.ds', 'fanout', 'q.qts.ds.proto', 'r.qts.ds.proto', 'amqp://guest:guest@localhost:5672/%2F')

@singleton
class QtsGUIReceiver(QtsComponentReceiver):
    def __init__(self):
        QtsComponentReceiver.__init__(self,'e.qts.gui', 'fanout', 'q.qts.gui.proto', 'r.qts.gui.proto', 'amqp://guest:guest@localhost:5672/%2F')

class QtsMonitorAllGui(QtsMonitorApp) :
    def __init__(self):
        self.qtsmysql = QtsMySqlRecorder('localhost',3306,'root','1111','qts_ss_backup')

    def start(self):
        self.qtsmysql.Start()
        qts_ss = QtsSSReceiver()
        qts_gw = QtsGWReceiver()
        qts_ds = QtsDSReceiver()
        qts_gui = QtsGUIReceiver()
        qts_ss.start()
        qts_gw.start()
        qts_ds.start()
        qts_gui.start()

    def stop(self):
        qts_ss = QtsSSReceiver()
        qts_gw = QtsGWReceiver()
        qts_ds = QtsDSReceiver()
        qts_gui = QtsGUIReceiver()
        qts_ss.stop()
        qts_gw.stop()
        qts_ds.stop()
        qts_gui.stop()
        self.qtsmysql.Stop()

    def Pages(self):
        _pages = list()
        _pages.append(self.AddPage('accountview',AccountView()))
        _pages.append(self.AddPage('positionview',PositionView()))
        _pages.append(self.AddPage('recordview',RecordView()))
        #_pages.append(self.AddPage('deploydview',QtsDeployView()))
        return _pages

if __name__ == "__main__":
    WinMain(QtsMonitorAllGui())
