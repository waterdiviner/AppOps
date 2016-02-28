CREATE TABLE qts_positions(qts_autoid INT NOT NULL AUTO_INCREMENT,
							qts_secuid BIGINT NOT NULL,
							qts_account BIGINT NOT NULL,
							qts_code BIGINT NOT NULL,
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
							
ALTER TABLE qts_positions ADD INDEX qts_positions_index(qts_secuid,qts_account,qts_code,qts_type,qts_level);							