#coding=utf-8
from qtswebutility import *

import sys

sys.path.append('../../database')
sys.path.append('../../utility')
#import os
#sys.path.append(os.path.join(os.getenv('QTS_BASE_PATH','../..'),'pylib/database'))
#sys.path.append(os.path.join(os.getenv('QTS_BASE_PATH','../..'),'pylib/utility'))
from qtsmysql import QtsMySql
from qtsvar import *
from qtsbizfun import *

############################################################################################################################################
def connect_db(dbname):
    try:
        current_app.logger.debug('create db client:host={0} port={1} user={2} passwd={3} dbname={4}'.format(current_app.config['HOST'],
                            current_app.config['PORT'],current_app.config['USERNAME'],current_app.config['PASSWORD'],dbname))
        return QtsMySql(current_app.config['HOST'],current_app.config['PORT'],current_app.config['USERNAME'],current_app.config['PASSWORD'],dbname)
    except :
        return None

def get_db_config(key,defvalue = None) :
    return get_global_var('qts_db_{0}'.format(key),defvalue)

def set_db_config(key,db) :
    set_global_var('qts_db_{0}'.format(key), db)

def get_db(dbname) :
    db = None
    try :
        db = get_db_config(dbname,None)
        if db == None :
            db = connect_db(dbname)
            set_db_config(dbname,db)
    except :
        current_app.logger.debug('open database is failed!')
    return db

def close_db(dbname) :
    db = None
    try :
        db = get_db_config(dbname,None)
        if db != None :
            db.Close()
    except :
        current_app.logger.debug('close database is failed!')

def db_sql_execute(dbname,sql) :
    db = get_db(dbname)
    if(db == None) :
        return False
    reses = False
    try:
        reses = db.Execute(sql)
    except:
        reses = False
    return reses

def db_sql_exist(dbname,sql) :
    db = get_db(dbname)
    if(db == None) :
        return False
    reses = False
    try:
        reses = db.Exist(sql)
    except:
        reses = False
    return reses

def db_sql_query(dbname,sql) :
    db = get_db(dbname)
    if(db == None) :
        return None
    reses = None
    try:
        reses = db.Query(sql)
    except:
        reses = None
    return reses

############################################################################################################################################
def build_insert(dbtable,kwargs) :
    fields = ''
    values = ''
    for kwarg in kwargs :
        if not kwarg.startswith(qts_db_prefix) :
            continue
        if fields == '' :
            fields = kwarg
        else :
            fields += ',' + kwarg
        if values == '' :
            if isinstance(kwargs[kwarg],str) :
                values = "'{0}'".format(kwargs[kwarg])
            else :
                values = "{0}".format(kwargs[kwarg])
        else :
            if isinstance(kwargs[kwarg],str) :
                values  += ',' "'{0}'".format(kwargs[kwarg])
            else :
                values  += ',' "{0}".format(kwargs[kwarg])
    sql = 'INSERT INTO {0}({1}) VALUES({2})'.format(dbtable,fields,values)
    return sql

def build_insert_by_dict(dbtable,rows) :
    fields = ''
    values = ''
    for field in rows :
        if not field.startswith(qts_db_prefix) :
            continue
        if fields == '' :
            fields = field
        else :
            fields += ',' + field
        if values == '' :
            if isinstance(rows[field],str) :
                values = "'{0}'".format(rows[field])
            else :
                values = "{0}".format(rows[field])
        else :
            if isinstance(rows[field],str) :
                values  += ',' "'{0}'".format(rows[field])
            else :
                values  += ',' "{0}".format(rows[field])
    sql = 'INSERT INTO {0}({1}) VALUES({2})'.format(dbtable,fields,values)
    return sql

def build_update(dbtable,kwargs) :
    updates = ''
    for kwarg in kwargs :
        if not kwarg.startswith(qts_db_prefix) :
            continue
        if updates == '' :
            if isinstance(kwargs[kwarg],str) :
                updates = kwarg + '=' + "'{0}'".format(kwargs[kwarg])
            else :
                updates = kwarg + '=' + "{0}".format(kwargs[kwarg])
        else :
            if isinstance(kwargs[kwarg],str) :
                updates += ',' + kwarg + '=' + "'{0}'".format(kwargs[kwarg])
            else :
                updates += ',' + kwarg + '=' + "{0}".format(kwargs[kwarg])
    sql = 'UPDATE {0} set {1} WHERE '.format(dbtable,updates)
    return sql

def build_update_by_dict(dbtable,rows) :
    updates = ''
    for field in rows :
        if not field.startswith(qts_db_prefix) :
            continue
        if updates == '' :
            if isinstance(rows[field],str) :
                updates = field + '=' + "'{0}'".format(rows[field])
            else :
                updates = field + '=' + "{0}".format(rows[field])
        else :
            if isinstance(rows[field],str) :
                updates += ',' + field + '=' + "'{0}'".format(rows[field])
            else :
                updates += ',' + field + '=' + "{0}".format(rows[field])
    sql = 'UPDATE {0} set {1} WHERE '.format(dbtable,updates)
    return sql

def build_query(dbtable,fields) :
    f_fields = '*'
    if (fields != None) and isinstance(fields,list) :
        f_fields = ''
        for field in fields :
            if not field.startswith(qts_db_prefix) :
                continue
            if f_fields == '' :
                f_fields = field
            else :
                f_fields += "," + field
    sql = 'SELECT {0} from {1} '.format(f_fields,dbtable)
    return sql

def build_query_condition(dbtable,fields,value,idfield=qts_id_field) :
    f_fields = '*'
    if (fields != None) and isinstance(fields,list) :
        f_fields = ''
        for field in fields :
            if not field.startswith(qts_db_prefix) :
                continue
            if f_fields == '' :
                f_fields = field
            else :
                f_fields += "," + field
    if isinstance(value,str) :
        sql = "SELECT {0} FROM {1} WHERE {2}='{3} '".format(f_fields,dbtable,idfield,value)
    else :
        sql = "SELECT {0} FROM {1} WHERE {2}={3} ".format(f_fields,dbtable,idfield,value)
    return sql

def build_query_size(dbtable,field) :
    sql = 'SELECT count({0}) as size FROM {1}'.format(field,dbtable)
    return sql

def build_query_size_condition(dbtable,field,value,idfield=qts_id_field) :
    sql = ''
    if isinstance(value,str) :
        sql = "SELECT count({0}) as size FROM {1} WHERE {2}='{3}' ".format(field,dbtable,idfield,value)
    else :
        sql = "SELECT count({0}) as size FROM {1} WHERE {2}={3} ".format(field,dbtable,idfield,value)
    return sql

def build_delete(dbtable,value,idfield=qts_id_field) :
    sql = ''
    if isinstance(value,str) :
        sql = "DELETE FROM {0} WHERE {1}='{2}' ".format(dbtable,idfield,value)
    else :
        sql = 'DELETE FROM {0} WHERE {1}={2} '.format(dbtable,idfield,value)
    return sql

############################################################################################################################################
def insert_row(dbname,dbtable,kwargs) :
    sql = build_insert(dbtable,kwargs)
    return db_sql_execute(dbname,sql)

def insert_row_by_dict(dbname,dbtable,rows) :
    sql = build_insert_by_dict(dbtable,rows)
    return db_sql_execute(dbname,sql)

def update_row(dbname,dbtable,id,kwargs,idfield = qts_autoid_field) :
    sql = build_update(dbtable,kwargs)
    sql = '{0} {1}={2} '.format(sql,idfield,id)
    return db_sql_execute(dbname,sql)

def update_row_by_dict(dbname,dbtable,rows,id,idfield = qts_autoid_field) :
    sql = build_update_by_dict(dbtable,rows)
    sql = '{0} {1}={2} '.format(sql,idfield,id)
    return db_sql_execute(dbname,sql)

def exist_row(dbname,dbtable,id,idfield = qts_id_field) :
     sql = build_query(dbtable,[idfield])
     sql = '{0} WHERE {1}={2} '.format(sql,idfield,id)
     return db_sql_exist(dbname,sql)

def delete_row(dbname,dbtable,id,idfield = qts_id_field) :
    return db_sql_execute(dbname,build_delete(dbtable,id,idfield))

def delete_rows_by_list(dbname,dbtable,lists,idfield = qts_id_field) :
    rows = list(eval(lists))
    for row in rows :
        delete_row(dbname,dbtable,row[idfield],idfield)

def update_rows_by_list(dbname,dbtable,lists,idfield = qts_autoid_field) :
    rows = list(eval(lists))
    for row in rows :
        update_row_by_dict(dbname,dbtable,row,row[idfield],idfield)

def insert_rows_by_list(dbname,dbtable,lists) :
    rows = list(eval(lists))
    for row in rows :
        insert_row_by_dict(dbname,dbtable,row)

############################################################################################################################################
def get_rows_size(dbname,dbtable,idfield = qts_autoid_field) :
    sql = build_query_size(dbtable,idfield)
    res = db_sql_query(dbname,sql)
    if res == None :
        return 0
    else :
        return res[0][0]

def get_rows_size_condition(dbname,dbtable,value,idfield = qts_id_field) :
    sql = build_query_size_condition(dbtable,value,idfield)
    res = db_sql_query(dbname,sql)
    if res == None :
        return 0
    else :
        return res[0][0]

def get_rows_list(dbname,dbtable,idfield = qts_autoid_field,fields=None) :
    sql = build_query(dbtable,fields)
    sql = '{0} ORDER BY {1} DESC '.format(sql,idfield)
    return db_sql_query(dbname,sql)

def get_rows_list_condition(dbname,dbtable,value,idfield = qts_id_field,fields=None) :
    sql = build_query_condition(dbtable,fields,value,idfield)
    sql = "{0} ORDER BY {1} DESC ".format(sql,idfield)
    return db_sql_query(dbname,sql)

def get_rows_list_by_page(dbname,dbtable,page,size,idfield = qts_autoid_field,fields=None) :
    begin = page * size
    end = begin + size
    sql = build_query(dbtable,fields)
    sql = '{0} ORDER BY {1} DESC limit {2},{3} '.format(sql,idfield,begin,end)
    return db_sql_query(dbname,sql)

def get_rows_list_condition_by_page(dbname,dbtable,page,size,value,idfield = qts_id_field,fields=None) :
    begin = page * size
    end = begin + size
    sql = build_query_condition(dbtable,fields,value,idfield)
    sql = '{0} ORDER BY {1} DESC limit {2},{3} '.format(sql,idfield,begin,end)
    return db_sql_query(dbname,sql)

def build_row_dict(datas,id,row,fun=None) :
    m_dict = dict()
    append_col(m_dict,qts_json_id_field,id)
    for col in row :
        if fun != None :
            append_col(m_dict,col,convert_number_to_str(fun(datas[row[col]],col)))
        else :
            append_col(m_dict,col,convert_number_to_str(datas[row[col]]))
    return m_dict

def get_rows_json_dict(dbname,dbtable,row,idfield=qts_autoid_field,fun=None,fields=None) :
    index = 1
    results = dict()
    results[qts_json_rows_field] = list()
    results[qts_json_total_field] = get_rows_size(dbname,dbtable,idfield)
    markets = get_rows_list(dbname,dbtable,idfield,fields)
    if markets != None :
        for market in markets :
            results[qts_json_rows_field].append(build_row_dict(market,index,row,fun))
            index += 1
    return results

def get_rows_json_dict_condition(dbname,dbtable,row,value,idfield=qts_id_field,fun=None,fields=None) :
    index = 1
    results = dict()
    results[qts_json_rows_field] = list()
    results[qts_json_total_field] = get_rows_size_condition(dbname,dbtable,value,idfield)
    markets = get_rows_list_condition(dbname,dbtable,value,idfield,fields)
    if markets != None :
        for market in markets :
            results[qts_json_rows_field].append(build_row_dict(market,index,row,fun))
            index += 1
    return results

def get_rows_json_dict_by_page(dbname,dbtable,page,size,row,idfield=qts_autoid_field,fun=None,fields=None) :
    index = 1
    results = dict()
    results["rows"] = list()
    results["total"] = get_rows_size(dbname,dbtable,idfield)
    markets = get_rows_list_by_page(dbname,dbtable,page,size,idfield,fields)
    if markets != None :
        for market in markets :
            results['rows'].append(build_row_dict(market,index,row,fun))
            index += 1
    return results

def get_rows_json_dict_condition_by_page(dbname,dbtable,page,size,row,value,idfield=qts_id_field,fun=None,fields=None) :
    index = 1
    results = dict()
    results["rows"] = list()
    results["total"] = get_rows_size_condition(dbname,dbtable,value,idfield)
    markets = get_rows_list_condition_by_page(dbname,dbtable,page,size,value,idfield,fields)
    if markets != None :
        for market in markets :
            results['rows'].append(build_row_dict(market,index,row,fun))
            index += 1
    return results

def get_rows_json(dbname,dbtable,row,idfield=qts_autoid_field,fun=None,fields=None) :
    return make_response_json_for_dict(get_rows_json_dict(dbname,dbtable,row,idfield,fun,fields))

def get_rows_json_condition(dbname,dbtable,row,value,idfield=qts_id_field,fun=None,fields=None) :
    return make_response_json_for_dict(get_rows_json_dict_condition(dbname,dbtable,row,value,idfield,fun,fields))

def get_rows_json_by_page(dbname,dbtable,page,size,row,idfield=qts_autoid_field,fun=None,fields=None) :
    return make_response_json_for_dict(get_rows_json_dict_by_page(dbname,dbtable,page,size,row,idfield,fun,fields))

def get_rows_json_condition_by_page(dbname,dbtable,page,size,row,value,idfield=qts_id_field,fun=None,fields=None) :
    return make_response_json_for_dict(get_rows_json_dict_condition_by_page(dbname,dbtable,page,size,row,value,idfield,fun,fields))

############################################################################################################################################
def get_complex_childs_list(results,dbname,dbtable,depth,items,idpos,idfield=qts_autoid_field,pidfield=qts_parentid_field) :
    f_conds = list()
    for item in items :
        f_conds.append(item[idpos])
    if len(f_conds) == 0 :
        return None
    sql = 'SELECT * FROM {0} WHERE {1} in {2}'.format(dbtable,pidfield,str(f_conds).replace('[','(').replace(']',')').replace('L',''))
    reses = db_sql_query(dbname,sql)
    if reses == None :
        return None
    results.append(reses)
    depth -= 1
    if depth > 0 :
        get_complex_childs_list(results,dbname,dbtable,depth,reses,idpos,idfield,pidfield)

def get_complex_rows_list(dbname,dbtable,depth,idpos,idfield=qts_autoid_field,pidfield=qts_parentid_field) :
    results = list()
    sqlone = 'SELECT * FROM {0} WHERE {1}=0 ORDER BY {2} DESC '.format(dbtable,pidfield,idfield)
    reses = db_sql_query(dbname,sqlone)
    if reses == None :
        return None
    results.append(reses)
    if depth == 0 :
        return results
    else :
        get_complex_childs_list(results,dbname,dbtable,depth,reses,idpos,idfield,pidfield)
    return results

def get_complex_rows_list_by_page(dbname,dbtable,page,size,depth,idpos,idfield=qts_autoid_field,pidfield=qts_parentid_field) :
    results = list()
    begin = page * size
    end = begin + size
    sqlone = 'SELECT * FROM {0} WHERE {1}=0 ORDER BY {2} DESC LIMIT {3},{4}'.format(dbtable,pidfield,idfield,begin,end)
    reses = db_sql_query(dbname,sqlone)
    if reses == None :
        return None
    results.append(reses)
    if depth == 0 :
        return results
    else :
        get_complex_childs_list(results,dbname,dbtable,depth,reses,idpos,idfield,pidfield)
    return results

def get_complex_rows_by_parentid(parentid,rows,pidpos) :
    results = list()
    if rows != None :
        for row in rows :
            if row[pidpos] == parentid :
                results.append(row)
    return results

def has_complex_child(parentid,rows,pidpos) :
    has_child = False
    if rows != None :
        for row in rows :
            if row[pidpos] == parentid :
                has_child = True
                break
    return has_child

def build_complex_row_dict(datas,ownerid,parentid,haschild,row,fun=None):
    rec_dict = build_row_dict(datas,ownerid,row,fun)
    if parentid :
        append_col(rec_dict,qts_json_parent_field,parentid)
    if haschild :
        append_col(rec_dict,qts_json_state_field,"closed")
    return rec_dict

def build_complex_rows_by_child(results,totals,depth,indexes,index,idpos,pidpos,row,fun=None) :
    cindex = index
    pindex = 0
    haschild = False
    if len(totals) > depth :
        for item in totals[depth] :
            pindex = get_parentid(indexes,item[pidpos])
            if depth < (len(totals) - 1) :
                haschild = has_complex_child(item[idpos],totals[depth + 1],pidpos)
            append_row(results,build_complex_row_dict(item,cindex,pindex,haschild,row,fun))
            append_parentid(indexes,item[idpos],cindex)
            cindex += 1
    return cindex

def get_complex_rows_json_dict(dbname,dbtable,depth,idpos,pidpos,row,fun=None,idfield=qts_autoid_field,pidfield=qts_parentid_field) :
    indexes = dict()
    results = dict()
    index = 1
    findex = 0
    results[qts_json_rows_field] = list()
    results[qts_json_total_field] = get_rows_size(dbname,dbtable,idfield)
    totals = get_complex_rows_list(dbname,dbtable,depth,idpos,idfield,pidfield)
    if totals != None :
        while True :
            index = build_complex_rows_by_child(results,totals,findex,indexes,index,idpos,pidpos,row,fun)
            findex += 1
            if findex >= depth :
                break
    return results

def get_complex_rows_json_dict_by_page(dbname,dbtable,page,size,depth,idpos,pidpos,row,fun=None,idfield=qts_autoid_field,pidfield=qts_parentid_field) :
    indexes = dict()
    results = dict()
    index = 1
    findex = 0
    results[qts_json_rows_field] = list()
    results[qts_json_total_field] = get_rows_size(dbname,dbtable,idfield)
    totals = get_complex_rows_list_by_page(dbname,dbtable,page,size,depth,idpos,idfield,pidfield)
    if totals != None :
        while True :
            index = build_complex_rows_by_child(results,totals,findex,indexes,index,idpos,pidpos,row,fun)
            findex += 1
            if findex >= depth :
                break
    return results

def get_complex_rows_json(dbname,dbtable,depth,idpos,pidpos,row,fun=None,idfield=qts_autoid_field,pidfield=qts_parentid_field) :
    return make_response_json_for_dict(get_complex_rows_json_dict(dbname,dbtable,depth,idpos,pidpos,row,fun,idfield,pidfield))

def get_complex_rows_json_by_page(dbname,dbtable,page,size,depth,idpos,pidpos,row,fun=None,idfield=qts_autoid_field,pidfield=qts_parentid_field) :
    return make_response_json_for_dict(get_complex_rows_json_dict_by_page(dbname,dbtable,page,size,depth,idpos,pidpos,row,fun,idfield,pidfield))

############################################################################################################################################
