#coding=utf-8
from qtsclearingposition import *
sys.path.append('../database')
from qtsmysql import *

class QtsClearingPositionToDB(object) :
    def __init__(self,_flag,_source) :
        self.items = dict()
        self.flag = _flag
        self.source = _source
        self.reader = csv.reader(open(self.source,'rb'),delimiter=self.flag)
        self.db = None
        self.table = None

    def Run(self,host,port,user,psw,dbname,dbtable,date) :
        self.table = dbtable
        self.db = QtsMySql(host,port,user,psw,dbname)
        self.db.Clear(self.table)
        for row in self.reader :
            self.HandleRow(row,date)
        self.Save()
        self.db.Commit()

    def HandleRow(self,row,date):
        pos_row = list()
        pos_row.append(row[1])
        market = GetMarketFromCode(string.atol(row[2]))
        category = GetCategoryFromCode(string.atol(row[2]))
        secucode = GetSecuCodeFromCode(string.atol(row[2]))
        pos_row.append(market)
        pos_row.append(category)
        pos_row.append(secucode)
        pos_row.append(row[3])
        pos_row.append(row[8])
        pos_row.append(row[4])
        pos_row.append(row[5])
        pos_row.append(row[6])
        pos_row.append(row[7])
        pos_row.append(date)
        if category == EQUIT_CATEGORY:
            pos_row.append(row[4])
        else :
            pos_row.append(0)
        pos_row.append(0)
        self.items[self.BuildKey(row)] = pos_row

    def Save(self):
        for row in self.items.values() :
            if string.atol(row[6]) != 0 :
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

    def BuildKey(self,row) :
        return "{0}-{1}-{2}".format(row[1],row[2],row[3])

#if __name__ == "__main__":
	#clear = QtsClearingPositionToDB(QTS_CSV_FLAG,'H:/Onuca/backup/exposition.bup')
	#clear.Run()