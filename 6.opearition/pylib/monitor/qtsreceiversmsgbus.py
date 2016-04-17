import sys
sys.path.append(os.path.join(os.getenv('QTS_BASE_PATH','..'),'pylib/utility'))
from qtssingleton import singleton
from qtsdelegate import delegate

@singleton
class QtsReceiversMsgBus(object):
    def __init__(self):
        self.EOnPosition    = delegate (proto='OnPosition()')
        self.EOnAccount     = delegate (proto='OnAccount()')
        self.EOnRecord      = delegate (proto='OnRecord()')
        self.EOnMessage     = delegate (proto='OnMessage()')
        self.EOnStrategy    = delegate (proto='OnStrategy()')
        self.EOnControl     = delegate (proto='OnControl()')
        self.EOnParameter   = delegate (proto='OnParameter()')
        self.EOnData        = delegate (proto='OnData()')
        self.EOnPnl         = delegate (proto='OnPnl()')
        self.EOnWorking     = delegate (proto='OnWorking()')
        self.EOnBook        = delegate (proto='OnBook()')
        self.EOnEvent       = delegate (proto='OnEvent()')
        self.EOnRemote      = delegate (proto='OnRemote()')
