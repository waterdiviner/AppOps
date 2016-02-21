#coding=utf-8
import sys
import time
import os
################################################################################################
from flask import Flask, current_app

#py库的路径
sys.path.append('../../pylib/utility')
sys.path.append('../common')

from qtsvar import *
from qtsfun import *
from qtswebssh import *

######################################################################################################################################
def get_control_message(host,user,passwd,port) :
    return get_ssh_result(host,user,passwd,port)

def execute_command(host,user,passwd,port,cmdpath,cmd) :
    if ssh_command_has_port(host,user,passwd,port,'cd {0}'.format(cmdpath)) :
        return ssh_command_has_port(host,user,passwd,port,cmd)
    return False

######################################################################################################################################
def exist_app(host,user,passwd,port,flag) :
    if ssh_command_has_port(host,user,passwd,port,'ps -ef |grep app_name={0} |'.format(flag) + "awk '{print $2}'") :
        str_result = get_control_message(host,user,passwd,port)
        str_items = str_result.split('\n')
        size = 0
        for str_item in str_items :
            if str_item.strip("\r\n").strip().isdigit() :
                size += 1
        return (size >= 2)
    else :
        return False

def stop_app(host,user,passwd,port,flag) :
    if exist_app(host,user,passwd,port,flag) :
        return ssh_command_has_port(host,user,passwd,port,'ps -ef |grep app_name={0} |'.format(flag) + "awk '{print $2}'|xargs kill -9")

def start_app(host,user,passwd,port,cmdpath,cmd,flag) :
    stop_app(host,user,passwd,port,flag)
    if not execute_command(host,user,passwd,port,cmdpath,cmd) :
        stop_app(host,user,passwd,port,flag)
        return False
    else :
        return exist_app(host,user,passwd,port,flag)

######################################################################################################################################
def exist_file(host,user,passwd,port,path,file) :
    if execute_command(host,user,passwd,port,path,'ls |grep {0}'.format(file)) :
        str_result = get_control_message(host,user,passwd,port)
        if str_result.find(file) >= 1 :
            return True
    return False

def exist_path(host,user,passwd,port,path) :
    if ssh_command_has_port(host,user,passwd,port,'cd {0}'.format(path)) :
        str_result = get_control_message(host,user,passwd,port)
        if (str_result.find('没有') >= 1) or (str_result.find('No') >= 1) or (str_result.find('no') >= 1) :
            return False
        else :
            return True
    return False

def exist_dir(host,user,passwd,port,path,dir) :
    return exist_path(host,user,passwd,port,'{0}/{1}'.format(path,dir))

######################################################################################################################################
def start_ss(host,user,passwd,port,path,flag) :
    cfg_path = CombinePath(path,'cfg')
    script_path = CombinePath(path,'script')
    data_path = CombinePath(path,'data')

######################################################################################################################################
(QTS_CONVERT_TYPE_FILE,
QTS_CONVERT_TYPE_DB,
QTS_CONVERT_TYPE_DBTOFILE)=(1,2,3)

######################################################################################################################################
def get_secuinfo_from_server(host,user,passwd,port,cmdpath,target) :
    return execute_command(host,user,passwd,port,cmdpath,'./{0} --cmd=query --type=2 --file={1}/{2}'.format(qts_get_secuinfo_file,target,qts_secuinfo_middle_csv))

def secuinfo_to_file(host,user,passwd,port,cmdpath,source,target) :
    return execute_command(host,user,passwd,port,cmdpath,'python {0} {1} {2} {3}'.format(qts_convert_secuinfo_cmd,QTS_CONVERT_TYPE_FILE,source,target))

def secuinfo_to_db(cmdpath,source,dbname) :
    return execute_command(host,user,passwd,port,cmdpath,'python {0}  {1} {2} {3} {4} {5} {6} {7}'.format(qts_convert_secuinfo_cmd,QTS_CONVERT_TYPE_DB,source,
                current_app.config['HOST'],current_app.config['PORT'],current_app.config['USERNAME'],current_app.config['PASSWORD'],dbname))

def secuinfo_db_to_file(cmdpath,dbname,target) :
    return execute_command(host,user,passwd,port,cmdpath,'python {0}  {1} {2} {3} {4} {5} {6} {7}'.format(qts_convert_secuinfo_cmd,QTS_CONVERT_TYPE_DBTOFILE,target,
                current_app.config['HOST'],current_app.config['PORT'],current_app.config['USERNAME'],current_app.config['PASSWORD'],dbname))

######################################################################################################################################
(QTS_CONVERT_BACKUP_TYPE_RECORD,
QTS_CONVERT_BACKUP_TYPE_POSITION,
QTS_CONVERT_BACKUP_TYPE_ACCOUNT,
QTS_CONVERT_BACKUP_TYPE_WORKING)=(1,2,3,4)

def convert_backup_dat_to_csv(cmdpath,type,source,target) :
    return execute_command(host,user,passwd,port,cmdpath,'./{0} --cmd=btox --type={1} --source={2} --target={3}'.format(qts_convert_backup_file,type,source,target))

def convert_backup_csv_to_dat(cmdpath,type,source,target) :
    return execute_command(host,user,passwd,port,cmdpath,'./{0} --cmd=xtob --type={1} --source={2} --target={3}'.format(qts_convert_backup_file,type,source,target))

######################################################################################################################################
def clearing_position_to_file(cmdpath,source,target) :
    return execute_command(host,user,passwd,port,cmdpath,'python {0} {1} {2} {3}'.format(qts_clearing_position_cmd,QTS_CONVERT_TYPE_FILE,source,target))

def clearing_position_to_db(cmdpath,source,dbname) :
    return execute_command(host,user,passwd,port,cmdpath,'python {0}  {1} {2} {3} {4} {5} {6} {7}'.format(qts_clearing_position_cmd,QTS_CONVERT_TYPE_DB,source,
                current_app.config['HOST'],current_app.config['PORT'],current_app.config['USERNAME'],current_app.config['PASSWORD'],dbname))

def clearing_position_db_to_file(cmdpath,dbname,target) :
    return execute_command(host,user,passwd,port,cmdpath,'python {0}  {1} {2} {3} {4} {5} {6} {7}'.format(qts_clearing_position_cmd,QTS_CONVERT_TYPE_DBTOFILE,target,
                current_app.config['HOST'],current_app.config['PORT'],current_app.config['USERNAME'],current_app.config['PASSWORD'],dbname))

######################################################################################################################################
def clearing_account_to_file(cmdpath,source,target) :
    return execute_command(host,user,passwd,port,cmdpath,'python {0} {1} {2} {3}'.format(qts_clearing_account_cmd,QTS_CONVERT_TYPE_FILE,source,target))

def clearing_account_to_db(cmdpath,source,dbname) :
    return execute_command(host,user,passwd,port,cmdpath,'python {0}  {1} {2} {3} {4} {5} {6} {7}'.format(qts_clearing_account_cmd,QTS_CONVERT_TYPE_DB,source,
                current_app.config['HOST'],current_app.config['PORT'],current_app.config['USERNAME'],current_app.config['PASSWORD'],dbname))

def clearing_account_db_to_file(cmdpath,dbname,target) :
    return execute_command(host,user,passwd,port,cmdpath,'python {0}  {1} {2} {3} {4} {5} {6} {7}'.format(qts_clearing_account_cmd,QTS_CONVERT_TYPE_DBTOFILE,target,
                current_app.config['HOST'],current_app.config['PORT'],current_app.config['USERNAME'],current_app.config['PASSWORD'],dbname))

######################################################################################################################################



######################################################################################################################################