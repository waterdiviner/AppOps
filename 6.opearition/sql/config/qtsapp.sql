CREATE TABLE qts_apps(qts_autoid INT NOT NULL AUTO_INCREMENT,
						qts_id BIGINT NOT NULL,
						qts_name CHAR(40) NULL,
						qts_type INT NOT NULL,
						qts_path CHAR(255),
						qts_machineid INT NOT NULL,
						qts_position CHAR(20),
						qts_detail CHAR(255),
						PRIMARY KEY(qts_autoid));
					
ALTER TABLE qts_apps ADD UNIQUE(qts_id);