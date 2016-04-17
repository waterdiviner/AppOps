#coding=utf-8
import sys
import os
sys.path.append('../common')
#sys.path.append(os.path.join(os.getenv('QTS_BASE_PATH','..'),'pylib/common'))
from qtswebdb import *

#########################################################################################################################
taccount_head_dcit = {qts_autoid_field:0,qts_market_field:1,qts_category_field:2,qts_account_field:3,qts_totalamount_field:4,
                     qts_avlamount_field:5,qts_freezeamount_field:6,qts_currency_field:7,qts_date_field:8}

def exist_taccount(dbname,dbtable,id) :
     return exist_row(dbname,dbtable,id,qts_autoid_field)

def get_taccounts_size(dbname,dbtable) :
    return get_rows_size(dbname,dbtable)

def get_taccounts_list(dbname,dbtable) :
    return get_rows_list(dbname,dbtable)

def get_taccounts_list_by_page(dbname,dbtable,page,size) :
    return get_rows_list_by_page(dbname,dbtable,page,size)

def get_taccounts_json(dbname,dbtable) :
    return get_rows_json(dbname,dbtable,taccount_head_dcit)

def get_taccounts_json_by_page(dbname,dbtable,page,size) :
     return get_rows_json_by_page(dbname,dbtable,page,size,taccount_head_dcit)

def delete_taccounts(dbname,dbtable,taccounts) :
    delete_rows_by_list(dbname,dbtable,taccounts,qts_autoid_field)

def update_taccounts(dbname,dbtable,taccounts) :
    update_rows_by_list(dbname,dbtable,taccounts)

def insert_taccounts(dbname,dbtable,markets) :
    insert_rows_by_list(dbname,dbtable,markets)

def insert_taccount(dbname,dbtable,kwargs) :
    insert_row(dbname,dbtable,kwargs)

#########################################################################################################################
eaccount_head_dcit = {qts_autoid_field:0,qts_market_field:1,qts_category_field:2,qts_viraccount_field:3,qts_relaccount_field:4,
                     qts_sharetag_field:5,qts_totalamount_field:6,qts_avlamount_field:7,qts_freezeamount_field:8,qts_date_field:9}

def exist_eaccount(dbname,dbtable,id) :
     return exist_row(dbname,dbtable,id,qts_autoid_field)

def get_eaccounts_size(dbname,dbtable) :
    return get_rows_size(dbname,dbtable)

def get_eaccounts_list(dbname,dbtable) :
    return get_rows_list(dbname,dbtable)

def get_eaccounts_list_by_page(dbname,dbtable,page,size) :
    return get_rows_list_by_page(dbname,dbtable,page,size)

def get_eaccounts_json(dbname,dbtable) :
    return get_rows_json(dbname,dbtable,eaccount_head_dcit)

def get_eaccounts_json_by_page(dbname,dbtable,page,size) :
     return get_rows_json_by_page(dbname,dbtable,page,size,eaccount_head_dcit)

def delete_eaccounts(dbname,dbtable,eaccounts) :
    delete_rows_by_list(dbname,dbtable,eaccounts,qts_autoid_field)

def update_eaccounts(dbname,dbtable,eaccounts) :
    update_rows_by_list(dbname,dbtable,eaccounts)

def insert_eaccounts(dbname,dbtable,markets) :
    insert_rows_by_list(dbname,dbtable,markets)

def insert_eaccount(dbname,dbtable,kwargs) :
    insert_row(dbname,dbtable,kwargs)

#########################################################################################################################
uaccount_head_dcit = {qts_autoid_field:0,qts_user_field:1,qts_account_field:2,qts_viraccount_field:3}

def exist_uaccount(dbname,dbtable,id) :
     return exist_row(dbname,dbtable,id,qts_autoid_field)

def get_uaccounts_size(dbname,dbtable) :
    return get_rows_size(dbname,dbtable)

def get_uaccounts_list(dbname,dbtable) :
    return get_rows_list(dbname,dbtable)

def get_uaccounts_list_by_page(dbname,dbtable,page,size) :
    return get_rows_list_by_page(dbname,dbtable,page,size)

def get_uaccounts_json(dbname,dbtable) :
    return get_rows_json(dbname,dbtable,uaccount_head_dcit)

def get_uaccounts_json_by_page(dbname,dbtable,page,size) :
     return get_rows_json_by_page(dbname,dbtable,page,size,uaccount_head_dcit)

def delete_uaccounts(dbname,dbtable,uaccounts) :
    delete_rows_by_list(dbname,dbtable,uaccounts,qts_autoid_field)

def update_uaccounts(dbname,dbtable,uaccounts) :
    update_rows_by_list(dbname,dbtable,uaccounts)

def insert_uaccounts(dbname,dbtable,markets) :
    insert_rows_by_list(dbname,dbtable,markets)

def insert_uaccount(dbname,dbtable,kwargs) :
    insert_row(dbname,dbtable,kwargs)

#########################################################################################################################