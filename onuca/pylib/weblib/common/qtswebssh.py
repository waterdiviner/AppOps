#coding=utf-8
from qtswebutility import *

import sys
sys.path.append('../../utility')
sys.path.append('../../net/control')

from qtsvar import *
from qtsbiz import *
from qtsssh import *

############################################################################################################################################
def get_ssh_config(host,user,port,defvalue = None) :
    try :
        if port != None :
            return get_global_var('qts_ssh_{0}_{1}_{2}'.format(host,user,port),defvalue)
        else :
            return get_global_var('qts_ssh_{0}_{1}'.format(host,user),defvalue)
    except:
        return defvalue

def set_ssh_config(host,user,port,ssh) :
    if port != None :
        set_global_var('qts_ssh_{0}_{1}_{2}'.format(host,user,port),ssh)
    else :
        set_global_var('qts_ssh_{0}_{1}'.format(host,user), ssh)

def get_ssh(host,user,passwd,port = None) :
    ssh = None
    try :
        ssh = get_ssh_config(host,user,port,None)
        if ssh == None :
            current_app.logger.debug('create ssh client:host={0} user={1} passwd={2} port={3}'.format(host,user,passwd,port))
            ssh = QtsSSHClient(host,user,passwd,port)
            ssh.connect()
            set_ssh_config(host,user,port,ssh)
    except :
        current_app.logger.debug('open ssh is failed!')
    return ssh

def close_ssh(host,user,port = None) :
    ssh = None
    try :
        ssh = get_ssh_config(host,user,port,None)
        if ssh != None :
            ssh.close()
    except :
        current_app.logger.debug('close ssh is failed!')

def ssh_command_no_port(host,user,passwd,cmd) :
    result = False
    ssh = get_ssh(host,user,passwd)
    if ssh != None :
        result = ssh.command(cmd)
        if result :
            current_app.logger.debug(ssh.tostring())
        else :
            current_app.logger.error(ssh.tostring())
    else :
        result = False
    return result

def ssh_command_has_port(host,user,passwd,port,cmd) :
    result = False
    ssh = get_ssh(host,user,passwd,port)
    if ssh != None :
        result = ssh.command(cmd)
        if result :
            current_app.logger.debug(ssh.tostring())
        else :
            current_app.logger.error(ssh.tostring())
    else :
        result = False
    return result

def get_ssh_result(host,user,passwd,port) :
    ssh = get_ssh(host,user,passwd,port)
    if ssh != None :
        return ssh.tostring()
    else :
        return ''