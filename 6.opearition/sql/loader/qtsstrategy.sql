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
						