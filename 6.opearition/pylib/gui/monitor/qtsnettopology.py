from PyQt5 import QtWidgets
from qtsreceiversqtbus import *

import sys
import os
sys.path.append(os.path.join(os.getenv('QTS_BASE_PATH','../..'),'pylib/utility'))
from qtsdelegate import delegate
from qtssingleton import singleton

@singleton
class QtsNetTopology(QtWidgets.QWidget):
    def __init__(self):
        super(QtsNetTopology, self).__init__()
