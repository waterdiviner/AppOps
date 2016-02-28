CREATE TABLE qts_rights(qts_autoid INT NOT NULL AUTO_INCREMENT,
						qts_id INT NOT NULL,
						qts_target INT NOT NULL,
						qts_type INT NOT NULL,						
						qts_read smallint NOT NULL,	
						qts_insert smallint NOT NULL,	
						qts_delete smallint NOT NULL,	
						qts_update smallint NOT NULL,	
						PRIMARY KEY(qts_autoid));

ALTER TABLE qts_rights ADD UNIQUE(qts_id);
