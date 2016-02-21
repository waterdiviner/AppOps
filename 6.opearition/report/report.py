#coding=utf-8
from flask import Flask, current_app, Blueprint, render_template

report_page = Blueprint('report',__name__,template_folder='templates',static_folder='static',static_url_path='/report/static')

import sys
sys.path.append('{0}/../utility'.format(report_page.root_path))
from qtsinc import _include_plat
_include_plat(report_page.root_path)

@report_page.route('/',defaults={'page':'report'})
@report_page.route('/<page>')
def show(page):
    try:
        return 'hello world! report page!'
    except :
        abort(404)