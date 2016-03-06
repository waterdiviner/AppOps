#coding=utf-8
import sys
sys.path.append('../common')
from qtswebdb import *

#########################################################################################################################
strategyinproduct_head_fields = [qts_autoid_field,qts_productid_field,qts_strategyid_field]
strategyinproduct_head_dcit = {strategyinproduct_head_fields[0]:0,strategyinproduct_head_fields[1]:1,strategyinproduct_head_fields[2]:2}
strategyinproduct_head_texts = [get_text(strategyinproduct_head_fields[0]),get_text(strategyinproduct_head_fields[1]),get_text(strategyinproduct_head_fields[2])]

def get_strategyinproduct_head_fields() :
    return strategyinproduct_head_fields

def get_strategyinproduct_head_texts() :
    return strategyinproduct_head_texts

def exist_strategyinproduct(dbname,dbtable,id) :
     return exist_row(dbname,dbtable,id)

def get_strategyinproducts_size(dbname,dbtable) :
    return get_rows_size(dbname,dbtable)

def get_strategyinproducts_list(dbname,dbtable) :
    return get_rows_list(dbname,dbtable)

def get_strategyinproducts_list_by_page(dbname,dbtable,page,size) :
    return get_rows_list_by_page(dbname,dbtable,page,size)

def get_strategyinproducts_json(dbname,dbtable) :
    return get_rows_json(dbname,dbtable,right_head_dcit)

def get_strategyinproducts_json_by_page(dbname,dbtable,page,size) :
     return get_rows_json_by_page(dbname,dbtable,page,size,right_head_dcit)

def delete_strategyinproducts(dbname,dbtable,rights) :
    delete_rows_by_list(dbname,dbtable,rights)

def update_strategyinproducts(dbname,dbtable,rights) :
    update_rows_by_list(dbname,dbtable,rights)

def insert_strategyinproducts(dbname,dbtable,markets) :
    insert_rows_by_list(dbname,dbtable,markets)

def insert_strategyinproduct(dbname,dbtable,kwargs) :
    insert_row(dbname,dbtable,kwargs)

def get_strategyinproduct_type(file) :
    return load_json(file)

#########################################################################################################################
