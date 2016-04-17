#coding=utf-8
import os
from qtsclearingposition import *
sys.path.append(os.path.join(os.getenv('QTS_BASE_PATH','..'),'pylib/database'))
from qtsmysql import *

class QtsClearingPositionFileToDB(object) :
    def __init__(self,_flag,_source) :
        self.items = dict()
        self.flag = _flag
        self.source = _source
        self.db = None
        self.table = None
        self.bopen = True
        if os.path.isfile(self.source) :
            self.reader = csv.reader(open(self.source,'rb'),delimiter=self.flag)
        else :
            self.bopen = False
            TraceError('open file {0} is failed!'.format(self.source))

    def Run(self,host,port,user,psw,dbname,dbtable,date) :
        if self.bopen :
            self.table = dbtable
            self.db = QtsMySql(host,port,user,psw,dbname)
            self.db.Clear(self.table)
            for row in self.reader :
                self.HandleRow(row,date)
            self.db.Commit()
        else :
            TraceError('file is not opened!')

    def HandleRow(self,row,date):
        sql = "INSERT INTO {0}({1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12},{13})" \
              " VALUES({14},{15},{16},{17},{18},{19},{20},{21},{22},{23},{24},{25},{26})".format(
            self.table,
            qts_account_field,
            qts_market_field,
            qts_category_field,
            qts_code_field,
            qts_type_field,
            qts_level_field,
            qts_totalvol_field,
            qts_avlvol_field,
            qts_workingvol_field,
            qts_toalcost_field,
            qts_date_field,
            qts_avlcredempvol_field,
            qts_todayvol_field,
            row[0],
            row[1],
            row[2],
            row[3],
            row[4],
            row[5],
            row[6],
            row[7],
            row[8],
            row[9],
            row[10],
            row[11],
            row[12])
        self.db.Execute(sql,False)

#if __name__ == "__main__":
	#clear = QtsClearingPositionToDB(QTS_CSV_FLAG,'H:/Onuca/backup/exposition.bup')
	#clear.Run()