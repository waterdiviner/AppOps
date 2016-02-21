#coding=utf-8
import sys
import os
import datetime
import csv
import string
from md_query import QtsMDQuery

sys.path.append('../../pylib/utility')
from qtsfun import *

market_str={1:'SZSE',2:'SHSE',3:'CFFEX'}

def Download_DataByCsv(_get_data,_date,file) :
    reader = csv.reader(open(file,'rb'),delimiter=',')
    first=True
    for row in reader :
        if first :
            first = False
            continue
        else :
            _get_data.GetData(market_str[string.atoi(row[0])],row[3],'{0}-{1}-{2}'.format(_date.year,Format_Date(_date.month),Format_Date(_date.day)))

def Format_SecuCode(_prefix,_date) :
    return '{0}{1}{2}'.format(_prefix,str(_date.year)[2:4],Format_Date(_date.month))

def Download_DataByCal(_get_data,_date,_prefix) :
    d1 = _date
    d2 = AddMonth(d1,1)
    d3 = AddMonth(d2,3)
    d4 = AddMonth(d3,3)
    _get_data.GetData(market_str[3],Format_SecuCode(_prefix,d1),'{0}-{1}-{2}'.format(d1.year,Format_Date(d1.month),Format_Date(d1.day)))
    _get_data.GetData(market_str[3],Format_SecuCode(_prefix,d2),'{0}-{1}-{2}'.format(d2.year,Format_Date(d2.month),Format_Date(d2.day)))
    _get_data.GetData(market_str[3],Format_SecuCode(_prefix,d3),'{0}-{1}-{2}'.format(d3.year,Format_Date(d3.month),Format_Date(d3.day)))
    _get_data.GetData(market_str[3],Format_SecuCode(_prefix,d4),'{0}-{1}-{2}'.format(d4.year,Format_Date(d4.month),Format_Date(d4.day)))

def Download_DataByFuture(_get_data,_date) :
    Download_DataByCal(_get_data,_date,'IF')
    Download_DataByCal(_get_data,_date,'IC')
    Download_DataByCal(_get_data,_date,'IH')

def Download_DataByIndex(_get_data,_date) :
    _get_data.GetData(market_str[2],'000300','{0}-{1}-{2}'.format(_date.year,Format_Date(_date.month),Format_Date(_date.day)))
    _get_data.GetData(market_str[2],'000016','{0}-{1}-{2}'.format(_date.year,Format_Date(_date.month),Format_Date(_date.day)))
    _get_data.GetData(market_str[2],'000998','{0}-{1}-{2}'.format(_date.year,Format_Date(_date.month),Format_Date(_date.day)))

def Format_Date(_date) :
    if _date < 10 :
        return "0{0}".format(_date)
    else :
        return "{0}".format(_date)

def Download_ByDate(_get_data,_start,_end,_step,file) :
    curr = _start
    while (curr < _end) :
        if curr.weekday() != 5 and curr.weekday() != 6 :
            #Download_DataByCsv(_get_data,curr,file)
            Download_DataByIndex(_get_data,curr)
            Download_DataByFuture(_get_data,curr)
        curr += _step

def Main() :
    _get_data = QtsMDQuery()
    start = datetime.date(2015,10,01)
    end = datetime.date(2015,10,30)
    step = datetime.timedelta(days=1)
    Download_ByDate(_get_data,start,end,step,'qtsinfo_s.info')

if __name__ == "__main__":	
    Main()