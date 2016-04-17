#coding=utf-8
import sys
import os
sys.path.append(os.path.join(os.getenv('QTS_BASE_PATH','..'),'pylib/common'))
from qtswebdb import *

record_head_fields =[qts_orderid_field,qts_account_field,qts_market_field,qts_category_field,qts_secucode_field,
                        qts_strategyid_field,qts_algoid_field,qts_algoindex_field,qts_action_field,qts_status_field,qts_oprice_field,
                        qts_iprice_field,qts_ovolume_field,qts_ivolume_field,qts_otime_field,qts_itime_field,qts_property_field,
                        qts_direction_field,qts_userid_field,qts_refid_field,qts_sessionid_field,qts_source_field]

record_head_dict ={record_head_fields[1]:2,record_head_fields[0]:4,record_head_fields[2]:8,record_head_fields[3]:8,record_head_fields[4]:8,
                    record_head_fields[5]:3,record_head_fields[6]:5,record_head_fields[7]:6,record_head_fields[8]:9,record_head_fields[9]:11,record_head_fields[10]:13,
                    record_head_fields[11]:14,record_head_fields[12]:15,record_head_fields[13]:16,record_head_fields[14]:17,record_head_fields[15]:18,record_head_fields[16]:19,
                    record_head_fields[17]:20,record_head_fields[18]:22,record_head_fields[19]:23,record_head_fields[20]:24,record_head_fields[21]:25}

record_head_texts =[get_text(record_head_fields[0]),get_text(record_head_fields[1]),get_text(record_head_fields[2]),get_text(record_head_fields[3]),get_text(record_head_fields[4])
                    ,get_text(record_head_fields[5]),get_text(record_head_fields[6]),get_text(record_head_fields[7]),get_text(record_head_fields[8]),get_text(record_head_fields[9])
                    ,get_text(record_head_fields[10]),get_text(record_head_fields[11]),get_text(record_head_fields[12]),get_text(record_head_fields[13]),get_text(record_head_fields[14])
                    ,get_text(record_head_fields[15]),get_text(record_head_fields[16]),get_text(record_head_fields[17]),get_text(record_head_fields[18]),get_text(record_head_fields[19])
                    ,get_text(record_head_fields[20]),get_text(record_head_fields[21])]

def get_mrecord_head_fields() :
    return record_head_fields

def get_mrecord_head_texts() :
    return record_head_texts

def convert_record(data,field) :
    if field == qts_market_field :
        return GetMarketStr(GetMarketFromCode(data))
    elif field == qts_category_field :
        return GetCategoryStr(GetCategoryFromCode(data))
    elif field == qts_secucode_field :
        return GetDisplayCodeFromCode(data)
    elif field == qts_action_field :
        return GetActionStr(data)
    elif field == qts_status_field :
        return GetStatusStr(data)
    elif field == qts_oprice_field :
        return GetRealPrice(data)
    elif field == qts_iprice_field :
        return GetRealPrice(data)
    elif field == qts_direction_field :
        return GetDirectionStr(data)
    else :
        return data

def get_mrecords_json_by_page(dbname,dbtable,page,size) :
    return get_complex_rows_json_by_page(dbname,dbtable,page,size,3,4,7,record_head_dict,fun=convert_record)
