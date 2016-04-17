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
        self.bopen = True
        if os.path.isfile(self.source) :
            self.reader = csv.reader(open(self.source,'rb'),delimiter=self.flag)
        else :
            self.bopen = False
            TraceError('open file {0} is failed!'.format(self.source))
        self.swriter = csv.writer(open(self.starget,'wb'),delimiter=self.flag,quotechar='\r',quoting=csv.QUOTE_MINIMAL)
        self.dwriter = csv.writer(open(self.dtarget,'wb'),delimiter=self.flag,quotechar='\r',quoting=csv.QUOTE_MINIMAL)

    def Run(self) :
        if self.bopen :
            self.swriter.writerow(static_secuinfo_headers)
            self.dwriter.writerow(dynamic_secuinfo_headers)
            for row in self.reader :
                self.HandleRow(row)
        else :
            TraceError('file is not opened!')

    def HandleStaticRow(self,static_row):
        self.swriter.writerow(static_row)
        return True

    def HandleDynamicRow(self,dynamic_row):
        self.dwriter.writerow(dynamic_row)
        return True

