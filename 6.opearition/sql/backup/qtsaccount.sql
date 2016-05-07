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
ALTER TABLE qts_parameters ADD INDEX qts_parameters_index(qts_strategyid);CREATE TABLE qts_positions(qts_autoid INT NOT NULL AUTO_INCREMENT,
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
							
ALTER TABLE qts_positions ADD INDEX qts_positions_index(qts_secuid,qts_account,qts_code,qts_type,qts_level);							CREATE TABLE qts_records(qts_autoid INT NOT NULL AUTO_INCREMENT,
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
ALTER TABLE qts_records ADD INDEX qts_records_index(qts_account,qts_algoid,qts_parentid);CREATE TABLE qts_remotes(qts_autoid INT NOT NULL AUTO_INCREMENT,
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
						
ALTER TABLE qts_remotes ADD INDEX qts_remotes_index(qts_key,qts_appid);						CREATE TABLE qts_strategys(qts_autoid INT NOT NULL AUTO_INCREMENT,
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
							
ALTER TABLE qts_strategys ADD UNIQUE(qts_strategyid);						CREATE TABLE qts_workings(qts_autoid INT NOT NULL AUTO_INCREMENT,
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
						
ALTER TABLE qts_workings ADD INDEX qts_workings_index(qts_secuid,qts_strategyid,qts_code,qts_action);						CREATE TABLE qts_admins(qts_autoid INT NOT NULL AUTO_INCREMENT,
						qts_id INT NOT NULL,
						qts_name CHAR(40) NULL,						
						qts_parentid INT NOT NULL,
						qts_type INT NOT NULL,						
						qts_subtype INT NOT NULL,
						qts_password CHAR(20) NOT NULL,	
						qts_againpassword CHAR(20) NOT NULL,	
						qts_detail CHAR(255),
						PRIMARY KEY(qts_autoid));
					
ALTER TABLE qts_admins ADD UNIQUE(qts_id);
ALTER TABLE qts_admins ADD INDEX qts_admins_index(qts_parentid);CREATE TABLE qts_apps(qts_autoid INT NOT NULL AUTO_INCREMENT,
						qts_id BIGINT NOT NULL,
						qts_name CHAR(40) NULL,
						qts_type INT NOT NULL,
						qts_path CHAR(255),
						qts_machineid INT NOT NULL,
						qts_detail CHAR(255),
						PRIMARY KEY(qts_autoid));
					
ALTER TABLE qts_apps ADD UNIQUE(qts_id);drop database qts_config;
create database qts_config;
use qts_config;

CREATE TABLE qts_admins(qts_autoid INT NOT NULL AUTO_INCREMENT,
						qts_id INT NOT NULL,
						qts_name CHAR(40) NULL,
						qts_type INT NOT NULL,
						qts_detail CHAR(255),
						PRIMARY KEY(qts_autoid));
					
ALTER TABLE qts_jobs ADD UNIQUE(qts_id);


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

CREATE TABLE qts_products(qts_autoid INT NOT NULL AUTO_INCREMENT,
							qts_id INT NOT NULL,
							qts_parentid INT NOT NULL,
							qts_name CHAR(40) NOT NULL,
							qts_manager INT,
							qts_bdate CHAR(20),
							qts_edate CHAR(20),
							qts_status smallint,
							qts_property CHAR(40),
							qts_detail CHAR(255),
							PRIMARY KEY(qts_autoid));
							
ALTER TABLE qts_products ADD UNIQUE(qts_id);
ALTER TABLE qts_products ADD INDEX qts_products_index(qts_parentid);


CREATE TABLE qts_strategyinapp(qts_autoid INT NOT NULL AUTO_INCREMENT,
							qts_appid INT NOT NULL,
							qts_strategyid INT NOT NULL,
							PRIMARY KEY(qts_autoid));
							
ALTER TABLE qts_strategyinapp ADD INDEX qts_strategyinapp_index(qts_appid,qts_strategyid);	

CREATE TABLE qts_strategyinproduct(qts_autoid INT NOT NULL AUTO_INCREMENT,
							qts_productid INT NOT NULL,
							qts_strategyid INT NOT NULL,
							PRIMARY KEY(qts_autoid));
							
ALTER TABLE qts_strategyinproduct ADD INDEX qts_strategyinproduct_index(qts_productid,qts_strategyid);	CREATE TABLE qts_jobs(qts_autoid INT NOT NULL AUTO_INCREMENT,
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
					
ALTER TABLE qts_jobs ADD UNIQUE(qts_id);CREATE TABLE qts_machines(qts_autoid INT NOT NULL AUTO_INCREMENT,
							qts_id INT NOT NULL,
							qts_name CHAR(40) NOT NULL,
							qts_host CHAR(40) NOT NULL,
							qts_user CHAR(40) NOT NULL,
							qts_password CHAR(20) NOT NULL,	
							qts_type smallint,
						    qts_position CHAR(20),
							qts_detail CHAR(255),
							PRIMARY KEY(qts_autoid));

ALTER TABLE qts_machines ADD UNIQUE(qts_id);CREATE TABLE qts_products(qts_autoid INT NOT NULL AUTO_INCREMENT,
							qts_id INT NOT NULL,
							qts_parentid INT NOT NULL,
							qts_name CHAR(40) NOT NULL,
							qts_manager INT,
							qts_bdate CHAR(20),
							qts_edate CHAR(20),
							qts_status smallint,
							qts_property CHAR(40),
							qts_detail CHAR(255),
							PRIMARY KEY(qts_autoid));
							
ALTER TABLE qts_products ADD UNIQUE(qts_id);
ALTER TABLE qts_products ADD INDEX qts_products_index(qts_parentid);CREATE TABLE qts_rights(qts_autoid INT NOT NULL AUTO_INCREMENT,
						qts_id INT NOT NULL,
						qts_target INT NOT NULL,
						qts_type INT NOT NULL,						
						qts_read smallint NOT NULL,	
						qts_insert smallint NOT NULL,	
						qts_delete smallint NOT NULL,	
						qts_update smallint NOT NULL,	
						PRIMARY KEY(qts_autoid));

ALTER TABLE qts_rights ADD UNIQUE(qts_id);
CREATE TABLE qts_strategyinapp(qts_autoid INT NOT NULL AUTO_INCREMENT,
							qts_appid INT NOT NULL,
							qts_strategyid INT NOT NULL,
							PRIMARY KEY(qts_autoid));
							
ALTER TABLE qts_strategyinapp ADD INDEX qts_strategyinapp_index(qts_appid,qts_strategyid);	CREATE TABLE qts_strategyinproduct(qts_autoid INT NOT NULL AUTO_INCREMENT,
							qts_productid INT NOT NULL,
							qts_strategyid INT NOT NULL,
							PRIMARY KEY(qts_autoid));
							
ALTER TABLE qts_strategyinproduct ADD INDEX qts_strategyinproduct_index(qts_productid,qts_strategyid);	/*##############################################################
#交易帐户。对应的CSV文件是qttrade.acc
#---------------------------------------------------------------
#qts_market				ushort 			帐户所在的市场
#qts_category			ushort			帐户所在的品种
#qts_account			int64			子帐户
#qts_totalamoumt		int64			总的资金
#qts_avlamount			int64			可用资金
#qts_freezeamount		int64			冻结资金
#qts_currency			ushort			币种
#qts_date				int64			日期
##############################################################*/					
CREATE TABLE qts_trade(qts_autoid INT NOT NULL AUTO_INCREMENT,
						qts_market INT NOT NULL,
						qts_category INT NOT NULL,
						qts_account BIGINT NOT NULL,
						qts_totalamount BIGINT NOT NULL,
						qts_avlamount BIGINT NOT NULL,
						qts_freezeamount BIGINT NOT NULL,
						qts_currency INT NOT NULL,
						qts_date BIGINT NOT NULL,
						PRIMARY KEY(qts_autoid));

ALTER TABLE qts_trade ADD INDEX qts_trade_index(qts_market,qts_category,qts_account);	
	
/*##############################################################
#qts_user			uint		用户
#qts_account			int64		子帐户
#qts_viraccount			int64		虚拟帐户，是总帐户对应的唯一值
##############################################################*/		
CREATE TABLE qts_user(qts_autoid INT NOT NULL AUTO_INCREMENT,
						qts_user INT NOT NULL,
						qts_account BIGINT NOT NULL,
						qts_viraccount BIGINT NOT NULL,
						PRIMARY KEY(qts_autoid));

ALTER TABLE qts_user ADD INDEX qts_user_index(qts_user,qts_account,qts_viraccount);
						
/*##############################################################
#qts_market				ushort 			帐户所在的市场
#qts_category			ushort			帐户所在的品种
#qts_viraccount			int64			虚拟帐户，是总帐户对应的唯一值
#qts_relaccount			string			实际的交易所帐户
#qts_sharetag			ushort			是否资金共享标志，同一标志的资金是共享的
#qts_totalamoumt		int64			总的资金
#qts_avlamount			int64			可用资金
#qts_freezeamount		int64			冻结资金
#qts_date				int64			日期
##############################################################*/						
CREATE TABLE qts_exchange(qts_autoid INT NOT NULL AUTO_INCREMENT,
							qts_market INT NOT NULL,
							qts_category INT NOT NULL,
							qts_viraccount BIGINT NOT NULL,
							qts_relaccount CHAR(100) NOT NULL,
							qts_sharetag INT NOT NULL,
							qts_totalamount BIGINT NOT NULL,
							qts_avlamount BIGINT NOT NULL,
							qts_freezeamount BIGINT NOT NULL,
							qts_date BIGINT NOT NULL,
							PRIMARY KEY(qts_autoid));
							
ALTER TABLE qts_exchange ADD INDEX qts_exchange_index(qts_market,qts_category,qts_viraccount);
drop database qts_loader;
create database qts_loader;
use qts_loader;

/*##############################################################
#交易帐户。对应的CSV文件是qttrade.acc
#---------------------------------------------------------------
#qts_market				ushort 			帐户所在的市场
#qts_category			ushort			帐户所在的品种
#qts_account			int64			子帐户
#qts_totalamoumt		int64			总的资金
#qts_avlamount			int64			可用资金
#qts_freezeamount		int64			冻结资金
#qts_currency			ushort			币种
#qts_date				int64			日期
##############################################################*/					
CREATE TABLE qts_trade(qts_autoid INT NOT NULL AUTO_INCREMENT,
						qts_market INT NOT NULL,
						qts_category INT NOT NULL,
						qts_account BIGINT NOT NULL,
						qts_totalamount BIGINT NOT NULL,
						qts_avlamount BIGINT NOT NULL,
						qts_freezeamount BIGINT NOT NULL,
						qts_currency INT NOT NULL,
						qts_date BIGINT NOT NULL,
						PRIMARY KEY(qts_autoid));

ALTER TABLE qts_trade ADD INDEX qts_trade_index(qts_market,qts_category,qts_account);	
	
/*##############################################################
#qts_user			uint		用户
#qts_account			int64		子帐户
#qts_viraccount			int64		虚拟帐户，是总帐户对应的唯一值
##############################################################*/		
CREATE TABLE qts_user(qts_autoid INT NOT NULL AUTO_INCREMENT,
						qts_user INT NOT NULL,
						qts_account BIGINT NOT NULL,
						qts_viraccount BIGINT NOT NULL,
						PRIMARY KEY(qts_autoid));

ALTER TABLE qts_user ADD INDEX qts_user_index(qts_user,qts_account,qts_viraccount);
						
/*##############################################################
#qts_market				ushort 			帐户所在的市场
#qts_category			ushort			帐户所在的品种
#qts_viraccount			int64			虚拟帐户，是总帐户对应的唯一值
#qts_relaccount			string			实际的交易所帐户
#qts_sharetag			ushort			是否资金共享标志，同一标志的资金是共享的
#qts_totalamoumt		int64			总的资金
#qts_avlamount			int64			可用资金
#qts_freezeamount		int64			冻结资金
#qts_date				int64			日期
##############################################################*/						
CREATE TABLE qts_exchange(qts_autoid INT NOT NULL AUTO_INCREMENT,
							qts_market INT NOT NULL,
							qts_category INT NOT NULL,
							qts_viraccount BIGINT NOT NULL,
							qts_relaccount CHAR(100) NOT NULL,
							qts_sharetag INT NOT NULL,
							qts_totalamount BIGINT NOT NULL,
							qts_avlamount BIGINT NOT NULL,
							qts_freezeamount BIGINT NOT NULL,
							qts_date BIGINT NOT NULL,
							PRIMARY KEY(qts_autoid));
							
ALTER TABLE qts_exchange ADD INDEX qts_exchange_index(qts_market,qts_category,qts_viraccount);


/*##############################################################
#qts_account						int64					参位所在的帐户
#qts_market							ushort					标的所在的市场
#qts_category						ushort					标的所在的品种
#qts_code							uint					标的的证券代码
#qts_type							enum					仓位类型，0是长仓，1是短仓
#qts_level							enum					仓位级别，0是子仓位，1是总仓位
#qts_totalvol						int64					总的仓位
#qts_avlvol							int64					可用仓位
#qts_workingvol						int64					在途仓位
#qts_toalcost						int64					总的费用
#qts_qtsdate						int64					仓位日期
#qts_avlcredempvol					int64					可申赎仓位
#qts_todayvol						int64					今日仓位
##############################################################*/					
CREATE TABLE qts_position(qts_autoid INT NOT NULL AUTO_INCREMENT,
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
							
ALTER TABLE qts_position ADD INDEX qts_position_index(qts_secuid,qts_account,qts_code,qts_type,qts_level);								

/*##############################################################
#证券信息的静态数据表，这是主要数据列，可以根据需要在后面添加列，
#但不能在头或中间插入数据。列名称必须是唯一的，这个会被程序作为
#访问的键值。对应的CSV文件是qtsinfo_s.info
#---------------------------------------------------------------
#qts_market  					ushort		标的所在的市场
#qts_category					ushort		标的所在的品种
#qts_secucode					uint		标的的证券代码
#qts_ordercode					string		标的的交易代码，可以加一个@带标记
#qts_marketname					string		标的的市场名称
#qts_categoryname				string		标的的品种名称
#qts_secuname					string		标的的证券名称
#qts_minorderqty				int64		标的的最小订单量
#qts_maxorderqty				int64		标的的最大订单量
#qts_pricetick					int64		标的的最小报价差
#qts_tradetype					enum		标的的清算类型，0是T+0、1是T+1，2是T+2，3是未知
#qts_postype					enum		标的的仓位类型，0是长仓，1是短仓，2是双向仓
#qts_multipler					INT			标的的价格乘数
#qts_margin						INT			标的的保证金比例，乘100后的值
##############################################################*/
CREATE TABLE qts_secuinfo_s(qts_autoid INT NOT NULL AUTO_INCREMENT,
							qts_market INT NOT NULL,
							qts_category INT NOT NULL,
							qts_secucode INT NOT NULL,
							qts_ordercode  CHAR(50) NOT NULL,
							qts_marketname CHAR(40) NOT NULL,
							qts_categoryname CHAR(40) NOT NULL,
							qts_secuname CHAR(40) NOT NULL,
							qts_minorderqty BIGINT NOT NULL,
							qts_maxorderqty BIGINT NOT NULL,
							qts_pricetick INT NOT NULL,
							qts_tradetn INT NOT NULL,
							qts_posmode INT NOT NULL,
							qts_multipler INT NOT NULL,
							qts_margin INT NOT NULL,
							PRIMARY KEY(qts_autoid));

ALTER TABLE qts_secuinfo_s ADD INDEX qts_secuinfo_s_index(qts_market,qts_category,qts_secucode);	
							
/*##############################################################
#证券信息的动态数据表，这是主要数据列，可以根据需要在后面添加列，
#但不能在头或中间插入数据。列名称必须是唯一的，这个会被程序作为
#访问的键值。对应的CSV文件是qtsinfo_d.info
#---------------------------------------------------------------
#qts_market  					ushort		标的所在的市场
#qts_category					ushort		标的所在的品种
#qts_secucode					uint		标的的证券代码
#qts_lastprice					int64		标的昨手收价格，乘以10000
#qts_lolimitedprice				int64		标的的跌停价格，乘以10000
#qts_uplimitedprice				int64		标的的涨停价格，乘以10000
#qts_suspension					enum		标的的停牌类型,0是昨日停牌，1是今日停牌，2是未停牌，3是未知
#qts_tradingfee					string		标的的交易费用
##############################################################*/
CREATE TABLE qts_secuinfo_d(qts_autoid INT NOT NULL AUTO_INCREMENT,
							qts_market INT NOT NULL,
							qts_category INT NOT NULL,
							qts_secucode INT NOT NULL,	
							qts_lastprice BIGINT NOT NULL,
							qts_lolimitprice BIGINT NOT NULL,
							qts_uplimitprice BIGINT NOT NULL,
							qts_suspension INT NOT NULL,
							qts_tradingfee CHAR(255),
							PRIMARY KEY(qts_autoid));
							
ALTER TABLE qts_secuinfo_d ADD INDEX qts_secuinfo_d_index(qts_market,qts_category,qts_secucode);
							
							
/*##############################################################
#qts_strategyid			INT	   			策略ID
#qts_name				string			策略名称
#qts_account			string			帐户，可以是多个帐户，以,分开
#qts_minorderid			int64			订单ID的起始值
#qts_maxorderid			int64			订单ID的结束值
#qts_orderidstep		INT				订单ID的步进值
#qts_status				enum			策略的启动的状态，0是
#qts_threadid			INT				策略所运行的线程ID值
##############################################################*/
CREATE TABLE qts_strategy(qts_autoid INT NOT NULL AUTO_INCREMENT,
							qts_strategyid INT NOT NULL,
							qts_name CHAR(20) NOT NULL,
							qts_account CHAR(255) NOT NULL,
							qts_minorderid BIGINT NOT NULL,
							qts_maxorderid BIGINT NOT NULL,
							qts_orderidstep INT NOT NULL,
							qts_status INT NOT NULL,
							qts_threadid INT NOT NULL,
							PRIMARY KEY(qts_autoid));

ALTER TABLE qts_strategy ADD UNIQUE(qts_strategyid);

/*##############################################################
#qts_strategyid				INT			策略ID
#qts_key					INT			参数ID
#qts_name					string		参数名称
#qts_codetype				INT			标的类型
#qts_market					ushort		标的所在的市场
#qts_category				ushort 		标的所在的品种
#qts_secucode				INT			标的的交易代码
#qts_index					INT			显示序号
#qts_level					INT			显示级别
#qts_status					bool		显示状态，0是不显示，1是显示
#qts_mode					enum		显示模式：
										0是未知，
										1是所有信息都发，
										2是仅发盈亏信息，
										3是仅发订单本信息，
										4是仅发在途信息，
										5是发订单和盈亏信息，
										6是发订单和在途信息，
										7是发盈亏和在途信息
#qts_component				string		控件内容
#qts_style					string		控件样式
##############################################################*/		
CREATE TABLE qts_instrument(qts_autoid INT NOT NULL AUTO_INCREMENT,
							qts_strategyid INT NOT NULL,
							qts_key INT NOT NULL,
							qts_name CHAR(20) NOT NULL,
							qts_codetype INT NOT NULL,
							qts_market INT NOT NULL,
							qts_category INT NOT NULL,
							qts_secucode INT NOT NULL,
							qts_index INT NOT NULL,
							qts_level INT NOT NULL,
							qts_status INT NOT NULL,
							qts_mode INT NOT NULL,
							qts_component CHAR(255),
							qts_style CHAR(255),
							PRIMARY KEY(qts_autoid));
		
ALTER TABLE qts_instrument ADD INDEX qts_instrument_index(qts_strategyid,qts_key);
		
/*##############################################################
#qts_strategyid				INT			策略ID
#qts_key					INT			参数ID
#qts_name					string		参数名称
#qts_value					int64		标的类型
#qts_vardecimal				INT			小数位数
#qts_index					INT			显示序号
#qts_level					INT			显示级别
#qts_save					bool		是否备份
#qts_status					bool		显示状态，0是不可编辑，1是可编辑
#qts_mode					enum		显示模式：
										0是文本框，
										1是下拉选择框，
										2是一般按钮，
										3是确认按钮，
										4是显示标签
#qts_component				string		控件内容
#qts_style					string		控件样式
##############################################################*/		
CREATE TABLE qts_parameter(qts_autoid INT NOT NULL AUTO_INCREMENT,
							qts_strategyid INT NOT NULL,
							qts_key INT NOT NULL,
							qts_name CHAR(20) NOT NULL,
							qts_value BIGINT NOT NULL,
							qts_vardecimal INT NOT NULL,
							qts_index INT NOT NULL,
							qts_level INT NOT NULL,
							qts_save INT NOT NULL,
							qts_status INT NOT NULL,
							qts_mode INT NOT NULL,
							qts_component CHAR(255),
							qts_style CHAR(255),
							PRIMARY KEY(qts_autoid));

ALTER TABLE qts_parameter ADD INDEX qts_parameter_index(qts_strategyid,qts_key);
							
/*##############################################################
#qts_strategyid				INT			策略ID
#qts_key					INT			参数ID
#qts_name					string		参数名称
#qts_value					int64		标的类型
#qts_vardecimal				INT			小数位数
#qts_index					INT			显示序号
#qts_level					INT			显示级别
#qts_modify					bool		是否可向GUI发送此数据
#qts_status					bool		显示状态，无意义
#qts_mode					enum		显示模式：
										0是文本框，
										1是下拉选择框，
										2是一般按钮，
										3是确认按钮，
										4是显示标签
#qts_component				string		控件内容
#qts_style					string		控件样式
##############################################################*/					
CREATE TABLE qts_comment(qts_autoid INT NOT NULL AUTO_INCREMENT,
						qts_strategyid INT NOT NULL,
						qts_key INT NOT NULL,
						qts_name CHAR(20) NOT NULL,
						qts_value BIGINT NOT NULL,
						qts_vardecimal INT NOT NULL,
						qts_index INT NOT NULL,
						qts_level INT NOT NULL,
						qts_modify INT NOT NULL,
						qts_status INT NOT NULL,
						qts_mode INT NOT NULL,
						qts_component CHAR(255),
						qts_style CHAR(255),
						PRIMARY KEY(qts_autoid));					
					
ALTER TABLE qts_comment ADD INDEX qts_comment_index(qts_strategyid,qts_key);
					
/*##############################################################
#qts_strategyid				INT			策略ID
#qts_key					INT			参数ID
#qts_name					string		参数名称
#qts_index					INT			显示序号
#qts_level					INT			显示级别
#qts_status					bool		显示状态，0是不可点击，1是可点击
#qts_mode					enum		显示模式：
										0是文本框，
										1是下拉选择框，
										2是一般按钮，
										3是确认按钮，
										4是显示标签
#qts_component				string		控件内容
#qts_style					string		控件样式
##############################################################*/					
CREATE TABLE qts_command(qts_autoid INT NOT NULL AUTO_INCREMENT,
						qts_strategyid INT NOT NULL,
						qts_key INT NOT NULL,
						qts_name CHAR(20) NOT NULL,
						qts_index INT NOT NULL,
						qts_level INT NOT NULL,
						qts_status INT NOT NULL,
						qts_mode INT NOT NULL,
						qts_component CHAR(255),
						qts_style CHAR(255),
						PRIMARY KEY(qts_autoid));	
						
ALTER TABLE qts_command ADD INDEX qts_command_index(qts_strategyid,qts_key);
						/*##############################################################
#qts_market							ushort					标的所在的市场
#qts_category						ushort					标的所在的品种
#qts_secucode						uint					标的的证券代码
#qts_account						int64					参位所在的帐户
#qts_type							enum					仓位类型，0是长仓，1是短仓
#qts_level							enum					仓位级别，0是子仓位，1是总仓位
#qts_totalvol						int64					总的仓位
#qts_avlvol							int64					可用仓位
#qts_workingvol						int64					在途仓位
#qts_toalcost						int64					总的费用
#qts_qtsdate						int64					仓位日期
#qts_avlcredempvol					int64					可申赎仓位
#qts_todayvol						int64					今日仓位
##############################################################*/					
CREATE TABLE qts_position(qts_autoid INT NOT NULL AUTO_INCREMENT,
							qts_market SMALLINT NOT NULL,
							qts_category SMALLINT NOT NULL,
							qts_secucode INT NOT NULL,
							qts_account BIGINT NOT NULL,
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
							
ALTER TABLE qts_position ADD INDEX qts_position_index(qts_market,qts_category,qts_secucode,qts_account,qts_code,qts_type,qts_level);								/*##############################################################
#证券信息的静态数据表，这是主要数据列，可以根据需要在后面添加列，
#但不能在头或中间插入数据。列名称必须是唯一的，这个会被程序作为
#访问的键值。对应的CSV文件是qtsinfo_s.info
#---------------------------------------------------------------
#qts_market  					ushort		标的所在的市场
#qts_category					ushort		标的所在的品种
#qts_secucode					uint		标的的证券代码
#qts_ordercode					string		标的的交易代码，可以加一个@带标记
#qts_marketname					string		标的的市场名称
#qts_categoryname				string		标的的品种名称
#qts_secuname					string		标的的证券名称
#qts_minorderqty				int64		标的的最小订单量
#qts_maxorderqty				int64		标的的最大订单量
#qts_pricetick					int64		标的的最小报价差
#qts_tradetype					enum		标的的清算类型，0是T+0、1是T+1，2是T+2，3是未知
#qts_postype					enum		标的的仓位类型，0是长仓，1是短仓，2是双向仓
#qts_multipler					INT			标的的价格乘数
#qts_margin						INT			标的的保证金比例，乘100后的值
##############################################################*/
CREATE TABLE qts_secuinfo_s(qts_autoid INT NOT NULL AUTO_INCREMENT,
							qts_market INT NOT NULL,
							qts_category INT NOT NULL,
							qts_secucode INT NOT NULL,
							qts_ordercode  CHAR(50) NOT NULL,
							qts_marketname CHAR(40) NOT NULL,
							qts_categoryname CHAR(40) NOT NULL,
							qts_secuname CHAR(40) NOT NULL,
							qts_minorderqty BIGINT NOT NULL,
							qts_maxorderqty BIGINT NOT NULL,
							qts_pricetick INT NOT NULL,
							qts_tradetn INT NOT NULL,
							qts_posmode INT NOT NULL,
							qts_multipler INT NOT NULL,
							qts_margin INT NOT NULL,
							qts_currency CHAR(10), 
							qts_expiry CHAR(10),  
							qts_right CHAR(10), 
							qts_strike CHAR(10), 
							qts_tradingclass CHAR(10),
							PRIMARY KEY(qts_autoid));

ALTER TABLE qts_secuinfo_s ADD INDEX qts_secuinfo_s_index(qts_market,qts_category,qts_secucode);	
							
/*##############################################################
#证券信息的动态数据表，这是主要数据列，可以根据需要在后面添加列，
#但不能在头或中间插入数据。列名称必须是唯一的，这个会被程序作为
#访问的键值。对应的CSV文件是qtsinfo_d.info
#---------------------------------------------------------------
#qts_market  					ushort		标的所在的市场
#qts_category					ushort		标的所在的品种
#qts_secucode					uint		标的的证券代码
#qts_lastprice					int64		标的昨手收价格，乘以10000
#qts_lolimitedprice				int64		标的的跌停价格，乘以10000
#qts_uplimitedprice				int64		标的的涨停价格，乘以10000
#qts_suspension					enum		标的的停牌类型,0是昨日停牌，1是今日停牌，2是未停牌，3是未知
#qts_tradingfee					string		标的的交易费用
##############################################################*/
CREATE TABLE qts_secuinfo_d(qts_autoid INT NOT NULL AUTO_INCREMENT,
							qts_market INT NOT NULL,
							qts_category INT NOT NULL,
							qts_secucode INT NOT NULL,	
							qts_lastprice BIGINT NOT NULL,
							qts_lolimitprice BIGINT NOT NULL,
							qts_uplimitprice BIGINT NOT NULL,
							qts_suspension INT NOT NULL,
							qts_tradingfee CHAR(255),
							PRIMARY KEY(qts_autoid));
							
ALTER TABLE qts_secuinfo_d ADD INDEX qts_secuinfo_d_index(qts_market,qts_category,qts_secucode);
							/*##############################################################
#qts_strategyid			INT	   			策略ID
#qts_name				string			策略名称
#qts_account			string			帐户，可以是多个帐户，以,分开
#qts_minorderid			int64			订单ID的起始值
#qts_maxorderid			int64			订单ID的结束值
#qts_orderidstep		INT				订单ID的步进值
#qts_status				enum			策略的启动的状态，0是
#qts_threadid			INT				策略所运行的线程ID值
##############################################################*/
CREATE TABLE qts_strategy(qts_autoid INT NOT NULL AUTO_INCREMENT,
							qts_strategyid INT NOT NULL,
							qts_name CHAR(20) NOT NULL,
							qts_account CHAR(255) NOT NULL,
							qts_minorderid BIGINT NOT NULL,
							qts_maxorderid BIGINT NOT NULL,
							qts_orderidstep INT NOT NULL,
							qts_status INT NOT NULL,
							qts_threadid INT NOT NULL,
							PRIMARY KEY(qts_autoid));

ALTER TABLE qts_strategy ADD UNIQUE(qts_strategyid);

/*##############################################################
#qts_strategyid				INT			策略ID
#qts_key					INT			参数ID
#qts_name					string		参数名称
#qts_codetype				INT			标的类型
#qts_market					ushort		标的所在的市场
#qts_category				ushort 		标的所在的品种
#qts_secucode				INT			标的的交易代码
#qts_index					INT			显示序号
#qts_level					INT			显示级别
#qts_status					bool		显示状态，0是不显示，1是显示
#qts_mode					enum		显示模式：
										0是未知，
										1是所有信息都发，
										2是仅发盈亏信息，
										3是仅发订单本信息，
										4是仅发在途信息，
										5是发订单和盈亏信息，
										6是发订单和在途信息，
										7是发盈亏和在途信息
#qts_component				string		控件内容
#qts_style					string		控件样式
##############################################################*/		
CREATE TABLE qts_instrument(qts_autoid INT NOT NULL AUTO_INCREMENT,
							qts_strategyid INT NOT NULL,
							qts_key INT NOT NULL,
							qts_name CHAR(20) NOT NULL,
							qts_codetype INT NOT NULL,
							qts_market INT NOT NULL,
							qts_category INT NOT NULL,
							qts_secucode INT NOT NULL,
							qts_index INT NOT NULL,
							qts_level INT NOT NULL,
							qts_status INT NOT NULL,
							qts_mode INT NOT NULL,
							qts_component CHAR(255),
							qts_style CHAR(255),
							PRIMARY KEY(qts_autoid));
		
ALTER TABLE qts_instrument ADD INDEX qts_instrument_index(qts_strategyid,qts_key);
		
/*##############################################################
#qts_strategyid				INT			策略ID
#qts_key					INT			参数ID
#qts_name					string		参数名称
#qts_value					int64		标的类型
#qts_vardecimal				INT			小数位数
#qts_index					INT			显示序号
#qts_level					INT			显示级别
#qts_save					bool		是否备份
#qts_status					bool		显示状态，0是不可编辑，1是可编辑
#qts_mode					enum		显示模式：
										0是文本框，
										1是下拉选择框，
										2是一般按钮，
										3是确认按钮，
										4是显示标签
#qts_component				string		控件内容
#qts_style					string		控件样式
##############################################################*/		
CREATE TABLE qts_parameter(qts_autoid INT NOT NULL AUTO_INCREMENT,
							qts_strategyid INT NOT NULL,
							qts_key INT NOT NULL,
							qts_name CHAR(20) NOT NULL,
							qts_value BIGINT NOT NULL,
							qts_decimal INT NOT NULL,
							qts_index INT NOT NULL,
							qts_level INT NOT NULL,
							qts_save INT NOT NULL,
							qts_status INT NOT NULL,
							qts_mode INT NOT NULL,
							qts_component CHAR(255),
							qts_style CHAR(255),
							PRIMARY KEY(qts_autoid));

ALTER TABLE qts_parameter ADD INDEX qts_parameter_index(qts_strategyid,qts_key);
							
/*##############################################################
#qts_strategyid				INT			策略ID
#qts_key					INT			参数ID
#qts_name					string		参数名称
#qts_value					int64		标的类型
#qts_vardecimal				INT			小数位数
#qts_index					INT			显示序号
#qts_level					INT			显示级别
#qts_modify					bool		是否可向GUI发送此数据
#qts_status					bool		显示状态，无意义
#qts_mode					enum		显示模式：
										0是文本框，
										1是下拉选择框，
										2是一般按钮，
										3是确认按钮，
										4是显示标签
#qts_component				string		控件内容
#qts_style					string		控件样式
##############################################################*/					
CREATE TABLE qts_comment(qts_autoid INT NOT NULL AUTO_INCREMENT,
						qts_strategyid INT NOT NULL,
						qts_key INT NOT NULL,
						qts_name CHAR(20) NOT NULL,
						qts_value BIGINT NOT NULL,
						qts_vardecimal INT NOT NULL,
						qts_index INT NOT NULL,
						qts_level INT NOT NULL,
						qts_modify INT NOT NULL,
						qts_status INT NOT NULL,
						qts_mode INT NOT NULL,
						qts_component CHAR(255),
						qts_style CHAR(255),
						PRIMARY KEY(qts_autoid));					
					
ALTER TABLE qts_comment ADD INDEX qts_comment_index(qts_strategyid,qts_key);
					
/*##############################################################
#qts_strategyid				INT			策略ID
#qts_key					INT			参数ID
#qts_name					string		参数名称
#qts_index					INT			显示序号
#qts_level					INT			显示级别
#qts_status					bool		显示状态，0是不可点击，1是可点击
#qts_mode					enum		显示模式：
										0是文本框，
										1是下拉选择框，
										2是一般按钮，
										3是确认按钮，
										4是显示标签
#qts_component				string		控件内容
#qts_style					string		控件样式
##############################################################*/					
CREATE TABLE qts_command(qts_autoid INT NOT NULL AUTO_INCREMENT,
						qts_strategyid INT NOT NULL,
						qts_key INT NOT NULL,
						qts_name CHAR(20) NOT NULL,
						qts_index INT NOT NULL,
						qts_level INT NOT NULL,
						qts_status INT NOT NULL,
						qts_mode INT NOT NULL,
						qts_component CHAR(255),
						qts_style CHAR(255),
						PRIMARY KEY(qts_autoid));	
						
ALTER TABLE qts_command ADD INDEX qts_command_index(qts_strategyid,qts_key);
						