#coding=utf-8
import sys
from flask import Flask, current_app, request

############################################################################
def register_entry(app) :
    sys.path.append('./entry')
    from entry import entry_page
    app.register_blueprint(entry_page)

def register_info(app) :
    sys.path.append('./info')
    from info import info_page
    app.register_blueprint(info_page,url_prefix='/info')

def register_monitor(app) :
    sys.path.append('./monitor')
    from monitor import monitor_page
    app.register_blueprint(monitor_page,url_prefix='/monitor')

def register_report(app) :
    sys.path.append('./report')
    from report import report_page
    app.register_blueprint(report_page,url_prefix='/report')

def register_risk(app) :
    sys.path.append('./risk')
    from risk import risk_page
    app.register_blueprint(risk_page,url_prefix='/risk')

def register_all(app) :
    register_entry(app)
    register_info(app)
    register_monitor(app)
    register_report(app)
    register_risk(app)

def print_blueprints(app):
    app.logger.debug(app.blueprints)

############################################################################
def update_config(app,config):
    app.config.from_object(config)
    app.config.from_pyfile('{0}.py'.format(config))

def print_config(app):
    app.logger.debug(app.config)

############################################################################
app = Flask(__name__,static_folder='static',template_folder='templates')
def create_app(config):
    update_config(app,config)
    print_config(app)
    register_all(app)
    print_blueprints(app)
    return app


############################################################################