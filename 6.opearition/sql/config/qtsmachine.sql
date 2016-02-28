CREATE TABLE qts_machines(qts_autoid INT NOT NULL AUTO_INCREMENT,
							qts_id INT NOT NULL,
							qts_name CHAR(40) NOT NULL,
							qts_host CHAR(40) NOT NULL,
							qts_user CHAR(40) NOT NULL,
							qts_password CHAR(20) NOT NULL,	
							qts_type smallint,
						    qts_position CHAR(20),
							qts_detail CHAR(255),
							PRIMARY KEY(qts_autoid));

ALTER TABLE qts_machines ADD UNIQUE(qts_id);