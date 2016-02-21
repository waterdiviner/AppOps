from PyQt5 import QtWidgets
from qtsreceiversqtbus import *

import sys
sys.path.append('../../utility')
from qtsdelegate import delegate
from qtssingleton import singleton

@singleton
class QtsNetTopology(QtWidgets.QWidget):
    def __init__(self):
        super(QtsNetTopology, self).__init__()
