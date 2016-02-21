#coding=utf-8
import os
import sys
import threading
import string
import platform
import csv

sys.path.append('../utility')
from qtsdelegate import delegate
from qtsvar import *
from qtsgproto_pb2 import *
from qtsbiz import *

account_headers = [qts_secuid_field,qts_account_field,qts_totalamount_field,qts_avlamount_field,qts_freezeamount_field,qts_date_field,qts_currency_field,qts_user_field,
qts_sharetag_field,qts_level_field,qts_viraccount_field]