from qtscommon import *

if GetBackupType() == bfile or GetBackupType() == qts_all_file :
	CreatePluginForBackup(999,ALL_MARKET,'','QtsFileBackup','CreateFileBackup')