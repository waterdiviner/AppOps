#coding=utf-8
import sys
sys.path.append('../common')
from qtswebdb import *

mposition_head_fields =[qts_market_field,qts_category_field,qts_account_field,qts_ordercode_field,qts_type_field,qts_level_field,qts_date_field,qts_totalvol_field,
                        qts_avlvol_field,qts_workingvol_field,qts_totalcost_field,qts_avlcredempvol_field,qts_todayvol_field]

mposition_head_dict ={mposition_head_fields[0]:1,mposition_head_fields[1]:1,mposition_head_fields[2]:2,mposition_head_fields[3]:3,mposition_head_fields[4]:4,
                      mposition_head_fields[5]:5,mposition_head_fields[6]:6,mposition_head_fields[7]:7,mposition_head_fields[8]:8,mposition_head_fields[9]:9,
                      mposition_head_fields[10]:10,mposition_head_fields[11]:11,mposition_head_fields[12]:12}

mposition_head_texts =[get_text(mposition_head_fields[0]),get_text(mposition_head_fields[1]),get_text(mposition_head_fields[2]),get_text(mposition_head_fields[3]),get_text(mposition_head_fields[4]),
                     get_text(mposition_head_fields[5]),get_text(mposition_head_fields[6]),get_text(mposition_head_fields[7]),get_text(mposition_head_fields[8]),get_text(mposition_head_fields[9]),
                     get_text(mposition_head_fields[10]),get_text(mposition_head_fields[11]),get_text(mposition_head_fields[12])]

def get_mposition_head_fields() :
    return mposition_head_fields

def get_mposition_head_texts() :
    return mposition_head_texts

def convert_mposition(data,field) :
    if field == qts_market_field :
        return GetMarketStr(GetMarketFromCode(data))
    elif field == qts_category_field :
        return GetCategoryStr(GetCategoryFromCode(data))
    elif field == qts_ordercode_field :
        return GetDisplayCodeFromCode(data)
    else :
        return data

def get_mpositions_json_by_page(dbname,dbtable,page,size) :
    return get_rows_json_by_page(dbname,dbtable,page,size,mposition_head_dict,fun=convert_mposition)