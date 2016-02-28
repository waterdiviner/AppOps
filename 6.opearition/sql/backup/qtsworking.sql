CREATE TABLE qts_workings(qts_autoid INT NOT NULL AUTO_INCREMENT,
						qts_secuid BIGINT NOT NULL,
						qts_strategyid INT NOT NULL,
						qts_code BIGINT NOT NULL,
						qts_action INT NOT NULL,
						qts_workingvol BIGINT NOT NULL,
						qts_workingsize INT NOT NULL,
						qts_ordervol BIGINT NOT NULL,
						qts_ordersize INT NOT NULL,
						qts_cancelvol BIGINT NOT NULL,
						qts_cancelsize INT NOT NULL,
						qts_unackedvol BIGINT NOT NULL,
						qts_unackedsize INT NOT NULL,
						qts_avprice BIGINT NOT NULL,
						qts_amount BIGINT NOT NULL,
						PRIMARY KEY(qts_autoid));
						
ALTER TABLE qts_workings ADD INDEX qts_workings_index(qts_secuid,qts_strategyid,qts_code,qts_action);						