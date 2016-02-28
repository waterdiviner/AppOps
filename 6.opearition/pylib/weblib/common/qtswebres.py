#coding=utf-8
from flask import Flask, current_app, g, jsonify, make_response
from qtswebutility import *

qts_res_texts={'operator':get_text('operator'),
               'display':get_text('display'),
               'submit':get_text('submit'),
               'clear':get_text('clear'),
               'append':get_text('append'),
               'remove':get_text('remove'),
               'accept':get_text('accept'),
               'reject':get_text('reject'),
               'getchanges':get_text('getchanges'),
               'ssrecord':get_text('ssrecord'),
               'gwrecord':get_text('gwrecord'),
               'ssaccount':get_text('ssaccount'),
               'gwaccount':get_text('gwaccount'),
               'ssposition':get_text('ssposition'),
               'gwposition':get_text('gwposition'),
               'secuinfos':get_text('secuinfos'),
               'secuinfod':get_text('secuinfod'),

}

def get_resources() :
    return qts_res_texts
