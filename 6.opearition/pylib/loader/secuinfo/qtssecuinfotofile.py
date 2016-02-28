#coding=utf-8
from qtssecuinfo import *

class QtsSecuInfoToFile(QtsSecuinfoConvert) :
    def __init__(self,_flag,_source,_starget,_dtarget) :
        self.sitems = dict()
        self.ditems = dict()
        self.flag = _flag
        self.source = _source
        self.starget = _starget
        self.dtarget = _dtarget
        self.reader = csv.reader(open(self.source,'rb'),delimiter=self.flag)
        self.swriter = csv.writer(open(self.starget,'wb'),delimiter=self.flag,quotechar='\r',quoting=csv.QUOTE_MINIMAL)
        self.dwriter = csv.writer(open(self.dtarget,'wb'),delimiter=self.flag,quotechar='\r',quoting=csv.QUOTE_MINIMAL)

    def Run(self) :
        self.swriter.writerow(static_secuinfo_headers)
        self.dwriter.writerow(dynamic_secuinfo_headers)
        for row in self.reader :
            self.HandleRow(row)

    def HandleStaticRow(self,static_row):
        self.swriter.writerow(static_row)
        return True

    def HandleDynamicRow(self,dynamic_row):
        self.dwriter.writerow(dynamic_row)
        return True

