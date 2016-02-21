from qtscommon import *

if GetLoaderType() == sqlite :
	CreatePluginForLoader(998,ALL_MARKET,GetDataPath('qtsloader.db3'),'QtsSQLiteLoader','CreateSQLiteLoader')