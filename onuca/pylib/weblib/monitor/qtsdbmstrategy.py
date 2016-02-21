#coding=utf-8
import sys
sys.path.append('../common')
from qtswebdb import *

mstrategy_head_fields =[qts_autoid_field,qts_market_field,qts_category_field,qts_account_field,qts_totalamount_field,qts_avlamount_field,
                        qts_freezeamount_field,qts_date_field,qts_currency_field,qts_user_field,qts_sharetag_field,qts_level_field,qts_viraccount_field]

mstrategy_head_dict ={mstrategy_head_fields[0]:0,mstrategy_head_fields[1]:1,mstrategy_head_fields[2]:1,mstrategy_head_fields[3]:2,mstrategy_head_fields[4]:3,mstrategy_head_fields[5]:4,
                        mstrategy_head_fields[6]:5,mstrategy_head_fields[7]:6,mstrategy_head_fields[8]:7,mstrategy_head_fields[9]:8,mstrategy_head_fields[10]:9,mstrategy_head_fields[11]:10,mstrategy_head_fields[12]:11}

mstrategy_head_texts =[get_text(mstrategy_head_fields[0]),get_text(mstrategy_head_fields[1]),get_text(mstrategy_head_fields[2]),get_text(mstrategy_head_fields[3]),get_text(mstrategy_head_fields[4]),
                     get_text(mstrategy_head_fields[5]),get_text(mstrategy_head_fields[6]),get_text(mstrategy_head_fields[7]),get_text(mstrategy_head_fields[8]),get_text(mstrategy_head_fields[9]),
                     get_text(mstrategy_head_fields[10]),get_text(mstrategy_head_fields[11]),get_text(mstrategy_head_fields[12])]

def get_mstrategy_head_fields() :
    return mstrategy_head_fields

def get_mstrategy_head_texts() :
    return mstrategy_head_texts

def get_mstrategys_json_by_page(dbname,dbtable,page,size) :
    return get_complex_rows_json_by_page(dbname,dbtable,page,size,2,2,11,mstrategy_head_dict,None)