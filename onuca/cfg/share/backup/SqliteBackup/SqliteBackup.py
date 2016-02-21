from qtscommon import *

if GetBackupType() == sqlite :
	CreatePluginForBackup(998,ALL_MARKET,GetDataPath('qtsbackup.db3'),'QtsSQLiteBackup','CreateSQLiteBackup')	