

from conexion import *
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
        globals.venAbout = About()

        # Conexion
        varcli = True #Solo muestra clientes True
        Conexion.db_conexion(self)
        Customers.loadTablecli(varcli)
        Events.resizeTabCustomer(self)

        # Functions in menu bar
        globals.ui.actionExit.triggered.connect(Events.messageExit)
        globals.ui.actionAbout.triggered.connect(Events.messageAbout)


        # Funciones en lineEdit
        globals.ui.txtDnicli.editingFinished.connect(Customers.checkDni)
        globals.ui.txtNombrecli.editingFinished.connect(lambda: Customers.capitalizar(globals.ui.txtNombrecli.text(), globals.ui.txtNombrecli))
        globals.ui.txtApelcli.editingFinished.connect(lambda: Customers.capitalizar(globals.ui.txtApelcli.text(), globals.ui.txtApelcli))
        globals.ui.txtEmailcli.editingFinished.connect(lambda: Customers.checkEmail(globals.ui.txtEmailcli.text()))
        globals.ui.txtMobilecli.editingFinished.connect(lambda: Customers.checkMobile(globals.ui.txtMobilecli.text()))

        # Function of chkHistoriccli
        globals.ui.chkHistoriccli.stateChanged.connect(Customers.historicoCli)

        # Functions comboBox
        Events.loadProvincia(self)
        globals.ui.cmbProvincecli.currentIndexChanged.connect(events.Events.loadMunicli)

        # Funciones de botones
        globals.ui.btnFechaaltacli.clicked.connect(Events.openCalendar)
        globals.ui.btnDelcli.clicked.connect(Customers.delCustomer)
        globals.ui.btnSavecli.clicked.connect(Customers.saveCli)
        globals.ui.btnCleancli.clicked.connect(Customers.cleanCli)
        # globals.ui.btnModycli.clicked.connect(Customers.modyCli)

        # Functions of tables
        globals.ui.tableCustomerList.clicked.connect(Customers.selectCustomer)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.showMaximized()
    sys.exit(app.exec())