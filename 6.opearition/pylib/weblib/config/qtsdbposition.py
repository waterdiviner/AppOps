#coding=utf-8
import sys
import os
sys.path.append('../common')
#sys.path.append(os.path.join(os.getenv('QTS_BASE_PATH','..'),'pylib/common'))
from qtswebdb import *

#########################################################################################################################
#position_head_dcit = {qts_autoid_field:0,qts_market_field:1,qts_category_field:2,qts_secucode_field:3,qts_account_field:4,
#                     qts_type_field:5,qts_level_field:6,qts_date_field:7,qts_totalvol_field:8,qts_avlvol_field:9,qts_workingvol_field:10,
#                     qts_totalcost_field:11,qts_avlcredempvol_field:12,qts_todayvol_field:13}

position_head_fields = [qts_autoid_field,qts_market_field,qts_category_field,qts_secucode_field,qts_account_field,
                     qts_type_field,qts_level_field,qts_date_field,qts_totalvol_field,qts_avlvol_field,qts_workingvol_field,
                     qts_totalcost_field,qts_avlcredempvol_field,qts_todayvol_field]
position_head_dcit = {position_head_fields[0]:0,position_head_fields[1]:1,position_head_fields[2]:2,position_head_fields[3]:3,position_head_fields[4]:4,
                     position_head_fields[5]:5,position_head_fields[6]:6,position_head_fields[7]:7,position_head_fields[8]:8,position_head_fields[9]:9,
                     position_head_fields[10]:10,position_head_fields[11]:11,position_head_fields[12]:12,position_head_fields[13]:13}
position_head_texts = [get_text(position_head_fields[0]),get_text(position_head_fields[1]),get_text(position_head_fields[2]),get_text(position_head_fields[3]),get_text(position_head_fields[4]),get_text(position_head_fields[5]),get_text(position_head_fields[6]),get_text(position_head_fields[7]),get_text(position_head_fields[8]),get_text(position_head_fields[9]),get_text(position_head_fields[10]),get_text(position_head_fields[11]),get_text(position_head_fields[12]),get_text(position_head_fields[13])]

def get_position_head_fields() :
    return position_head_fields

def get_position_head_texts() :
    return position_head_texts

def exist_position(dbname,dbtable,id) :
     return exist_row(dbname,dbtable,id,qts_autoid_field)

def get_positions_size(dbname,dbtable) :
    return get_rows_size(dbname,dbtable)

def get_positions_list(dbname,dbtable) :
    return get_rows_list(dbname,dbtable)

def get_positions_list_by_page(dbname,dbtable,page,size) :
    return get_rows_list_by_page(dbname,dbtable,page,size)

def get_positions_json(dbname,dbtable) :
    return get_rows_json(dbname,dbtable,position_head_dcit)

def get_positions_json_by_page(dbname,dbtable,page,size) :
     return get_rows_json_by_page(dbname,dbtable,page,size,position_head_dcit)

def delete_positions(dbname,dbtable,positions) :
    delete_rows_by_list(dbname,dbtable,positions,qts_autoid_field)

def update_positions(dbname,dbtable,positions) :
    update_rows_by_list(dbname,dbtable,positions)

def insert_positions(dbname,dbtable,markets) :
    insert_rows_by_list(dbname,dbtable,markets)

def insert_position(dbname,dbtable,kwargs) :
    insert_row(dbname,dbtable,kwargs)

#########################################################################################################################
