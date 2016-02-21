#coding=utf-8
import sys
import os
import traceback
import pexpect

class QtsConsole(object) :
    @staticmethod
    def scp(host,port,user,pwd,source,target,folder):
        cmd = ''
        if folder :
            if port != None :
                cmd = 'scp -r {0} {1}@{2}:{3} -P={4}'.format(source,user,host,target,port)
            else :
                cmd = 'scp -r {0} {1}@{2}:{3}'.format(source,user,host,target)
        else :
            if port != None :
                cmd = 'scp {0} {1}@{2}:{3} -P={4}'.format(source,user,host,target,port)
            else :
                cmd = 'scp {0} {1}@{2}:{3}'.format(source,user,host,target)
        try :
            remote = pexpect.spawn(cmd)
            remote.expect('password:')
            remote.sendline(pwd)
            remote.wait()
        except pexpect.EOF :
            return False
        except pexpect.TIMEOUT :
            return False
        return True

