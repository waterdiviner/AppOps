#coding=utf-8
import sys
import time
################################################################################################
#py库的路径
sys.path.append('../../pylib/utility')
sys.path.append('../../pylib/monitor')

from qtssingleton import singleton
from qtsdelegate import delegate
from qtsreceiversmsgbus import *
from qtsmonitorreceivers import *
################################################################################################

@singleton
class QtsDSReceiver(QtsComponentReceiver):
    def __init__(self):
        QtsComponentReceiver.__init__(self,'e.qts.ds', 'fanout', 'q.qts.ds.proto', 'r.qts.ds.proto', 'amqp://guest:guest@localhost:5672/%2F')

class QtsMonitorDSGui(object) :
    def __init__(self) :
		qts_ds = QtsDSReceiver()
		qts_rmq_receivers_msg_bus = QtsReceiversMsgBus()
		qts_rmq_receivers_msg_bus.EOnRemote += self.OnRemote

    def OnRemote(self,data):
		print(data)
		
    def start(self):
        qts_ds = QtsDSReceiver()
        qts_ds.start()

    def stop(self):
        qts_ds = QtsDSReceiver()
        qts_ds.stop()
		
def main():
   example = QtsMonitorDSGui()
   example.start()
   print('start')
   time.sleep(100000)
   print('start exit')
   print('end')
   example.stop()

if __name__ == "__main__":
    main()
