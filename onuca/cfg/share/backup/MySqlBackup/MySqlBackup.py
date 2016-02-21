from qtscommon import *

if GetBackupType() == mysql :
	CreatePluginForBackup(997,ALL_MARKET,'root@localhost:1111:qtsbackup','QtsMySqlBackup','CreateMySqlBackup')	