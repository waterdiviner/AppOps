#coding=utf-8
from qtssecuinfo import *
sys.path.append('../database')
from qtsmysql import *

class QtsSecuInfoToDB(QtsSecuinfoConvert) :
    def __init__(self,_flag,_source) :
        self.sitems = dict()
        self.ditems = dict()
        self.flag = _flag
        self.source = _source
        self.reader = csv.reader(open(self.source,'rb'),delimiter=self.flag)
        self.db = None

    def Run(self,host,port,user,psw,dbname) :
        self.db = QtsMySql(host,port,user,psw,dbname)
        self.db.Clear(qts_secuinfo_s_table)
        self.db.Clear(qts_secuinfo_d_table)
        for row in self.reader :
            self.HandleRow(row)
        self.db.Commit()

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