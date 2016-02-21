#coding=utf-8
from flask import Flask, current_app, Blueprint, render_template

admin_page = Blueprint('admin',__name__,template_folder='templates',static_folder='static',static_url_path='/admin/static')

@admin_page.route('/',defaults={'page':'admin'})
@admin_page.route('/<page>')
def show(page):
    try:
        return 'hello world! admin page!'
    except :
        abort(404)