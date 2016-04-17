#coding=utf-8
import time
import string
import os
import sys
import csv

sys.path.append(os.path.join(os.getenv('QTS_BASE_PATH','../..'),'pylib/utility'))
from qtsvar import *
try :
    from qtsgproto_pb2 import *
except :
    print('warning>> python lib no support protocol buffer')
from qtsbizfun import *

static_secuinfo_headers = [qts_market_field, qts_category_field, qts_secucode_field, qts_ordercode_field, qts_marketname_field, qts_categoryname_field, 
qts_secuname_field, qts_minorderqty_field, qts_maxorderqty_field, qts_pricetick_field, qts_tradetn_field, qts_posmode_field, qts_multipler_field, qts_margin_field,
qts_currency_field,qts_expiry_field,qts_right_field,qts_strike_field,qts_tradingclass_field]
dynamic_secuinfo_headers = [qts_market_field, qts_category_field, qts_secucode_field, qts_lastprice_field, qts_settlementprice_field, qts_lolimitedprice_field,
qts_uplimitedprice_field,  qts_suspension_field, qts_tradingfee_field]

qts_sz_filters=['00','30','39']
qts_sh_filters=['00','60','51','99']

#####################################################################################################################################################
class QtsSecuinfo(object) :
    def __init__(self,_sfile,_dfile,_flag):
        self.flag = _flag
        self.bopen = True
        self.sfile = _sfile
        self.dfile = _dfile
        self.items = dict()
        self.heads = dict()
        if os.path.isfile(self.sfile) :
            self.sreader = csv.reader(open(self.sfile,'rb'),delimiter=self.flag)
        else :
            self.bopen = False
            TraceError('open file {0} is failed!'.format(self.sfile))
        if os.path.isfile(self.dfile) :
            self.dreader = csv.reader(open(self.dfile,'rb'),delimiter=self.flag)
        else :
            self.bopen = False
            TraceError('open file {0} is failed!'.format(self.dfile))
        if self.bopen :
            self.Load()

    @property
    def Heads(self):
        return self.heads

    @property
    def Items(self):
        return self.items

    def Load(self):
        s_size = 0
        d_size = 0
        s_size = self.LoadStaticHeads(0)
        d_size = self.LoadDynamicHeads(s_size)
        self.LoadStaticItems(s_size)
        self.LoadDynamicItems(d_size)

    def LoadStaticHeads(self,index):
        col = index
        size = 0
        for row in self.sreader :
            if len(row) == 0 :
                continue
            if row[0] == '#' :
                continue
            for field in row :
                self.heads[field] = col
                col += 1
                size += 1
            break
        return size

    def LoadDynamicHeads(self,index):
        col = index
        size = 0
        for row in self.dreader :
            if len(row) == 0 :
                continue
            if row[0] == '#' :
                continue
            for field in row :
                if self.GetField(field) == None :
                    self.heads[field] = col
                    col += 1
                    size += 1
            break
        return size

    def LoadStaticItems(self,size):
        line = 0
        row_size = 0
        for row in self.sreader :
            if len(row) == 0 :
                continue
            if row[0] == '#' :
                continue
            if line == 0 :
                line += 1
                continue
            row_size = len(row)
            while row_size < size :
                row.append(0)
                row_size += 1
            self.items[self.BuildKey(row[0],row[1],row[2])] = row

    def LoadDynamicItems(self,size):
        line = 0
        row_size = 0
        for row in self.dreader :
            if len(row) == 0 :
                continue
            if row[0] == '#' :
                continue
            if line == 0 :
                line += 1
                continue
            row_size = len(row)
            while row_size < size :
                row.append(0)
                row_size += 1
            item = self.GetItem(row[0],row[1],row[2])
            if item != None :
                self.items[self.BuildKey(row[0],row[1],row[2])] = item + row[3:]

    def BuildKey(self,market,category,secucode):
        return '{0}-{1}-{2}'.format(market.strip(' \t ').strip(),
                                    category.strip(' \t ').strip(),
                                    secucode.strip(' \t ').strip())

    def GetItem(self,market,category,secucode):
        if not self.bopen :
            return None
        try :
            return self.items[self.BuildKey(str(market),str(category),str(secucode))]
        except :
            return None

    def Find(self,market,category,ordercode):
        if self.bopen :
            return self.GetItem(market,category,GetSecuCode(market,ordercode))
        else :
            return None

    def GetField(self,field):
        if not self.bopen :
            return None
        try :
            return self.heads[field]
        except :
            return None

    def Field(self,item,field):
        index = self.GetField(field)
        if index != None :
            if len(item) > index :
                return item[index]
        return None

    def FieldValue(self,market,category,ordercode,field):
        item = self.Find(market,category,ordercode)
        if item != None :
            return self.Field(item,field)
        return None

    def ToString(self,market,category,ordercode):
        item_str = ''
        item = self.Find(market,category,ordercode)
        if item != None :
            for field,index in self.heads.iteritems() :
                if len(item) > index :
                    if field == qts_tradetn_field :
                        item_str += '{0}={1}\r\n'.format(field,GetTradeStr(string.atoi(item[index])))
                    elif field == qts_posmode_field :
                        item_str += '{0}={1}\r\n'.format(field,GetPositionModeStr(string.atoi(item[index])))
                    elif field == qts_suspension_field :
                        item_str += '{0}={1}\r\n'.format(field,GetSuspensionStr(string.atoi(item[index])))
                    else :
                        item_str += '{0}={1}\r\n'.format(field,item[index])
        return item_str

#####################################################################################################################################################
class QtsSecuinfoConvert(object) :
    def PriceTick(self,market,tick) :
        if tick != 0 :
            return tick
        if (market == MARKET.SZSE) or (market == MARKET.SSE) :
            tick = 100
        elif market == MARKET.CFFEX :
            tick = 2000
        return tick

    def MarginRate(self,market,rate) :
        if rate != 0 :
            return rate
        if (market == MARKET.SZSE) or (market == MARKET.SSE) :
            rate = 100
        elif market == MARKET.CFFEX :
            rate = 15
        return rate

    def FilterCode(self,market,ordercode) :
        bfilter = True
        if market == MARKET.SZSE :
            if ordercode[0:2] in qts_sz_filters :
                bfilter = False
        elif market == MARKET.SSE :
            if ordercode[0:2] in qts_sh_filters  :
                bfilter = False
        else :
            bfilter = False
        return bfilter

    def ConvertCode(self,market,ordercode) :
        #return ConvertOrderCode(market,ordercode)
        return ordercode

    def FilterMarket(self,market):
        if market == 'SZE' :
            return 'SZSE'
        else:
            return market

    def HandleRow(self,row):
        if not IsValidOrderCode(self.FilterMarket(row[1]),row[0]) :
            return False
        static_row = list()
        dynamic_row = list()
        market = GetMarketEnum(self.FilterMarket(row[1]))
        category = GetCategoryEnum(market,row[0])
        ordercode = self.ConvertCode(market,row[0])
        secucode = GetSecuCode(market,ordercode)
        if self.FilterCode(market,ordercode) :
            return False
        if not QtsMath.IsDigit(secucode) :
            return False
        if secucode == 0 :
            return False
        static_row.append(market)
        static_row.append(category)
        static_row.append(secucode)
        static_row.append(ordercode)
        static_row.append(GetMarketStr(market))
        static_row.append(GetCategoryStr(category))
        static_row.append(row[2])
        static_row.append(row[6])
        static_row.append(row[7])
        static_row.append(self.PriceTick(market,GetSystemPrice(string.atof(row[5]))))
        static_row.append(row[9])
        static_row.append(row[10])
        static_row.append(row[4])
        static_row.append(self.MarginRate(market,0))
        dynamic_row.append(market)
        dynamic_row.append(category)
        dynamic_row.append(secucode)
        dynamic_row.append(GetSystemPrice(string.atof(row[14])))
        dynamic_row.append(GetSystemPrice(string.atof(row[13])))
        dynamic_row.append(GetSystemPrice(string.atof(row[15])))
        dynamic_row.append(GetSystemPrice(string.atof(row[16])))
        dynamic_row.append(row[8])
        dynamic_row.append(0)
        self.HandleStaticRow(static_row)
        self.HandleDynamicRow(dynamic_row)
        return True

    def HandleStaticRow(self,static_row):pass
    def HandleDynamicRow(self,dynamic_row):pass

