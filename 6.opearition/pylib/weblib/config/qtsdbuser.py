#coding=utf-8
import sys
sys.path.append('../common')
from qtswebdb import *

#########################################################################################################################
user_head_fields = [qts_autoid_field,qts_user_field,qts_account_field,qts_viraccount_field]
user_head_dcit = {user_head_fields[0]:0,user_head_fields[1]:1,user_head_fields[2]:2,user_head_fields[3]:3}
user_head_texts = [get_text(user_head_fields[0]),get_text(user_head_fields[1]),get_text(user_head_fields[2]),get_text(user_head_fields[3])]

def get_user_head_fields() :
    return user_head_fields

def get_user_head_texts() :
    return user_head_texts

def exist_user(dbname,dbtable,id) :
     return exist_row(dbname,dbtable,id)

def get_users_size(dbname,dbtable) :
    return get_rows_size(dbname,dbtable)

def get_users_list(dbname,dbtable) :
    return get_rows_list(dbname,dbtable)

def get_users_list_by_page(dbname,dbtable,page,size) :
    return get_rows_list_by_page(dbname,dbtable,page,size)

def get_users_json(dbname,dbtable) :
    return get_rows_json(dbname,dbtable,user_head_dcit)

def get_users_json_by_page(dbname,dbtable,page,size) :
     return get_rows_json_by_page(dbname,dbtable,page,size,user_head_dcit)

def delete_users(dbname,dbtable,users) :
    delete_rows_by_list(dbname,dbtable,users)

def update_users(dbname,dbtable,users) :
    update_rows_by_list(dbname,dbtable,users)

def insert_users(dbname,dbtable,markets) :
    insert_rows_by_list(dbname,dbtable,markets)

def insert_user(dbname,dbtable,kwargs) :
    insert_row(dbname,dbtable,kwargs)

def get_user_type(file) :
    return load_json(file)

#########################################################################################################################
