#coding=utf-8
import sys
import time
################################################################################################
#py库的路径

sys.path.append('../../pylib/utility')
sys.path.append('../../pylib/secuinfo')
from qtssecuinfo import *

if __name__ == "__main__":
	convert = QtsSecuInfoCreater(QTS_CSV_FLAG,'/home/jack/Develop/build/Debug/dist/script/secuinfo.csv','/home/jack/Develop/temp/qtsinfo_s.info','/home/jack/Develop/temp/qtsinfo_d.info')
	convert.Run()
