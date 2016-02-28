CREATE TABLE qts_admins(qts_autoid INT NOT NULL AUTO_INCREMENT,
						qts_id INT NOT NULL,
						qts_name CHAR(40) NULL,						
						qts_parentid INT NOT NULL,
						qts_type INT NOT NULL,						
						qts_subtype INT NOT NULL,
						qts_password CHAR(20) NOT NULL,	
						qts_detail CHAR(255),
						PRIMARY KEY(qts_autoid));
					
ALTER TABLE qts_admins ADD UNIQUE(qts_id);
ALTER TABLE qts_admins ADD INDEX qts_admins_index(qts_parentid);