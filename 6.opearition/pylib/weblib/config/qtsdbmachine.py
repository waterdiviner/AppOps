#coding=utf-8
import sys
import os
sys.path.append('../common')
#sys.path.append(os.path.join(os.getenv('QTS_BASE_PATH','..'),'pylib/common'))
from qtswebdb import *


########################################################################################################################
machine_head_fields = [qts_autoid_field,qts_id_field,qts_name_field,qts_host_field,qts_user_field,
                    qts_password_field,qts_type_field,qts_position_field,qts_detail_field]
machine_head_dcit = {machine_head_fields[0]:0,machine_head_fields[1]:1,machine_head_fields[2]:2,machine_head_fields[3]:3,machine_head_fields[4]:4,
                    machine_head_fields[5]:5,machine_head_fields[6]:6,machine_head_fields[7]:7,machine_head_fields[8]:8}
machine_head_texts = [get_text(machine_head_fields[0]),get_text(machine_head_fields[1]),get_text(machine_head_fields[2]),get_text(machine_head_fields[3]),get_text(machine_head_fields[4]),
                    get_text(machine_head_fields[5]),get_text(machine_head_fields[6]),get_text(machine_head_fields[7]),get_text(machine_head_fields[8])]

def get_machine_head_fields() :
    return machine_head_fields

def get_machine_head_texts() :
    return machine_head_texts

def exist_machine(dbname,dbtable,id) :
     return exist_row(dbname,dbtable,id)

def get_machines_size(dbname,dbtable) :
    return get_rows_size(dbname,dbtable)

def get_machines_list(dbname,dbtable) :
    return get_rows_list(dbname,dbtable)

def get_machines_list_by_page(dbname,dbtable,page,size) :
    return get_rows_list_by_page(dbname,dbtable,page,size)

def get_machines_json(dbname,dbtable) :
    return get_rows_json(dbname,dbtable,machine_head_dcit)

def get_machines_json_dict(dbname,dbtable) :
    return get_rows_json_dict(dbname,dbtable,machine_head_dcit)

def get_machines_json_machineid(dbname,dbtable) :
    return get_rows_json_dict(dbname,dbtable,{machine_head_fields[1]:0,machine_head_fields[2]:1},qts_autoid_field,None,[machine_head_fields[1],machine_head_fields[2]])[qts_json_rows_field]

def get_machines_json_by_page(dbname,dbtable,page,size) :
     return get_rows_json_by_page(dbname,dbtable,page,size,machine_head_dcit)

def delete_machines(dbname,dbtable,machines) :
    delete_rows_by_list(dbname,dbtable,machines)

def update_machines(dbname,dbtable,machines) :
    update_rows_by_list(dbname,dbtable,machines)

def insert_machines(dbname,dbtable,markets) :
    insert_rows_by_list(dbname,dbtable,markets)

def insert_machine(dbname,dbtable,kwargs) :
    insert_row(dbname,dbtable,kwargs)

def get_machine_type(file) :
    return load_json(file)

########################################################################################################################