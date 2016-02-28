#coding=utf-8
import sys
sys.path.append('../common')
from qtswebdb import *

#########################################################################################################################
position_head_dcit = {qts_autoid_field:0,qts_market_field:1,qts_category_field:2,qts_secucode_field:3,qts_account_field:4,
                     qts_type_field:5,qts_level_field:6,qts_date_field:7,qts_totalvol_field:8,qts_avlvol_field:9,qts_workingvol_field:10,
                     qts_totalcost_field:11,qts_avlcredempvol_field:12,qts_todayvol_field:13}

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
