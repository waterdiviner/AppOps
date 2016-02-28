CREATE TABLE qts_strategyinapp(qts_autoid INT NOT NULL AUTO_INCREMENT,
							qts_appid INT NOT NULL,
							qts_strategyid INT NOT NULL,
							PRIMARY KEY(qts_autoid));
							
ALTER TABLE qts_strategyinapp ADD INDEX qts_strategyinapp_index(qts_appid,qts_strategyid);	