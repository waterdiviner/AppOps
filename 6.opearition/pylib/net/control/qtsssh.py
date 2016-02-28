#coding=utf-8
import sys
import os
import traceback
import pxssh

class QtsSSHClient(object):
    def __init__(self,_host,_user,_psw,_port=None) :
        self.host = _host
        self.user = _user
        self.psw = _psw
        self.port = _port
        self.ssh = pxssh.pxssh()
        self.login = False

    def __del__(self):
        self.close()

    @property
    def sshclient(self):
        return self.ssh

    @property
    def islogin(self):
        return self.login

    def connect(self):
        try :
            if not self.login :
                if self.port == None :
                    self.ssh.login(self.host,self.user,self.psw)
                else :
                    self.ssh.login(self.host,self.user,self.psw,port=self.port)
                self.login = True
        except Exception,e:
            traceback.print_exc()
        return self.login

    def command(self,cmd):
        result = False
        if self.login :
            try :
                self.ssh.sendline(cmd)
                result = self.ssh.prompt()
            except Exception,e:
                traceback.print_exc()
        else :
            result = False
        return result

    def tostring(self):
        if self.login :
            return self.ssh.before
        else :
            return ''

    def close(self):
        if self.login :
            try :
                self.login = False
                self.ssh.logout()
            except Exception,e:
                traceback.print_exc()