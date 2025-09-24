from venAux import *

import events
from customers import *
from events import *
from window import *
import globals
import sys

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        globals.ui = Ui_MainWindow()
        globals.ui.setupUi(self)

        # Instance
        globals.vencal = Calendar()

        # Functions in menu bar
        globals.ui.actionExit.triggered.connect(Events.messageExit)

        # Funciones en lineEdit
        globals.ui.txtDnicli.editingFinished.connect(Customers.checkDni)
        globals.ui.txtNombrecli.editingFinished.connect(lambda: Customers.capitalizar(globals.ui.txtNombrecli.text()))
        globals.ui.txtApelcli.editingFinished.connect(lambda: Customers.capitalizar(globals.ui.txtApelcli.text()))

        # Funciones de botones
        globals.ui.btnFechaaltacli.clicked.connect(Events.openCalendar)
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.showMaximized()
    sys.exit(app.exec())