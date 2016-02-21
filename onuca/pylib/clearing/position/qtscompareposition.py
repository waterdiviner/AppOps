#coding=utf-8
from qtsclearingposition import *

class QtsComparePosition(object) :
    def __init__(self,_flag,_source,_target) :
        self.sitems = dict()
        self.titems = dict()
        self.flag = _flag
        self.source = _source
        self.target = _target
        self.sreader = csv.reader(open(self.source,'rb'),delimiter=self.flag)
        self.treader = csv.reader(open(self.target,'rb'),delimiter=self.flag)

    def Load(self,reader,items) :
        first = True
        for row in reader :
            if row[0][0].strip() == '#' :
                continue
            if first == False :
                self.HandleRow(row,items)
            first = False

    def HandleRow(self,row,items) :
        pos_row = list()
        pos_row.append(row[1].strip())
        market = GetMarketFromCode(string.atol(row[2].strip()))
        category = GetCategoryFromCode(string.atol(row[2].strip()))
        secucode = GetSecuCodeFromCode(string.atol(row[2].strip()))
        pos_row.append(market)
        pos_row.append(category)
        pos_row.append(secucode)
        pos_row.append(row[3].strip())
        pos_row.append(row[8].strip())
        pos_row.append(row[4].strip())
        pos_row.append(row[5].strip())
        pos_row.append(row[6].strip())
        pos_row.append(row[7].strip())
        pos_row.append(row[9].strip())
        if category == EQUIT_CATEGORY:
            pos_row.append(row[4].strip())
        else :
            pos_row.append(0)
        pos_row.append(0)
        items[self.BuildKey(row)] = pos_row

    def BuildKey(self,row) :
        return "{0}-{1}-{2}".format(row[1].strip(),row[2].strip(),row[3].strip())

    def Compare(self) :
        bresult = True
        line = 1
        for key in self.sitems.keys() :
            if not self.CompareItem(key,line) :
                bresult = False
            line = line + 1
        return bresult

    def CompareItem(self,key,line) :
        bresult = False
        if not self.ExistItem(key,self.titems) :
            print('source line {0}: {1} is not exist in target file {2}'.format(line,key,self.target))
        else :
            svalue = self.sitems[key]
            tvalue = self.titems[key]
            bresult = self.CompareValues(svalue,tvalue,line)
        return bresult

    def CompareValues(self,svalue,tvalue,line) :
        bresult = True
        if len(svalue) != len(tvalue) :
            print('source line {0}: {1} is not equal size'.format(line,key))
            bresult = False
        else :
            col = 1
            for i in range(0,len(svalue)) :
                if svalue[i] != tvalue[i] :
                    print('source line {0}: {1} is not equal'.format(line,col))
                    col = col + 1
                    bresult = False
                    break
        return bresult

    def ExistItem(self,key,items) :
        item = None
        try:
            item = items[key]
        except Exception,e:
            item = None
        return item != None

    def Run(self) :
        self.Load(self.sreader,self.sitems)
        self.Load(self.treader,self.titems)
        if self.Compare() :
            print('compare finish,file is equal!')
        else :
            print('compare finish,file is not equal!')

if __name__ == "__main__":
    compare = QtsComparePosition(QTS_CSV_FLAG,'E:/QTS/2.other/data/loader/qtsexposition.pos','E:/QTS/2.other/data/loader/qtsexposition.pos')
    compare.Run()