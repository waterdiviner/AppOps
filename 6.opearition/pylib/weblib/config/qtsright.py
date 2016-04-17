#coding=utf-8
import sys
import os
sys.path.append(os.path.join(os.getenv('QTS_BASE_PATH','..'),'pylib/common'))
from qtswebdb import *

#########################################################################################################################
right_head_fields = [qts_autoid_field,qts_id_field,qts_name_field,qts_type_field,qts_path_field,qts_machineid_field,qts_position_field,qts_detail_field]
right_head_dcit = {right_head_fields[0]:0,right_head_fields[1]:1,right_head_fields[2]:2,right_head_fields[3]:3,right_head_fields[4]:4,
                     right_head_fields[5]:5,right_head_fields[6]:6,right_head_fields[7]:7}
right_head_texts = [get_text(right_head_fields[0]),get_text(right_head_fields[1]),get_text(right_head_fields[2]),get_text(right_head_fields[3]),get_text(right_head_fields[4]),
                     get_text(right_head_fields[5]),get_text(right_head_fields[6]),get_text(right_head_fields[7])]

def get_right_head_fields() :
    return right_head_fields

def get_right_head_texts() :
    return right_head_texts

def exist_right(dbname,dbtable,id) :
     return exist_row(dbname,dbtable,id)

def get_rights_size(dbname,dbtable) :
    return get_rows_size(dbname,dbtable)

def get_rights_list(dbname,dbtable) :
    return get_rows_list(dbname,dbtable)

def get_rights_list_by_page(dbname,dbtable,page,size) :
    return get_rows_list_by_page(dbname,dbtable,page,size)

def get_rights_json(dbname,dbtable) :
    return get_rows_json(dbname,dbtable,right_head_dcit)

def get_rights_json_by_page(dbname,dbtable,page,size) :
     return get_rows_json_by_page(dbname,dbtable,page,size,right_head_dcit)

def delete_rights(dbname,dbtable,rights) :
    delete_rows_by_list(dbname,dbtable,rights)

def update_rights(dbname,dbtable,rights) :
    update_rows_by_list(dbname,dbtable,rights)

def insert_rights(dbname,dbtable,markets) :
    insert_rows_by_list(dbname,dbtable,markets)

def insert_right(dbname,dbtable,kwargs) :
    insert_row(dbname,dbtable,kwargs)

def get_right_type(file) :
    return load_json(file)

#########################################################################################################################