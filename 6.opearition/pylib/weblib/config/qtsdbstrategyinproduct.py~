#coding=utf-8
import sys
sys.path.append('../common')
from qtswebdb import *

#########################################################################################################################
strategyinapp_head_fields = [qts_autoid_field,qts_appid_field,qts_strategyid_field]
strategyinapp_head_dcit = {strategyinapp_head_fields[0]:0,strategyinapp_head_fields[1]:1,strategyinapp_head_fields[2]:2}
strategyinapp_head_texts = [get_text(strategyinapp_head_fields[0]),get_text(strategyinapp_head_fields[1]),get_text(strategyinapp_head_fields[2])]

def get_strategyinapp_head_fields() :
    return strategyinapp_head_fields

def get_strategyinapp_head_texts() :
    return strategyinapp_head_texts

def exist_strategyinapp(dbname,dbtable,id) :
     return exist_row(dbname,dbtable,id)

def get_strategyinapps_size(dbname,dbtable) :
    return get_rows_size(dbname,dbtable)

def get_strategyinapps_list(dbname,dbtable) :
    return get_rows_list(dbname,dbtable)

def get_strategyinapps_list_by_page(dbname,dbtable,page,size) :
    return get_rows_list_by_page(dbname,dbtable,page,size)

def get_strategyinapps_json(dbname,dbtable) :
    return get_rows_json(dbname,dbtable,right_head_dcit)

def get_strategyinapps_json_by_page(dbname,dbtable,page,size) :
     return get_rows_json_by_page(dbname,dbtable,page,size,right_head_dcit)

def delete_strategyinapps(dbname,dbtable,rights) :
    delete_rows_by_list(dbname,dbtable,rights)

def update_strategyinapps(dbname,dbtable,rights) :
    update_rows_by_list(dbname,dbtable,rights)

def insert_strategyinapps(dbname,dbtable,markets) :
    insert_rows_by_list(dbname,dbtable,markets)

def insert_strategyinapp(dbname,dbtable,kwargs) :
    insert_row(dbname,dbtable,kwargs)

def get_strategyinapp_type(file) :
    return load_json(file)

#########################################################################################################################
