/*##############################################################
#qts_market							ushort					标的所在的市场
#qts_category						ushort					标的所在的品种
#qts_secucode						uint					标的的证券代码
#qts_account						int64					参位所在的帐户
#qts_type							enum					仓位类型，0是长仓，1是短仓
#qts_level							enum					仓位级别，0是子仓位，1是总仓位
#qts_totalvol						int64					总的仓位
#qts_avlvol							int64					可用仓位
#qts_workingvol						int64					在途仓位
#qts_toalcost						int64					总的费用
#qts_qtsdate						int64					仓位日期
#qts_avlcredempvol					int64					可申赎仓位
#qts_todayvol						int64					今日仓位
##############################################################*/					
CREATE TABLE qts_position(qts_autoid INT NOT NULL AUTO_INCREMENT,
							qts_market SMALLINT NOT NULL,
							qts_category SMALLINT NOT NULL,
							qts_secucode INT NOT NULL,
							qts_account BIGINT NOT NULL,
							qts_type INT NOT NULL,
							qts_level INT NOT NULL,
							qts_date BIGINT NOT NULL,
							qts_totalvol BIGINT NOT NULL,
							qts_avlvol BIGINT NOT NULL,
							qts_workingvol BIGINT NOT NULL,
							qts_totalcost BIGINT NOT NULL,
							qts_avlcredempvol BIGINT NOT NULL,
							qts_todayvol BIGINT NOT NULL,
							PRIMARY KEY(qts_autoid));
							
ALTER TABLE qts_position ADD INDEX qts_position_index(qts_market,qts_category,qts_secucode,qts_account,qts_code,qts_type,qts_level);								