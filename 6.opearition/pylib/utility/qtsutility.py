#coding=utf-8
import os
import sys
import string
import platform
import traceback 
from ctypes import * 
from qtssecurity import *

#######################################################################################################################################
def PrintCharPointer(data,size) :
	data = cast(data,POINTER(c_char))
	for i in range(size) :
		print(data[i])

def SerializeToString(data) :
	try:
		return data.SerializeToString()
	except Exception,e:
		traceback.print_exc()
	return None

def CStringToPyString(idata,size) :
	return create_string_buffer(idata,size)
	
def ParseFromString(idata,size,rdata) :
	if idata == 0 or size == 0 :
		return False
	oresult = True
	try:
		uion_code = CStringToPyString(idata,size)
		rdata.ParseFromString(uion_code)
	except Exception,e:
		oresult = False
		traceback.print_exc()
	return oresult

def VoidPointerToString(idata,size) :
	pystr = ""
	data = cast(idata,POINTER(c_char))
	for i in range(size) :
		pystr += data[i]
	return pystr
	
def ParseFromPointer(idata,size,rdata) :
	if idata == 0 or size == 0 :
		return False
	oresult = True
	try:
		pystr = VoidPointerToString(idata,size)
		rdata.ParseFromString(pystr)
	except Exception,e:
		oresult = False
		traceback.print_exc()
	return oresult


#######################################################################################################################################