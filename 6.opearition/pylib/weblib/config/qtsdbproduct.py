#coding=utf-8
import sys
import os
sys.path.append('../common')
#sys.path.append(os.path.join(os.getenv('QTS_BASE_PATH','..'),'pylib/common'))
from qtswebdb import *

############################################################################################################################
product_head_fields = [qts_autoid_field,qts_id_field,qts_parentid_field,qts_name_field,qts_manager_field,qts_bdate_field,qts_edate_field,qts_status_field,qts_property_field,qts_detail_field]
product_head_dcit = {product_head_fields[0]:0,product_head_fields[1]:1,product_head_fields[2]:2,product_head_fields[3]:3,product_head_fields[4]:4,
                     product_head_fields[5]:5,product_head_fields[6]:6,product_head_fields[7]:7,product_head_fields[8]:8,product_head_fields[9]:9}
product_head_texts = [get_text(product_head_fields[0]),get_text(product_head_fields[1]),get_text(product_head_fields[2]),get_text(product_head_fields[3]),get_text(product_head_fields[4]),
                     get_text(product_head_fields[5]),get_text(product_head_fields[6]),get_text(product_head_fields[7]),get_text(product_head_fields[8]),get_text(product_head_fields[9])]


def get_product_head_fields() :
    return product_head_fields

def get_product_head_texts() :
    return product_head_texts

def exist_product(dbname,dbtable,id) :
     return exist_row(dbname,dbtable,id)

def get_products_size(dbname,dbtable) :
    return get_rows_size(dbname,dbtable)

def get_products_list(dbname,dbtable) :
    return get_rows_list(dbname,dbtable)

def get_products_list_by_page(dbname,dbtable,page,size) :
    return get_rows_list_by_page(dbname,dbtable,page,size)

def get_products_json(dbname,dbtable) :
    return get_rows_json(dbname,dbtable,product_head_dcit)

def get_products_json_by_page(dbname,dbtable,page,size) :
     return get_rows_json_by_page(dbname,dbtable,page,size,product_head_dcit)

def delete_products(dbname,dbtable,products) :
    delete_rows_by_list(dbname,dbtable,products)

def update_products(dbname,dbtable,products) :
    update_rows_by_list(dbname,dbtable,products)

def insert_products(dbname,dbtable,markets) :
    insert_rows_by_list(dbname,dbtable,markets)

def insert_product(dbname,dbtable,kwargs) :
    insert_row(dbname,dbtable,kwargs)

############################################################################################################################
strategy_product_head_dcit = {qts_autoid_field:0,qts_productid_field:1,qts_strategyid_field:2}

def exist_strategy_product(dbname,dbtable,id) :
     return exist_row(dbname,dbtable,id,qts_autoid_field)

def get_strategy_products_size(dbname,dbtable) :
    return get_rows_size(dbname,dbtable)

def get_strategy_products_list(dbname,dbtable) :
    return get_rows_list(dbname,dbtable)

def get_strategy_products_list_by_page(dbname,dbtable,page,size) :
    return get_rows_list_by_page(dbname,dbtable,page,size)

def get_strategy_products_json(dbname,dbtable) :
    return get_rows_json(dbname,dbtable,strategy_product_head_dcit)

def get_strategy_products_json_by_page(dbname,dbtable,page,size) :
     return get_rows_json_by_page(dbname,dbtable,page,size,strategy_product_head_dcit)

def delete_strategy_products(dbname,dbtable,strategy_products) :
    delete_rows_by_list(dbname,dbtable,strategy_products,qts_autoid_field)

def update_strategy_products(dbname,dbtable,strategy_products) :
    update_rows_by_list(dbname,dbtable,strategy_products)

def insert_strategy_products(dbname,dbtable,markets) :
    insert_rows_by_list(dbname,dbtable,markets)

def insert_strategy_product(dbname,dbtable,kwargs) :
    insert_row(dbname,dbtable,kwargs)

############################################################################################################################