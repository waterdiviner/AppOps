#coding=utf-8
import sys
sys.path.append('../common')
from qtswebdb import *

#########################################################################################################################

secuinfo_s_head_fields = [qts_autoid_field,qts_market_field,qts_category_field,qts_secucode_field,qts_ordercode_field,qts_marketname_field,qts_categoryname_field,
qts_secuname_field,qts_minorderqty_field,qts_maxorderqty_field,qts_pricetick_field,qts_tradetn_field,qts_posmode_field,qts_multipler_field,
qts_margin_field,qts_currency_field,qts_expiry_field,qts_right_field,qts_strike_field,qts_tradingclass_field]

secuinfo_s_head_dcit = {secuinfo_s_head_fields[0]:0,secuinfo_s_head_fields[1]:1,secuinfo_s_head_fields[2]:2,secuinfo_s_head_fields[3]:3,secuinfo_s_head_fields[4]:4,secuinfo_s_head_fields[5]:5,secuinfo_s_head_fields[6]:6,secuinfo_s_head_fields[7]:7,secuinfo_s_head_fields[8]:8,secuinfo_s_head_fields[9]:9,secuinfo_s_head_fields[10]:10,secuinfo_s_head_fields[11]:11,secuinfo_s_head_fields[12]:12,secuinfo_s_head_fields[13]:13,secuinfo_s_head_fields[14]:14,secuinfo_s_head_fields[15]:15,secuinfo_s_head_fields[16]:16,secuinfo_s_head_fields[17]:17,secuinfo_s_head_fields[18]:18,secuinfo_s_head_fields[19]:19 }

secuinfo_s_head_texts = [get_text(secuinfo_s_head_fields[0]),get_text(secuinfo_s_head_fields[1]),get_text(secuinfo_s_head_fields[2]),get_text(secuinfo_s_head_fields[3]),get_text(secuinfo_s_head_fields[4]),get_text(secuinfo_s_head_fields[5]),get_text(secuinfo_s_head_fields[6]),get_text(secuinfo_s_head_fields[7]),get_text(secuinfo_s_head_fields[8]),get_text(secuinfo_s_head_fields[9]),get_text(secuinfo_s_head_fields[10]),get_text(secuinfo_s_head_fields[11]),get_text(secuinfo_s_head_fields[12]),get_text(secuinfo_s_head_fields[13]),get_text(secuinfo_s_head_fields[14]),get_text(secuinfo_s_head_fields[15]),get_text(secuinfo_s_head_fields[16]),get_text(secuinfo_s_head_fields[17]),get_text(secuinfo_s_head_fields[18]),get_text(secuinfo_s_head_fields[19])]

def get_secuinfo_s_head_fields() :
    return secuinfo_s_head_fields

def get_secuinfo_s_head_texts() :
    return secuinfo_s_head_texts

def exist_secuinfos(dbname,dbtable,id) :
     return exist_row(dbname,dbtable,id)

def get_secuinfoss_size(dbname,dbtable) :
    return get_rows_size(dbname,dbtable)

def get_secuinfoss_list(dbname,dbtable) :
    return get_rows_list(dbname,dbtable)

def get_secuinfoss_list_by_page(dbname,dbtable,page,size) :
    return get_rows_list_by_page(dbname,dbtable,page,size)

def get_secuinfoss_json(dbname,dbtable) :
    return get_rows_json(dbname,dbtable,secuinfo_s_head_dcit)

def get_secuinfoss_json_by_page(dbname,dbtable,page,size) :
     return get_rows_json_by_page(dbname,dbtable,page,size,secuinfo_s_head_dcit)

def delete_secuinfoss(dbname,dbtable,secuinfoss) :
    delete_rows_by_list(dbname,dbtable,secuinfoss)

def update_secuinfoss(dbname,dbtable,secuinfoss) :
    update_rows_by_list(dbname,dbtable,secuinfoss)

def insert_secuinfoss(dbname,dbtable,markets) :
    insert_rows_by_list(dbname,dbtable,markets)

def insert_secuinfos(dbname,dbtable,kwargs) :
    insert_row(dbname,dbtable,kwargs)

#########################################################################################################################

secuinfo_d_head_fields = [qts_autoid_field,qts_market_field,qts_category_field,qts_secucode_field,qts_lastprice_field,qts_lolimitedprice_field,qts_uplimitedprice_field,qts_suspension_field,
qts_tradingfee_field]
secuinfo_d_head_dcit = {secuinfo_d_head_fields[0]:0,secuinfo_d_head_fields[1]:1,secuinfo_d_head_fields[2]:2,secuinfo_d_head_fields[3]:3,secuinfo_d_head_fields[4]:4,secuinfo_d_head_fields[5]:5,secuinfo_d_head_fields[6]:6,secuinfo_d_head_fields[7]:7,secuinfo_d_head_fields[8]:8}
secuinfo_d_head_texts = [get_text(secuinfo_d_head_fields[0]),get_text(secuinfo_d_head_fields[1]),get_text(secuinfo_d_head_fields[2]),get_text(secuinfo_d_head_fields[3]),get_text(secuinfo_d_head_fields[4]),get_text(secuinfo_d_head_fields[5]),get_text(secuinfo_d_head_fields[6]),get_text(secuinfo_d_head_fields[7]),get_text(secuinfo_d_head_fields[8])]

def get_secuinfo_d_head_fields() :
    return secuinfo_d_head_fields

def get_secuinfo_d_head_texts() :
    return secuinfo_d_head_texts

def exist_secuinfod(dbname,dbtable,id) :
     return exist_row(dbname,dbtable,id)

def get_secuinfods_size(dbname,dbtable) :
    return get_rows_size(dbname,dbtable)

def get_secuinfods_list(dbname,dbtable) :
    return get_rows_list(dbname,dbtable)

def get_secuinfods_list_by_page(dbname,dbtable,page,size) :
    return get_rows_list_by_page(dbname,dbtable,page,size)

def get_secuinfods_json(dbname,dbtable) :
    return get_rows_json(dbname,dbtable,secuinfo_d_head_dcit)

def get_secuinfods_json_by_page(dbname,dbtable,page,size) :
     return get_rows_json_by_page(dbname,dbtable,page,size,secuinfo_d_head_dcit)

def delete_secuinfods(dbname,dbtable,secuinfods) :
    delete_rows_by_list(dbname,dbtable,secuinfods)

def update_secuinfods(dbname,dbtable,secuinfods) :
    update_rows_by_list(dbname,dbtable,secuinfods)

def insert_secuinfods(dbname,dbtable,markets) :
    insert_rows_by_list(dbname,dbtable,markets)

def insert_secuinfod(dbname,dbtable,kwargs) :
    insert_row(dbname,dbtable,kwargs)

#########################################################################################################################
