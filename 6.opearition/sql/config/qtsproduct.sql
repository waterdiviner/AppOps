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