#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def _include_plat(path) :
    root_path = '../pylib'
    web_path = '{0}/weblib'.format(root_path)
    sys.path.append('{0}/{1}/utility'.format(path,root_path))
    sys.path.append('{0}/{1}/net/control'.format(path,root_path))
    sys.path.append('{0}/{1}/database'.format(path,root_path))
    sys.path.append('{0}/{1}/common'.format(path,web_path))
    sys.path.append('{0}/{1}/config'.format(path,web_path))
    sys.path.append('{0}/{1}/monitor'.format(path,web_path))
    sys.path.append('{0}/{1}/control'.format(path,web_path))
