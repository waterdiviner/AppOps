CREATE TABLE qts_parameters(qts_autoid INT NOT NULL AUTO_INCREMENT,
							qts_strategyid INT NOT NULL,
							qts_key INT NOT NULL, 
							qts_name CHAR(20) NOT NULL,
							qts_value BIGINT NOT NULL,
							qts_type INT NOT NULL,
							qts_level INT NOT NULL,
							qts_decimal INT NOT NULL,
							qts_status INT NOT NULL,
							qts_mode INT NOT NULL,
							qts_style CHAR(255),
							qts_component CHAR(255),
							qts_index INT NOT NULL,
							PRIMARY KEY(qts_autoid));
							
ALTER TABLE qts_parameters	ADD	UNIQUE(qts_key);
ALTER TABLE qts_parameters ADD INDEX qts_parameters_index(qts_strategyid);