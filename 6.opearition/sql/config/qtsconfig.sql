drop database qts_config;
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
							
ALTER TABLE qts_strategyinproduct ADD INDEX qts_strategyinproduct_index(qts_productid,qts_strategyid);	