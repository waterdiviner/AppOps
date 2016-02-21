#coding=utf-8
import sys
import time
################################################################################################
#py库的路径
sys.path.append('../../pylib/utility')
sys.path.append('../../pylib/monitor')
sys.path.append('../../thirdpart/Lib/site-packages/pika-0.9.14-py2.7.egg')
sys.path.append('../../thirdpart/Lib/site-packages/protobuf-2.6.0-py2.7.egg')
sys.path.append('../../thirdpart/Lib/site-packages/setuptools-0.6c11-py2.7.egg')

from qtsrmqmonitor import *

################################################################################################

class QtsMonitorSend(QtsRMQMonitor) :
    def __init__(self,url) :
        QtsRMQMonitor.__init__(self)
        self.AddPublisher('qtsww','e.qts.ww','fanout','q.qts.ww.proto','r.qts.ww.proto',url)

    def Start(self):
        self.Run('qtsww')

    def Dispose(self):
        self.Close('qtsww')

    def Send(self,stype,ssubtype,message):
        return self.Publish('qtsww',stype,ssubtype,message)

def main():
    example = QtsMonitorSend('amqp://guest:guest@localhost:5672/%2F')
    try:
        print('start')
        example.Start()
        print('send data one')
        example.Send('1','0','this is a sample 1')
        print('send data two')
        example.Send('2','0','this is a sample 2')
        print('start exit')
        example.Dispose()
        print('end')
    except KeyboardInterrupt:
       example.Dispose()

if __name__ == "__main__":
    main()


