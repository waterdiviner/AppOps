#coding=utf-8
from flask import Flask, current_app, Blueprint, render_template, request, session, g, redirect, url_for, abort, flash

entry_page = Blueprint('entry',__name__,template_folder='templates',static_folder='static',static_url_path='/entry/static')

@entry_page.route('/',defaults={'page':'entry'})
@entry_page.route('/<page>')
def show(page):
    try:
        if not session.get('logged_in') :
            return render_template('login.html', title='login')
        else :
            if session['logged_in'] :
                return render_template('index.html',title='index')
            else :
                return render_template('login.html', title='login')
    except :
        abort(404)

@entry_page.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'root':
            error = 'Invalid username'
        elif request.form['password'] != '111':
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return render_template('index.html',title='index')
    return render_template('login.html', error=error,title='login')

@entry_page.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('entry.login'))

@entry_page.route('/index')
def index():
    if session['logged_in'] :
        return render_template('index.html',title='index')
    else :
        return render_template('login.html', title='login')