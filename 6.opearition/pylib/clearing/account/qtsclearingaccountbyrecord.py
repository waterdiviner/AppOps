#coding=utf-8
from qtsclearingaccount import *

class QtsClearingAccountByRecord(object) :
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
            self.writer.writerow(account_headers)
            for row in self.reader :
                self.HandleRow(row,date,level)
            self.Save()
        else :
            TraceError('file is not opened!')

    def HandleRow(self,row,date,level):
        pos_row = [0,0,0,0,0,0,0,0,0,0,0]
        pos_row[0] = long(row[0])
        pos_row[1] = long(row[1])
        pos_row[2] = long(row[13]) * long(row[14])
        pos_row[3] = long(row[13]) * long(row[14])
        pos_row[5] = date
        if (int(row[10]) == 6) or (int(row[10]) == 9) :
            if (GetCategoryFromCode(long(row[7])) == CATEGORY.FUTURES_IDX)  or (GetCategoryFromCode(long(row[7])) == CATEGORY.FUTURES):
                if int(row[8]) == 0 :
                    if int(row[23]) == 1 :
                        pos_row[2] *= -1
                        pos_row[3] *= -1
                    else :
                        pass
                else :
                    if int(row[23]) == 1 :
                        pos_row[2] *= -1
                        pos_row[3] *= -1
                    else :
                        pass
            else :
                if int(row[8]) == 0 :
                    pos_row[2] *= -1
                    pos_row[3] *= -1
                else :
                    pass
            self.UpdateRow(pos_row)

    def UpdateRow(self,up_row):
        pos_row = self.GetRow(up_row[0],up_row[1])
        if pos_row == None :
            pos_row = up_row
        else :
            pos_row[2] += up_row[2]
            pos_row[3] += up_row[3]
        self.items[self.BuildKey(up_row[0],up_row[1])] = pos_row

    def Save(self):
        for row in self.items.values() :
            if row[2] != 0 :
                self.writer.writerow(row)

    def BuildKey(self,secuid,account) :
        return "{0}-{1}".format(secuid,account)

    def GetRow(self,secuid,account):
        try :
            return self.items[self.BuildKey(secuid,account)]
        except :
            return None

if __name__ == "__main__":
    clear = QtsClearingPositionByRecord(QTS_CSV_FLAG,'H:/Onuca/backup/exposition.bup','H:/Onuca/backup/exposition.pos')
    clear.Run()