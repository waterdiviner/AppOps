/*##############################################################
#交易帐户。对应的CSV文件是qttrade.acc
#---------------------------------------------------------------
#qts_market				ushort 			帐户所在的市场
#qts_category			ushort			帐户所在的品种
#qts_account			int64			子帐户
#qts_totalamoumt		int64			总的资金
#qts_avlamount			int64			可用资金
#qts_freezeamount		int64			冻结资金
#qts_currency			ushort			币种
#qts_date				int64			日期
##############################################################*/					
CREATE TABLE qts_trade(qts_autoid INT NOT NULL AUTO_INCREMENT,
						qts_market INT NOT NULL,
						qts_category INT NOT NULL,
						qts_account BIGINT NOT NULL,
						qts_totalamount BIGINT NOT NULL,
						qts_avlamount BIGINT NOT NULL,
						qts_freezeamount BIGINT NOT NULL,
						qts_currency INT NOT NULL,
						qts_date BIGINT NOT NULL,
						PRIMARY KEY(qts_autoid));

ALTER TABLE qts_trade ADD INDEX qts_trade_index(qts_market,qts_category,qts_account);	
	
/*##############################################################
#qts_user			uint		用户
#qts_account			int64		子帐户
#qts_viraccount			int64		虚拟帐户，是总帐户对应的唯一值
##############################################################*/		
CREATE TABLE qts_user(qts_autoid INT NOT NULL AUTO_INCREMENT,
						qts_user INT NOT NULL,
						qts_account BIGINT NOT NULL,
						qts_viraccount BIGINT NOT NULL,
						PRIMARY KEY(qts_autoid));

ALTER TABLE qts_user ADD INDEX qts_user_index(qts_user,qts_account,qts_viraccount);
						
/*##############################################################
#qts_market				ushort 			帐户所在的市场
#qts_category			ushort			帐户所在的品种
#qts_viraccount			int64			虚拟帐户，是总帐户对应的唯一值
#qts_relaccount			string			实际的交易所帐户
#qts_sharetag			ushort			是否资金共享标志，同一标志的资金是共享的
#qts_totalamoumt		int64			总的资金
#qts_avlamount			int64			可用资金
#qts_freezeamount		int64			冻结资金
#qts_date				int64			日期
##############################################################*/						
CREATE TABLE qts_exchange(qts_autoid INT NOT NULL AUTO_INCREMENT,
							qts_market INT NOT NULL,
							qts_category INT NOT NULL,
							qts_viraccount BIGINT NOT NULL,
							qts_relaccount CHAR(100) NOT NULL,
							qts_sharetag INT NOT NULL,
							qts_totalamount BIGINT NOT NULL,
							qts_avlamount BIGINT NOT NULL,
							qts_freezeamount BIGINT NOT NULL,
							qts_date BIGINT NOT NULL,
							PRIMARY KEY(qts_autoid));
							
ALTER TABLE qts_exchange ADD INDEX qts_exchange_index(qts_market,qts_category,qts_viraccount);
