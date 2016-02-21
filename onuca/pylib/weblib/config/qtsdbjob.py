#coding=utf-8
import sys
sys.path.append('../common')
from qtswebdb import *

#########################################################################################################################
job_head_fields = [qts_autoid_field,qts_id_field,qts_name_field,qts_type_field,qts_path_field,qts_file_field,qts_command_field,qts_property_field,qts_machineid_field,qts_detail_field]
job_head_dcit = {job_head_fields[0]:0,job_head_fields[1]:1,job_head_fields[2]:2,job_head_fields[3]:3,job_head_fields[4]:4,
                     job_head_fields[5]:5,job_head_fields[6]:6,job_head_fields[7]:7,job_head_fields[8]:8,job_head_fields[9]:9}
job_head_texts = [job_head_fields[0],job_head_fields[1],job_head_fields[2],job_head_fields[3],job_head_fields[4],
                    job_head_fields[5],job_head_fields[6],job_head_fields[7],job_head_fields[8],job_head_fields[9]]

def get_job_head_fields() :
    return job_head_fields

def get_job_head_texts() :
    return job_head_texts

def exist_job(dbname,dbtable,id) :
     return exist_row(dbname,dbtable,id)

def get_jobs_size(dbname,dbtable) :
    return get_rows_size(dbname,dbtable)

def get_jobs_list(dbname,dbtable) :
    return get_rows_list(dbname,dbtable)

def get_jobs_list_by_page(dbname,dbtable,page,size) :
    return get_rows_list_by_page(dbname,dbtable,page,size)

def get_jobs_json(dbname,dbtable) :
    return get_rows_json(dbname,dbtable,job_head_dcit)

def get_jobs_json_by_page(dbname,dbtable,page,size) :
     return get_rows_json_by_page(dbname,dbtable,page,size,job_head_dcit)

def delete_jobs(dbname,dbtable,jobs) :
    delete_rows_by_list(dbname,dbtable,jobs)

def update_jobs(dbname,dbtable,jobs) :
    update_rows_by_list(dbname,dbtable,jobs)

def insert_jobs(dbname,dbtable,markets) :
    insert_rows_by_list(dbname,dbtable,markets)

def insert_job(dbname,dbtable,kwargs) :
    insert_row(dbname,dbtable,kwargs)

def get_job_type(file) :
    return load_json(file)