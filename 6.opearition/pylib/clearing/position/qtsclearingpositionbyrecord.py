#coding=utf-8
from qtsclearingposition import *

class QtsClearingPositionByRecord(object) :
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

    def Run(self,level,date) :
        if self.bopen :
            self.writer.writerow(pos_headers)
            for row in self.reader :
                self.HandleRow(row,level,date)
            self.Save()
        else :
            TraceError('file is not opened!')

    def HandleRow(self,row,level,date):
        pos_row = [0,0,0,0,0,0,0,0,0,0,0,0,0]
        pos_row[0] = long(row[1])
        pos_row[1] = GetMarketFromCode(long(row[7]))
        pos_row[2] = GetCategoryFromCode(long(row[7]))
        pos_row[3] = GetSecuCodeFromCode(long(row[7]))
        pos_row[5] = level
        pos_row[6] = long(row[14])
        pos_row[7] = long(row[14])
        pos_row[10] = date
        if (int(row[10]) == 6) or (int(row[10]) == 9) :
            if (GetCategoryFromCode(long(row[7])) == CATEGORY.FUTURES_IDX)  or (GetCategoryFromCode(long(row[7])) == CATEGORY.FUTURES) :
                if int(row[8]) == 0 :
                    if int(row[23]) == 1 :
                        pos_row[4] = 0
                    else :
                        pos_row[4] = 1
                        pos_row[6] *= -1
                        pos_row[7] *= -1
                        pos_row[11] *= -1
                else :
                    if int(row[23]) == 1 :
                        pos_row[4] = 1
                    else :
                        pos_row[4] = 0
                        pos_row[6] *= -1
                        pos_row[7] *= -1
                        pos_row[11] *= -1
            else :
                pos_row[4] = 0
                pos_row[11] = pos_row[6]
                if int(row[8]) == 1 :
                    pos_row[6] *= -1
                    pos_row[7] *= -1
                    pos_row[11] *= -1
            self.UpdateRow(pos_row)

    def UpdateRow(self,up_row):
        pos_row = self.GetRow(up_row[0],up_row[1],up_row[2],up_row[4])
        if pos_row == None :
            pos_row = up_row
        else :
            pos_row[6] += up_row[6]
            pos_row[7] += up_row[7]
            pos_row[11] += up_row[11]
        self.items[self.BuildKey(up_row[0],up_row[1],up_row[2],up_row[4])] = pos_row

    def Save(self):
        for row in self.items.values() :
            if row[6] != 0 :
                self.writer.writerow(row)

    def BuildKey(self,account,market,category,type) :
        return "{0}-{1}-{2}-{3}".format(account,market,category,type)

    def GetRow(self,account,market,category,type):
        try :
            return self.items[self.BuildKey(account,market,category,type)]
        except :
            return None

if __name__ == "__main__":
    clear = QtsClearingPositionByRecord(QTS_CSV_FLAG,'H:/Onuca/backup/exposition.bup','H:/Onuca/backup/exposition.pos')
    clear.Run()