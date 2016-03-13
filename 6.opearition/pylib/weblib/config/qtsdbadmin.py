#coding=utf-8
import sys
sys.path.append('../common')
from qtswebdb import *

#########################################################################################################################
admin_head_fields = [qts_autoid_field,qts_id_field,qts_name_field,qts_parentid_field,qts_type_field,qts_subtype_field,qts_password_field,qts_detail_field]
admin_head_dcit = {admin_head_fields[0]:0,admin_head_fields[1]:1,admin_head_fields[2]:2,admin_head_fields[3]:3,admin_head_fields[4]:4,
                     admin_head_fields[5]:5,admin_head_fields[6]:6,admin_head_fields[7]:7}
admin_head_texts = [get_text(admin_head_fields[0]),get_text(admin_head_fields[1]),get_text(admin_head_fields[2]),get_text(admin_head_fields[3]),get_text(admin_head_fields[4]),
                     get_text(admin_head_fields[5]),get_text(admin_head_fields[6]),get_text(admin_head_fields[7])]

def get_admin_head_fields() :
    return admin_head_fields

def get_admin_head_texts() :
    return admin_head_texts

def exist_admin(dbname,dbtable,id) :
     return exist_row(dbname,dbtable,id)

def get_admins_size(dbname,dbtable) :
    return get_rows_size(dbname,dbtable)

def get_admins_list(dbname,dbtable) :
    return get_rows_list(dbname,dbtable)

def get_admins_list_by_page(dbname,dbtable,page,size) :
    return get_rows_list_by_page(dbname,dbtable,page,size)

def get_admins_json(dbname,dbtable) :
    return get_rows_json(dbname,dbtable,admin_head_dcit)

def get_admins_json_by_page(dbname,dbtable,page,size) :
     return get_rows_json_by_page(dbname,dbtable,page,size,admin_head_dcit)

def delete_admins(dbname,dbtable,admins) :
    delete_rows_by_list(dbname,dbtable,admins)

def update_admins(dbname,dbtable,admins) :
    update_rows_by_list(dbname,dbtable,admins)

def insert_admins(dbname,dbtable,markets) :
    insert_rows_by_list(dbname,dbtable,markets)

def insert_admin(dbname,dbtable,kwargs) :
    insert_row(dbname,dbtable,kwargs)

def get_admin_type(file) :
    return load_json(file)

#########################################################################################################################
