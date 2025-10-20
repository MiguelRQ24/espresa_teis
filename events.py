import sys
import time

from PyQt6 import QtWidgets, QtCore, QtGui

import conexion
import globals


class Events:
    @staticmethod
    def messageExit():
        try:
            mbox = QtWidgets.QMessageBox()
            mbox.setIcon(QtWidgets.QMessageBox.Icon.Question)
            mbox.setWindowIcon(QtGui.QIcon("./img/logo.png"))
            mbox.setWindowTitle("Exit Message")
            mbox.setText("Are you sure you want to exit?")
            mbox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
            mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.No)
            if mbox.exec() == QtWidgets.QMessageBox.StandardButton.Yes:
                sys.exit()
            else:
                mbox.hide()
        except Exception as e:
            print("error salida", e)

    @staticmethod
    def messageAbout():
        try:
            globals.venAbout.show()
        except Exception as e:
            print("error en mostrar version", e)

    @staticmethod
    def closeAbout():
        try:
            globals.venAbout.hide()
        except Exception as e:
            print("error en cerrar version", e)

    def openCalendar(self):
        try:
            globals.vencal.show()
        except Exception as e:
            print("error en claendario", e)

    def loadData(qDate):
        try:
            data = ('{:02d}/{:02d}/{:4d}'.format(qDate.day(), qDate.month(), qDate.year()))
            if globals.ui.panMain.currentIndex() == 0:
                globals.ui.txtAltacli.setText(data)
            time.sleep(0.1)
            globals.vencal.hide()

        except Exception as e:
            print("error en cargar Data", e)


    def loadProvincia(self):
        try:
            globals.ui.cmbProvincecli.clear()
            list = conexion.Conexion.listProv(self)

            globals.ui.cmbProvincecli.addItems(list)
        except Exception as e:
            print("error en cargar Provincia:", e)

    def loadMunicli(self):
        try:
            provincia = globals.ui.cmbProvincecli.currentText()
            list = conexion.Conexion.listMuniProv(provincia)
            globals.ui.cmbCitycli.clear()
            globals.ui.cmbCitycli.addItems(list)
        except Exception as e:
            print("error en cargar Municipio:", e)

    def resizeTabCustomer(self):
        try:
            header = globals.ui.tableCustomerList.horizontalHeader()
            for i in range(header.count()):
                if i == 2:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
                else:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.Stretch)
                header_items = globals.ui.tableCustomerList.horizontalHeaderItem(i)
                font = header_items.font()
                font.setBold(True)
                header_items.setFont(font)
        except Exception as e:
            print("error en cargar Tab Customer:", e)