import events
from customers import *
from events import *
from window import *
from venCalendar import *
import globals
import sys

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        globals.ui = Ui_MainWindow()
        globals.ui.setupUi(self)

        # Functions in menu bar
        globals.ui.actionExit.triggered.connect(Events.messageExit)

        # Funciones en lineEdit
        globals.ui.txtDnicli.editingFinished.connect(Customers.checkDni)

        # Funciones de botones
        globals.ui.btnFechaaltacli.clicked.connect(Events.openCalendar)
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.showMaximized()
    sys.exit(app.exec())