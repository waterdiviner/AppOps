from qtscommon import *

if GetIsReplay() and GetReplayType() == xml :
	CreatePluginForMarket(3,ALL_MARKET,BuildTestInputFile('input.xml'),'QtsXmlReplay','CreateXmlReplay')