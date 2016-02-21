#coding=utf-8
import sys
import time
import csv
import string

################################################################################################
#py库的路径
sys.path.append('../../pylib/utility')
from qtsutility import *
from qtsvar import *

(QTS_HEDGE_ITEM_UNKNOWN,QTS_HEDGE_ITEM_PARA,QTS_HEDGE_ITEM_HOLDING,QTS_HEDGE_ITEM_TRADE)=(0,1,2,3)

################################################################################################
class HedgeCsv(object) :
    def __init__(self,flag,source,target) :
        self.source = csv.reader(open(source,'rb'),delimiter=flag)
        self.target = csv.writer(open(target,'wb'),delimiter=flag,quotechar='\r',quoting=csv.QUOTE_MINIMAL)
		
    def Run(self) :
        type = QTS_HEDGE_ITEM_UNKNOWN
        for row in self.source :
            if len(row) == 0 :
                continue
            elif row[0].startswith('#') :
                continue
            elif row[0].startswith('BEGIN_PARA') :
                type = QTS_HEDGE_ITEM_PARA
                self.target.writerow(['BEGIN_PARA'])
            elif row[0].startswith('END_PARA') :
                type = QTS_HEDGE_ITEM_UNKNOWN
                self.target.writerow(['END_PARA'])
            elif row[0].startswith('BEGIN_HOLDING') :
                type = QTS_HEDGE_ITEM_HOLDING
                self.target.writerow(['BEGIN_HOLDING'])
            elif row[0].startswith('END_HOLDING') :
                type = QTS_HEDGE_ITEM_UNKNOWN
                self.target.writerow(['END_HOLDING'])
            elif row[0].startswith('BEGIN_TRADE') :
                type = QTS_HEDGE_ITEM_TRADE
                self.target.writerow(['BEGIN_TRADE'])
            elif row[0].startswith('END_TRADE') :
                type = QTS_HEDGE_ITEM_UNKNOWN
                self.target.writerow(['END_TRADE'])
            else :
                if type == QTS_HEDGE_ITEM_PARA :
                    self.HandlePara(row)
                elif type == QTS_HEDGE_ITEM_HOLDING :
                    self.HandleHolding(row)
                elif type == QTS_HEDGE_ITEM_TRADE:
                    self.HandleTrade(row)
                else :
                    print('Error type: {0}'.format(row))
	
    def HandlePara(self,row) :
        if string.atoi(row[0]) == 100 :
            self.target.writerow([row[0],CreateCode(GetMarketEnum(row[1].split('.')[1]),GetCategoryEnum(GetMarketEnum(row[1].split('.')[1]),row[1].split('.')[0]),GetSecuCode(GetMarketEnum(row[1].split('.')[1]),row[1].split('.')[0]))])
        elif string.atoi(row[0]) == 101 :
            self.target.writerow([row[0],CreateCode(GetMarketEnum(row[1].split('.')[1]),GetCategoryEnum(GetMarketEnum(row[1].split('.')[1]),row[1].split('.')[0]),GetSecuCode(GetMarketEnum(row[1].split('.')[1]),row[1].split('.')[0]))])
        else :
            self.target.writerow(row)

    def HandleHolding(self,row) :
        self.target.writerow([CreateCode(GetMarketEnum(row[0].split('.')[1]),GetCategoryEnum(GetMarketEnum(row[0].split('.')[1]),row[0].split('.')[0]),GetSecuCode(GetMarketEnum(row[0].split('.')[1]),row[0].split('.')[0])),row[1]])

    def HandleTrade(self,row) :
        self.target.writerow([CreateCode(GetMarketEnum(row[0].split('.')[1]),GetCategoryEnum(GetMarketEnum(row[0].split('.')[1]),row[0].split('.')[0]),GetSecuCode(GetMarketEnum(row[0].split('.')[1]),row[0].split('.')[0])),row[1]])
	
if __name__ == "__main__":
	hedge = HedgeCsv(QTS_CSV_FLAG,'G:/Test/hedgetrademode.csv','G:/Test/hedgetrade.csv',)
	hedge.Run()	