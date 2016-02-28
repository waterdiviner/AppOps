#coding=utf-8
import csv
import sys

sys.path.append('../database')
sys.path.append('../clearing/account')

from qtsmysql import *

trade_headers=[qts_market_field,qts_category_field,qts_account_field,qts_totalamoumt_field,qts_avlamount_field,qts_freezeamount_field,qts_currency_field,qts_date_field]
user_headers=[qts_user_field,qts_account_field,qts_viraccount_field]
ex_headers=[qts_market_field,qts_category_field,qts_viraccount_field,qts_relaccount_field,qts_sharetag_field,qts_totalamoumt_field,qts_avlamount_field,qts_freezeamount_field,qts_date_field]

class QtsAccountDBToFile(object) :
    def __init__(self,_flag,_trade,_user,_ex) :
        self.sitems = dict()
        self.ditems = dict()
        self.flag = _flag
        self.trade = _trade
        self.user = _user
        self.ex = _ex
        self.db = None
        self.twriter = csv.writer(open(self.trade,'wb'),delimiter=self.flag,quotechar='\r',quoting=csv.QUOTE_MINIMAL)
        self.uwriter = csv.writer(open(self.user,'wb'),delimiter=self.flag,quotechar='\r',quoting=csv.QUOTE_MINIMAL)
        self.ewriter = csv.writer(open(self.ex,'wb'),delimiter=self.flag,quotechar='\r',quoting=csv.QUOTE_MINIMAL)

    def Run(self,host,port,user,psw,dbname,dbtrade,dbuser,dbex) :
        self.db = QtsMySql(host,port,user,psw,dbname)
        self.HandleTable(dbtrade,trade_headers)
        self.HandleTable(dbuser,user_headers)
        self.HandleTable(dbex,ex_headers)

    def HandleTable(self,dbtable,headers):
        self.writer.writerow(headers)
        rows = self.db.QueryAll(dbtable)
        for row in rows :
            self.HandleRow(row)

    def HandleRow(self,row):
        self.writer.writerow(row[1:])
        return True

#if __name__ == "__main__":
#    clear = QtsAccountDBToFile(QTS_CSV_FLAG,'H:/Onuca/backup/exposition.pos')
#    clear.Run()
