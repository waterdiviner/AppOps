drop database qts_gw_backup;
create database qts_gw_backup;
use qts_gw_backup;

CREATE TABLE qts_accounts(qts_autoid INT NOT NULL AUTO_INCREMENT,
						 qts_secuid BIGINT NOT NULL,
						 qts_account BIGINT NOT NULL,
						 qts_totalamount BIGINT NOT NULL,
						 qts_avlamount BIGINT NOT NULL,
						 qts_freezeamount BIGINT NOT NULL,
						 qts_date BIGINT NOT NULL,
						 qts_currency INT NOT NULL,
						 qts_user INT NOT NULL,
						 qts_sharetag INT NOT NULL,
						 qts_level INT NOT NULL,
						 qts_viraccount BIGINT NOT NULL,
						 PRIMARY KEY(qts_autoid));
						 
ALTER TABLE qts_accounts ADD UNIQUE(qts_account);
ALTER TABLE qts_accounts ADD INDEX qts_accounts_index(qts_secuid,qts_user,qts_viraccount);						 

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

CREATE TABLE qts_records(qts_autoid INT NOT NULL AUTO_INCREMENT,
						qts_secuid BIGINT NOT NULL,
						qts_account BIGINT NOT NULL,
						qts_strategyid INT NOT NULL,
						qts_orderid BIGINT NOT NULL,
						qts_algoid BIGINT NOT NULL,
						qts_algoindex BIGINT NOT NULL,
						qts_parentid BIGINT NOT NULL,
						qts_code BIGINT NOT NULL,
						qts_action INT NOT NULL,
						qts_paction INT NOT NULL,
						qts_status INT NOT NULL,
						qts_prevstatus INT NOT NULL,
						qts_oprice BIGINT NOT NULL,
						qts_iprice BIGINT NOT NULL,
						qts_ovolume BIGINT NOT NULL,
						qts_ivolume BIGINT NOT NULL,
						qts_otime BIGINT NOT NULL,
						qts_itime BIGINT NOT NULL,
						qts_property INT NOT NULL,
						qts_direction INT NOT NULL,
						qts_canceled INT NOT NULL,
						qts_userid INT NOT NULL,
						qts_refid BIGINT NOT NULL,
						qts_sessionid INT NOT NULL,
						qts_source INT NOT NULL,
						qts_ss INT NOT NULL,
						qts_gw INT NOT NULL,						
						PRIMARY KEY(qts_autoid));
						
ALTER TABLE qts_records	ADD	UNIQUE(qts_orderid);
ALTER TABLE qts_records ADD INDEX qts_records_index(qts_account,qts_algoid,qts_parentid);

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


drop database qts_ss_backup;
create database qts_ss_backup;
use qts_ss_backup;

CREATE TABLE qts_accounts(qts_autoid INT NOT NULL AUTO_INCREMENT,
						 qts_secuid BIGINT NOT NULL,
						 qts_account BIGINT NOT NULL,
						 qts_totalamount BIGINT NOT NULL,
						 qts_avlamount BIGINT NOT NULL,
						 qts_freezeamount BIGINT NOT NULL,
						 qts_date BIGINT NOT NULL,
						 qts_currency INT NOT NULL,
						 qts_user INT NOT NULL,
						 qts_sharetag INT NOT NULL,
						 qts_level INT NOT NULL,
						 qts_viraccount BIGINT NOT NULL,
						 PRIMARY KEY(qts_autoid));
						 
ALTER TABLE qts_accounts ADD UNIQUE(qts_account);
ALTER TABLE qts_accounts ADD INDEX qts_accounts_index(qts_secuid,qts_user,qts_viraccount);		

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

CREATE TABLE qts_records(qts_autoid INT NOT NULL AUTO_INCREMENT,
						qts_secuid BIGINT NOT NULL,
						qts_account BIGINT NOT NULL,
						qts_strategyid INT NOT NULL,
						qts_orderid BIGINT NOT NULL,
						qts_algoid BIGINT NOT NULL,
						qts_algoindex BIGINT NOT NULL,
						qts_parentid BIGINT NOT NULL,
						qts_code BIGINT NOT NULL,
						qts_action INT NOT NULL,
						qts_paction INT NOT NULL,
						qts_status INT NOT NULL,
						qts_prevstatus INT NOT NULL,
						qts_oprice BIGINT NOT NULL,
						qts_iprice BIGINT NOT NULL,
						qts_ovolume BIGINT NOT NULL,
						qts_ivolume BIGINT NOT NULL,
						qts_otime BIGINT NOT NULL,
						qts_itime BIGINT NOT NULL,
						qts_property INT NOT NULL,
						qts_direction INT NOT NULL,
						qts_canceled INT NOT NULL,
						qts_userid INT NOT NULL,
						qts_refid BIGINT NOT NULL,
						qts_sessionid INT NOT NULL,
						qts_source INT NOT NULL,
						qts_ss INT NOT NULL,
						qts_gw INT NOT NULL,							
						PRIMARY KEY(qts_autoid));
						
ALTER TABLE qts_records	ADD	UNIQUE(qts_orderid);
ALTER TABLE qts_records ADD INDEX qts_records_index(qts_account,qts_algoid,qts_parentid);

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

drop database qts_ds_backup;
create database qts_ds_backup;
use qts_ds_backup;

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

drop database qts_gui_backup;
create database qts_gui_backup;
use qts_gui_backup;				

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
