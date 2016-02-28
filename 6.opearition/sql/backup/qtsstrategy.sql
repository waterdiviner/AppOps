CREATE TABLE qts_strategys(qts_autoid INT NOT NULL AUTO_INCREMENT,
							qts_strategyid INT NOT NULL,
							qts_name CHAR(20) NOT NULL,
							qts_account CHAR(255) NOT NULL,
							qts_minorderid BIGINT NOT NULL,
							qts_maxorderid BIGINT NOT NULL,
							qts_currorderid BIGINT NOT NULL,
							qts_orderidstep BIGINT NOT NULL,
							qts_status INT NOT NULL,
							qts_threadid INT NOT NULL,
							qts_cycle BIGINT NOT NULL,
							qts_tradecycle BIGINT NOT NULL,
							qts_ismanual INT NOT NULL,
							PRIMARY KEY(qts_autoid));
							
ALTER TABLE qts_strategys ADD UNIQUE(qts_strategyid);						