#coding=utf-8
from qtsbizenum import *

#######################################################################################################################################
QTS_STATUS_TYPE_STR={0:'初始化',1:'未报',2:'待报',3:'已报',6:'部撤',7:'已撤',8:'部成',9:'全成',10:'拒单'}
def GetStatusStr(status) :
    try :
        return QTS_STATUS_TYPE_STR[status]
    except Exception,e:
        return QTS_STATUS_TYPE_STR[0]

#######################################################################################################################################
QTS_ACTION_TYPE_STR={0:'买',1:'卖',255:'未知'}
def GetActionStr(action) :
    try :
        return QTS_ACTION_TYPE_STR[action]
    except Exception,e:
        return QTS_ACTION_TYPE_STR[255]

#######################################################################################################################################
QTS_POSISTION_TYPE_STR={0:'多',1:'空',255:'未知'}
def GetPosTypeStr(type) :
    try :
        return QTS_POSISTION_TYPE_STR[type]
    except Exception,e:
        return QTS_POSISTION_TYPE_STR[255]

#######################################################################################################################################
QTS_POSITION_LEVEL_STR={0:'主仓',1:'子仓',255:'未知'}
def GetPosLevelStr(level) :
    try :
        return QTS_POSITION_LEVEL_STR[type]
    except Exception,e:
        return QTS_POSITION_LEVEL_STR[255]

#######################################################################################################################################
QTS_DIRECTION_TYPE_STR={0:'未知类型',1:'开仓',2:'平仓',3:'平昨仓',4:'平今仓'}
def GetDirectionStr(direction) :
    try :
        return QTS_DIRECTION_TYPE_STR[direction]
    except Exception,e:
        return QTS_DIRECTION_TYPE_STR[0]

#######################################################################################################################################
QTS_BOOL_TYPE_STR={QTS_FALSE:'否',QTS_TRUE:'是'}
def GetBoolTypeStr(btype) :
    try :
        return QTS_BOOL_TYPE_STR[btype]
    except Exception,e:
        return QTS_BOOL_TYPE_STR[0]

#######################################################################################################################################
QTS_SUSPENSION_TYPE_STR={0:'昨日停牌',1:'今日停牌',2:'未停牌',3:'未知'}
def GetSuspensionStr(type) :
    try :
        return QTS_SUSPENSION_TYPE_STR[type]
    except Exception,e:
        return QTS_SUSPENSION_TYPE_STR[3]

#######################################################################################################################################
QTS_TRADE_TYPE_STR={0:'T+0',1:'T+1',2:'T+2',3:'T+N'}
def GetTradeStr(type) :
    try :
        return QTS_TRADE_TYPE_STR[type]
    except Exception,e:
        return QTS_TRADE_TYPE_STR[3]

#######################################################################################################################################
QTS_POSITION_MODE_STR={0:'多仓',1:'空仓',2:'双向仓'}
def GetPositionModeStr(type) :
    try :
        return QTS_POSITION_MODE_STR[type]
    except Exception,e:
        return QTS_POSITION_MODE_STR[0]

#######################################################################################################################################
def GetMarketEnum(smarket) :
    index = MARKET.INVALID
    try :
        temp = smarket.strip(' \t ').strip()
        obj = MARKET.get_by_flag(temp)
        if obj != None :
            index = obj.Key
    except Exception,e:
        index = MARKET.INVALID
    return index

def GetMarketStr(emarket) :
    name = MARKET.InvalidDisplay
    try :
        obj = MARKET.get_by_key(emarket)
        if obj != None :
            name = obj.Display
    except Exception,e:
        name = MARKET.InvalidDisplay
    return name

def GetMarketPrefix(emarket) :
    prefix = MARKET.InvalidFlag
    try :
        obj = MARKET.get_by_key(emarket)
        if obj != None :
            prefix = obj.Flag
    except Exception,e:
        prefix = MARKET.InvalidFlag
    return prefix

#######################################################################################################################################
def GetSecuCodeFlagSize(emarket) :
    return MARKET.FlagSize(emarket)

def GetSecuCodeBegin(emarket) :
    return MARKET.SecuCodeBegin(emarket)

def GetOrderCodePrefix(emarket,ordercode) :
    return MARKET.CodePrefix(emarket,ordercode)

def GetOriSecuCode(emarket,ordercode) :
    if QtsMath.IsDigit(ordercode) :
        return string.atoi(ordercode)
    secucode = 0
    try :
        size = GetSecuCodeBegin(emarket)
        temp = ordercode.strip(' \t ').strip()
        flag = temp[0:size]
        secucode = temp
        index = 0
        while size >= index :
            index += 1
            if not QtsMath.IsDigit(flag[size - index]) :
                secucode = temp[size - index + 1:]
                break
        return string.atoi(secucode)
    except Exception,e:
        secucode = 0
    return secucode

def IsValidOriSecuCode(emarket,ordercode) :
    return GetOriSecuCode(emarket,ordercode) != 0

#######################################################################################################################################
def IsIndex(market,ordercode) :
    try :
        if market == MARKET.SSE :
            return SSE.IsIndex(ordercode)
        elif market == MARKET.SZSE :
            return SZSE.IsIndex(ordercode)
        else :
            return False
    except Exception,e:
        return False

#######################################################################################################################################
def GetCategoryEnum(emarket,ordercode) :
    return CATEGORY.Category(emarket,ordercode)

def GetCategoryStr(ecategory) :
    name = CATEGORY.InvalidDisplay
    try :
        obj = CATEGORY.get_by_key(ecategory)
        if obj != None :
            name = obj.Display
    except Exception,e:
        name = CATEGORY.InvalidDisplay
    return name

def GetCategoryPrefix(emarket,secucode) :
    return CATEGORY.CodePrefix(emarket,secucode)

def GetSubCategoryEnum(emarket,ordercode) :
    return CATEGORY.SubCategory(emarket,ordercode)

#######################################################################################################################################
def IsValidOrderCode(smarket,ordercode) :
    if GetMarketEnum(smarket) == 0 :
        return False
    if GetCategoryEnum(GetMarketEnum(smarket),ordercode) == 0:
        return False
    return True

def GetSecuCode(emarket,ordercode) :
    if IsValidOriSecuCode(emarket,ordercode) :
        return CreateSecuCode(GetSubCategoryEnum(emarket,ordercode),GetOriSecuCode(emarket,ordercode))
    else :
        return 0

def GetDisplayCodeFromCode(code) :
    secucode = GetSecuCodeFromCode(code)
    category = GetCategoryFromCode(code)
    rcode = secucode
    str_secucode = str(secucode)
    if category == CATEGORY.EQUITY or category == CATEGORY.INDEX :
        if len(str_secucode) == 1 :
            rcode = '00000{0}'.format(secucode)
        elif len(str_secucode) == 2 :
            rcode = '0000{0}'.format(secucode)
        elif len(str_secucode) == 3 :
            rcode = '000{0}'.format(secucode)
        elif len(str_secucode) == 4 :
            rcode = '00{0}'.format(secucode)
        elif len(str_secucode) == 5 :
            rcode = '0{0}'.format(secucode)
    elif category == CATEGORY.FUTURES_IDX or category == CATEGORY.FUTURES :
        rcode = '{0}{1}'.format(GetCategoryPrefix(GetMarketFromCode(code),secucode),GetSubCodeFromSecuCode(secucode))
    return rcode

def GetOrderCodeFromCode(code) :
    return GetDisplayCodeFromCode(code)

def GetCodeInfo(code) :
    return (GetMarketStr(GetMarketFromCode(code)),GetCategoryStr(GetCategoryFromCode(code)),GetDisplayCodeFromCode(code))

def PrintCodeInfo(code) :
    infoes = GetCodeInfo(code)
    print('{0} {1} {2}'.format(infoes[0],infoes[1],infoes[2]))

#######################################################################################################################################
