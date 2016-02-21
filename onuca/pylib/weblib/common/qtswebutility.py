#coding=utf-8
import json
from flask import Flask, current_app, g, jsonify, request, session, make_response

############################################################################################################################################
def get_global_var(key,defvalue = None) :
    try :
        return current_app.config[key]
    except:
        return defvalue

def set_global_var(key,db) :
    current_app.config[key] = db

def get_text(text,**kwargs) :
    return text

def get_root_path(blue_print_path) :
    return blue_print_path + '/../'

def build_path(blue_print_path,subpath):
    return get_root_path(blue_print_path) + subpath

############################################################################################################################################
def get_form(key,defvalue=None) :
    try :
        return request.form[key]
    except :
        return defvalue

def append_item_from_form(items,field) :
    try :
        items[field] = str(request.form[field].encode('utf8'))
    except :
        return False
    return True

def append_items_from_form(items,fields) :
    breturn = True
    for field in fields :
        if not append_item_from_form(items,field) :
            breturn = False
            break
    return breturn

def get_arg_string(key,defvalue='') :
     try :
        return request.args.get(key,defvalue)
     except :
         return defvalue

def get_arg_int(key,defvalue=0) :
     try :
        return request.args.get(key,defvalue,type=int)
     except :
         return defvalue

def get_arg_float(key,defvalue=0) :
     try :
        return request.args.get(key,defvalue,type=float)
     except :
         return defvalue

def build_reponse(msg_dict,code) :
    return make_response(jsonify(msg_dict), code)

############################################################################################################################################
def convert_number_to_str(number):
    return "{0}".format(str(number).replace('L',''))

def append_row(results,row) :
    results["rows"].append(row)

def append_col(row,key,value) :
    row["{0}".format(key)] = value

def get_parentid(indexes,key) :
    name = 'key_{0}'.format(key)
    try :
        return indexes[name]
    except :
        return 0

def append_parentid(indexes,key,value) :
    name = 'key_{0}'.format(key)
    indexes[name] = value

############################################################################################################################################
def make_response_json_for_dict(dict) :
    return jsonify(dict)

def make_response_json_for_list(list) :
    return make_response(json.dumps(list))

############################################################################################################################################
def load_json(file) :
    fin = open(file,'r')
    s = json.load(fin)
    fin.close()
    return s

def json_file_response(file) :
    return make_response(load_json(file))

############################################################################################################################################