#coding=utf-8
from qtssecuinfo import *
sys.path.append('../database')
from qtsmysql import *

class QtsSecuInfoDBToFile(object) :
    def __init__(self,_flag,_starget,_dtarget) :
        self.sitems = dict()
        self.ditems = dict()
        self.flag = _flag
        self.starget = _starget
        self.dtarget = _dtarget
        self.db = None
        self.swriter = csv.writer(open(self.starget,'wb'),delimiter=self.flag,quotechar='\r',quoting=csv.QUOTE_MINIMAL)
        self.dwriter = csv.writer(open(self.dtarget,'wb'),delimiter=self.flag,quotechar='\r',quoting=csv.QUOTE_MINIMAL)

    def Run(self,host,port,user,psw,dbname) :
        self.db = QtsMySql(host,port,user,psw,dbname)
        self.swriter.writerow(static_secuinfo_headers)
        self.dwriter.writerow(dynamic_secuinfo_headers)
        statics = self.db.QueryAll(qts_secuinfo_s_table)
        for row in statics :
            self.HandleStaticRow(row)
        dynamics = self.db.QueryAll(qts_secuinfo_d_table)
        for row in dynamics :
            self.HandleDynamicRow(row)

    def HandleStaticRow(self,row):
        self.swriter.writerow(row[1:])
        return True

    def HandleDynamicRow(self,row):
        self.dwriter.writerow(row[1:])
        return True
