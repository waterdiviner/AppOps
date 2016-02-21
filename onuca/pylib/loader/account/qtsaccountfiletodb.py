#coding=utf-8
from qtsclearingposition import *
sys.path.append('../database')
from qtsmysql import *

class QtsClearingAccountFileToDB(object) :
    def __init__(self,_flag,_source) :
        self.items = dict()
        self.flag = _flag
        self.source = _source
        self.reader = csv.reader(open(self.source,'rb'),delimiter=self.flag)
        self.db = None
        self.table = None

    def Run(self,host,port,user,psw,dbname,dbtable) :
        self.table = dbtable
        self.db = QtsMySql(host,port,user,psw,dbname)
        self.db.Clear(self.table)
        for row in self.reader :
            self.HandleRow(row)
        self.db.Commit()

    def HandleRow(self,row):
        sql = "INSERT INTO {0}({1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11})" \
              " VALUES({12},{13},{14},{15},{16},{17},{18},{19},{20},{21},{22})".format(
            self.table,
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
            row[10])
        self.db.Execute(sql,False)

#if __name__ == "__main__":
	#clear = QtsClearingAccountToDB(QTS_CSV_FLAG,'H:/Onuca/backup/exposition.bup')
	#clear.Run()