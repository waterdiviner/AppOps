#coding=utf-8
from singletonno import singletonno
from qtsmath import *
from qtsbiztype import *

#######################################################################################################################################
@singletonno
class QtsMarketEnum(QtsEnum) :
    def __init__(self) :
        QtsEnum.__init__(self)
        self._ALL = self.add(0,'ALL','ALL','全市场')
        self._SZSE = self.add(1,'SZSE','SZSE','深市','SZSE',qts_flag_size=1,qts_secucode_begin=0)
        self._SSE = self.add(2,'SSE','SSE','沪市','SSE',qts_flag_size=1,qts_secucode_begin=0)
        self._CFFEX = self.add(3,'CFFEX','CFFEX','中金','CFFEX',qts_flag_size=2,qts_secucode_begin=2)
        self._DCE = self.add(4,'DCE','DCE','大连','DCE',qts_flag_size=2,qts_secucode_begin=2)
        self._CZCE = self.add(5,'CZCE','CZCE','郑州','CZCE',qts_flag_size=2,qts_secucode_begin=2)
        self._SHFE = self.add(6,'SHFE','SHFE','上期','SHFE',qts_flag_size=2,qts_secucode_begin=2)
        self._SMART = self.add(10,'SMART','SMART','国外','SMART')

    @property
    def ALL(self):
        return self._ALL
    @property
    def SZSE(self):
        return self._SZSE

    @property
    def SSE(self):
        return self._SSE

    @property
    def CFFEX(self):
       return self._CFFEX

    @property
    def DCE(self):
        return self._DCE

    @property
    def CZCE(self):
        return self._CZCE

    @property
    def SHFE(self):
        return self._SHFE

    @property
    def SMART(self):
        return self._SMART

    def SecuCodeBegin(self,market):
        size = 0
        try :
            obj = self.get_by_key(market)
            if obj != None :
                size = obj.Item('qts_secucode_begin')
        except Exception,e:
            size = 0
        return size

    def FlagSize(self,market):
        size = 0
        try :
            obj = self.get_by_key(market)
            if obj != None :
                size = obj.Item('qts_flag_size')
        except Exception,e:
            size = 0
        return size

    def CodePrefix(self,market,ordercode) :
        flag = ''
        try :
            size = self.FlagSize(market)
            temp = ordercode.strip(' \t ').strip()
            if (market == self.SSE) or (market == self.SZSE) :
                flag = temp[0:size]
            else :
                flag = temp[0:size]
                if QtsMath.IsDigit(flag[size-1]) :
                    flag = temp[0:size-1]
        except Exception,e:
            flag = ''
        return flag

MARKET = QtsMarketEnum()

#######################################################################################################################################
@singletonno
class QtsCATEGORY(QtsEnum) :
    def __init__(self) :
        QtsEnum.__init__(self)
        self._ALL = self.add(0,'ALL','ALL','全品种')
        self._EQUITY = self.add(1,'EQUITY','EQUITY','股票')
        self._INDEX = self.add(2,'INDEX','INDEX','指数')
        self._FUTURES_IDX = self.add(3,'FUTURES_IDX','FUTURES_IDX','股指期货')
        self._FUTURES = self.add(4,'FUTURES','FUTURES','商品期货')
        self._OPTION = self.add(5,'OPTION','OPTION','期权')
        self._BOND = self.add(6,'BOND','BOND','债券')
        self._ETF = self.add(7,'ETF','ETF','基金')

    @property
    def ALL(self):
        return self._ALL

    @property
    def EQUITY(self):
        return self._EQUITY

    @property
    def INDEX(self):
        return self._INDEX

    @property
    def FUTURES_IDX(self):
        return self._FUTURES_IDX

    @property
    def FUTURES(self):
        return self._FUTURES

    @property
    def OPTION(self):
        return self._OPTION

    @property
    def BOND(self):
        return self._BOND

    @property
    def ETF(self):
        return self._ETF

    def Category(self,emarket,ordercode) :
        category = CATEGORY.INVALID
        try :
            if emarket == MARKET.CFFEX :
                flag = MARKET.CodePrefix(emarket,ordercode)
                obj = CFFEX.get_by_flag(flag)
                if obj != None :
                    category = obj.Item('category')
            elif emarket == MARKET.DCE :
                flag = MARKET.CodePrefix(emarket,ordercode)
                obj = DCE.get_by_flag(flag)
                if obj != None :
                    category = obj.Item('category')
            elif emarket == MARKET.CZCE :
                flag = MARKET.CodePrefix(emarket,ordercode)
                obj = CZCE.get_by_flag(flag)
                if obj != None :
                    category = obj.Item('category')
            elif emarket == MARKET.SHFE :
                flag = MARKET.CodePrefix(emarket,ordercode)
                obj = SHFE.get_by_flag(flag)
                if obj != None :
                    category = obj.Item('category')
            elif emarket == MARKET.SZSE :
                if SZSE.IsIndex(ordercode) :
                    return CATEGORY.INDEX
                else :
                    return CATEGORY.EQUITY
            elif emarket == MARKET.SSE :
                if SSE.IsIndex(ordercode) :
                    return CATEGORY.INDEX
                else :
                    return CATEGORY.EQUITY
        except Exception,e:
            category = CATEGORY.INVALID
        return category

    def CodePrefix(self,market,secucode):
        flag = ''
        try :
            if market == MARKET.CFFEX :
                obj = CFFEX.get_by_key(GetSubCategoryFromSecuCode(secucode))
                if obj != None :
                    flag = obj.Flag
            elif market == MARKET.DCE :
                obj = DCE.get_by_key(GetSubCategoryFromSecuCode(secucode))
                if obj != None :
                    flag = obj.Flag
            elif market == MARKET.CZCE :
                obj = CZCE.get_by_key(GetSubCategoryFromSecuCode(secucode))
                if obj != None :
                    flag = obj.Flag
            elif market == MARKET.SHFE :
                obj = SHFE.get_by_key(GetSubCategoryFromSecuCode(secucode))
                if obj != None :
                    flag = obj.Flag
        except Exception,e:
            flag = ''
        return flag

    def SubCategory(self,market,ordercode):
        category = CATEGORY.INVALID
        try :
            if market == MARKET.CFFEX :
                obj = CFFEX.get_by_flag(MARKET.CodePrefix(market,ordercode))
                if obj != None :
                    category = obj.Key
            elif market == MARKET.DCE :
                obj = DCE.get_by_flag(MARKET.CodePrefix(market,ordercode))
                if obj != None :
                    category = obj.Key
            elif market == MARKET.CZCE :
                obj = CZCE.get_by_flag(MARKET.CodePrefix(market,ordercode))
                if obj != None :
                    category = obj.Key
            elif market == MARKET.SHFE :
                obj = SHFE.get_by_flag(MARKET.CodePrefix(market,ordercode))
                if obj != None :
                    category = obj.Key
        except Exception,e:
            category = CATEGORY.INVALID
        return category

CATEGORY = QtsCATEGORY()

#######################################################################################################################################
#上海品种子集
@singletonno
class QtsSSE(QtsEnum) :
    def __init__(self) :
        QtsEnum.__init__(self)
        self._EQUITY = self.add(1,'EQUITY','EQUITY','股票',['0','1','3','5','6','7'])
        self._INDEX = self.add(2,'INDEX','INDEX','指数',['000001','000002','000003','000004','000005','000006','000007','000008','000011','000012','000013',
                '000015','000016','000019','000048','000401','000820','000901'])

    @property
    def INDEX(self):
        return self._INDEX

    @property
    def EQUITY(self):
        return self._EQUITY

    def IsIndex(self,code):
        return (code in self.get_by_key(self.INDEX).Flag)

SSE = QtsSSE()

#######################################################################################################################################
#深圳品种子集
@singletonno
class QtsSZSE(QtsEnum) :
    def __init__(self) :
        QtsEnum.__init__(self)
        self._EQUITY = self.add(1,'EQUITY','EQUITY','股票',['0','1','3','5','6','7'])
        self._INDEX = self.add(2,'INDEX','INDEX','指数',[399001,399999])

    @property
    def INDEX(self):
        return self._INDEX

    @property
    def EQUITY(self):
        return self._EQUITY

    def IsIndex(self,code):
        obj = self.get_by_key(self.INDEX)
        if (int(code) >= obj.Flag[0]) and (int(code) <= obj.Flag[1]) :
            return True
        return False

SZSE = QtsSZSE()

#######################################################################################################################################
#中金品种子集
@singletonno
class QtsCFFEX(QtsEnum) :
    def __init__(self) :
        QtsEnum.__init__(self)
        self._IF = self.add(1,'IF','IF','沪深指数期货','IF',category=CATEGORY.FUTURES_IDX)
        self._IH = self.add(2,'IH','IH','上证指数期货','IH',category=CATEGORY.FUTURES_IDX)
        self._IC = self.add(3,'IC','IC','中证指数期货','IC',category=CATEGORY.FUTURES_IDX)
        self._T = self.add(4,'T','T','国债期货','T',category=CATEGORY.FUTURES_IDX)
        self._TF = self.add(5,'TF','TF','国债期货','TF',category=CATEGORY.FUTURES_IDX)

    @property
    def IF(self):
        return self._IF

    @property
    def IH(self):
        return self._IH

    @property
    def IC(self):
        return self._IC

    @property
    def T(self):
        return self._T

    @property
    def TF(self):
        return self._TF

CFFEX = QtsCFFEX()

#######################################################################################################################################
#大连品种子集
@singletonno
class QtsDCE(QtsEnum) :
    def __init__(self) :
        QtsEnum.__init__(self)
        self._a = self.add(1,'a','a','豆一商品期货','a',category=CATEGORY.FUTURES)
        self._b = self.add(2,'b','b','豆二商品期货','b',category=CATEGORY.FUTURES)
        self._bb = self.add(3,'bb','bb','胶板商品期货','bb',category=CATEGORY.FUTURES)
        self._c = self.add(4,'c','c','玉米商品期货','c',category=CATEGORY.FUTURES)
        self._cs = self.add(5,'cs','cs','淀粉商品期货','cs',category=CATEGORY.FUTURES)
        self._fb = self.add(6,'fb','fb','纤板商品期货','fb',category=CATEGORY.FUTURES)
        self._i = self.add(7,'i','i','铁矿商品期货','i',category=CATEGORY.FUTURES)
        self._j = self.add(8,'j','j','焦炭商品期货','j',category=CATEGORY.FUTURES)
        self._jd = self.add(9,'jd','jd','鸡蛋商品期货','jd',category=CATEGORY.FUTURES)
        self._jm = self.add(10,'jm','jm','焦煤商品期货','jm',category=CATEGORY.FUTURES)
        self._l = self.add(11,'l','l','塑料商品期货','l',category=CATEGORY.FUTURES)
        self._m = self.add(12,'m','m','豆粕商品期货','m',category=CATEGORY.FUTURES)
        self._p = self.add(13,'p','p','棕榈品期货','p',category=CATEGORY.FUTURES)
        self._pp = self.add(14,'pp','pp','PP商品期货','pp',category=CATEGORY.FUTURES)
        self._v = self.add(15,'v','v','PVC商品期货','v',category=CATEGORY.FUTURES)
        self._y = self.add(16,'y','y','豆油商品期货','y',category=CATEGORY.FUTURES)

    @property
    def a(self):
        return self._a

    @property
    def b(self):
        return self._b

    @property
    def bb(self):
        return self._bb

    @property
    def c(self):
        return self._c

    @property
    def cs(self):
        return self._cs

    @property
    def fb(self):
        return self._fb

    @property
    def i(self):
        return self._i

    @property
    def j(self):
        return self._j

    @property
    def jd(self):
        return self._jd

    @property
    def jm(self):
        return self._jm

    @property
    def l(self):
        return self._l

    @property
    def m(self):
        return self._m

    @property
    def p(self):
        return self._p

    @property
    def pp(self):
        return self._pp

    @property
    def v(self):
        return self._v

    @property
    def y(self):
        return self._y

DCE = QtsDCE()

#######################################################################################################################################
#郑州品种子集
@singletonno
class QtsCZCE(QtsEnum) :
    def __init__(self) :
        QtsEnum.__init__(self)
        self._CF = self.add(1,'CF','CF','棉花商品期货','CF',category=CATEGORY.FUTURES)
        self._FG = self.add(2,'FG','FG','玻璃商品期货','FG',category=CATEGORY.FUTURES)
        self._JR = self.add(3,'JR','JR','粳稻商品期货','JR',category=CATEGORY.FUTURES)
        self._LR = self.add(4,'LR','LR','晚稻商品期货','LR',category=CATEGORY.FUTURES)
        self._MA = self.add(5,'MA','MA','甲醇商品期货','MA',category=CATEGORY.FUTURES)
        self._OI = self.add(6,'OI','OI','菜油商品期货','OI',category=CATEGORY.FUTURES)
        self._PM = self.add(7,'PM','PM','普麦商品期货','PM',category=CATEGORY.FUTURES)
        self._RI = self.add(8,'RI','RI','早稻商品期货','RI',category=CATEGORY.FUTURES)
        self._RM = self.add(9,'RM','RM','菜粕商品期货','RM',category=CATEGORY.FUTURES)
        self._RS = self.add(10,'RS','RS','菜子商品期货','RS',category=CATEGORY.FUTURES)
        self._SF = self.add(11,'SF','SF','硅铁商品期货','SF',category=CATEGORY.FUTURES)
        self._SM = self.add(12,'SM','SM','硅锰商品期货','SM',category=CATEGORY.FUTURES)
        self._SR = self.add(13,'SR','SR','白糖商品期货','SR',category=CATEGORY.FUTURES)
        self._TA = self.add(14,'TA','TA','PTA商品期货','TA',category=CATEGORY.FUTURES)
        self._TC = self.add(15,'TC','TC','动煤商品期货','TC',category=CATEGORY.FUTURES)
        self._WH = self.add(16,'WH','WH','强麦商品期货','WH',category=CATEGORY.FUTURES)
        self._ZC = self.add(17,'ZC','ZC','动煤商品期货','ZC',category=CATEGORY.FUTURES)

    @property
    def CF(self):
        return self._CF

    @property
    def FG(self):
        return self._FG

    @property
    def JR(self):
        return self._JR

    @property
    def LR(self):
        return self._LR

    @property
    def MA(self):
        return self._MA

    @property
    def OI(self):
        return self._OI

    @property
    def PM(self):
        return self._PM

    @property
    def RI(self):
        return self._RI

    @property
    def RM(self):
        return self._RM

    @property
    def RS(self):
        return self._RS

    @property
    def SF(self):
        return self._SF

    @property
    def SM(self):
        return self._SM

    @property
    def SR(self):
        return self._SR

    @property
    def TA(self):
        return self._TA

    @property
    def TC(self):
        return self._TC

    @property
    def WH(self):
        return self._WH

    @property
    def ZC(self):
        return self._ZC

CZCE = QtsCZCE()

#######################################################################################################################################
#上期品种子集
@singletonno
class QtsSHFE(QtsEnum) :
    def __init__(self) :
        QtsEnum.__init__(self)
        self._ag = self.add(1,'ag','ag','沪银商品期货','ag',category=CATEGORY.FUTURES)
        self._al = self.add(2,'al','al','沪铝商品期货','al',category=CATEGORY.FUTURES)
        self._au = self.add(3,'au','au','沪金商品期货','au',category=CATEGORY.FUTURES)
        self._bu = self.add(4,'bu','bu','沥青商品期货','bu',category=CATEGORY.FUTURES)
        self._cu = self.add(5,'cu','cu','沪铜商品期货','cu',category=CATEGORY.FUTURES)
        self._fu = self.add(6,'fu','fu','燃油商品期货','pu',category=CATEGORY.FUTURES)
        self._hc = self.add(7,'hc','hc','热卷商品期货','hc',category=CATEGORY.FUTURES)
        self._ni = self.add(8,'ni','ni','沪镍商品期货','ni',category=CATEGORY.FUTURES)
        self._pb = self.add(9,'pb','pb','沪铅商品期货','pb',category=CATEGORY.FUTURES)
        self._rb = self.add(10,'rb','rb','螺纹商品期货','rb',category=CATEGORY.FUTURES)
        self._ru = self.add(11,'ru','ru','橡胶商品期货','ru',category=CATEGORY.FUTURES)
        self._sn = self.add(12,'sn','sn','沪锡商品期货','sn',category=CATEGORY.FUTURES)
        self._wr = self.add(13,'wr','wr','线材商品期货','wr',category=CATEGORY.FUTURES)
        self._zn = self.add(14,'zn','zn','沪锌商品期货','zn',category=CATEGORY.FUTURES)

    @property
    def ag(self):
        return self._ag

    @property
    def al(self):
        return self._al

    @property
    def au(self):
        return self._au

    @property
    def bu(self):
        return self._bu

    @property
    def cu(self):
        return self._cu

    @property
    def fu(self):
        return self._fu

    @property
    def hc(self):
        return self._hc

    @property
    def ni(self):
        return self._ni

    @property
    def pb(self):
        return self._pb

    @property
    def rb(self):
        return self._rb

    @property
    def ru(self):
        return self._ru

    @property
    def sn(self):
        return self._sn

    @property
    def wr(self):
        return self._wr

    @property
    def zn(self):
        return self._zn

SHFE = QtsSHFE()

#######################################################################################################################################
