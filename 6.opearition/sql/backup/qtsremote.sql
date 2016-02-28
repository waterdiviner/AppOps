CREATE TABLE qts_remotes(qts_autoid INT NOT NULL AUTO_INCREMENT,
						qts_key INT NOT NULL,
						qts_localid BIGINT NOT NULL,
						qts_localport INT NOT NULL,
						qts_remoteid BIGINT NOT NULL,
						qts_remoteport INT NOT NULL,
						qts_appid BIGINT NOT NULL,
						qts_apptype INT NOT NULL,
						qts_name CHAR(20) NOT NULL,
						qts_version CHAR(10) NOT NULL,
						qts_mode INT NOT NULL,
						qts_status INT NOT NULL,
						qts_group INT NOT NULL,
						qts_type INT NOT NULL,
						PRIMARY KEY(qts_autoid));
						
ALTER TABLE qts_remotes ADD INDEX qts_remotes_index(qts_key,qts_appid);						