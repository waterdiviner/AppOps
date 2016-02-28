#coding=utf-8
import time
import string
import os
import sys
import csv

sys.path.append('../utility')
from qtsvar import *
from qtsgproto_pb2 import *
from qtsbiz import *

static_secuinfo_headers = [qts_market_field, qts_category_field, qts_secucode_field, qts_ordercode_field, qts_marketname_field, qts_categoryname_field, 
qts_secuname_field, qts_minorderqty_field, qts_maxorderqty_field, qts_pricetick_field, qts_tradetn_field, qts_posmode_field, qts_multipler_field, qts_margin_field,
qts_currency_field,qts_expiry_field,qts_right_field,qts_strike_field,qts_tradingclass_field]
dynamic_secuinfo_headers = [qts_market_field, qts_category_field, qts_secucode_field, qts_lastprice_field, qts_settlementprice_field, qts_lolimitedprice_field,
qts_uplimitedprice_field,  qts_suspension_field, qts_tradingfee_field]

qts_sz_filters=['00','30','39']
qts_sh_filters=['00','60','51','99']

#####################################################################################################################################################
class QtsSecuinfoConvert(object) :
    def PriceTick(self,market,tick) :
        if tick != 0 :
            return tick
        if (market == SZ_MARKET) or (market == SH_MARKET) :
            tick = 100
        elif market == ZJ_MARKET :
            tick = 2000
        return tick

    def MarginRate(self,market,rate) :
        if rate != 0 :
            return rate
        if (market == SZ_MARKET) or (market == SH_MARKET) :
            rate = 100
        elif market == ZJ_MARKET :
            rate = 15
        return rate

    def FilterCode(self,market,ordercode) :
        bfilter = True
        if market == SZ_MARKET :
            if ordercode[0:2] in qts_sz_filters :
                bfilter = False
        elif market == SH_MARKET :
            if ordercode[0:2] in qts_sh_filters  :
                bfilter = False
        else :
            bfilter = False
        return bfilter

    def ConvertCode(self,market,ordercode) :
        #return ConvertOrderCode(market,ordercode)
        return ordercode

    def HandleRow(self,row):
        if not IsValidOrderCode(row[1],row[0]) :
            return False
        static_row = list()
        dynamic_row = list()
        market = GetMarketEnum(row[1])
        category = GetCategoryEnum(market,row[0])
        ordercode = self.ConvertCode(market,row[0])
        secucode = GetSecuCode(market,ordercode)
        if self.FilterCode(market,ordercode) :
            return False
        if not IsDigit(secucode) :
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

