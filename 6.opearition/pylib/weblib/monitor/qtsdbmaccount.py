#coding=utf-8
import sys
import os
sys.path.append(os.path.join(os.getenv('QTS_BASE_PATH','..'),'pylib/common'))
from qtswebdb import *

maccount_head_fields =[qts_account_field,qts_market_field,qts_category_field,qts_totalamount_field,qts_avlamount_field,
                        qts_freezeamount_field,qts_date_field,qts_currency_field,qts_user_field,qts_sharetag_field,qts_level_field,qts_viraccount_field]

maccount_head_dict ={maccount_head_fields[1]:1,maccount_head_fields[2]:1,maccount_head_fields[0]:2,maccount_head_fields[3]:3,maccount_head_fields[4]:4,
                     maccount_head_fields[5]:5,maccount_head_fields[6]:6,maccount_head_fields[7]:7,maccount_head_fields[8]:8,maccount_head_fields[9]:9,
                     maccount_head_fields[10]:10,maccount_head_fields[11]:11}

maccount_head_texts =[get_text(maccount_head_fields[0]),get_text(maccount_head_fields[1]),get_text(maccount_head_fields[2]),get_text(maccount_head_fields[3]),get_text(maccount_head_fields[4]),
                     get_text(maccount_head_fields[5]),get_text(maccount_head_fields[6]),get_text(maccount_head_fields[7]),get_text(maccount_head_fields[8]),get_text(maccount_head_fields[9]),
                     get_text(maccount_head_fields[10]),get_text(maccount_head_fields[11])]

def get_maccount_head_fields() :
    return maccount_head_fields

def get_maccount_head_texts() :
    return maccount_head_texts

def convert_maccount(data,field) :
    if field == qts_market_field :
        return GetMarketStr(GetMarketFromCode(data))
    elif field == qts_category_field :
        return GetCategoryStr(GetCategoryFromCode(data))
    elif field == qts_totalamount_field :
        return GetRealPrice(data)
    elif field == qts_avlamount_field :
        return GetRealPrice(data)
    elif field == qts_freezeamount_field :
        return GetRealPrice(data)
    else :
        return data

def get_maccounts_json_by_page(dbname,dbtable,page,size) :
    return get_complex_rows_json_by_page(dbname,dbtable,page,size,2,2,11,maccount_head_dict,pidfield=maccount_head_fields[11],fun=convert_maccount)