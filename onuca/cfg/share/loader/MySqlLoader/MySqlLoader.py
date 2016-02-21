from qtscommon import *

if GetLoaderType() == mysql :
	CreatePluginForLoader(997,ALL_MARKET,'root@localhost:1111:qtsloader','QtsMySqlLoader','CreateMySqlLoader')