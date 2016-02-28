/*##############################################################
#证券信息的静态数据表，这是主要数据列，可以根据需要在后面添加列，
#但不能在头或中间插入数据。列名称必须是唯一的，这个会被程序作为
#访问的键值。对应的CSV文件是qtsinfo_s.info
#---------------------------------------------------------------
#qts_market  					ushort		标的所在的市场
#qts_category					ushort		标的所在的品种
#qts_secucode					uint		标的的证券代码
#qts_ordercode					string		标的的交易代码，可以加一个@带标记
#qts_marketname					string		标的的市场名称
#qts_categoryname				string		标的的品种名称
#qts_secuname					string		标的的证券名称
#qts_minorderqty				int64		标的的最小订单量
#qts_maxorderqty				int64		标的的最大订单量
#qts_pricetick					int64		标的的最小报价差
#qts_tradetype					enum		标的的清算类型，0是T+0、1是T+1，2是T+2，3是未知
#qts_postype					enum		标的的仓位类型，0是长仓，1是短仓，2是双向仓
#qts_multipler					INT			标的的价格乘数
#qts_margin						INT			标的的保证金比例，乘100后的值
##############################################################*/
CREATE TABLE qts_secuinfo_s(qts_autoid INT NOT NULL AUTO_INCREMENT,
							qts_market INT NOT NULL,
							qts_category INT NOT NULL,
							qts_secucode INT NOT NULL,
							qts_ordercode  CHAR(50) NOT NULL,
							qts_marketname CHAR(40) NOT NULL,
							qts_categoryname CHAR(40) NOT NULL,
							qts_secuname CHAR(40) NOT NULL,
							qts_minorderqty BIGINT NOT NULL,
							qts_maxorderqty BIGINT NOT NULL,
							qts_pricetick INT NOT NULL,
							qts_tradetn INT NOT NULL,
							qts_posmode INT NOT NULL,
							qts_multipler INT NOT NULL,
							qts_margin INT NOT NULL,
							qts_currency CHAR(10), 
							qts_expiry CHAR(10),  
							qts_right CHAR(10), 
							qts_strike CHAR(10), 
							qts_tradingclass CHAR(10),
							PRIMARY KEY(qts_autoid));

ALTER TABLE qts_secuinfo_s ADD INDEX qts_secuinfo_s_index(qts_market,qts_category,qts_secucode);	
							
/*##############################################################
#证券信息的动态数据表，这是主要数据列，可以根据需要在后面添加列，
#但不能在头或中间插入数据。列名称必须是唯一的，这个会被程序作为
#访问的键值。对应的CSV文件是qtsinfo_d.info
#---------------------------------------------------------------
#qts_market  					ushort		标的所在的市场
#qts_category					ushort		标的所在的品种
#qts_secucode					uint		标的的证券代码
#qts_lastprice					int64		标的昨手收价格，乘以10000
#qts_lolimitedprice				int64		标的的跌停价格，乘以10000
#qts_uplimitedprice				int64		标的的涨停价格，乘以10000
#qts_suspension					enum		标的的停牌类型,0是昨日停牌，1是今日停牌，2是未停牌，3是未知
#qts_tradingfee					string		标的的交易费用
##############################################################*/
CREATE TABLE qts_secuinfo_d(qts_autoid INT NOT NULL AUTO_INCREMENT,
							qts_market INT NOT NULL,
							qts_category INT NOT NULL,
							qts_secucode INT NOT NULL,	
							qts_lastprice BIGINT NOT NULL,
							qts_lolimitprice BIGINT NOT NULL,
							qts_uplimitprice BIGINT NOT NULL,
							qts_suspension INT NOT NULL,
							qts_tradingfee CHAR(255),
							PRIMARY KEY(qts_autoid));
							
ALTER TABLE qts_secuinfo_d ADD INDEX qts_secuinfo_d_index(qts_market,qts_category,qts_secucode);
							
