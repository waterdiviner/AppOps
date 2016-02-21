#coding=utf-8
from flask import Flask, current_app, Blueprint, render_template

risk_page = Blueprint('risk',__name__,template_folder='templates',static_folder='static',static_url_path='/risk/static')

import sys
sys.path.append('{0}/../utility'.format(risk_page.root_path))
from qtsinc import _include_plat
_include_plat(risk_page.root_path)

from qtscontrol import *

@risk_page.route('/',defaults={'page':'risk'})
@risk_page.route('/<page>')
def show(page):
    try:
        return 'hello risk!'
    except :
        abort(404)

@risk_page.route('/start')
def start() :
    start_app('localhost','jack','111',None,'/home/jack/Develop/build/Debug/dist/script','./runc_server.sh myserver','myserver')
    return "start"

@risk_page.route('/stop')
def stop() :
    stop_app('localhost','jack','111',None,'myserver')
    return "stop"