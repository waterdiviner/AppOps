CREATE TABLE qts_strategyinproduct(qts_autoid INT NOT NULL AUTO_INCREMENT,
							qts_productid INT NOT NULL,
							qts_strategyid INT NOT NULL,
							PRIMARY KEY(qts_autoid));
							
ALTER TABLE qts_strategyinproduct ADD INDEX qts_strategyinproduct_index(qts_productid,qts_strategyid);	