#coding=utf-8
from qtsenvir import *

class QtsApp(object) :
	def start(self):pass
	def stop(self):pass
	def oncommand(self,cmd):pass
	def run(self):
		self.start()
		command = ''
		while True :
			command = sys.stdin.readline()
			if command[:-1] == 'quit' :
				break
			else :
				self.oncommand(command[:-1])
			time.sleep(1)
		self.stop()