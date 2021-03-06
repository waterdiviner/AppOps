#coding=utf-8
import sys
sys.path.append('../common')
from qtswebdb import *

#########################################################################################################################
exchange_head_fields = [qts_autoid_field,qts_market_field,qts_category_field,qts_viraccount_field,qts_relaccount_field,
qts_sharetag_field,qts_totalamount_field,qts_avlamount_field,qts_freezeamount_field,qts_date_field]
exchange_head_dcit = {exchange_head_fields[0]:0,exchange_head_fields[1]:1,exchange_head_fields[2]:2,exchange_head_fields[3]:3,exchange_head_fields[4]:4,exchange_head_fields[5]:5,exchange_head_fields[6]:6,exchange_head_fields[7]:7,exchange_head_fields[8]:8,exchange_head_fields[9]:9}
exchange_head_texts = [get_text(exchange_head_fields[0]),get_text(exchange_head_fields[1]),get_text(exchange_head_fields[2]),get_text(exchange_head_fields[3]),get_text(exchange_head_fields[4]),get_text(exchange_head_fields[5]),get_text(exchange_head_fields[6]),get_text(exchange_head_fields[7]),get_text(exchange_head_fields[8]),get_text(exchange_head_fields[9])]

def get_exchange_head_fields() :
    return exchange_head_fields

def get_exchange_head_texts() :
    return exchange_head_texts

def exist_exchange(dbname,dbtable,id) :
     return exist_row(dbname,dbtable,id)

def get_exchanges_size(dbname,dbtable) :
    return get_rows_size(dbname,dbtable)

def get_exchanges_list(dbname,dbtable) :
    return get_rows_list(dbname,dbtable)

def get_exchanges_list_by_page(dbname,dbtable,page,size) :
    return get_rows_list_by_page(dbname,dbtable,page,size)

def get_exchanges_json(dbname,dbtable) :
    return get_rows_json(dbname,dbtable,exchange_head_dcit)

def get_exchanges_json_by_page(dbname,dbtable,page,size) :
     return get_rows_json_by_page(dbname,dbtable,page,size,exchange_head_dcit)

def delete_exchanges(dbname,dbtable,exchanges) :
    delete_rows_by_list(dbname,dbtable,exchanges)

def update_exchanges(dbname,dbtable,exchanges) :
    update_rows_by_list(dbname,dbtable,exchanges)

def insert_exchanges(dbname,dbtable,markets) :
    insert_rows_by_list(dbname,dbtable,markets)

def insert_exchange(dbname,dbtable,kwargs) :
    insert_row(dbname,dbtable,kwargs)

def get_exchange_type(file) :
    return load_json(file)

#########################################################################################################################
