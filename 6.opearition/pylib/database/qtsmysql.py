#coding=utf-8

import sys
import os

try :
	import MySQLdb
except :
	print('warning>> python lib no support MySQLdb')

reload(sys)
sys.setdefaultencoding('utf-8')

sys.path.append(os.path.join(os.getenv('QTS_BASE_PATH','..'),'pylib/utility'))
from qtsdatabase import *

class QtsMySql(QtsDatabase) :
    def __init__(self, _address,_port,_user,_password,_dbname):
        self.address = _address
        self.port = _port
        self.user = _user
        self.password = _password
        self.dbname = _dbname
        self.conn = None
        self.Connect()

    def __del__(self):
        self.Close()

    def Connect(self):
        try:
            self.conn = MySQLdb.connect(host=self.address,port=self.port,user=self.user,passwd=self.password,db=self.dbname)
            self.conn.ping(True)
        except:
            print('connect database is failed! address={0} port={1} user={2} passwd={3} dbname={4}'.format(self.address,self.port,self.user,self.password,self.dbname))

    def Close(self):
        try:
            if self.Connected() :
                self.conn.close()
                self.conn = None
        except:
            self.conn = None
            print('close database is failed! address={0} port={1} user={2} passwd={3} dbname={4}'.format(self.address,self.port,self.user,self.password,self.dbname))

    def Commit(self):
        try:
            if self.Connected() :
                self.conn.commit()
        except:
            print('commit is failed!')

    def Exist(self, sql):
        breturn = False
        if self.Connected() and sql != None:
            try:
                with self.conn as cursor :
                    cursor.execute(sql)
                    dbres = cursor.fetchall()
                    breturn = (len(dbres) > 0)
            except:
                print('query database is failed!sql:{0}'.format(sql))
        return breturn

    def Execute(self, sql,commit=True):
        breturn = False
        if self.Connected() and sql != None:
            try:
                with self.conn as cursor :
                    cursor.execute(sql)
                    if commit :
                        self.conn.commit()
                    breturn = True
            except:
                self.conn.rollback()
                print('write database is failed!sql:{0}'.format(sql))
        return breturn

    def Connected(self):
        if self.conn != None :
            return True
        else:
            print('database is no connected! address={0} port={1} user={2} passwd={3} dbname={4}'.format(self.address,self.port,self.user,self.password,self.dbname))
            return False

    def Query(self,sql):
        if self.Connected() and sql != None :
            try:
                with self.conn as cursor :
                    cursor.execute(sql)
                    dbres = cursor.fetchall()
                    return dbres
            except:
                print('query database is failed!sql:{0}'.format(sql))
        return None