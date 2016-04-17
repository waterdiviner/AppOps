#coding=utf-8
from qtsenvir import *

class QtsMath(object) :
	@staticmethod
	def IsDigit(value) :
		return all(c in "0123456789" for c in str(value))