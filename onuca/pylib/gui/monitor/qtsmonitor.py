import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QDockWidget,QMainWindow)

class MainWindow(QMainWindow):
    def __init__(self,_qtsplugins):
        super(MainWindow, self).__init__()
        self.qtsplugins = _qtsplugins
        self.add_pages()

    def add_pages(self):
        first = True
        dock = None
        pages = self.qtsplugins.Pages()
        if pages != None :
            for page in pages :
                if first :
                    dock = self.add_view(page[0],page[1],dock,True)
                    first = False
                else :
                    dock = self.add_view(page[0],page[1],dock,False)

    def add_view(self, name, widget,parent,first):
        dock = QDockWidget(name, self)
        dock.setAllowedAreas(Qt.AllDockWidgetAreas)
        dock.setWidget(widget)
        widget.show()
        if first :
            self.addDockWidget(Qt.TopDockWidgetArea, dock)
        else :
            self.tabifyDockWidget(parent,dock)
        return dock

def WinMain(qtsapp) :
    app = QApplication(sys.argv)
    mainWindow = MainWindow(qtsapp)
    mainWindow.show()
    qtsapp.start()
    sys.exit(app.exec_())
    qtsapp.stop()