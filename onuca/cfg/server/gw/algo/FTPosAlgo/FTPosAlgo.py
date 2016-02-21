from qtscommon import *

CreatePluginForAlgo(2,[[ZJ_MARKET,IF_CATEGORY],[ZJ_MARKET,IC_CATEGORY],[ZJ_MARKET,IH_CATEGORY],[DL_MARKET,JD_CATEGORY]],'','QtsFTPosAlgo','CreateFTPosAlgo')
#AppendPropertyForAlgo(2,QTS_CFG_KEY_MINORDERID,BuildAlgoOrderId(2,0))
AppendPropertyForAlgo(2,QTS_CFG_KEY_LOADER,['qts_exposition'])
#QTS_CFG_KEY_BACKUP: index is 0 backup exrecord,index is 1 backup exposition ,index is 2 backup exaccount,if no backup set BuildBackupFile(None)
#[BuildBackupFile('exrecord'),BuildBackupFile('exposition'),BuildBackupFile('exaccount')]
#[BuildBackupFile(None),BuildBackupFile(None),BuildBackupFile(None)]	
AppendPropertyForAlgo(2,QTS_CFG_KEY_BACKUP,[BuildBackupFile(QTS_BACKUP_GW_EXCHANGE_RECORD),BuildBackupFile(QTS_BACKUP_GW_EXCHANGE_POSITION),BuildBackupFile(QTS_BACKUP_GW_EXCHANGE_ACCOUNT),BuildBackupFile(QTS_BACKUP_GW_EXCHANGE_WORKING)])
AppendPropertyForAlgo(2,QTS_CFG_KEY_CHECKS,[GetPluginIdForCheck(998)])
