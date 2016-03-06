#coding=utf-8
import sys
sys.path.append('../common')
from qtswebdb import *

#########################################################################################################################
trade_head_fields = [qts_autoid_field,qts_market_field,qts_category_field,qts_account_field,qts_totalamount_field,qts_avlamount_field,qts_freezeamount_field,
qts_currency_field,qts_date_field]
trade_head_dcit = {trade_head_fields[0]:0,trade_head_fields[1]:1,trade_head_fields[2]:2,trade_head_fields[3]:3,trade_head_fields[4]:4,trade_head_fields[5]:5,trade_head_fields[6]:6,trade_head_fields[7]:7,trade_head_fields[8]:8}
trade_head_texts = [get_text(trade_head_fields[0]),get_text(trade_head_fields[1]),get_text(trade_head_fields[2]),get_text(trade_head_fields[3]),get_text(trade_head_fields[4]),get_text(trade_head_fields[5]),get_text(trade_head_fields[6]),get_text(trade_head_fields[7]),get_text(trade_head_fields[8])]

def get_trade_head_fields() :
    return trade_head_fields

def get_trade_head_texts() :
    return trade_head_texts

def exist_trade(dbname,dbtable,id) :
     return exist_row(dbname,dbtable,id)

def get_trades_size(dbname,dbtable) :
    return get_rows_size(dbname,dbtable)

def get_trades_list(dbname,dbtable) :
    return get_rows_list(dbname,dbtable)

def get_trades_list_by_page(dbname,dbtable,page,size) :
    return get_rows_list_by_page(dbname,dbtable,page,size)

def get_trades_json(dbname,dbtable) :
    return get_rows_json(dbname,dbtable,trade_head_dcit)

def get_trades_json_by_page(dbname,dbtable,page,size) :
     return get_rows_json_by_page(dbname,dbtable,page,size,trade_head_dcit)

def delete_trades(dbname,dbtable,trades) :
    delete_rows_by_list(dbname,dbtable,trades)

def update_trades(dbname,dbtable,trades) :
    update_rows_by_list(dbname,dbtable,trades)

def insert_trades(dbname,dbtable,markets) :
    insert_rows_by_list(dbname,dbtable,markets)

def insert_trade(dbname,dbtable,kwargs) :
    insert_row(dbname,dbtable,kwargs)

def get_trade_type(file) :
    return load_json(file)

#########################################################################################################################
