#coding=utf-8
import sys
sys.path.append('../common')
from qtswebdb import *

####################################################################################################################################################

strategy_head_fields = [qts_autoid_field,qts_strategyid_field,qts_name_field,qts_account_field,qts_minorderid_field,
                      qts_maxorderid_field,qts_orderidstep_field,qts_status_field,qts_threadid_field]
strategy_head_dcit = {strategy_head_fields[0]:0,strategy_head_fields[1]:1,strategy_head_fields[2]:2,strategy_head_fields[3]:3,strategy_head_fields[4]:4,strategy_head_fields[5]:5,strategy_head_fields[6]:6,strategy_head_fields[7]:7,strategy_head_fields[8]:8}
strategy_head_texts = [get_text(strategy_head_fields[0]),get_text(strategy_head_fields[1]),get_text(strategy_head_fields[2]),get_text(strategy_head_fields[3]),get_text(strategy_head_fields[4]),get_text(strategy_head_fields[5]),get_text(strategy_head_fields[6]),get_text(strategy_head_fields[7]),get_text(strategy_head_fields[8])]

def get_strategy_head_fields() :
    return strategy_head_fields

def get_strategy_head_texts() :
    return strategy_head_texts

def exist_strategy(dbname,dbtable,id) :
     return exist_row(dbname,dbtable,id)

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
    delete_rows_by_list(dbname,dbtable,strategys)

def update_strategys(dbname,dbtable,strategys) :
    update_rows_by_list(dbname,dbtable,strategys)

def insert_strategys(dbname,dbtable,markets) :
    insert_rows_by_list(dbname,dbtable,markets)

def insert_strategy(dbname,dbtable,kwargs) :
    insert_row(dbname,dbtable,kwargs)

def get_strategy_type(file) :
    return load_json(file)

####################################################################################################################################################

instrument_head_fields = [qts_autoid_field,qts_strategyid_field,qts_key_field,qts_name_field,qts_codetype_field,qts_market_field,qts_category_field,qts_secucode_field,qts_index_field,qts_level_field,qts_status_field,qts_mode_field,qts_component_field,qts_style_field]
instrument_head_dcit = {instrument_head_fields[0]:0,instrument_head_fields[1]:1,instrument_head_fields[2]:2,instrument_head_fields[3]:3,instrument_head_fields[4]:4,instrument_head_fields[5]:5,instrument_head_fields[6]:6,instrument_head_fields[7]:7,instrument_head_fields[8]:8,instrument_head_fields[9]:9,instrument_head_fields[10]:10,instrument_head_fields[11]:11,instrument_head_fields[12]:12,instrument_head_fields[13]:13}
instrument_head_texts = [get_text(instrument_head_fields[0]),get_text(instrument_head_fields[1]),get_text(instrument_head_fields[2]),get_text(instrument_head_fields[3]),get_text(instrument_head_fields[4]),get_text(instrument_head_fields[5]),get_text(instrument_head_fields[6]),get_text(instrument_head_fields[7]),get_text(instrument_head_fields[8]),get_text(instrument_head_fields[9]),get_text(instrument_head_fields[10]),get_text(instrument_head_fields[11]),get_text(instrument_head_fields[12]),get_text(instrument_head_fields[13])]

def get_instrument_head_fields() :
    return instrument_head_fields

def get_instrument_head_texts() :
    return instrument_head_texts

def exist_instrument(dbname,dbtable,id) :
     return exist_row(dbname,dbtable,id)

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
    delete_rows_by_list(dbname,dbtable,instruments)

def update_instruments(dbname,dbtable,instruments) :
    update_rows_by_list(dbname,dbtable,instruments)

def insert_instruments(dbname,dbtable,markets) :
    insert_rows_by_list(dbname,dbtable,markets)

def insert_instrument(dbname,dbtable,kwargs) :
    insert_row(dbname,dbtable,kwargs)

def get_instrument_type(file) :
    return load_json(file)

####################################################################################################################################################

parameter_head_fields = [qts_autoid_field,qts_strategyid_field,qts_key_field,qts_name_field,qts_value_field,qts_vardecimal_field,qts_index_field,qts_level_field,
                        qts_save_field,qts_status_field,qts_mode_field,qts_component_field,qts_style_field]
parameter_head_dcit = {parameter_head_fields[0]:0,parameter_head_fields[1]:1,parameter_head_fields[2]:2,parameter_head_fields[3]:3,parameter_head_fields[4]:4,parameter_head_fields[5]:5,parameter_head_fields[6]:6,parameter_head_fields[7]:7,parameter_head_fields[8]:8,parameter_head_fields[9]:9,parameter_head_fields[10]:10,parameter_head_fields[11]:11,parameter_head_fields[12]:12}
parameter_head_texts = [get_text(parameter_head_fields[0]),get_text(parameter_head_fields[1]),get_text(parameter_head_fields[2]),get_text(parameter_head_fields[3]),get_text(parameter_head_fields[4]),get_text(parameter_head_fields[5]),get_text(parameter_head_fields[6]),get_text(parameter_head_fields[7]),get_text(parameter_head_fields[8]),get_text(parameter_head_fields[9]),get_text(parameter_head_fields[10]),get_text(parameter_head_fields[11]),get_text(parameter_head_fields[12])]

def get_parameter_head_fields() :
    return parameter_head_fields

def get_parameter_head_texts() :
    return parameter_head_texts

def exist_parameter(dbname,dbtable,id) :
     return exist_row(dbname,dbtable,id)

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
    delete_rows_by_list(dbname,dbtable,parameters)

def update_parameters(dbname,dbtable,parameters) :
    update_rows_by_list(dbname,dbtable,parameters)

def insert_parameters(dbname,dbtable,markets) :
    insert_rows_by_list(dbname,dbtable,markets)

def insert_parameter(dbname,dbtable,kwargs) :
    insert_row(dbname,dbtable,kwargs)

def get_parameter_type(file) :
    return load_json(file)

####################################################################################################################################################

comment_head_fields = [qts_autoid_field,qts_strategyid_field,qts_key_field,qts_name_field,qts_value_field,qts_vardecimal_field,qts_index_field,qts_level_field,
                        qts_modify_field,qts_status_field,qts_mode_field,qts_component_field,qts_style_field]
comment_head_dcit = {comment_head_fields[0]:0,comment_head_fields[1]:1,comment_head_fields[2]:2,comment_head_fields[3]:3,comment_head_fields[4]:4,comment_head_fields[5]:5,comment_head_fields[6]:6,comment_head_fields[7]:7,comment_head_fields[8]:8,comment_head_fields[9]:9,comment_head_fields[10]:10,comment_head_fields[11]:11,comment_head_fields[12]:12}
comment_head_texts = [get_text(comment_head_fields[0]),get_text(comment_head_fields[1]),get_text(comment_head_fields[2]),get_text(comment_head_fields[3]),get_text(comment_head_fields[4]),get_text(comment_head_fields[5]),get_text(comment_head_fields[6]),get_text(comment_head_fields[7]),get_text(comment_head_fields[8]),get_text(comment_head_fields[9]),get_text(comment_head_fields[10]),get_text(comment_head_fields[11]),get_text(comment_head_fields[12])]

def get_comment_head_fields() :
    return comment_head_fields

def get_comment_head_texts() :
    return comment_head_texts

def exist_comment(dbname,dbtable,id) :
     return exist_row(dbname,dbtable,id)

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
    delete_rows_by_list(dbname,dbtable,comments)

def update_comments(dbname,dbtable,comments) :
    update_rows_by_list(dbname,dbtable,comments)

def insert_comments(dbname,dbtable,markets) :
    insert_rows_by_list(dbname,dbtable,markets)

def insert_comment(dbname,dbtable,kwargs) :
    insert_row(dbname,dbtable,kwargs)

def get_comment_type(file) :
    return load_json(file)

####################################################################################################################################################

command_head_fields = [qts_autoid_field,qts_strategyid_field,qts_key_field,qts_name_field,qts_index_field,qts_level_field,
                     qts_status_field,qts_mode_field,qts_component_field,qts_style_field]
command_head_dcit = {command_head_fields[0]:0,command_head_fields[1]:1,command_head_fields[2]:2,command_head_fields[3]:3,command_head_fields[4]:4,command_head_fields[5]:5,command_head_fields[6]:6,command_head_fields[7]:7,command_head_fields[8]:8,command_head_fields[9]:9}
command_head_texts = [get_text(command_head_fields[0]),get_text(command_head_fields[1]),get_text(command_head_fields[2]),get_text(command_head_fields[3]),get_text(command_head_fields[4]),get_text(command_head_fields[5]),get_text(command_head_fields[6]),get_text(command_head_fields[7]),get_text(command_head_fields[8]),get_text(command_head_fields[9])]

def get_command_head_fields() :
    return command_head_fields

def get_command_head_texts() :
    return command_head_texts

def exist_command(dbname,dbtable,id) :
     return exist_row(dbname,dbtable,id)

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
    delete_rows_by_list(dbname,dbtable,commands)

def update_commands(dbname,dbtable,commands) :
    update_rows_by_list(dbname,dbtable,commands)

def insert_commands(dbname,dbtable,markets) :
    insert_rows_by_list(dbname,dbtable,markets)

def insert_command(dbname,dbtable,kwargs) :
    insert_row(dbname,dbtable,kwargs)

def get_command_type(file) :
    return load_json(file)
####################################################################################################################################################

