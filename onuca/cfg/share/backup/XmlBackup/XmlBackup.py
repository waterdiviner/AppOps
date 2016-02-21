from qtscommon import *

if GetBackupType() == xml :
	CreatePluginForBackup(996,ALL_MARKET,BuildTestOutputFile('output.xml'),'QtsXmlBackup','CreateXmlBackup')