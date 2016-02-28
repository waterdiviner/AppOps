#coding=utf-8
import csv
import sys

sys.path.append('../database')
sys.path.append('../clearing/position')

from qtsclearingposition import *
from qtsmysql import *

class QtsPositionDBToFile(object) :
    def __init__(self,_flag,_target) :
        self.flag = _flag
        self.target = _target
        self.db = None
        self.writer = csv.writer(open(self.target,'wb'),delimiter=self.flag,quotechar='\r',quoting=csv.QUOTE_MINIMAL)

    def Run(self,host,port,user,psw,dbname,dbtable) :
        self.db = QtsMySql(host,port,user,psw,dbname)
        self.writer.writerow(pos_headers)
        rows = self.db.QueryAll(dbtable)
        for row in rows :
            self.HandleRow(row)

    def HandleRow(self,row):
        self.writer.writerow(row[1:])
        return True

#if __name__ == "__main__":
#    clear = QtsPositionDBToFile(QTS_CSV_FLAG,'H:/Onuca/backup/exposition.pos')
#    clear.Run()
