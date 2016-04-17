#coding=utf-8
from qtsclearingposition import *

class QtsClearingPositionToFile(object) :
    def __init__(self,_flag,_source,_target) :
        self.items = dict()
        self.flag = _flag
        self.source = _source
        self.target = _target
        self.bopen = True
        if os.path.isfile(self.source) :
            self.reader = csv.reader(open(self.source,'rb'),delimiter=self.flag)
        else :
            self.bopen = False
            TraceError('open file {0} is failed!'.format(self.source))
        if self.bopen :
            self.writer = csv.writer(open(self.target,'wb'),delimiter=self.flag)

    def Run(self,date) :
        if self.bopen :
            self.writer.writerow(pos_headers)
            for row in self.reader :
                self.HandleRow(row,date)
            self.Save()
        else :
            TraceError('file is not opened!')

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
        if category == CATEGORY.EQUITY:
            pos_row.append(row[4])
        else :
            pos_row.append(0)
        pos_row.append(0)
        self.items[self.BuildKey(row)] = pos_row

    def Save(self):
        for row in self.items.values() :
            if string.atol(row[6]) != 0 :
                self.writer.writerow(row)

    def BuildKey(self,row) :
        return "{0}-{1}-{2}".format(row[1],row[2],row[3])

if __name__ == "__main__":
    clear = QtsClearingPositionToFile(QTS_CSV_FLAG,'H:/Onuca/backup/exposition.bup','H:/Onuca/backup/exposition.pos')
    clear.Run()