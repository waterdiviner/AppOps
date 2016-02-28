#coding=utf-8
from qtsclearingaccount import *

class QtsClearingAccountToFile(object) :
    def __init__(self,_flag,_source,_target) :
        self.items = dict()
        self.flag = _flag
        self.source = _source
        self.target = _target
        self.reader = csv.reader(open(self.source,'rb'),delimiter=self.flag)
        self.writer = csv.writer(open(self.target,'wb'),delimiter=self.flag)

    def Run(self,date) :
        self.writer.writerow(account_headers)
        for row in self.reader :
            self.HandleRow(row,date)
        self.Save()

    def HandleRow(self,row,date):
        pos_row = list()
        pos_row.append(row[0])
        pos_row.append(row[1])
        pos_row.append(row[2])
        pos_row.append(row[3])
        pos_row.append(row[4])
        pos_row.append(date)
        pos_row.append(row[6])
        pos_row.append(row[7])
        pos_row.append(row[8])
        pos_row.append(row[9])
        pos_row.append(row[10])
        self.items[self.BuildKey(row)] = pos_row

    def Save(self):
        for row in self.items.values() :
            if string.atol(row[3]) != 0 :
                self.writer.writerow(row)

    def BuildKey(self,row) :
        return "{0}-{1}".format(row[1],row[2])

if __name__ == "__main__":
    clear = QtsClearingAccountToFile(QTS_CSV_FLAG,'H:/Onuca/backup/exposition.bup','H:/Onuca/backup/exposition.pos')
    clear.Run()