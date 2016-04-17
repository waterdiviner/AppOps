#coding=utf-8
import os
import sys
import threading
import string
import platform
import csv

sys.path.append(os.path.join(os.getenv('QTS_BASE_PATH','..'),'pylib/utility'))
from qtsdelegate import delegate
from qtsvar import *
try :
	from qtsgproto_pb2 import *
except :
	print('warning>> python lib no support protocol buffer')
from qtsbizfun import *

account_headers = [qts_secuid_field,qts_account_field,qts_totalamount_field,qts_avlamount_field,qts_freezeamount_field,qts_date_field,qts_currency_field,qts_user_field,
qts_sharetag_field,qts_level_field,qts_viraccount_field]