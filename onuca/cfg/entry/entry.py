#coding=utf-8
############################################
import sys
import os

############################################
#这些只对python入口程序有用
QTS_APP_REPLAY_PATH = os.getenv('QTS_REPLAY_PATH','f:/market') 
QTS_APP_BASE_PATH = os.getenv('QTS_BASE_PATH','{0}/../../'.format(os.path.abspath(os.curdir)))
QTS_PYTHON_LIBS_PATH = os.getenv('QTS_PYTHON_LIBS_PATH','{0}/thirdpart/python/libs'.format(QTS_APP_BASE_PATH))

############################################
#py库的路径
sys.path.append('{0}/pylib/utility'.format(QTS_APP_BASE_PATH))
sys.path.append('{0}/pylib/strategy'.format(QTS_APP_BASE_PATH))
sys.path.append('{0}/pylib/monitor'.format(QTS_APP_BASE_PATH))

############################################
from qtsfun import *

############################################
#设置应用程序的版本，release、debug和publish,定义参看qts_security.py中的定义
if GetEnv(QTS_APP_PY_VERSION_KEY,QTS_APP_RUN_VERSION_DEBUG_STR) == QTS_APP_RUN_VERSION_PUBLISH_STR :
	QTS_APP_PY_VERSION = publish
elif GetEnv(QTS_APP_PY_VERSION_KEY,QTS_APP_RUN_VERSION_DEBUG_STR) == QTS_APP_RUN_VERSION_RELEASE_STR :
	QTS_APP_PY_VERSION = release
else :
	QTS_APP_PY_VERSION = debug

if QTS_APP_PY_VERSION == debug :
	AppendEnv('PATH','{0}'.format(QTS_APP_BASE_PATH))
	AppendEnv('PATH','{0}/lib/Debug'.format(QTS_APP_BASE_PATH))
	
############################################
#设置监控时间
SetMonitorTime(30)
#创建应用
CreateRootGlobals()

############################################
#加载器类型,xfile,sqlite,mysql,mixplugin,mysql,xml
QTS_LOADER_TYPE = xfile
#备份器类型,xfile,sqlite,mysql,mixplugin,mysql,xml
QTS_BACKUP_TYPE = bfile
#回放器类型,xfile,sqlite,mysql,mixplugin,mysql,xml
QTS_REPLAY_TYPE = sqlite
#系统是否是多线程的
SetMultiThread(True)
############################################
