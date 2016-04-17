#coding=utf-8
import sys
import os
sys.path.append(os.path.join(os.getenv('QTS_BASE_PATH','../..'),'pylib/utility'))
sys.path.append(os.path.join(os.getenv('QTS_BASE_PATH','../..'),'pylib/qtsplat/share'))
from qtsfun import *
try :
    from qtsgproto_pb2 import *
except :
    print('warning>> python lib no support protocol buffer')
from qtsenvir import *
from qtsguiapi import *
from qtsadapter import *
from qtspycfg import *

g_oGuiApp=None
def OnEvent(itype,subtype,pro,data,size,para) :
    TraceMessage('receive event!')
    #global g_oGuiApp
    #g_oGuiApp.onevent(itype,subtype,pro,data,size,para)
    return 1

class QtsGuiApp(object) :
    def __init__(self):
        g_oGuiApp = self
        self.bcreate = False
        self.args = '{0} {1}={2} {3}={4} {5}={6}'.format(BuildLocalCfg('qtsgui','CreateConfig','QtsPythonDCfg',
                                                    GetProtoPath(),GetProtoFile()),QTS_EVN_FILE_KEY,
                                                    CombinePath(GetEntryPath(),'mainrs_all.qts'),
                                                    QTS_TRACE_MESSAGE_KEY,GetTraceMessage(),
                                                    QTS_TRACE_DEBUG_KEY,GetTraceDebug())
        self.fun = QTS_ADAPTER_EVENT_CALLBACK(OnEvent)

    def RegisterGuiEvent(self) :
        RegisterEvent(QTS_GPROTO_EVENT_TYPE_INIT,self.fun)
        RegisterEvent(QTS_GPROTO_EVENT_TYPE_DATA,self.fun)
        RegisterEvent(QTS_GPROTO_EVENT_TYPE_PARAMETER,self.fun)
        RegisterEvent(QTS_GPROTO_EVENT_TYPE_STRATEGY_START,self.fun)
        RegisterEvent(QTS_GPROTO_EVENT_TYPE_STRATEGY_PAUSE,self.fun)
        RegisterEvent(QTS_GPROTO_EVENT_TYPE_STRATEGY_WATCH,self.fun)
        RegisterEvent(QTS_GPROTO_EVENT_TYPE_STRATEGY_STOP,self.fun)
        RegisterEvent(QTS_GPROTO_EVENT_TYPE_RETURN,self.fun)
        RegisterEvent(QTS_GPROTO_EVENT_TYPE_MESSAGE,self.fun)
        RegisterEvent(QTS_GPROTO_EVENT_TYPE_CONTROL,self.fun)
        RegisterEvent(QTS_GPROTO_EVENT_TYPE_STRATEGYINFO,self.fun)
        RegisterEvent(QTS_GPROTO_EVENT_TYPE_DATAEND,self.fun)
        RegisterCfgEvent()

    def create(self):
        try :
            self.RegisterGuiEvent()
            if qts_CreateAppcation(self.args) :
                TraceMessage('create application is success!')
                qts_RegisterCallbacks()
                qts_RegisterCommands()
                qts_RequestDatas()
                self.bcreate = True
            else :
                TraceError('create application is failed!')
        except Exception,e:
            traceback.print_exc()

    def destroy(self):
        if self.bcreate :
            qts_DestroyApplication()

    def run(self):
        self.create()
        if self.bcreate :
            self.onrun()
            command = ''
            while True :
                command = sys.stdin.readline()
                if command[:-1] == 'quit' :
                    break
                time.sleep(1)
        self.destroy()

    def onevent(self,itype,subtype,pro,data,size,para):
        TraceMessage('receive event!')

    def onrun(self):pass
