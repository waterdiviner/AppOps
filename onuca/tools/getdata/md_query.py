#coding=utf-8
import sys
sys.path.append('../../pylib/database')
import time
import string
from gmsdk import md
from qtsmarket import QtsSqliteMarket

class QtsMDQuery(QtsSqliteMarket) :
    def __init__(self):
        self.btime = '09:00:00'
        self.etime = '15:30:00'
        self.user = 'jack.lxd@gmail.com'
        self.password = '12345678'
        self.connected = self.TickInit()

    def TickInit(self) :
        print('start reg')
        if md.init(self.user, self.password) :
            print('end reg, connect successed!')
            return True
        else :
            print('end reg, connect failed!')
            return False

    def GetTicks(self) :
        _order_code = '{0}.{1}'.format(self.market,self.code)
        _begin_time = '{0} {1}'.format(self.date,self.btime)
        _end_time = '{0} {1}'.format(self.date,self.etime)
        print('start get tick data {0} {1} {2}'.format(_order_code,_begin_time,_end_time))
        data = md.get_ticks(_order_code,_begin_time,_end_time)
        print('end get tick data,data size: ', len(data))
        return data

    def BuildSql(self,index,tick) :
        bidvalues=''
        askvalues=''
        if self.IsValidAskAndBid(tick.asks,tick.bids) :
            for i in range(0,len(tick.asks)) :
                if bidvalues == '' :
                    bidvalues = "{0}:{1}".format(self.RoundPrice(tick.bids[i][0]),tick.bids[i][1])
                else :
                    bidvalues = "{0};{1}:{2}".format(bidvalues,self.RoundPrice(tick.bids[i][0]),tick.bids[i][1])
                if askvalues == '' :
                    askvalues = "{0}:{1}".format(self.RoundPrice(tick.asks[i][0]),tick.asks[i][1])
                else :
                    askvalues = "{0};{1}:{2}".format(askvalues,self.RoundPrice(tick.asks[i][0]),tick.asks[i][1])
        _values = "'{0}','{1}',{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12},{13},{14},{15},{16}".format(
                        self.market,
                        self.ConvertIndex(tick.sec_id),
                        self.UtcToLocal(tick.utc_time),
                        self.RoundPrice(tick.last_price),
                        self.RoundPrice(tick.open),
                        self.RoundPrice(tick.high),
                        self.RoundPrice(tick.low),
                        tick.cum_volume,
                        tick.cum_amount,
                        tick.cum_position,
                        tick.last_amount,
                        tick.last_volume,
                        self.RoundPrice(tick.upper_limit),
                        self.RoundPrice(tick.lower_limit),
                        self.RoundPrice(tick.settle_price),
                        tick.trade_type,
                        self.RoundPrice(tick.pre_close))
        return ("insert into mkdata values({0},{1},{2},'{3}','{4}')").format(index,self.BuildTime(tick.utc_time),_values,askvalues,bidvalues)

    def HandleData(self,data) :
        if len(data) > 0 :
            print('start save db')
            self.Open()
            index = 0
            for tick in data :
                _sql = self.BuildSql(index,tick)
                self.cursor.execute(_sql)
                index = index + 1
            self.Close()
            print('end save db')

    def GetData(self,_market,_code,_date,_path='') :
        if not self.connected :
            return
        print('download {0}.{1} {2}'.format(_market,_code,_date))
        self.market = _market
        self.code = _code
        self.date = _date
        if _path == '' :
            self.path = 'F:/market/{0}'.format(_date.replace('-','/'))
        else :
            self.path = _path
        self.HandleData(self.GetTicks())		
