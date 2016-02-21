from qtscommon import *

CreatePluginForAlgo(1,[[ZJ_MARKET,IF_CATEGORY],[ZJ_MARKET,IC_CATEGORY],[ZJ_MARKET,IH_CATEGORY],[DL_MARKET,JD_CATEGORY]],'','QtsFutureAlgo','CreateFutureAlgo')
#AppendPropertyForAlgo(1,QTS_CFG_KEY_MINORDERID,BuildAlgoOrderId(2,0))
AppendPropertyForAlgo(1,QTS_CFG_KEY_ALGOES,[GetPluginIdForAlgo(2)])
#QTS_CFG_KEY_BACKUP: index is 0 backup gwftrecord
#[BuildBackupFile('gwftrecord')]
#[BuildBackupFile(None)]	
AppendPropertyForAlgo(1,QTS_CFG_KEY_BACKUP,[BuildBackupFile(QTS_BACKUP_GW_TRADE_CHILD_RECORD)])