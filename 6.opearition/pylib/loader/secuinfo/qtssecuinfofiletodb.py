#coding=utf-8
from qtssecuinfo import *
sys.path.append(os.path.join(os.getenv('QTS_BASE_PATH','..'),'pylib/database'))
from qtsmysql import *

class QtsSecuInfoFileToDB(object) :
    def __init__(self,_flag,_static,_dynamic) :
        self.sitems = dict()
        self.ditems = dict()
        self.flag = _flag
        self.static = _static
        self.dynamic = _dynamic
        self.bopen = True
        if os.path.isfile(self.static) :
            self.sreader = csv.reader(open(self.static,'rb'),delimiter=self.flag)
        else :
            self.bopen = False
            TraceError('open file {0} is failed!'.format(self.static))
        if os.path.isfile(self.dynamic) :
            self.dreader = csv.reader(open(self.dynamic,'rb'),delimiter=self.flag)
        else :
            self.bopen = False
            TraceError('open file {0} is failed!'.format(self.dynamic))
        self.db = None

    def Run(self,host,port,user,psw,dbname) :
        if self.bopen :
            self.db = QtsMySql(host,port,user,psw,dbname)
            self.db.Clear(qts_secuinfo_s_table)
            self.db.Clear(qts_secuinfo_d_table)
            for row in self.sreader :
                self.HandleStaticRow(row)
            for row in self.dreader :
                self.HandleDynamicRow(row)
            self.db.Commit()
        else :
            TraceError('file is not opened!')

    def HandleStaticRow(self,row):
        sql = ("INSERT INTO {0}({1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12},{13},{14})"
              " VALUES({15},{16},{17},'{18}','{19}','{20}','{21}',{22},{23},{24},{25},{26},{27},{28})").format(
                                                qts_secuinfo_s_table,
                                                qts_market_field,
                                                qts_category_field,
                                                qts_secucode_field,
                                                qts_ordercode_field,
                                                qts_marketname_field,
                                                qts_categoryname_field,
                                                qts_secuname_field,
                                                qts_minorderqty_field,
                                                qts_maxorderqty_field,
                                                qts_pricetick_field,
                                                qts_tradetn_field,
                                                qts_posmode_field,
                                                qts_multipler_field,
                                                qts_margin_field,
                                                row[0],
                                                row[1],
                                                row[2],
                                                row[3],
                                                row[4].encode('utf8'),
                                                row[5].encode('utf8'),
                                                row[6].encode('utf8'),
                                                row[7],
                                                row[8],
                                                row[9],
                                                row[10],
                                                row[11],
                                                row[12],
                                                row[13])
        self.db.Execute(sql,False)

    def HandleDynamicRow(self,row):
        sql = ("INSERT INTO {0}({1},{2},{3},{4},{5},{6},{7},{8})"
              " VALUES({9},{10},{11},{12},{13},{14},{15},{16})").format(
                                                qts_secuinfo_d_table,
                                                qts_market_field,
                                                qts_category_field,
                                                qts_secucode_field,
                                                qts_lastprice_field,
                                                qts_lolimitedprice_field,
                                                qts_uplimitedprice_field,
                                                qts_suspension_field,
                                                qts_tradingfee_field,
                                                row[0],
                                                row[1],
                                                row[2],
                                                row[3],
                                                row[4],
                                                row[5],
                                                row[6],
                                                row[7])
        self.db.Execute(sql,False)