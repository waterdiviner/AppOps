#coding=utf-8
from flask import Flask, current_app, Blueprint, render_template
from operation import create_app

if __name__ == '__main__' :
    app = create_app('config')
    app.run(use_debugger=app.debug, debug=app.debug,use_reloader=app.debug,host='0.0.0.0')