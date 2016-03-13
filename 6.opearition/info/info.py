#coding=utf-8
from flask import Flask, current_app, Blueprint, render_template , request, session, g, redirect, url_for, abort, flash, jsonify ,make_response

info_page = Blueprint('info',__name__,template_folder='templates',static_folder='static',static_url_path='/info/static')

import sys
sys.path.append('{0}/../utility'.format(info_page.root_path))
from qtsinc import _include_plat
_include_plat(info_page.root_path)

from qtswebres import *
from qtsdbmachine import *
from qtsdbadmin import *
from qtsdbapp import *
from qtsdbjob import *
from qtsdbright import *
from qtsdbproduct import *
from qtsdbsecuinfo import *
from qtsdbstrategyinapp import *
from qtsdbstrategyinproduct import *
from qtsdbposition import *
from qtsdbtrade import *
from qtsdbuser import *
from qtsdbexchange import *
from qtsdbstrategy import *


##########################################################################################################
@info_page.route('/',defaults={'page':'info'})
@info_page.route('/<page>')
def show(page):
    try:
        return render_template('info.html', title='info',reses=get_resources())
    except :
        abort(404)

##########################################################################################################
@info_page.route('/machine')
def show_machine():
    machine_types = get_machine_type(build_path(info_page.root_path,'static/data/qts_machine_type.json'))
    return render_template('info_machine.html', title='machine',fields=get_machine_head_fields(),
                           texts=get_machine_head_texts(),reses=get_resources(),colsize=len(get_machine_head_fields()),
                           machine_types=machine_types)

@info_page.route('/get_machine')
def get_machine():
    page = get_arg_int(qts_json_page_field)
    rows = get_arg_int(qts_json_rows_field)
    return get_machines_json_by_page(qts_config_db,qts_machines_table,page - 1,rows)
    #print x;
    #return x;

@info_page.route('/_insert_machine', methods=[qts_web_get_field, qts_web_post_field])
def _insert_machine():
    if request.method == qts_web_post_field :
        items = dict()
        append_items_from_form(items,get_machine_head_fields()[1:])
        print(items)
        if not exist_machine(qts_config_db,qts_machines_table,items[qts_id_field]) :
            insert_machine(qts_config_db,qts_machines_table,items)
            return build_reponse({'success': 'insert successed!'}, 200)
        else :
            return build_reponse({'success': 'insert failed!'}, 400)
    return build_reponse({'error': 'insert failed!'}, 400)

@info_page.route('/_update_machine', methods=[qts_web_get_field, qts_web_post_field])
def _update_machine():
    inserted = get_form(qts_json_inserted,'')
    deleted = get_form(qts_json_deleted,'')
    updated = get_form(qts_json_updated,'')
    current_app.logger.debug('update_machine: {0} {1} {2}'.format(inserted,deleted,updated))
    if inserted != '' :
        insert_machines(qts_config_db,qts_machines_table,inserted)
    if deleted != '' :
        delete_machines(qts_config_db,qts_machines_table,deleted)
    if updated != '' :
        update_machines(qts_config_db,qts_machines_table,updated)
    return build_reponse({'success': 'update successed!'}, 200)

##########################################################################################################
@info_page.route('/app')
def show_app():
    machine_ids = get_machines_json_machineid(qts_config_db,qts_machines_table)
    app_types = get_app_type(build_path(info_page.root_path,'static/data/qts_app_type.json'))
    return render_template('info_app.html', title='app',fields=get_app_head_fields(),texts=get_app_head_texts(),reses=get_resources(),
                           colsize=len(get_app_head_fields()),machine_ids=machine_ids,app_types=app_types)

@info_page.route('/get_app_machineid')
def get_app_machineid():
    return make_response_json_for_list(get_machines_json_machineid(qts_config_db,qts_machines_table))

@info_page.route('/get_app')
def get_app():
    page = get_arg_int(qts_json_page_field)
    rows = get_arg_int(qts_json_rows_field)
    return get_apps_json_by_page(qts_config_db,qts_apps_table,page - 1,rows)

@info_page.route('/_insert_app', methods=[qts_web_get_field, qts_web_post_field])
def _insert_app():
    if request.method == qts_web_post_field :
        items = dict()
        append_items_from_form(items,get_app_head_fields()[1:])
        print(items)
        if not exist_app(qts_config_db,qts_apps_table,items[qts_id_field]) :
            insert_app(qts_config_db,qts_apps_table,items)
            return build_reponse({'success': 'insert successed!'}, 200)
        else :
            return build_reponse({'success': 'insert failed!'}, 400)
    return build_reponse({'error': 'insert failed!'}, 400)

@info_page.route('/_update_app', methods=[qts_web_get_field, qts_web_post_field])
def _update_app():
    inserted = get_form(qts_json_inserted,'')
    deleted = get_form(qts_json_deleted,'')
    updated = get_form(qts_json_updated,'')
    current_app.logger.debug('update_app: {0} {1} {2}'.format(inserted,deleted,updated))
    if inserted != '' :
        insert_apps(qts_config_db,qts_apps_table,inserted)
    if deleted != '' :
        delete_apps(qts_config_db,qts_apps_table,deleted)
    if updated != '' :
        update_apps(qts_config_db,qts_apps_table,updated)
    return build_reponse({'success': 'update successed!'}, 200)

##########################################################################################################
@info_page.route('/job')
def show_job():
    machine_ids = get_machines_json_machineid(qts_config_db,qts_machines_table)
    job_types = get_job_type(build_path(info_page.root_path,'static/data/qts_job_type.json'))
    return render_template('info_job.html', title='job',fields=get_job_head_fields(),texts=get_job_head_texts(),reses=get_resources(),
                           colsize=len(get_job_head_fields()),machine_ids=machine_ids,job_types=job_types)

@info_page.route('/get_job_machineid')
def get_job_machineid():
    return make_response_json_for_list(get_machines_json_machineid(qts_config_db,qts_machines_table))

@info_page.route('/get_job')
def get_job():
    page = get_arg_int(qts_json_page_field)
    rows = get_arg_int(qts_json_rows_field)
    return get_jobs_json_by_page(qts_config_db,qts_jobs_table,page - 1,rows)

@info_page.route('/_insert_job', methods=[qts_web_get_field, qts_web_post_field])
def _insert_job():
    if request.method == qts_web_post_field :
        items = dict()
        jobend_items_from_form(items,get_job_head_fields()[1:])
        print(items)
        if not exist_job(qts_config_db,qts_jobs_table,items[qts_id_field]) :
            insert_job(qts_config_db,qts_jobs_table,items)
            return build_reponse({'success': 'insert successed!'}, 200)
        else :
            return build_reponse({'success': 'insert failed!'}, 400)
    return build_reponse({'error': 'insert failed!'}, 400)

@info_page.route('/_update_job', methods=[qts_web_get_field, qts_web_post_field])
def _update_job():
    inserted = get_form(qts_json_inserted,'')
    deleted = get_form(qts_json_deleted,'')
    updated = get_form(qts_json_updated,'')
    current_job.logger.debug('update_job: {0} {1} {2}'.format(inserted,deleted,updated))
    if inserted != '' :
        insert_jobs(qts_config_db,qts_jobs_table,inserted)
    if deleted != '' :
        delete_jobs(qts_config_db,qts_jobs_table,deleted)
    if updated != '' :
        update_jobs(qts_config_db,qts_jobs_table,updated)
    return build_reponse({'success': 'update successed!'}, 200)
    
##########################################################################################################

@info_page.route('/right')
def show_right():
#    machine_types = get_machine_type(build_path(info_page.root_path,'static/data/qts_machine_type.json'))
    return render_template('info_right.html', title='right',fields=get_right_head_fields(),
                           texts=get_right_head_texts(),reses=get_resources(),colsize=len(get_right_head_fields()) )

@info_page.route('/get_right')
def get_right():
    page = get_arg_int(qts_json_page_field)
    rows = get_arg_int(qts_json_rows_field)
    items= get_rights_json_by_page(qts_config_db,qts_rights_table,page - 1,rows)
    print items
    return items

@info_page.route('/_insert_right', methods=[qts_web_get_field, qts_web_post_field])
def _insert_right():
    if request.method == qts_web_post_field :
        items = dict()
        append_items_from_form(items,get_right_head_fields()[1:])
        print(items)
        if not exist_right(qts_config_db,qts_rights_table,items[qts_id_field]) :
            insert_right(qts_config_db,qts_rights_table,items)
            return build_reponse({'success': 'insert successed!'}, 200)
        else :
            return build_reponse({'success': 'insert failed!'}, 400)
    return build_reponse({'error': 'insert failed!'}, 400)

@info_page.route('/_update_right', methods=[qts_web_get_field, qts_web_post_field])
def _update_right():
    inserted = get_form(qts_json_inserted,'')
    deleted = get_form(qts_json_deleted,'')
    updated = get_form(qts_json_updated,'')
    current_app.logger.debug('update_right: {0} {1} {2}'.format(inserted,deleted,updated))
    if inserted != '' :
        insert_rights(qts_config_db,qts_rights_table,inserted)
    if deleted != '' :
        delete_rights(qts_config_db,qts_rights_table,deleted)
    if updated != '' :
        update_rights(qts_config_db,qts_rights_table,updated)
    return build_reponse({'success': 'update successed!'}, 200)

##########################################################################################################

@info_page.route('/product')
def show_product():
    machine_ids = get_machines_json_machineid(qts_config_db,qts_machines_table)
    app_types = get_app_type(build_path(info_page.root_path,'static/data/qts_app_type.json'))
    return render_template('info_product.html', title='product',fields=get_product_head_fields(),texts=get_product_head_texts(),reses=get_resources(),
                           colsize=len(get_product_head_fields()) )

@info_page.route('/get_product')
def get_product():
    page = get_arg_int(qts_json_page_field)
    rows = get_arg_int(qts_json_rows_field)
    return get_apps_json_by_page(qts_config_db,qts_products_table,page - 1,rows)

@info_page.route('/_insert_product', methods=[qts_web_get_field, qts_web_post_field])
def _insert_product():
    if request.method == qts_web_post_field :
        items = dict()
        append_items_from_form(items,get_app_head_fields()[1:])
        print(items)
        if not exist_product(qts_config_db,qts_products_table,items[qts_id_field]) :
            insert_product(qts_config_db,qts_products_table,items)
            return build_reponse({'success': 'insert successed!'}, 200)
        else :
            return build_reponse({'success': 'insert failed!'}, 400)
    return build_reponse({'error': 'insert failed!'}, 400)

@info_page.route('/_update_product', methods=[qts_web_get_field, qts_web_post_field])
def _update_product():
    inserted = get_form(qts_json_inserted,'')
    deleted = get_form(qts_json_deleted,'')
    updated = get_form(qts_json_updated,'')
    current_app.logger.debug('update_product: {0} {1} {2}'.format(inserted,deleted,updated))
    if inserted != '' :
        insert_products(qts_config_db,qts_products_table,inserted)
    if deleted != '' :
        delete_products(qts_config_db,qts_products_table,deleted)
    if updated != '' :
        update_products(qts_config_db,qts_products_table,updated)
    return build_reponse({'success': 'update successed!'}, 200)

##########################################################################################################

@info_page.route('/secuinfos')
def show_secuinfos():
    machine_ids = get_machines_json_machineid(qts_config_db,qts_machines_table)
    app_types = get_app_type(build_path(info_page.root_path,'static/data/qts_app_type.json'))
    return render_template('info_secuinfos.html', title='secuinfos',fields=get_secuinfo_s_head_fields(),texts=get_secuinfo_s_head_texts(),reses=get_resources(),colsize=len(get_secuinfo_s_head_fields()) )


@info_page.route('/get_secuinfos')
def get_secuinfos():
    page = get_arg_int(qts_json_page_field)
    rows = get_arg_int(qts_json_rows_field)
    return get_apps_json_by_page(qts_config_db,qts_products_table,page - 1,rows)

@info_page.route('/_insert_secuinfos', methods=[qts_web_get_field, qts_web_post_field])
def _insert_secuinfos():
    if request.method == qts_web_post_field :
        items = dict()
        append_items_from_form(items,get_app_head_fields()[1:])
        print(items)
        if not exist_secuinfos(qts_loader_db,qts_secuinfo_s_table,items[qts_id_field]) :
            insert_secuinfos(qts_loader_db,qts_secuinfo_s_table,items)
            return build_reponse({'success': 'insert successed!'}, 200)
        else :
            return build_reponse({'success': 'insert failed!'}, 400)
    return build_reponse({'error': 'insert failed!'}, 400)

@info_page.route('/_update_secuinfos', methods=[qts_web_get_field, qts_web_post_field])
def _update_secuinfos():
    inserted = get_form(qts_json_inserted,'')
    deleted = get_form(qts_json_deleted,'')
    updated = get_form(qts_json_updated,'')
    current_app.logger.debug('update_product: {0} {1} {2}'.format(inserted,deleted,updated))
    if inserted != '' :
        insert_secuinfoss(qts_loader_db,qts_secuinfo_s_table,inserted)
    if deleted != '' :
        delete_secuinfoss(qts_loader_db,qts_secuinfo_s_table,deleted)
    if updated != '' :
        update_secuinfoss(qts_loader_db,qts_secuinfo_s_table,updated)
    return build_reponse({'success': 'update successed!'}, 200)

##########################################################################################################

@info_page.route('/secuinfod')
def show_secuinfod():
    machine_ids = get_machines_json_machineid(qts_config_db,qts_machines_table)
    app_types = get_app_type(build_path(info_page.root_path,'static/data/qts_app_type.json'))
    return render_template('info_secuinfod.html', title='secuinfod',fields=get_secuinfo_d_head_fields(),texts=get_secuinfo_d_head_texts(),reses=get_resources(),colsize=len(get_secuinfo_d_head_fields()) )


@info_page.route('/get_secuinfod')
def get_secuinfod():
    page = get_arg_int(qts_json_page_field)
    rows = get_arg_int(qts_json_rows_field)
    return get_apps_json_by_page(qts_loader_db,qts_secuinfo_d_table,page - 1,rows)

@info_page.route('/_insert_secuinfod', methods=[qts_web_get_field, qts_web_post_field])
def _insert_secuinfod():
    if request.method == qts_web_post_field :
        items = dict()
        append_items_from_form(items,get_app_head_fields()[1:])
        print(items)
        if not exist_secuinfod(qts_loader_db,qts_secuinfo_d_table,items[qts_id_field]) :
            insert_secuinfod(qts_loader_db,qts_secuinfo_d_table,items)
            return build_reponse({'success': 'insert successed!'}, 200)
        else :
            return build_reponse({'success': 'insert failed!'}, 400)
    return build_reponse({'error': 'insert failed!'}, 400)

@info_page.route('/_update_secuinfod', methods=[qts_web_get_field, qts_web_post_field])
def _update_secuinfod():
    inserted = get_form(qts_json_inserted,'')
    deleted = get_form(qts_json_deleted,'')
    updated = get_form(qts_json_updated,'')
    current_app.logger.debug('update_product: {0} {1} {2}'.format(inserted,deleted,updated))
    if inserted != '' :
        insert_secuinfods(qts_loader_db,qts_secuinfo_d_table,inserted)
    if deleted != '' :
        delete_secuinfods(qts_loader_db,qts_secuinfo_d_table,deleted)
    if updated != '' :
        update_secuinfods(qts_loader_db,qts_secuinfo_d_table,updated)
    return build_reponse({'success': 'update successed!'}, 200)


##########################################################################################################


@info_page.route('/strategyinapp')
def show_strategyinapp():
    return render_template('info_strategyinapp.html', title='strategyinapp',fields=get_strategyinapp_head_fields(),texts=get_strategyinapp_head_texts(),reses=get_resources(),
                           colsize=len(get_strategyinapp_head_fields()) )

@info_page.route('/get_strategyinapp')
def get_strategyinapp():
    page = get_arg_int(qts_json_page_field)
    rows = get_arg_int(qts_json_rows_field)
    return get_apps_json_by_page(qts_config_db,qts_strategyinapp_table,page - 1,rows)

@info_page.route('/_insert_strategyinapp', methods=[qts_web_get_field, qts_web_post_field])
def _insert_strategyinapp():
    if request.method == qts_web_post_field :
        items = dict()
        append_items_from_form(items,get_strategyinapp_head_fields()[1:])

        print(items)
        if not exist_strategyinapp(qts_config_db,qts_strategyinapps_table,items[qts_id_field]) :
            insert_strategyinapp(qts_config_db,qts_strategyinapps_table,items)
            return build_reponse({'success': 'insert successed!'}, 200)
        else :
            return build_reponse({'success': 'insert failed!'}, 400)
    return build_reponse({'error': 'insert failed!'}, 400)

@info_page.route('/_update_strategyinapp', methods=[qts_web_get_field, qts_web_post_field])
def _update_strategyinapp():
    inserted = get_form(qts_json_inserted,'')
    deleted = get_form(qts_json_deleted,'')
    updated = get_form(qts_json_updated,'')
    current_app.logger.debug('update_strategyinapp: {0} {1} {2}'.format(inserted,deleted,updated))
    if inserted != '' :
        insert_strategyinapps(qts_config_db,qts_strategyinapps_table,inserted)
    if deleted != '' :
        delete_strategyinapps(qts_config_db,qts_strategyinapps_table,deleted)
    if updated != '' :
        update_strategyinapps(qts_config_db,qts_strategyinapps_table,updated)
    return build_reponse({'success': 'update successed!'}, 200)

##########################################################################################################

@info_page.route('/strategyinproduct')
def show_strategyinproduct():
    return render_template('info_strategyinproduct.html', title='strategyinproduct',fields=get_strategyinproduct_head_fields(),texts=get_strategyinproduct_head_texts(),reses=get_resources(),
                           colsize=len(get_strategyinproduct_head_fields()) )

@info_page.route('/get_strategyinproduct')
def get_strategyinproduct():
    page = get_arg_int(qts_json_page_field)
    rows = get_arg_int(qts_json_rows_field)
    return get_apps_json_by_page(qts_config_db,qts_strategyinproduct_table,page - 1,rows)

@info_page.route('/_insert_strategyinproduct', methods=[qts_web_get_field, qts_web_post_field])
def _insert_strategyinproduct():
    if request.method == qts_web_post_field :
        items = dict()
        append_items_from_form(items,get_strategyinproduct_head_fields()[1:])

        print(items)
        if not exist_strategyinproduct(qts_config_db,qts_strategyinproducts_table,items[qts_id_field]) :
            insert_strategyinproduct(qts_config_db,qts_strategyinproducts_table,items)
            return build_reponse({'success': 'insert successed!'}, 200)
        else :
            return build_reponse({'success': 'insert failed!'}, 400)
    return build_reponse({'error': 'insert failed!'}, 400)

@info_page.route('/_update_strategyinproduct', methods=[qts_web_get_field, qts_web_post_field])
def _update_strategyinproduct():
    inserted = get_form(qts_json_inserted,'')
    deleted = get_form(qts_json_deleted,'')
    updated = get_form(qts_json_updated,'')
    current_app.logger.debug('update_strategyinproduct: {0} {1} {2}'.format(inserted,deleted,updated))
    if inserted != '' :
        insert_strategyinproducts(qts_config_db,qts_strategyinproducts_table,inserted)
    if deleted != '' :
        delete_strategyinproducts(qts_config_db,qts_strategyinproducts_table,deleted)
    if updated != '' :
        update_strategyinproducts(qts_config_db,qts_strategyinproducts_table,updated)
    return build_reponse({'success': 'update successed!'}, 200)


##########################################################################################################

@info_page.route('/admin')
def show_admin():
    #machine_types = get_machine_type(build_path(info_page.root_path,'static/data/qts_machine_type.json'))
    return render_template('info_admin.html', title='admin',fields=get_admin_head_fields(),
                           texts=get_admin_head_texts(),reses=get_resources(),colsize=len(get_admin_head_fields()) )

@info_page.route('/get_admin')
def get_admin():
    page = get_arg_int(qts_json_page_field)
    rows = get_arg_int(qts_json_rows_field)
    return get_admins_json_by_page(qts_config_db,qts_admins_table,page - 1,rows)

@info_page.route('/_insert_admin', methods=[qts_web_get_field, qts_web_post_field])
def _insert_admin():
    if request.method == qts_web_post_field :
        items = dict()
        append_items_from_form(items,get_admin_head_fields()[1:])
        print(items)
        if not exist_admin(qts_config_db,qts_admins_table,items[qts_id_field]) :
            insert_admin(qts_config_db,qts_admins_table,items)
            return build_reponse({'success': 'insert successed!'}, 200)
        else :
            return build_reponse({'success': 'insert failed!'}, 400)
    return build_reponse({'error': 'insert failed!'}, 400)

@info_page.route('/_update_admin', methods=[qts_web_get_field, qts_web_post_field])
def _update_admin():
    inserted = get_form(qts_json_inserted,'')
    deleted = get_form(qts_json_deleted,'')
    updated = get_form(qts_json_updated,'')
    current_app.logger.debug('update_admin: {0} {1} {2}'.format(inserted,deleted,updated))
    if inserted != '' :
        insert_admins(qts_config_db,qts_admins_table,inserted)
    if deleted != '' :
        delete_admins(qts_config_db,qts_admins_table,deleted)
    if updated != '' :
        update_admins(qts_config_db,qts_admins_table,updated)
    return build_reponse({'success': 'update successed!'}, 200)


##########################################################################################################

@info_page.route('/position')
def show_position():
    #machine_types = get_machine_type(build_path(info_page.root_path,'static/data/qts_machine_type.json'))
    return render_template('info_position.html', title='position',fields=get_position_head_fields(),
                           texts=get_position_head_texts(),reses=get_resources(),colsize=len(get_position_head_fields()) )

@info_page.route('/get_position')
def get_position():
    page = get_arg_int(qts_json_page_field)
    rows = get_arg_int(qts_json_rows_field)
    return get_positions_json_by_page(qts_config_db,qts_positions_table,page - 1,rows)

@info_page.route('/_insert_position', methods=[qts_web_get_field, qts_web_post_field])
def _insert_position():
    if request.method == qts_web_post_field :
        items = dict()
        append_items_from_form(items,get_position_head_fields()[1:])
        print(items)
        if not exist_position(qts_config_db,qts_positions_table,items[qts_id_field]) :
            insert_position(qts_config_db,qts_positions_table,items)
            return build_reponse({'success': 'insert successed!'}, 200)
        else :
            return build_reponse({'success': 'insert failed!'}, 400)
    return build_reponse({'error': 'insert failed!'}, 400)

@info_page.route('/_update_position', methods=[qts_web_get_field, qts_web_post_field])
def _update_position():
    inserted = get_form(qts_json_inserted,'')
    deleted = get_form(qts_json_deleted,'')
    updated = get_form(qts_json_updated,'')
    current_app.logger.debug('update_position: {0} {1} {2}'.format(inserted,deleted,updated))
    if inserted != '' :
        insert_positions(qts_loader_db,qts_positions_table,inserted)
    if deleted != '' :
        delete_positions(qts_loader_db,qts_positions_table,deleted)
    if updated != '' :
        update_positions(qts_loader_db,qts_positions_table,updated)
    return build_reponse({'success': 'update successed!'}, 200)

##########################################################################################################

@info_page.route('/trade')
def show_trade():
    #machine_types = get_machine_type(build_path(info_page.root_path,'static/data/qts_machine_type.json'))
    return render_template('info_trade.html', title='trade',fields=get_trade_head_fields(),
                           texts=get_trade_head_texts(),reses=get_resources(),colsize=len(get_trade_head_fields()) )

@info_page.route('/get_trade')
def get_trade():
    page = get_arg_int(qts_json_page_field)
    rows = get_arg_int(qts_json_rows_field)
    return get_trades_json_by_page(qts_config_db,qts_trades_table,page - 1,rows)

@info_page.route('/_insert_trade', methods=[qts_web_get_field, qts_web_post_field])
def _insert_trade():
    if request.method == qts_web_post_field :
        items = dict()
        append_items_from_form(items,get_trade_head_fields()[1:])
        print(items)
        if not exist_trade(qts_config_db,qts_trades_table,items[qts_id_field]) :
            insert_trade(qts_config_db,qts_trades_table,items)
            return build_reponse({'success': 'insert successed!'}, 200)
        else :
            return build_reponse({'success': 'insert failed!'}, 400)
    return build_reponse({'error': 'insert failed!'}, 400)

@info_page.route('/_update_trade', methods=[qts_web_get_field, qts_web_post_field])
def _update_trade():
    inserted = get_form(qts_json_inserted,'')
    deleted = get_form(qts_json_deleted,'')
    updated = get_form(qts_json_updated,'')
    current_app.logger.debug('update_trade: {0} {1} {2}'.format(inserted,deleted,updated))
    if inserted != '' :
        insert_trades(qts_loader_db,qts_trades_table,inserted)
    if deleted != '' :
        delete_trades(qts_loader_db,qts_trades_table,deleted)
    if updated != '' :
        update_trades(qts_loader_db,qts_trades_table,updated)
    return build_reponse({'success': 'update successed!'}, 200)

##########################################################################################################


@info_page.route('/user')
def show_user():
    #machine_types = get_machine_type(build_path(info_page.root_path,'static/data/qts_machine_type.json'))
    return render_template('info_user.html', title='user',fields=get_user_head_fields(),
                           texts=get_user_head_texts(),reses=get_resources(),colsize=len(get_user_head_fields()) )

@info_page.route('/get_user')
def get_user():
    page = get_arg_int(qts_json_page_field)
    rows = get_arg_int(qts_json_rows_field)
    return get_users_json_by_page(qts_config_db,qts_users_table,page - 1,rows)

@info_page.route('/_insert_user', methods=[qts_web_get_field, qts_web_post_field])
def _insert_user():
    if request.method == qts_web_post_field :
        items = dict()
        append_items_from_form(items,get_user_head_fields()[1:])
        print(items)
        if not exist_user(qts_config_db,qts_users_table,items[qts_id_field]) :
            insert_user(qts_config_db,qts_users_table,items)
            return build_reponse({'success': 'insert successed!'}, 200)
        else :
            return build_reponse({'success': 'insert failed!'}, 400)
    return build_reponse({'error': 'insert failed!'}, 400)

@info_page.route('/_update_user', methods=[qts_web_get_field, qts_web_post_field])
def _update_user():
    inserted = get_form(qts_json_inserted,'')
    deleted = get_form(qts_json_deleted,'')
    updated = get_form(qts_json_updated,'')
    current_app.logger.debug('update_user: {0} {1} {2}'.format(inserted,deleted,updated))
    if inserted != '' :
        insert_users(qts_loader_db,qts_users_table,inserted)
    if deleted != '' :
        delete_users(qts_loader_db,qts_users_table,deleted)
    if updated != '' :
        update_users(qts_loader_db,qts_users_table,updated)
    return build_reponse({'success': 'update successed!'}, 200)


##########################################################################################################

@info_page.route('/exchange')
def show_exchange():
    #machine_types = get_machine_type(build_path(info_page.root_path,'static/data/qts_machine_type.json'))
    return render_template('info_exchange.html', title='exchange',fields=get_exchange_head_fields(),
                           texts=get_exchange_head_texts(),reses=get_resources(),colsize=len(get_exchange_head_fields()) )

@info_page.route('/get_exchange')
def get_exchange():
    page = get_arg_int(qts_json_page_field)
    rows = get_arg_int(qts_json_rows_field)
    return get_exchanges_json_by_page(qts_config_db,qts_exchanges_table,page - 1,rows)

@info_page.route('/_insert_exchange', methods=[qts_web_get_field, qts_web_post_field])
def _insert_exchange():
    if request.method == qts_web_post_field :
        items = dict()
        append_items_from_form(items,get_exchange_head_fields()[1:])
        print(items)
        if not exist_exchange(qts_config_db,qts_exchanges_table,items[qts_id_field]) :
            insert_exchange(qts_config_db,qts_exchanges_table,items)
            return build_reponse({'success': 'insert successed!'}, 200)
        else :
            return build_reponse({'success': 'insert failed!'}, 400)
    return build_reponse({'error': 'insert failed!'}, 400)

@info_page.route('/_update_exchange', methods=[qts_web_get_field, qts_web_post_field])
def _update_exchange():
    inserted = get_form(qts_json_inserted,'')
    deleted = get_form(qts_json_deleted,'')
    updated = get_form(qts_json_updated,'')
    current_app.logger.debug('update_exchange: {0} {1} {2}'.format(inserted,deleted,updated))
    if inserted != '' :
        insert_exchanges(qts_loader_db,qts_exchanges_table,inserted)
    if deleted != '' :
        delete_exchanges(qts_loader_db,qts_exchanges_table,deleted)
    if updated != '' :
        update_exchanges(qts_loader_db,qts_exchanges_table,updated)
    return build_reponse({'success': 'update successed!'}, 200)


##########################################################################################################

@info_page.route('/strategy')
def show_strategy():
    #machine_types = get_machine_type(build_path(info_page.root_path,'static/data/qts_machine_type.json'))
    return render_template('info_strategy.html', title='strategy',fields=get_strategy_head_fields(),
                           texts=get_strategy_head_texts(),reses=get_resources(),colsize=len(get_strategy_head_fields()) )

@info_page.route('/get_strategy')
def get_strategy():
    page = get_arg_int(qts_json_page_field)
    rows = get_arg_int(qts_json_rows_field)
    return get_strategys_json_by_page(qts_config_db,qts_strategys_table,page - 1,rows)

@info_page.route('/_insert_strategy', methods=[qts_web_get_field, qts_web_post_field])
def _insert_strategy():
    if request.method == qts_web_post_field :
        items = dict()
        append_items_from_form(items,get_strategy_head_fields()[1:])
        print(items)
        if not exist_strategy(qts_config_db,qts_strategys_table,items[qts_id_field]) :
            insert_strategy(qts_config_db,qts_strategys_table,items)
            return build_reponse({'success': 'insert successed!'}, 200)
        else :
            return build_reponse({'success': 'insert failed!'}, 400)
    return build_reponse({'error': 'insert failed!'}, 400)

@info_page.route('/_update_strategy', methods=[qts_web_get_field, qts_web_post_field])
def _update_strategy():
    inserted = get_form(qts_json_inserted,'')
    deleted = get_form(qts_json_deleted,'')
    updated = get_form(qts_json_updated,'')
    current_app.logger.debug('update_strategy: {0} {1} {2}'.format(inserted,deleted,updated))
    if inserted != '' :
        insert_strategys(qts_loader_db,qts_strategys_table,inserted)
    if deleted != '' :
        delete_strategys(qts_loader_db,qts_strategys_table,deleted)
    if updated != '' :
        update_strategys(qts_loader_db,qts_strategys_table,updated)
    return build_reponse({'success': 'update successed!'}, 200)


##########################################################################################################

@info_page.route('/instrument')
def show_instrument():
    #machine_types = get_machine_type(build_path(info_page.root_path,'static/data/qts_machine_type.json'))
    return render_template('info_instrument.html', title='instrument',fields=get_instrument_head_fields(),
                           texts=get_instrument_head_texts(),reses=get_resources(),colsize=len(get_instrument_head_fields()) )

@info_page.route('/get_instrument')
def get_instrument():
    page = get_arg_int(qts_json_page_field)
    rows = get_arg_int(qts_json_rows_field)
    return get_instruments_json_by_page(qts_config_db,qts_instruments_table,page - 1,rows)

@info_page.route('/_insert_instrument', methods=[qts_web_get_field, qts_web_post_field])
def _insert_instrument():
    if request.method == qts_web_post_field :
        items = dict()
        append_items_from_form(items,get_instrument_head_fields()[1:])
        print(items)
        if not exist_instrument(qts_config_db,qts_instruments_table,items[qts_id_field]) :
            insert_instrument(qts_config_db,qts_instruments_table,items)
            return build_reponse({'success': 'insert successed!'}, 200)
        else :
            return build_reponse({'success': 'insert failed!'}, 400)
    return build_reponse({'error': 'insert failed!'}, 400)

@info_page.route('/_update_instrument', methods=[qts_web_get_field, qts_web_post_field])
def _update_instrument():
    inserted = get_form(qts_json_inserted,'')
    deleted = get_form(qts_json_deleted,'')
    updated = get_form(qts_json_updated,'')
    current_app.logger.debug('update_instrument: {0} {1} {2}'.format(inserted,deleted,updated))
    if inserted != '' :
        insert_instruments(qts_loader_db,qts_instruments_table,inserted)
    if deleted != '' :
        delete_instruments(qts_loader_db,qts_instruments_table,deleted)
    if updated != '' :
        update_instruments(qts_loader_db,qts_instruments_table,updated)
    return build_reponse({'success': 'update successed!'}, 200)


##########################################################################################################

@info_page.route('/parameter')
def show_parameter():
    #machine_types = get_machine_type(build_path(info_page.root_path,'static/data/qts_machine_type.json'))
    return render_template('info_parameter.html', title='parameter',fields=get_parameter_head_fields(),
                           texts=get_parameter_head_texts(),reses=get_resources(),colsize=len(get_parameter_head_fields()) )

@info_page.route('/get_parameter')
def get_parameter():
    page = get_arg_int(qts_json_page_field)
    rows = get_arg_int(qts_json_rows_field)
    return get_parameters_json_by_page(qts_config_db,qts_parameters_table,page - 1,rows)

@info_page.route('/_insert_parameter', methods=[qts_web_get_field, qts_web_post_field])
def _insert_parameter():
    if request.method == qts_web_post_field :
        items = dict()
        append_items_from_form(items,get_parameter_head_fields()[1:])
        print(items)
        if not exist_parameter(qts_config_db,qts_parameters_table,items[qts_id_field]) :
            insert_parameter(qts_config_db,qts_parameters_table,items)
            return build_reponse({'success': 'insert successed!'}, 200)
        else :
            return build_reponse({'success': 'insert failed!'}, 400)
    return build_reponse({'error': 'insert failed!'}, 400)

@info_page.route('/_update_parameter', methods=[qts_web_get_field, qts_web_post_field])
def _update_parameter():
    inserted = get_form(qts_json_inserted,'')
    deleted = get_form(qts_json_deleted,'')
    updated = get_form(qts_json_updated,'')
    current_app.logger.debug('update_parameter: {0} {1} {2}'.format(inserted,deleted,updated))
    if inserted != '' :
        insert_parameters(qts_loader_db,qts_parameters_table,inserted)
    if deleted != '' :
        delete_parameters(qts_loader_db,qts_parameters_table,deleted)
    if updated != '' :
        update_parameters(qts_loader_db,qts_parameters_table,updated)
    return build_reponse({'success': 'update successed!'}, 200)



##########################################################################################################

@info_page.route('/comment')
def show_comment():
    #machine_types = get_machine_type(build_path(info_page.root_path,'static/data/qts_machine_type.json'))
    return render_template('info_comment.html', title='comment',fields=get_comment_head_fields(),
                           texts=get_comment_head_texts(),reses=get_resources(),colsize=len(get_comment_head_fields()) )

@info_page.route('/get_comment')
def get_comment():
    page = get_arg_int(qts_json_page_field)
    rows = get_arg_int(qts_json_rows_field)
    return get_comments_json_by_page(qts_config_db,qts_comments_table,page - 1,rows)

@info_page.route('/_insert_comment', methods=[qts_web_get_field, qts_web_post_field])
def _insert_comment():
    if request.method == qts_web_post_field :
        items = dict()
        append_items_from_form(items,get_comment_head_fields()[1:])
        print(items)
        if not exist_comment(qts_config_db,qts_comments_table,items[qts_id_field]) :
            insert_comment(qts_config_db,qts_comments_table,items)
            return build_reponse({'success': 'insert successed!'}, 200)
        else :
            return build_reponse({'success': 'insert failed!'}, 400)
    return build_reponse({'error': 'insert failed!'}, 400)

@info_page.route('/_update_comment', methods=[qts_web_get_field, qts_web_post_field])
def _update_comment():
    inserted = get_form(qts_json_inserted,'')
    deleted = get_form(qts_json_deleted,'')
    updated = get_form(qts_json_updated,'')
    current_app.logger.debug('update_comment: {0} {1} {2}'.format(inserted,deleted,updated))
    if inserted != '' :
        insert_comments(qts_loader_db,qts_comments_table,inserted)
    if deleted != '' :
        delete_comments(qts_loader_db,qts_comments_table,deleted)
    if updated != '' :
        update_comments(qts_loader_db,qts_comments_table,updated)
    return build_reponse({'success': 'update successed!'}, 200)


##########################################################################################################


@info_page.route('/command')
def show_command():
    #machine_types = get_machine_type(build_path(info_page.root_path,'static/data/qts_machine_type.json'))
    return render_template('info_command.html', title='command',fields=get_command_head_fields(),
                           texts=get_command_head_texts(),reses=get_resources(),colsize=len(get_command_head_fields()) )

@info_page.route('/get_command')
def get_command():
    page = get_arg_int(qts_json_page_field)
    rows = get_arg_int(qts_json_rows_field)
    return get_commands_json_by_page(qts_config_db,qts_commands_table,page - 1,rows)

@info_page.route('/_insert_command', methods=[qts_web_get_field, qts_web_post_field])
def _insert_command():
    if request.method == qts_web_post_field :
        items = dict()
        append_items_from_form(items,get_command_head_fields()[1:])
        print(items)
        if not exist_command(qts_config_db,qts_commands_table,items[qts_id_field]) :
            insert_command(qts_config_db,qts_commands_table,items)
            return build_reponse({'success': 'insert successed!'}, 200)
        else :
            return build_reponse({'success': 'insert failed!'}, 400)
    return build_reponse({'error': 'insert failed!'}, 400)

@info_page.route('/_update_command', methods=[qts_web_get_field, qts_web_post_field])
def _update_command():
    inserted = get_form(qts_json_inserted,'')
    deleted = get_form(qts_json_deleted,'')
    updated = get_form(qts_json_updated,'')
    current_app.logger.debug('update_command: {0} {1} {2}'.format(inserted,deleted,updated))
    if inserted != '' :
        insert_commands(qts_loader_db,qts_commands_table,inserted)
    if deleted != '' :
        delete_commands(qts_loader_db,qts_commands_table,deleted)
    if updated != '' :
        update_commands(qts_loader_db,qts_commands_table,updated)
    return build_reponse({'success': 'update successed!'}, 200)

##########################################################################################################




##########################################################################################################




##########################################################################################################
