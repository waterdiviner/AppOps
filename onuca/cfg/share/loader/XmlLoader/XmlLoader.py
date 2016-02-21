from qtscommon import *

if GetLoaderType() == xml :
	CreatePluginForLoader(996,ALL_MARKET,BuildTestInputFile('input.xml'),'QtsXmlLoader','CreateXmlLoader')