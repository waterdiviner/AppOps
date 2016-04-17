import datetime
import uuid
import sys
import os

from qtsmonitorreceivers import QtsComponentReceiver

sys.path.append(os.path.join(os.getenv('QTS_BASE_PATH','..'),'pylib/utility'))
from qtslockhelper import *
from qtsrmqpublisher import *

HeartBeatSeconds = 10
ExpiredTimes = 3
ServerSynLock = threading.RLock()

class QtsDataClient:
    def __init__(self):
        self.url = '127.0.0.1'
        self.private_routingkey = uuid.uuid1()
        self.publisher = QtsRMQPublisher('e.qts.DataRequest',
                                         'fanout',
                                         'q.qts.DataRequest.proto',
                                         'r.qts.DataRequest.proto',
                                         self.url)
        self.receiver = QtsComponentReceiver('e.qts.DataPublish',
                                             'topic',
                                             'q.qts.DataReqReceiver.proto',
                                             self.private_routingkey,
                                             self.url)
        self.timeLastReceiveMessage = datetime.datetime.now()
        self.timeLastSendHeartbeat = datetime.datetime.now()

    def is_expired(self):
        timespec = datetime.datetime.now() - self.timeLastReceiveMessage
        if timespec > HeartBeatSeconds * ExpiredTimes:
            return True
        return False

    def send_heartbeat_if_necessary(self):
        timespec = datetime.datetime.now() - self.timeLastSendHeartbeat
        if timespec > HeartBeatSeconds:
            self.__send_heartbeat()

    def __send_heartbeat(self):
        self.timeLastSendHeartbeat = datetime.datetime.now()

    def send_message(self, data):
        pass

    def receive_heartbeat(self):
        self.timeLastReceiveMessage = datetime.datetime.now()