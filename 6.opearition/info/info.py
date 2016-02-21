#coding=utf-8
from flask import Flask, current_app, Blueprint, render_template , request, session, g, redirect, url_for, abort, flash, jsonify ,make_response

info_page = Blueprint('info',__name__,template_folder='templates',static_folder='static',static_url_path='/info/static')

import sys
sys.path.append('{0}/../utility'.format(info_page.root_path))
from qtsinc import _include_plat
_include_plat(info_page.root_path)

from qtswebres import *
from qtsdbmachine import *
from qtsdbapp import *
from qtsdbjob import *
from qtsdbright import *
from qtsdbproduct import *
from qtsdbsecuinfo import *
from qtsdbstrategyinapp import *


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

@info_page.route('/secuinfo')
def show_secuinfo():
    machine_ids = get_machines_json_machineid(qts_config_db,qts_machines_table)
    app_types = get_app_type(build_path(info_page.root_path,'static/data/qts_app_type.json'))
    return render_template('info_secuinfo.html', title='secuinfo',fields_s=get_secuinfo_s_head_fields(),texts_s=get_secuinfo_s_head_texts(),fields_d=get_secuinfo_d_head_fields(),texts_d=get_secuinfo_d_head_texts(),reses=get_resources(),
                           colsize_s=len(get_secuinfo_s_head_fields()), colsize_d=len(get_secuinfo_d_head_fields()))

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