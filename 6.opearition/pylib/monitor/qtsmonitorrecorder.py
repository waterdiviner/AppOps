#coding=utf-8
import sys
import os
reload(sys)
sys.setdefaultencoding( "utf-8" )

import Queue
from qtsreceiversmsgbus import *
from qtsmonitorreceivers import *

sys.path.append(os.path.join(os.getenv('QTS_BASE_PATH','..'),'pylib/utility'))
try :
	from qtsgproto_pb2 import *
except :
	print('warning>> python lib no support protocol buffer')
from qtsvar import *
from qtsdatabase import *
from qtslockhelper import *
from qtsrmqinfo import *

MySqlSynLock = threading.Lock()

class QtsMonitorRecorder(threading.Thread):
    def __init__(self,_database):
        self.database = _database
        self.monitors = list()
        self.items = Queue.Queue()
        qts_rmq_receivers_msg_bus = QtsReceiversMsgBus()
        qts_rmq_receivers_msg_bus.EOnPosition    += self.OnPosition
        qts_rmq_receivers_msg_bus.EOnAccount     += self.OnAccount
        qts_rmq_receivers_msg_bus.EOnRecord      += self.OnRecord
        qts_rmq_receivers_msg_bus.EOnMessage     += self.OnMessage
        qts_rmq_receivers_msg_bus.EOnStrategy    += self.OnStrategy
        qts_rmq_receivers_msg_bus.EOnParameter   += self.OnParameter
        qts_rmq_receivers_msg_bus.EOnData        += self.OnData
        qts_rmq_receivers_msg_bus.EOnPnl         += self.OnPnl
        qts_rmq_receivers_msg_bus.EOnWorking     += self.OnWorking
        qts_rmq_receivers_msg_bus.EOnBook        += self.OnBook
        qts_rmq_receivers_msg_bus.EOnEvent       += self.OnEvent
        qts_rmq_receivers_msg_bus.EOnRemote      += self.OnRemote
        threading.Thread.__init__(self,target=self.Run)

    def Start(self):
        self.brun = True
        threading.Thread.start(self)

    def Stop(self):
        self.brun = False
        threading.Thread.join(self)

    def Run(self):
        count = 0;
        while self.brun :
            count += 1
            if self.HasData() :
                data = self.Pop()
                if data[0] == QTS_GPROTO_EVENT_TYPE_REMOTE:
                    self.Execute(self.SqlRemote(data[1]))
                elif data[0] == QTS_GPROTO_EVENT_TYPE_POSITION:
                    self.Execute(self.SqlPosition(data[1]))
                elif data[0] == QTS_GPROTO_EVENT_TYPE_ACCOUNT:
                    self.Execute(self.SqlAccount(data[1]))
                elif data[0] == QTS_GPROTO_EVENT_TYPE_RECORD:
                    self.Execute(self.SqlRecord(data[1]))
                elif data[0] == QTS_GPROTO_EVENT_TYPE_MESSAGE:
                    self.Execute(self.SqlMessage(data[1]))
                elif data[0] == QTS_GPROTO_EVENT_TYPE_STRATEGYINFO:
                    self.Execute(self.SqlStrategy(data[1]))
                elif data[0] == QTS_GPROTO_EVENT_TYPE_PARAMETER:
                    self.Execute(self.SqlParameter(data[1]))
                elif data[0] == QTS_GPROTO_EVENT_TYPE_DATA:
                    self.Execute(self.SqlData(data[1]))
                elif data[0] == QTS_GPROTO_EVENT_TYPE_PNL:
                    self.Execute(self.SqlPnl(data[1]))
                elif data[0] == QTS_GPROTO_EVENT_TYPE_WORKING:
                    self.Execute(self.SqlWorking(data[1]))
                elif data[0] == QTS_GPROTO_EVENT_TYPE_BOOK:
                    self.Execute(self.SqlBook(data[1]))
                if (not self.HasData()) or (count >= 100) :
                    self.Commit()
                    count = 0
            time.sleep(0.01)

    def AddMonitor(self,_exchange,_queue,_routing_key):
        self.monitors.append(QtsRMQInfo(_exchange,'',_queue,_routing_key,''))

    def ExistMonitor(self,info):
        for target in self.monitors :
            if info.Compare(target) :
                return True
        return False

    def Push(self,key,para):
        self.items.put((key,para))

    def Pop(self):
        return self.items.get()

    def HasData(self):
        return not self.items.empty()

    def Execute(self,sql):
        self.database.Execute(sql,False)

    def Exist(self,sql):
        return self.database.Exist(sql)

    def Commit(self):
        self.database.Commit()

    @synchronizer(MySqlSynLock)
    def OnPosition(self, info, para) :
        if self.ExistMonitor(info) :
            self.Push(QTS_GPROTO_EVENT_TYPE_POSITION,para)

    @synchronizer(MySqlSynLock)
    def OnAccount(self, info, para) :
        if self.ExistMonitor(info) :
            self.Push(QTS_GPROTO_EVENT_TYPE_ACCOUNT,para)

    @synchronizer(MySqlSynLock)
    def OnRecord(self, info, para) :
        if self.ExistMonitor(info) :
            self.Push(QTS_GPROTO_EVENT_TYPE_RECORD,para)

    @synchronizer(MySqlSynLock)
    def OnMessage(self, info, para) :
        if self.ExistMonitor(info) :
            self.Push(QTS_GPROTO_EVENT_TYPE_MESSAGE,para)

    @synchronizer(MySqlSynLock)
    def OnStrategy(self, info, para) :
        if self.ExistMonitor(info) :
            self.Push(QTS_GPROTO_EVENT_TYPE_STRATEGYINFO,para)

    @synchronizer(MySqlSynLock)
    def OnParameter(self, info, para) :
        if self.ExistMonitor(info) :
            self.Push(QTS_GPROTO_EVENT_TYPE_PARAMETER,para)

    @synchronizer(MySqlSynLock)
    def OnData(self, info, para) :
        if self.ExistMonitor(info) :
            self.Push(QTS_GPROTO_EVENT_TYPE_DATA,para)

    @synchronizer(MySqlSynLock)
    def OnPnl(self, info, para) :
        if self.ExistMonitor(info) :
            self.Push(QTS_GPROTO_EVENT_TYPE_PNL,para)

    @synchronizer(MySqlSynLock)
    def OnWorking(self, info, para) :
        if self.ExistMonitor(info) :
            self.Push(QTS_GPROTO_EVENT_TYPE_WORKING,para)

    @synchronizer(MySqlSynLock)
    def OnBook(self, info, para) :
        if self.ExistMonitor(info) :
            self.Push(QTS_GPROTO_EVENT_TYPE_BOOK,para)

    @synchronizer(MySqlSynLock)
    def OnEvent(self, info, para) :
        if self.ExistMonitor(info) :
            self.Push(QTS_GPROTO_EVENT_TYPE_EVENT,para)

    @synchronizer(MySqlSynLock)
    def OnRemote(self, info, para) :
        if self.ExistMonitor(info) :
            self.Push(QTS_GPROTO_EVENT_TYPE_REMOTE,para)

    def ExistPosition(self, para) :
         return self.Exist(self.SqlExistPosition(para))

    def ExistAccount(self, para) :
        return self.Exist(self.SqlExistAccount(para))

    def ExistRecord(self, para) :
        return self.Exist(self.SqlExistRecord(para))

    def ExistRemote(self, para) :
        return self.Exist(self.SqlExistRemote(para))

    def ExistWorking(self, para) :
        return self.Exist(self.SqlExistWorking(para))

    def ExistMessage(self, para) :
        return self.Exist(self.SqlExistMessage(para))

    def ExistStrategy(self, para) :
        return self.Exist(self.SqlExistStrategy(para))

    def ExistParameter(self, para) :
        return self.Exist(self.SqlExistParameter(para))

    def ExistPnl(self, para) :
        return self.Exist(self.SqlExistPnl(para))

    def ExistData(self, para) :
        return self.Exist(self.SqlExistData(para))

    def ExistBook(self, para) :
        return self.Exist(self.SqlExistBook(para))

    def SqlExistPosition(self, para) :
        sql = "select * from {8} where {4}={0} and {5}={1} and {6}={2} and {7}={3}".format(
            para.secuid,
            para.account,
            para.code,
            para.type,
            qts_secuid_field,
            qts_account_field,
            qts_code_field,
            qts_type_field,
            qts_positions_table)
        return sql

    def SqlExistAccount(self, para) :
        sql = "select * from {4} where {2}={0} and {3}={1}".format(
            para.secuid,
            para.account,
            qts_secuid_field,
            qts_account_field,
            qts_accounts_table)
        return sql

    def SqlExistRecord(self, para) :
        sql = "select * from {2} where {1}={0}".format(
            para.orderid,
            qts_orderid_field,
            qts_records_table)
        return sql

    def SqlExistRemote(self, para) :
        sql = "select * from {4} where {2}={0} and {3}={1}".format(
            para.key,
            para.appid,
            qts_key_field,
            qts_appid_field,
            qts_remotes_table)
        return sql

    def SqlExistWorking(self, para) :
        sql = "select * from {10} where {5}={0} and {6}={1} and {7}={2} and {8}={3} and {9}={4}".format(
            para.secuid,
            para.strategyid,
            para.algoid,
            para.code,
            para.action,
            qts_secuid_field,
            qts_strategyid_field,
            qts_algoid_field,
            qts_code_field,
            qts_action_field,
            qts_workings_table)
        return sql

    def SqlExistMessage(self, para) :
        sql = "select * from {6} where {3}={0} and {4}={1} and {5}={2}".format(
            para.id,
            para.type,
            para.level,
            qts_id_field,
            qts_type_field,
            qts_level_field,
            qts_messages_field)
        return sql

    def SqlExistStrategy(self, para) :
        sql = "select * from {2} where {1}={0}".format(
            para.strategyid,
            qts_strategyid_field,
            qts_strategys_table)
        return sql

    def SqlExistParameter(self, para) :
        sql = "select * from {4} where {2}={0} and {3}={1}".format(
            para.strategyid,
            para.key,
            qts_strategyid_field,
            qts_key_field,
            qts_parameters_table)
        return sql

    def SqlExistData(self, para) :
        sql = "select * from {10} where {5}={0} and {6}={1} and {7}={2} and {8}={3} and {9}={4}".format(
            para.secuid,
            para.index,
            para.code,
            para.type,
            para.subtype,
            qts_secuid_field,
            qts_index_field,
            qts_code_field,
            qts_type_field,
            qts_subtype_field,
            qts_datas_table)
        return sql

    def SqlExistPnl(self, para) :
        sql = "select * from {6} where {3}={0} and {4}={1} and {5}={2}".format(
            para.secuid,
            para.account,
            para.code,
            qts_secuid_field,
            qts_account_field,
            qts_code_field,
            qts_pnls_table)
        return sql

    def SqlExistBook(self, para) :
        sql = "select * from {10} where {5}={0} and {6}={1} and {7}={2} and {8}={3} and {9}={4}".format(
            para.secuid,
            para.strategyid,
            para.algoid,
            para.code,
            para.price,
            qts_secuid_field,
            qts_strategyid_field,
            qts_algoid_field,
            qts_code_field,
            qts_price_field,
            qts_books_table)
        return sql

    def SqlPosition(self, para) :
        sql=''
        if self.ExistPosition(para) :
            sql=("update {22} set {15}={4}, {16}={5}, {17}={6}, {18}={7}, {19}={8}, {20}={9}, {21}={10}"
                " where {11}={0} and {12}={1} and {13}={2} and {14}={3}").format(
                para.secuid,
                para.account,
                para.code,
                para.type,
                para.date,
                para.totalvol,
                para.avlvol,
                para.workingvol,
                para.totalcost,
                para.avlcredempvol,
                para.todayvol,
                qts_secuid_field,
                qts_account_field,
                qts_code_field,
                qts_type_field,
                qts_date_field,
                qts_totalvol_field,
                qts_avlvol_field,
                qts_workingvol_field,
                qts_totalcost_field,
                qts_avlcredempvol_field,
                qts_todayvol_field,
                qts_positions_table
                )
        else :
            sql=("insert into {24}({12},{13},{14},{15},{16},{17},{18},{19},{20},{21},{22},{23})"
            " VALUES ({0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11})").format(
                para.secuid,
                para.account,
                para.code,
                para.type,
                para.date,
                para.totalvol,
                para.avlvol,
                para.workingvol,
                para.totalcost,
                para.level,
                para.avlcredempvol,
                para.todayvol,
                qts_secuid_field,
                qts_account_field,
                qts_code_field,
                qts_type_field,
                qts_date_field,
                qts_totalvol_field,
                qts_avlvol_field,
                qts_workingvol_field,
                qts_totalcost_field,
                qts_level_field,
                qts_avlcredempvol_field,
                qts_todayvol_field,
                qts_positions_table
                )
        return sql

    def SqlAccount(self, para):
        sql=''
        if self.ExistAccount(para) :
            sql=("update {12} set {8}={2}, {9}={3}, {10}={4}, {11}={5} "
                " where {6}={0} and {7}={1}").format(
                para.secuid,
                para.account,
                para.totalamount,
                para.avlamount,
                para.freezeamount,
                para.date,
                qts_secuid_field,
                qts_account_field,
                qts_totalamount_field,
                qts_avlamount_field,
                qts_freezeamount_field,
                qts_date_field,
                qts_accounts_table
            )
        else :
            viraccount = 0
            if para.level != 0 :
                viraccount = para.viraccount
            sql=("insert into {22}({11},{12},{13},{14},{15},{16},{17},{18},{19},{20},{21}) "
            "VALUES ({0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10})").format(
                para.secuid,
                para.account,
                para.totalamount,
                para.avlamount,
                para.freezeamount,
                para.date,
                para.currency,
                para.user,
                para.sharetag,
                para.level,
                viraccount,
                qts_secuid_field,
                qts_account_field,
                qts_totalamount_field,
                qts_avlamount_field,
                qts_freezeamount_field,
                qts_date_field,
                qts_currency_field,
                qts_user_field,
                qts_sharetag_field,
                qts_level_field,
                qts_viraccount_field,
                qts_accounts_table
            )
        return sql

    def SqlRecord(self, para):
        sql=''
        if self.ExistRecord(para) :
            sql=("update {18} set {12}={3}, {13}={4}, {14}={5}, {15}={6}, {16}={7}, {17}={8}"
                 " where {9}={0} and {10}={1} and {11}={2}").format(
                para.strategyid,
                para.orderid,
                para.parentid,
                para.status,
                para.prevstatus,
                para.iprice,
                para.ivolume,
                para.itime,
                int(para.canceled),
                qts_strategyid_field,
                qts_orderid_field,
                qts_parentid_field,
                qts_status_field,
                qts_prevstatus_field,
                qts_iprice_field,
                qts_ivolume_field,
                qts_itime_field,
                qts_canceled_field,
                qts_records_table
            )
        else :
            sql=("insert into {54}({27},{28},{29},{30},{31},{32},{33},{34},{35},{36},{37},{38},{39},{40},{41},"
                 "{42},{43},{44},{45},{46},{47},{48},{49},{50},{51},{52},{53}) "
                 "VALUES ({0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12},{13},{14},"
                 "{15},{16},{17},{18},{19},{20},{21},{22},{23},{24},{25},{26})").format(
                para.secuid,
                para.account,
                para.strategyid,
                para.orderid,
                para.algoid,
                para.algoindex,
                para.parentid,
                para.code,
                para.action,
                para.paction,
                para.status,
                para.prevstatus,
                para.oprice,
                para.iprice,
                para.ovolume,
                para.ivolume,
                para.otime,
                para.itime,
                para.property,
                para.direction,
                int(para.canceled),
                para.userid,
                para.refid,
                para.sessionid,
                para.source,
                para.ss,
                para.gw,
                qts_secuid_field,
                qts_account_field,
                qts_strategyid_field,
                qts_orderid_field,
                qts_algoid_field,
                qts_algoindex_field,
                qts_parentid_field,
                qts_code_field,
                qts_action_field,
                qts_paction_field,
                qts_status_field,
                qts_prevstatus_field,
                qts_oprice_field,
                qts_iprice_field,
                qts_ovolume_field,
                qts_ivolume_field,
                qts_otime_field,
                qts_itime_field,
                qts_property_field,
                qts_direction_field,
                qts_canceled_field,
                qts_userid_field,
                qts_refid_field,
                qts_sessionid_field,
                qts_source_field,
                qts_ss_field,
                qts_gw_field,
                qts_records_table
            )
        return sql

    def SqlRemote(self, para):
        sql=''
        if self.ExistRemote(para) :
            sql=("update {6} set {5}={2} "
                " where {3}={0} and {4}={1}").format(
                para.key,
                para.appid,
                para.status,
                qts_key_field,
                qts_appid_field,
                qts_status_field,
                qts_remotes_table
            )
        else :
            sql=("insert into {26}({13},{14},{15},{16},{17},{18},{19},{20},{21},{22},{23},{24},{25}) "
                 "VALUES ({0},{1},{2},{3},{4},{5},{6},'{7}','{8}',{9},{10},{11},{12})").format(
                para.key,
                para.localid,
                para.localport,
                para.remoteid,
                para.remoteport,
                para.appid,
                para.apptype,
                para.name,
                para.version,
                para.mode,
                para.status,
                para.group,
                para.type,
                qts_key_field,
                qts_localid_field,
                qts_localport_field,
                qts_remoteid_field,
                qts_remoteport_field,
                qts_appid_field,
                qts_apptype_field,
                qts_name_field,
                qts_version_field,
                qts_mode_field,
                qts_status_field,
                qts_group_field,
                qts_type_field,
                qts_remotes_table
            )
        return sql

    def SqlMessage(self, para):
        sql=("insert into {8}({4},{5},{6},{7}) "
             "VALUES ({0},{1},{2},{3}").format(
            para.id,
            para.type,
            para.level,
            para.msg,
            qts_id_field,
            qts_type_field,
            qts_level_field,
            qts_msg_field,
            qts_messages_table
        )
        return sql

    def SqlStrategy(self, para):
        sql=''
        if self.ExistStrategy(para) :
            sql=("update {4} set {3}={1} "
                " where {2}={0}").format(
                para.strategyid,
                para.status,
                qts_strategyid_field,
                qts_status_field,
                qts_strategys_table
            )
        else :
            sql=("insert into {24}({12},{13},{14},{15},{16},{17},{18},{19},{20},{21},{22},{23}) "
                 "VALUES ({0},'{1}','{2}',{3},{4},{5},{6},{7},{8},{9},{10},{11})").format(
                para.strategyid,
                para.name,
                str(para.account()).replace('[','').replace(']',''),
                para.minorderid,
                para.maxorderid,
                para.currorderid,
                para.orderidstep,
                para.status,
                para.threadid,
                para.cycle,
                para.tradecycle,
                para.ismanual,
                qts_strategyid_field,
                qts_name_field,
                qts_account_field,
                qts_minorderid_field,
                qts_maxorderid_field,
                qts_currorderid_field,
                qts_orderidstep_field,
                qts_status_field,
                qts_threadid_field,
                qts_cycle_field,
                qts_tradecycle_field,
                qts_ismanual_field,
                qts_strategys_table
            )
        return sql

    def SqlParameter(self, para):
        sql=''
        if self.ExistParameter(para) :
            sql=("update {8} set {6}={2}, {7}={3} "
                " where {4}={0} and {5}={1}").format(
                para.strategyid,
                para.key,
                para.value,
                para.status,
                qts_strategyid_field,
                qts_key_field,
                qts_value_field,
                qts_status_field,
                qts_parameters_table
            )
        else :
            sql=("insert into {24}({12},{13},{14},{15},{16},{17},{18},{19},{20},{21},{22},{23}) "
                 "VALUES ({0},{1},'{2}',{3},{4},{5},{6},{7},{8},'{9}','{10}',{11})").format(
                para.strategyid,
                para.key,
                para.name,
                para.value,
                para.type,
                para.level,
                para.decimal,
                para.status,
                para.mode,
                para.style,
                para.component,
                para.index,
                qts_strategyid_field,
                qts_key_field,
                qts_name_field,
                qts_value_field,
                qts_type_field,
                qts_level_field,
                qts_decimal_field,
                qts_status_field,
                qts_mode_field,
                qts_style_field,
                qts_component_field,
                qts_index_field,
                qts_parameters_table
            )
        return sql

    def SqlPnl(self, para): pass
    def SqlBook(self, para): pass
    def SqlWorking(self, para): pass
    def SqlData(self, para): pass
