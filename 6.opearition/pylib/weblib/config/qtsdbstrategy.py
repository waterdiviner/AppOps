#coding=utf-8
import sys
sys.path.append('../common')
from qtswebdb import *

####################################################################################################################################################
strategy_head_dcit = {qts_autoid_field:0,qts_strategyid_field:1,qts_name_field:2,qts_account_field:3,qts_minorderid_field:4,
                      qts_maxorderid_field:5,qts_orderidstep_field:6,qts_status_field:7,qts_threadid_field:8}

def exist_strategy(dbname,dbtable,id) :
     return exist_row(dbname,dbtable,id,qts_strategyid_field)

def get_strategys_size(dbname,dbtable) :
    return get_rows_size(dbname,dbtable)

def get_strategys_list(dbname,dbtable) :
    return get_rows_list(dbname,dbtable)

def get_strategys_list_by_page(dbname,dbtable,page,size) :
    return get_rows_list_by_page(dbname,dbtable,page,size)

def get_strategys_json(dbname,dbtable) :
    return get_rows_json(dbname,dbtable,strategy_head_dcit)

def get_strategys_json_by_page(dbname,dbtable,page,size) :
     return get_rows_json_by_page(dbname,dbtable,page,size,strategy_head_dcit)

def delete_strategys(dbname,dbtable,strategys) :
    delete_rows_by_list(dbname,dbtable,strategys,qts_strategyid_field)

def update_strategys(dbname,dbtable,strategys) :
    update_rows_by_list(dbname,dbtable,strategys)

def insert_strategys(dbname,dbtable,markets) :
    insert_rows_by_list(dbname,dbtable,markets)

def insert_strategy(dbname,dbtable,kwargs) :
    insert_row(dbname,dbtable,kwargs)

####################################################################################################################################################
instrument_head_dcit = {qts_autoid_field:0,qts_strategyid_field:1,qts_key_field:2,qts_name_field:3,qts_codetype_field:4,qts_market_field:5,qts_category_field:6,qts_secucode_field:7,
                        qts_index_field:8,qts_level_field:9,qts_status_field:10,qts_mode_field:11,qts_component_field:12,qts_style_field:13}

def exist_instrument(dbname,dbtable,id) :
     return exist_row(dbname,dbtable,id,qts_key_field)

def get_instruments_size(dbname,dbtable) :
    return get_rows_size(dbname,dbtable)

def get_instruments_list(dbname,dbtable) :
    return get_rows_list(dbname,dbtable)

def get_instruments_list_by_page(dbname,dbtable,page,size) :
    return get_rows_list_by_page(dbname,dbtable,page,size)

def get_instruments_json(dbname,dbtable) :
    return get_rows_json(dbname,dbtable,instrument_head_dcit)

def get_instruments_json_by_page(dbname,dbtable,page,size) :
     return get_rows_json_by_page(dbname,dbtable,page,size,instrument_head_dcit)

def delete_instruments(dbname,dbtable,instruments) :
    delete_rows_by_list(dbname,dbtable,instruments,qts_key_field)

def update_instruments(dbname,dbtable,instruments) :
    update_rows_by_list(dbname,dbtable,instruments)

def insert_instruments(dbname,dbtable,markets) :
    insert_rows_by_list(dbname,dbtable,markets)

def insert_instrument(dbname,dbtable,kwargs) :
    insert_row(dbname,dbtable,kwargs)

####################################################################################################################################################
parameter_head_dcit = {qts_autoid_field:0,qts_strategyid_field:1,qts_key_field:2,qts_name_field:3,qts_value_field:4,qts_vardecimal_field:5,qts_index_field:6,qts_level_field:7,
                        qts_save_field:8,qts_status_field:9,qts_mode_field:10,qts_component_field:11,qts_style_field:12}

def exist_parameter(dbname,dbtable,id) :
     return exist_row(dbname,dbtable,id,qts_key_field)

def get_parameters_size(dbname,dbtable) :
    return get_rows_size(dbname,dbtable)

def get_parameters_list(dbname,dbtable) :
    return get_rows_list(dbname,dbtable)

def get_parameters_list_by_page(dbname,dbtable,page,size) :
    return get_rows_list_by_page(dbname,dbtable,page,size)

def get_parameters_json(dbname,dbtable) :
    return get_rows_json(dbname,dbtable,parameter_head_dcit)

def get_parameters_json_by_page(dbname,dbtable,page,size) :
     return get_rows_json_by_page(dbname,dbtable,page,size,parameter_head_dcit)

def delete_parameters(dbname,dbtable,parameters) :
    delete_rows_by_list(dbname,dbtable,parameters,qts_key_field)

def update_parameters(dbname,dbtable,parameters) :
    update_rows_by_list(dbname,dbtable,parameters)

def insert_parameters(dbname,dbtable,markets) :
    insert_rows_by_list(dbname,dbtable,markets)

def insert_parameter(dbname,dbtable,kwargs) :
    insert_row(dbname,dbtable,kwargs)

####################################################################################################################################################
comment_head_dcit = {qts_autoid_field:0,qts_strategyid_field:1,qts_key_field:2,qts_name_field:3,qts_value_field:4,qts_vardecimal_field:5,qts_index_field:6,qts_level_field:7,
                        qts_modify_field:8,qts_status_field:9,qts_mode_field:10,qts_component_field:11,qts_style_field:12}

def exist_comment(dbname,dbtable,id) :
     return exist_row(dbname,dbtable,id,qts_key_field)

def get_comments_size(dbname,dbtable) :
    return get_rows_size(dbname,dbtable)

def get_comments_list(dbname,dbtable) :
    return get_rows_list(dbname,dbtable)

def get_comments_list_by_page(dbname,dbtable,page,size) :
    return get_rows_list_by_page(dbname,dbtable,page,size)

def get_comments_json(dbname,dbtable) :
    return get_rows_json(dbname,dbtable,comment_head_dcit)

def get_comments_json_by_page(dbname,dbtable,page,size) :
     return get_rows_json_by_page(dbname,dbtable,page,size,comment_head_dcit)

def delete_comments(dbname,dbtable,comments) :
    delete_rows_by_list(dbname,dbtable,comments,qts_key_field)

def update_comments(dbname,dbtable,comments) :
    update_rows_by_list(dbname,dbtable,comments)

def insert_comments(dbname,dbtable,markets) :
    insert_rows_by_list(dbname,dbtable,markets)

def insert_comment(dbname,dbtable,kwargs) :
    insert_row(dbname,dbtable,kwargs)

####################################################################################################################################################
command_head_dcit = {qts_autoid_field:0,qts_strategyid_field:1,qts_key_field:2,qts_name_field:3,qts_index_field:4,qts_level_field:5,
                     qts_status_field:6,qts_mode_field:7,qts_component_field:8,qts_style_field:9}

def exist_command(dbname,dbtable,id) :
     return exist_row(dbname,dbtable,id,qts_key_field)

def get_commands_size(dbname,dbtable) :
    return get_rows_size(dbname,dbtable)

def get_commands_list(dbname,dbtable) :
    return get_rows_list(dbname,dbtable)

def get_commands_list_by_page(dbname,dbtable,page,size) :
    return get_rows_list_by_page(dbname,dbtable,page,size)

def get_commands_json(dbname,dbtable) :
    return get_rows_json(dbname,dbtable,command_head_dcit)

def get_commands_json_by_page(dbname,dbtable,page,size) :
     return get_rows_json_by_page(dbname,dbtable,page,size,command_head_dcit)

def delete_commands(dbname,dbtable,commands) :
    delete_rows_by_list(dbname,dbtable,commands,qts_key_field)

def update_commands(dbname,dbtable,commands) :
    update_rows_by_list(dbname,dbtable,commands)

def insert_commands(dbname,dbtable,markets) :
    insert_rows_by_list(dbname,dbtable,markets)

def insert_command(dbname,dbtable,kwargs) :
    insert_row(dbname,dbtable,kwargs)

####################################################################################################################################################

