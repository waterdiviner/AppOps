#coding=utf-8
import time
import string
import os
import sys
import shutil
import sqlite3

reload(sys)
sys.setdefaultencoding('utf-8')

####################################################################
qts_index_code={'SHSE.000016':999987,'SHSE.000001':999999}
qts_time_tag={'CFFEX':1}
qts_price_tag={'9':0.0001,'8':0.0002,'7':0.0003,'6':0.0004,'5':0.0005,'4':0.0006,'3':0.0007,'2':0.0008,'1':0.0009}

####################################################################
class QtsMarket(object) :
    def __init__(self):
        self.market = ''
        self.code = ''
        self.path = ''
        self.date = ''

    def ConvertIndex(self,code) :
        ordercode = "{0}.{1}".format(self.market,code)
        if ordercode in qts_index_code :
            return qts_index_code[ordercode]
        else :
            return code

    def GetTimetag(self) :
        if self.market in qts_time_tag :
            return qts_time_tag[self.market]
        else :
            return 0

    def BuildMilliSecond(self,utc_time) :
        str=''
        millis = long((utc_time - long(utc_time)) * 1000)
        if millis < 10 :
            str = "00{0}".format(millis)
        elif millis < 100 :
            str = "0{0}".format(millis)
        else :
            str = "{0}".format(millis)
        return str

    def BuildDate(self,utc_time) :
        return string.atol(time.strftime('%Y%m%d',time.localtime(utc_time)))

    def BuildTime(self,utc_time) :
        _time = time.strftime('%H%M%S',time.localtime(utc_time))
        _milli = self.BuildMilliSecond(utc_time)
        return (string.atol("{0}{1}".format(_time,_milli)) + self.GetTimetag()) & 0x00000000FFFFFFFF

    def UtcToLocal(self,utc_time) :
        _date =self.BuildDate(utc_time)
        _time = self.BuildTime(utc_time)
        _datetime = (_date << 32) & 0xFFFFFFFF00000000
        _datetime = _datetime | _time
        return _datetime

    def IsValidAskAndBid(self,asks,bids) :
        return (len(asks) == len(bids)) and (len(asks) > 0) and (len(bids) > 0)

    def RoundPrice(self,price) :
        diffprice = price - long(price);
        lprice = long(diffprice * 10000)
        endchar = str(lprice)[len(str(lprice)) - 1]
        if endchar in qts_price_tag :
            return long((price + qts_price_tag[endchar]) * 10000)
        else :
            return long(price * 10000)

####################################################################
class QtsSqliteMarket(QtsMarket) :
    def BuildSql(self,index,tick) : pass
    def HandleData(self,data) : pass

    def GetPath(self) :
        path = sys.path[0]
        if os.path.isdir(path) :
            return path
        else :
            return os.path.dirname(path)

    def CopyFile(self,tfile) :
        if os.path.exists(tfile) :
            os.remove(tfile)
        sfile = '{0}/mode.db3'.format(self.GetPath())
        shutil.copy(sfile,tfile)

    def Open(self) :
        if not os.path.exists(self.path) :
            os.makedirs(self.path)
        dbfile = '{0}/{1}.{2}.db3'.format(self.path,self.market,self.ConvertIndex(self.code))
        self.CopyFile(dbfile)
        self.conn = sqlite3.connect(dbfile)
        self.cursor = self.conn.cursor()

    def Close(self) :
        self.conn.commit()
        self.conn.close()
   