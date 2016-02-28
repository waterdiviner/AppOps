CREATE TABLE qts_jobs(qts_autoid INT NOT NULL AUTO_INCREMENT,
						qts_id INT NOT NULL,
						qts_name CHAR(40) NULL,
						qts_type INT NOT NULL,						
						qts_path CHAR(255),
						qts_file CHAR(40),
						qts_command CHAR(255),							
						qts_property CHAR(40),
						qts_machineid INT NOT NULL,
						qts_detail CHAR(255),
						PRIMARY KEY(qts_autoid));
					
ALTER TABLE qts_jobs ADD UNIQUE(qts_id);