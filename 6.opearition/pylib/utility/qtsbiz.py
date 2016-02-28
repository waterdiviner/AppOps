#coding=utf-8
import os
import sys
import string
import platform
import traceback
from qtssecurity import *

#######################################################################################################################################
def GetPyTradeDate(timestamp) :
    return ((timestamp >> 32) & 0x00000000FFFFFFFF)

def GetPyTradeTime(timestamp) :
    return (timestamp & 0x00000000FFFFFFFF)

def CreatePyTradeTime(date,time) :
    return (((date << 32) & 0x00000000FFFFFFFF) | (time & 0x00000000FFFFFFFF))

#######################################################################################################################################
def GetMarketFromCode(code) :
    return ((code >> 48) & 0x000000000000FFFF)

def GetCategoryFromCode(code) :
    return ((code >> 32) & 0x000000000000FFFF)

def GetSecuCodeFromCode(code) :
    return (code & 0x00000000FFFFFFFF)

def GetSubCategoryFromCode(code) :
    return ((GetSecuCodeFromCode(code) >> 24) & 0x000000FF)

def GetSubCategoryFromSecuCode(secucode) :
    return ((secucode >> 24) & 0x000000FF)

def GetSubCodeFromSecuCode(secucode) :
    return (secucode& 0x00FFFFFF)

def GetRealPrice(price) :
    return float(float(price) / float(10000))

def GetSystemPrice(price) :
    return long((price + 0.00005) * 10000)

def CreateSecuCode(subcategory,num) :
    return (((subcategory << 24) & 0xFF000000) | (num & 0x00FFFFFF))

def CreateCode(market,category,secucode) :
    return (((market << 48) & 0xFFFF000000000000) | ((category << 32) & 0x0000FFFF00000000) | (secucode & 0x00000000FFFFFFFF))

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
Qts_Market_Enum={'SZE':SZ_MARKET,'SSE':SH_MARKET,'CFFEX':ZJ_MARKET,'DCE':DL_MARKET,'CZCE':ZZ_MARKET,'SHFE':SQ_MARKET,'SMART':SMART_MARKET}
def GetMarketEnum(smarket) :
    index = 0
    try :
        temp = smarket.strip(' \t ').strip()
        index = Qts_Market_Enum[temp]
    except Exception,e:
        index = 0
    return index

Qts_Market_Names={SZ_MARKET:'深市',SH_MARKET:'沪市',ZJ_MARKET:'中金',DL_MARKET:'大连',ZZ_MARKET:'郑州',SQ_MARKET:'上期',SMART_MARKET:'国外'}
def GetMarketStr(emarket) :
    name = '未知'
    try :
        name = Qts_Market_Names[emarket]
    except Exception,e:
        name = '未知'
    return name

Qts_Market_Prefixes={SZ_MARKET:'SZE',SH_MARKET:'SSE',ZJ_MARKET:'CFFEX',DL_MARKET:'DCE',ZZ_MARKET:'CZCE',SQ_MARKET:'SHFE',SMART_MARKET:'SMART'}
def GetMarketPrefix(emarket) :
    prefix = ''
    try :
        prefix = Qts_Market_Prefixes[emarket]
    except Exception,e:
        prefix = ''
    return prefix

#######################################################################################################################################
def IsDigit(value) :
    return all(c in "0123456789" for c in str(value))

Qts_SecuCodeFlag_Size={SZ_MARKET:1,SH_MARKET:1,ZJ_MARKET:2,DL_MARKET:2,ZZ_MARKET:2,SQ_MARKET:2}
def GetSecuCodeFlagSize(emarket) :
    size = 0
    try :
        size = Qts_SecuCodeFlag_Size[emarket]
    except Exception,e:
        size = 0
    return size

def GetOrderCodePrefix(emarket,ordercode) :
    flag = ''
    try :
        size = GetSecuCodeFlagSize(emarket)
        temp = ordercode.strip(' \t ').strip()
        if emarket == DL_MARKET :
            flag = temp[0:size]
            if IsDigit(flag[size-1]) :
                flag = temp[0:size-1]
        else :
            flag = temp[0:size]
    except Exception,e:
        flag = ''
    return flag

def GetOriSecuCode(emarket,ordercode) :
    if IsDigit(ordercode) :
        return string.atoi(ordercode)
    secucode = 0
    try :
        size = GetSecuCodeFlagSize(emarket)
        temp = ordercode.strip(' \t ').strip()
        if emarket == DL_MARKET :
            flag = temp[0:size]
            if IsDigit(flag[size-1]) :
                secucode = temp[size-1:]
            else :
                secucode = temp[size:]
        else :
            secucode = temp[size:]
        return string.atoi(secucode)
    except Exception,e:
        secucode = 0
    return secucode

def IsValidOriSecuCode(emarket,ordercode) :
    return GetOriSecuCode(emarket,ordercode) != 0

#######################################################################################################################################
Qts_SH_Indexes=['000001','000002','000003','000004','000005','000006','000007','000008','000011','000012','000013',
                '000015','000016','000019','000048','000401','000820','000901']
def IsIndex(market,ordercode) :
    try :
        if market == SH_MARKET :
            if ordercode in Qts_SH_Indexes :
                return True
        elif market == SZ_MARKET :
            if (int(ordercode) >= 399001) and (int(ordercode) <= 399999):
                return True
        else :
            return False
    except Exception,e:
        return False

#######################################################################################################################################
Qts_Equit_Category_Enum={'0':EQUIT_CATEGORY,'1':EQUIT_CATEGORY,'3':EQUIT_CATEGORY,'5':EQUIT_CATEGORY,'6':EQUIT_CATEGORY,'7':EQUIT_CATEGORY}
Qts_ZJ_Category_Enum={'IF':IF_CATEGORY,'IH':IF_CATEGORY,'IC':IF_CATEGORY}
Qts_DL_Category_Enum={'a':CF_CATEGORY,'b':CF_CATEGORY,'bb':CF_CATEGORY,'c':CF_CATEGORY,'cs':CF_CATEGORY,'f':CF_CATEGORY,
                      'i':CF_CATEGORY,'j':CF_CATEGORY,'jd':CF_CATEGORY,'jm':CF_CATEGORY,'l':CF_CATEGORY,'m':CF_CATEGORY,
                      'p':CF_CATEGORY,'pp':CF_CATEGORY,'v':CF_CATEGORY,'y':CF_CATEGORY}
Qts_ZZ_Category_Enum={'CF':CF_CATEGORY,'FG':CF_CATEGORY,'JR':CF_CATEGORY,'LR':CF_CATEGORY,'MA':CF_CATEGORY,'OI':CF_CATEGORY,
                      'PM':CF_CATEGORY,'RJ':CF_CATEGORY,'RM':CF_CATEGORY,'RS':CF_CATEGORY,'SF':CF_CATEGORY,'SM':CF_CATEGORY,
                      'SR':CF_CATEGORY,'TA':CF_CATEGORY,'TC':CF_CATEGORY,'WH':CF_CATEGORY,'ZC':CF_CATEGORY}
Qts_SQ_Category_Enum={'ag':CF_CATEGORY,'al':CF_CATEGORY,'aa':CF_CATEGORY,'bu':CF_CATEGORY,'cu':CF_CATEGORY,'fu':CF_CATEGORY,
                      'hc':CF_CATEGORY,'ni':CF_CATEGORY,'pb':CF_CATEGORY,'rb':CF_CATEGORY,'ru':CF_CATEGORY,'sn':CF_CATEGORY,
                      'wr':CF_CATEGORY,'zn':CF_CATEGORY}
def GetCategoryEnum(emarket,ordercode) :
    index = 0
    try :
        if emarket == ZJ_MARKET :
            flag = GetOrderCodePrefix(emarket,ordercode)
            index = Qts_ZJ_Category_Enum[flag]
        elif emarket == DL_MARKET :
            flag = GetOrderCodePrefix(emarket,ordercode)
            index = Qts_DL_Category_Enum[flag]
        elif emarket == ZZ_MARKET :
            flag = GetOrderCodePrefix(emarket,ordercode)
            index = Qts_ZZ_Category_Enum[flag]
        elif emarket == SQ_MARKET :
            flag = GetOrderCodePrefix(emarket,ordercode)
            index = Qts_SQ_Category_Enum[flag]
        else :
            if IsIndex(emarket,ordercode) :
                return INDEX_CATEGORY
            else :
                flag = GetOrderCodePrefix(emarket,ordercode)
                index = Qts_Equit_Category_Enum[flag]
    except Exception,e:
        index = 0
    return index

Qts_Category_Names={EQUIT_CATEGORY:'股票',INDEX_CATEGORY:'指数',IF_CATEGORY:'股指期货',CF_CATEGORY:'商品期货',OPTION_CATEGORY:'期权',BOND_CATEGORY:'债券',ETF_CATEGORY:'基金'}
def GetCategoryStr(ecategory) :
    name = '未知'
    try :
        name = Qts_Category_Names[ecategory]
    except Exception,e:
        name = '未知'
    return name

Qts_ZJ_Futures_Prefixes={ZJ_IF_SUB_CATEGORY:'IF',ZJ_IH_SUB_CATEGORY:'IH',ZJ_IC_SUB_CATEGORY:'IC'}
Qts_DL_Futures_Prefixes={DL_A_SUB_CATEGORY:'a',DL_B_SUB_CATEGORY:'b',DL_BB_SUB_CATEGORY:'bb',DL_C_SUB_CATEGORY:'c',DL_CS_SUB_CATEGORY:'cs',
                         DL_FB_SUB_CATEGORY:'f',DL_I_SUB_CATEGORY:'i',DL_J_SUB_CATEGORY:'j',DL_JD_SUB_CATEGORY:'jd',DL_JM_SUB_CATEGORY:'jm',
                         DL_L_SUB_CATEGORY:'l',DL_M_SUB_CATEGORY:'m',DL_P_SUB_CATEGORY:'p',DL_PP_SUB_CATEGORY:'pp',DL_V_SUB_CATEGORY:'v',
                         DL_Y_SUB_CATEGORY:'y'}
Qts_ZZ_Futures_Prefixes={ZZ_CF_SUB_CATEGORY:'CF',ZZ_FG_SUB_CATEGORY:'FG',ZZ_JR_SUB_CATEGORY:'JR',ZZ_LR_SUB_CATEGORY:'LR',ZZ_MA_SUB_CATEGORY:'MA',
                         ZZ_OI_SUB_CATEGORY:'OI',ZZ_PM_SUB_CATEGORY:'PM',ZZ_RJ_SUB_CATEGORY:'RJ',ZZ_RM_SUB_CATEGORY:'RM',ZZ_RS_SUB_CATEGORY:'RS',
                         ZZ_SF_SUB_CATEGORY:'SF',ZZ_SM_SUB_CATEGORY:'SM',ZZ_SR_SUB_CATEGORY:'SR',ZZ_TA_SUB_CATEGORY:'TA',ZZ_TC_SUB_CATEGORY:'TC',
                         ZZ_WH_SUB_CATEGORY:'WH',ZZ_ZC_SUB_CATEGORY:'ZC'}
Qts_SQ_Futures_Prefixes={SQ_AG_SUB_CATEGORY:'ag',SQ_AL_SUB_CATEGORY:'al',SQ_AU_SUB_CATEGORY:'au',SQ_BU_SUB_CATEGORY:'bu',SQ_CU_SUB_CATEGORY:'cu',
                         SQ_FU_SUB_CATEGORY:'fu',SQ_HC_SUB_CATEGORY:'hc',SQ_NI_SUB_CATEGORY:'ni',SQ_PB_SUB_CATEGORY:'pb',SQ_RB_SUB_CATEGORY:'rb',
                         SQ_RU_SUB_CATEGORY:'ru',SQ_SN_SUB_CATEGORY:'sn',SQ_WR_SUB_CATEGORY:'wr',SQ_ZN_SUB_CATEGORY:'zn'}
def GetCategoryPrefix(emarket,secucode) :
    try :
        if (emarket == SZ_MARKET) or (emarket == SH_MARKET) :
            return ''
        elif emarket == ZJ_MARKET :
            return Qts_ZJ_Futures_Prefixes[GetSubCategoryFromSecuCode(secucode)]
        elif emarket == DL_MARKET :
            return Qts_DL_Futures_Prefixes[GetSubCategoryFromSecuCode(secucode)]
        elif emarket == ZZ_MARKET :
            return Qts_ZZ_Futures_Prefixes[GetSubCategoryFromSecuCode(secucode)]
        elif emarket == SQ_MARKET :
            return Qts_SQ_Futures_Prefixes[GetSubCategoryFromSecuCode(secucode)]
        else :
            return ''
    except Exception,e:
        return ''

Qts_ZJ_Futures_Enum={'IF':ZJ_IF_SUB_CATEGORY,'IH':ZJ_IH_SUB_CATEGORY,'IC':ZJ_IC_SUB_CATEGORY}
Qts_DL_Futures_Enum={'a':DL_A_SUB_CATEGORY,'b':DL_B_SUB_CATEGORY,'bb':DL_BB_SUB_CATEGORY,'c':DL_C_SUB_CATEGORY,'cs':DL_CS_SUB_CATEGORY,
                     'f':DL_FB_SUB_CATEGORY,'i':DL_I_SUB_CATEGORY,'j':DL_J_SUB_CATEGORY,'jd':DL_JD_SUB_CATEGORY,'jm':DL_JM_SUB_CATEGORY,
                     'l':DL_L_SUB_CATEGORY,'m':DL_M_SUB_CATEGORY,'p':DL_P_SUB_CATEGORY,'pp':DL_PP_SUB_CATEGORY,'v':DL_V_SUB_CATEGORY,
                     'y':DL_Y_SUB_CATEGORY}
Qts_ZZ_Futures_Enum={'CF':ZZ_CF_SUB_CATEGORY,'FG':ZZ_FG_SUB_CATEGORY,'JR':ZZ_JR_SUB_CATEGORY,'LR':ZZ_LR_SUB_CATEGORY,'MA':ZZ_MA_SUB_CATEGORY,
                     'OI':ZZ_OI_SUB_CATEGORY,'PM':ZZ_PM_SUB_CATEGORY,'RJ':ZZ_RJ_SUB_CATEGORY,'RM':ZZ_RM_SUB_CATEGORY,'RS':ZZ_RS_SUB_CATEGORY,
                     'SF':ZZ_SF_SUB_CATEGORY,'SM':ZZ_SM_SUB_CATEGORY,'SR':ZZ_SR_SUB_CATEGORY,'TA':ZZ_TA_SUB_CATEGORY,'TC':ZZ_TC_SUB_CATEGORY,
                     'WH':ZZ_WH_SUB_CATEGORY,'ZC':ZZ_ZC_SUB_CATEGORY}
Qts_SQ_Futures_Enum={'ag':SQ_AG_SUB_CATEGORY,'al':SQ_AL_SUB_CATEGORY,'au':SQ_AU_SUB_CATEGORY,'bu':SQ_BU_SUB_CATEGORY,'cu':SQ_CU_SUB_CATEGORY,
                     'fu':SQ_FU_SUB_CATEGORY,'hc':SQ_HC_SUB_CATEGORY,'ni':SQ_NI_SUB_CATEGORY,'pb':SQ_PB_SUB_CATEGORY,'rb':SQ_RB_SUB_CATEGORY,
                     'ru':SQ_RU_SUB_CATEGORY,'sn':SQ_SN_SUB_CATEGORY,'wr':SQ_WR_SUB_CATEGORY,'zn':SQ_ZN_SUB_CATEGORY}
def GetSubCategoryEnum(emarket,ordercode) :
    try :
        if (emarket == SZ_MARKET) or (emarket == SH_MARKET) :
            return 0
        elif emarket == ZJ_MARKET :
            return Qts_ZJ_Futures_Enum[GetOrderCodePrefix(emarket,ordercode)]
        elif emarket == DL_MARKET :
            return Qts_DL_Futures_Enum[GetOrderCodePrefix(emarket,ordercode)]
        elif emarket == ZZ_MARKET :
            return Qts_ZZ_Futures_Enum[GetOrderCodePrefix(emarket,ordercode)]
        elif emarket == SQ_MARKET :
            return Qts_SQ_Futures_Enum[GetOrderCodePrefix(emarket,ordercode)]
        else :
            return 0
    except Exception,e:
        return 0

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
    if category == EQUIT_CATEGORY :
        if len(secucode) == 1 :
            rcode = '00000{0}'.format(secucode)
        elif len(secucode) == 2 :
            rcode = '0000{0}'.format(secucode)
        elif len(secucode) == 3 :
            rcode = '000{0}'.format(secucode)
        elif len(secucode) == 4 :
            rcode = '00{0}'.format(secucode)
        elif len(secucode) == 5 :
            rcode = '0{0}'.format(secucode)
    elif category == IF_CATEGORY :
        rcode = '{0}{1}'.format(GetCategoryPrefix(GetMarketFromCode(code),secucode),GetSubCodeFromSecuCode(secucode))
    return rcode

def GetOrderCodeFromCode(code) :
    return GetDisplayCodeFromCode(code)

#######################################################################################################################################



#######################################################################################################################################