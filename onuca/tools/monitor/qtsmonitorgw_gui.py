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
class QtsGWReceiver(QtsComponentReceiver):
    def __init__(self):
        QtsComponentReceiver.__init__(self,'e.qts.gw', 'fanout', 'q.qts.gw.proto', 'r.qts.gw.proto', 'amqp://guest:guest@localhost:5672/%2F')

class QtsMonitorGWGui(object) :
    def __init__(self) :
		qts_gw = QtsGWReceiver()
		qts_rmq_receivers_msg_bus = QtsReceiversMsgBus()
		qts_rmq_receivers_msg_bus.EOnRemote += self.OnRemote

    def OnRemote(self,data):
		print(data)
		
    def start(self):
        qts_gw = QtsGWReceiver()
        qts_gw.start()

    def stop(self):
        qts_gw = QtsGWReceiver()
        qts_gw.stop()
		
def main():
   example = QtsMonitorGWGui()
   example.start()
   print('start')
   time.sleep(100000)
   print('start exit')
   print('end')
   example.stop()

if __name__ == "__main__":
    main()
