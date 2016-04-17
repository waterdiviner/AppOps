#coding=utf-8

import sys
import os

try :
	import sqlite3
except :
	print('warning>> python lib no support sqlite3')
	
reload(sys)
sys.setdefaultencoding('utf-8')

sys.path.append(os.path.join(os.getenv('QTS_BASE_PATH','..'),'pylib/utility'))
from qtsdatabase import *

class QtsSqlite(QtsDatabase) :
    def __init__(self, _dbname):
        self.dbname = _dbname
        self.conn = None
        self.Connect()

    def __del__(self):
        self.Close()

    def Connect(self):
        try:
            self.conn = sqlite3.connect(self.dbname)
        except:
            print('connect database is failed! dbname={0}'.format(self.dbname))

    def Close(self):
        try:
            self.conn.close()
            self.conn = None
        except:
            self.conn = None
            print('close database is failed! dbname={0}'.format(self.dbname))

    def Commit(self):
        self.conn.commit()

    def Exist(self, sql):
        breturn = False
        if self.Connected() :
            try:
                with self.conn as cursor :
                    cursor.execute(sql)
                    dbres = cursor.fetchall()
                    breturn = (len(dbres) > 0)
            except:
                print('query database is failed! sql={0}'.format(sql))
        return breturn

    def Execute(self, sql,commit=True):
        breturn = False
        if self.Connected() :
            try:
                with self.conn as cursor :
                    cursor.execute(sql)
                    if commit :
                        self.conn.commit()
                    breturn = True
            except:
                self.conn.rollback()
                print('write database is failed! sql={0}'.format(sql))
        return breturn

    def Connected(self):
        if self.conn != None :
            return True
        else:
            print('database is no connected! dbname={0}'.format(self.dbname))
            return False

    def Query(self,sql):
        if self.Connected() :
            try:
                with self.conn as cursor :
                    dbres = cursor.fetchall()
                    return dbres
            except:
                print('query database is failed! sql={0}'.format(sql))
        return None