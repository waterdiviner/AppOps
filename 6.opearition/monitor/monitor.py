#coding=utf-8
from flask import Flask, current_app, Blueprint, render_template , request, session, g, redirect, url_for, abort, flash, jsonify

monitor_page = Blueprint('monitor',__name__,template_folder='templates',static_folder='static',static_url_path='/monitor/static')

import sys
sys.path.append('{0}/../utility'.format(monitor_page.root_path))
from qtsinc import _include_plat
_include_plat(monitor_page.root_path)

from qtswebres import *
from qtsdbmrecord import *
from qtsdbmaccount import *
from qtsdbmposition import *
from qtsdbmremote import *
from qtsdbmstrategy import *

@monitor_page.route('/',defaults={'page':'monitor'})
@monitor_page.route('/<page>')
def show(page):
    try:
         return render_template('monitor.html', title='monitor')
    except :
        abort(404)

###############################################################################################################
@monitor_page.route('/record')
def show_record():
    return render_template('monitor_record.html', title='record',fields=get_mrecord_head_fields(),texts=get_mrecord_head_texts(),reses=get_resources(),colsize=len(get_mrecord_head_fields()))

@monitor_page.route('/get_record')
def get_record():
    page = request.args.get(qts_json_page_field, 0, type=int)
    rows = request.args.get(qts_json_rows_field, 0, type=int)
    dbname = request.args.get(qts_json_dbname_field, '')
    records = get_mrecords_json_by_page(dbname,qts_records_table,page-1,rows)
    return records

###############################################################################################################
@monitor_page.route('/account')
def show_account():
    return render_template('monitor_account.html', title='account',fields=get_maccount_head_fields(),texts=get_maccount_head_texts(),reses=get_resources(),colsize=len(get_maccount_head_fields()))

@monitor_page.route('/get_account')
def get_account():
    page = request.args.get(qts_json_page_field, 0, type=int)
    rows = request.args.get(qts_json_rows_field, 0, type=int)
    dbname = request.args.get(qts_json_dbname_field, '')
    accounts = get_maccounts_json_by_page(dbname,qts_accounts_table,page-1,rows)
    return accounts
###############################################################################################################
@monitor_page.route('/position')
def show_position():
    return render_template('monitor_position.html', title='position',fields=get_mposition_head_fields(),texts=get_mposition_head_texts(),reses=get_resources(),colsize=len(get_mposition_head_fields()))

@monitor_page.route('/get_position')
def get_position():
    page = request.args.get(qts_json_page_field, 0, type=int)
    rows = request.args.get(qts_json_rows_field, 0, type=int)
    dbname = request.args.get(qts_json_dbname_field, '')
    positions = get_mpositions_json_by_page(dbname,qts_positions_table,page-1,rows)
    return positions

###############################################################################################################
@monitor_page.route('/strategy')
def show_strategy():
    return render_template('monitor_strategy.html', title='strategy')

#@monitor_page.route('/get_strategy')
#def get_strategy():
#    page = request.args.get(qts_json_page_field, 0, type=int)
#    rows = request.args.get(qts_json_rows_field, 0, type=int)
#    strategys = get_mstrategys_json_by_page(qts_ss_backup_db,qts_strategys_table,page-1,rows)
#    return strategys
###############################################################################################################
@monitor_page.route('/remote')
def show_remote():
    return render_template('monitor_remote.html', title='remote',reses=get_resources())

###############################################################################################################
@monitor_page.route('/message')
def show_message():
    return render_template('monitor_message.html', title='message',reses=get_resources())

###############################################################################################################