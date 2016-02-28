#coding=utf-8
import os
import sys
import string
import platform
import traceback 
from ctypes import * 

onucafile=''
if sys.platform == 'win32' :
	onucafile = 'QGOnuca_dlc.dll'
else:
	onucafile = 'libQGOnuca_dlc.so'
	
#////////////////////////////////////////////////////////////////////
QtsOnuca = cdll.LoadLibrary(onucafile)

def RunPlat(arg) :
        result=False
	try:
		QtsOnuca.OnucaEntry.restype = c_int
		QtsOnuca.OnucaEntry.argtype = [c_char_p,c_int]
		carg = c_char_p()
		carg.value = arg
		result = QtsOnuca.OnucaEntry(carg,len(carg.value))
	except Exception,e:
		traceback.print_exc()
	return result
