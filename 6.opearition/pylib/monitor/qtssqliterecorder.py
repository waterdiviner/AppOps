#coding=utf-8

import sys
import time
import threading
from qtsmonitorrecorder import *

sys.path.append('../database')
from qtssqlite import *

class QtsSqliteRecorder(QtsMonitorRecorder):
    def __init__(self, _dbname):
        super(QtsMySqlRecorder,self).__init__(QtsSqlite(_dbname))

class QtsTestSqlite(threading.Thread) :
    def __init__(self,_mysql):
        self.mysql = _mysql
        threading.Thread.__init__(self,target=self.run)

    def run(self):
        position = QtsGProtoPosition()
        position.secuid = 33330;
        position.account = 1234560;
        position.code = 23456;
        position.type = 0;
        position.date = 20151109;
        position.totalvol = 10;
        position.avlvol = 7;
        position.workingvol = 0;
        position.totalcost = 0;
        position.level = 0;
        position.avlcredempvol = 0;
        position.todayvol = 0;
        for i in range(30):
            position.secuid = i;
            self.mysql.OnPosition(None,position)

    def start(self):
        threading.Thread.start(self)

    def stop(self):
        QtsMonitorReceiver.stop(self)
        threading.Thread.stop(self)

if __name__ == "__main__":
    qtsmysql = QtsSqliteRecorder('qts_ss_backup')
    testmysql = QtsTestSqlite(qtsmysql)
    testmysql.start()
    time.sleep(30)
    testmysql.stop()
