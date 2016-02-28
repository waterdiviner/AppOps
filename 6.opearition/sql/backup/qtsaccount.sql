CREATE TABLE qts_accounts(qts_autoid INT NOT NULL AUTO_INCREMENT,
						 qts_secuid BIGINT NOT NULL,
						 qts_account BIGINT NOT NULL,
						 qts_totalamount BIGINT NOT NULL,
						 qts_avlamount BIGINT NOT NULL,
						 qts_freezeamount BIGINT NOT NULL,
						 qts_date BIGINT NOT NULL,
						 qts_currency INT NOT NULL,
						 qts_user INT NOT NULL,
						 qts_sharetag INT NOT NULL,
						 qts_level INT NOT NULL,
						 qts_viraccount BIGINT NOT NULL,
						 PRIMARY KEY(qts_autoid));
						 
ALTER TABLE qts_accounts ADD UNIQUE(qts_account);
ALTER TABLE qts_accounts ADD INDEX qts_accounts_index(qts_secuid,qts_user,qts_viraccount);						 