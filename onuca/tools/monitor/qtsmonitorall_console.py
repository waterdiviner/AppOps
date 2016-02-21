#coding=utf-8
import sys
import time
################################################################################################
#py库的路径
sys.path.append('../../pylib/utility')
sys.path.append('../../pylib/monitor')
sys.path.append('../../pylib/database')

from qtsapp import *
from qtssingleton import singleton
from qtsdelegate import delegate
from qtsreceiversmsgbus import *
from qtsmonitorreceivers import *
from qtsmysqlrecorder import QtsMySqlRecorder

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

class QtsMonitorAllConsole(QtsApp) :
    def __init__(self):
        self.gw_backup = QtsMySqlRecorder('localhost',3306,'root','111','qts_gw_backup')
        self.gw_backup.AddMonitor('e.qts.gw','q.qts.gw.proto','r.qts.gw.proto')

    def start(self):
        self.gw_backup.Start()
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
        self.gw_backup.Stop()

def Main():
    app = QtsMonitorAllConsole()
    app.run()

if __name__ == "__main__":
   Main()
