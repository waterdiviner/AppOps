import threading
import datetime
import sys
import os

from qtsmonitorreceivers import QtsComponentReceiver
from qtssqliterecorder import *

sys.path.append(os.path.join(os.getenv('QTS_BASE_PATH','..'),'pylib/utility'))
from qtslockhelper import *
from qtsrmqpublisher import *
from qtssingleton import *
try :
	from qtsgproto_pb2 import *
except :
	print('warning>> python lib no support protocol buffer')

HeartBeatSeconds = 10
ExpiredTimes = 3
ServerSynLock = threading.RLock()

class QtsClientProxyInServer(QtsRMQPublisher):
    def __init__(self, routingkey, url):
        QtsRMQPublisher.__init__(self,'e.qts.DataPublish',
                                                     'topic',
                                                     'q.qts.DataReqReceiver.proto',
                                                     routingkey,
                                                     url)
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


@singleton
class QtsDataServer(QtsSqliteRecorder):
    def __init__(self, DB_SQLITE_NAME, url):
        QtsSqliteRecorder.__init__(DB_SQLITE_NAME)
        self.listenReceiver = QtsComponentReceiver('e.qts.DataReqReceiver',
                                                   'fanout',
                                                   'q.qts.DataReqReceiver.proto',
                                                   'r.qts.DataReqReceiver.proto',
                                                   url)
        self.client_proxies = set()
        self.heartbeat_check_timer = threading.Timer(HeartBeatSeconds, self.heartbeat_check, self)

    @synchronizer(ServerSynLock)
    def heartbeat_check(self):
        for client in self.client_proxies:
            if client.is_expired():
                self.client_proxies.remove(client)
            else:
                client.send_heartbeat_if_necessary()
        self.heartbeat_check_timer.start()

    @synchronizer(ServerSynLock)
    def accept_client(self, para):
        routingkey = ""
        url = ""
        client = QtsClientProxyInServer(routingkey, url)
        self.client_proxies.add(client)
        positions = self.load_all_positions()
        accounts = self.load_all_accounts()
        records = self.load_all_records()
        bpositions = SerializeToString(positions)
        baccounts = SerializeToString(accounts)
        brecords = SerializeToString(records)
        client.send_message(bpositions)
        client.send_message(baccounts)
        client.send_message(brecords)

    @synchronizer(ServerSynLock)
    def load_all_positions(self):
        res = QtsGProtoPositions
        sql = "select * from position"
        self.cursor.execute(sql)
        dbres = self.cursor.fetchall()
        for i in range(len(res)):
            item = dbres[i]
            gposition = res.add_positions()
            gposition.secuid = item[0]
            gposition.account = item[1]
            gposition.code = item[2]
            gposition.type = item[3]
            gposition.date = item[4]
            gposition.totalvol = item[5]
            gposition.avlvol = item[6]
            gposition.workingvol = item[7]
            gposition.totalcost = item[8]
            gposition.avlcredempvol = item[9]
            gposition.todayvol = item[10]
        return res

    @synchronizer(ServerSynLock)
    def load_all_accounts(self):
        res = QtsGProtoAccounts()
        sql = "select * from account"
        self.cursor.execute(sql)
        dbres = self.cursor.fetchall()
        for i in range(len(dbres)):
            item = dbres[i]
            gaccount = res.add_accounts()
            gaccount.secuid = item[0]
            gaccount.account = item[1]
            gaccount.totalamount = item[2]
            gaccount.avlamount = item[3]
            gaccount.freezeamount = item[4]
            gaccount.date = item[5]
            gaccount.currency = item[6]
        return res

    @synchronizer(ServerSynLock)
    def load_all_records(self):
        res = QtsGProtoRecords()
        sql = "select * from record"
        self.cursor.execute(sql)
        dbres = self.cursor.fetchall()
        for i in range(len(dbres)):
            item = dbres[i]
            grecord = res.add_records()
            grecord.secuid = item[0]
            grecord.account = item[1]
            grecord.strategyid = item[2]
            grecord.orderid = item[3]
            grecord.algoid = item[4]
            grecord.algoindex = item[5]
            grecord.parentid = item[6]
            grecord.code = item[7]
            grecord.action = item[8]
            grecord.paction = item[9]
            grecord.status = item[10]
            grecord.prevstatus = item[11]
            grecord.oprice = item[12]
            grecord.iprice = item[13]
            grecord.ovolume = item[14]
            grecord.ivolume = item[15]
            grecord.otime = item[16]
            grecord.itime = item[17]
            grecord.property = item[18]
            grecord.canceled = item[19]
            grecord.userid = item[20]
        return res

    @synchronizer(ServerSynLock)
    def OnPosition(self, para):
        super(QtsDataServer, self).OnPosition(para)
        for client in self.client_proxies:
            bpositions = SerializeToString(para)
            client.send_message(bpositions)

    @synchronizer(ServerSynLock)
    def OnAccount(self, para):
        super(QtsDataServer, self).OnAccount(para)
        for client in self.client_proxies:
            baccount = SerializeToString(para)
            client.send_message(baccount)

    @synchronizer(ServerSynLock)
    def OnRecord(self, para):
        super(QtsDataServer, self).OnRecord(para)
        for client in self.client_proxies:
            brecord = SerializeToString(para)
            client.send_message(brecord)

    # @synchronizer(ServerSynLock)
    # def OnMessage(self, para):
    #     super(QtsDataServer, self).OnMessage(para)
    #     for client in self.client_proxies:
    #         data = SerializeToString(para)
    #         client.send_message(data)
    #
    # @synchronizer(ServerSynLock)
    # def OnStrategy(self, para):
    #     super(QtsDataServer, self).OnStrategy(para)
    #     for client in self.client_proxies:
    #         data = SerializeToString(para)
    #         client.send_message(data)
    #
    # @synchronizer(ServerSynLock)
    # def OnControl(self, para):
    #     super(QtsDataServer, self).OnControl(para)
    #     for client in self.client_proxies:
    #         data = SerializeToString(para)
    #         client.send_message(data)
    #
    # @synchronizer(ServerSynLock)
    # def OnParamete(self, para):
    #     super(QtsDataServer, self).OnParamete(para)
    #     for client in self.client_proxies:
    #         data = SerializeToString(para)
    #         client.send_message(data)
    #
    # @synchronizer(ServerSynLock)
    # def OnData(self, para):
    #     super(QtsDataServer, self).OnData(para)
    #     for client in self.client_proxies:
    #         data = SerializeToString(para)
    #         client.send_message(data)
    #
    # @synchronizer(ServerSynLock)
    # def OnPnl(self, para):
    #     super(QtsDataServer, self).OnPnl(para)
    #     for client in self.client_proxies:
    #         data = SerializeToString(para)
    #         client.send_message(data)
    #
    # @synchronizer(ServerSynLock)
    # def OnWorking(self, para):
    #     super(QtsDataServer, self).OnWorking(para)
    #     for client in self.client_proxies:
    #         data = SerializeToString(para)
    #         client.send_message(data)
    #
    # @synchronizer(ServerSynLock)
    # def OnBook(self, para):
    #     super(QtsDataServer, self).OnBook(para)
    #     for client in self.client_proxies:
    #         data = SerializeToString(para)
    #         client.send_message(data)
    #
    # @synchronizer(ServerSynLock)
    # def OnEvent(self, para):
    #     super(QtsDataServer, self).OnEvent(para)
    #     for client in self.client_proxies:
    #         data = SerializeToString(para)
    #         client.send_message(data)
    #
    # @synchronizer(ServerSynLock)
    # def OnRemote(self, para):
    #     super(QtsDataServer, self).OnRemote(para)
    #     for client in self.client_proxies:
    #         data = SerializeToString(para)
    #         client.send_message(data)










