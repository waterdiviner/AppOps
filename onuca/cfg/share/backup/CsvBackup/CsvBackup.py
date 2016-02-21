from qtscommon import *

if GetBackupType() == xfile or GetBackupType() == qts_all_file :
	CreatePluginForBackup(995,ALL_MARKET,'','QtsCsvBackup','CreateCsvBackup')
	AppendPropertyForBackup(995,QTS_CFG_KEY_CSVFLAG,QTS_CSV_FLAG)
	