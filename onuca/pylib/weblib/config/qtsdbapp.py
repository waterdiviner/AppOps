#coding=utf-8
import sys
sys.path.append('../common')
from qtswebdb import *

#########################################################################################################################
app_head_fields = [qts_autoid_field,qts_id_field,qts_name_field,qts_type_field,qts_path_field,qts_machineid_field,qts_position_field,qts_detail_field]
app_head_dcit = {app_head_fields[0]:0,app_head_fields[1]:1,app_head_fields[2]:2,app_head_fields[3]:3,app_head_fields[4]:4,
                     app_head_fields[5]:5,app_head_fields[6]:6,app_head_fields[7]:7}
app_head_texts = [get_text(app_head_fields[0]),get_text(app_head_fields[1]),get_text(app_head_fields[2]),get_text(app_head_fields[3]),get_text(app_head_fields[4]),
                     get_text(app_head_fields[5]),get_text(app_head_fields[6]),get_text(app_head_fields[7])]

def get_app_head_fields() :
    return app_head_fields

def get_app_head_texts() :
    return app_head_texts

def exist_app(dbname,dbtable,id) :
     return exist_row(dbname,dbtable,id)

def get_apps_size(dbname,dbtable) :
    return get_rows_size(dbname,dbtable)

def get_apps_list(dbname,dbtable) :
    return get_rows_list(dbname,dbtable)

def get_apps_list_by_page(dbname,dbtable,page,size) :
    return get_rows_list_by_page(dbname,dbtable,page,size)

def get_apps_json(dbname,dbtable) :
    return get_rows_json(dbname,dbtable,app_head_dcit)

def get_apps_json_by_page(dbname,dbtable,page,size) :
     return get_rows_json_by_page(dbname,dbtable,page,size,app_head_dcit)

def delete_apps(dbname,dbtable,apps) :
    delete_rows_by_list(dbname,dbtable,apps)

def update_apps(dbname,dbtable,apps) :
    update_rows_by_list(dbname,dbtable,apps)

def insert_apps(dbname,dbtable,markets) :
    insert_rows_by_list(dbname,dbtable,markets)

def insert_app(dbname,dbtable,kwargs) :
    insert_row(dbname,dbtable,kwargs)

def get_app_type(file) :
    return load_json(file)

#########################################################################################################################
