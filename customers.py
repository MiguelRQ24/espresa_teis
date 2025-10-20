import re

from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import QMessageBox

import globals
from conexion import Conexion
from events import Events


class Customers:

    @staticmethod
    def checkDni():
        print("checkDni")
        try:
            globals.ui.txtDnicli.editingFinished.disconnect(Customers.checkDni)
            dni = globals.ui.txtDnicli.text()
            dni = str(dni).upper()
            globals.ui.txtDnicli.setText(dni)
            tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
            dig_ext = "XYZ"
            reemp_dig_ext = {'X': '0', 'Y': '1', 'Z': '2'}
            numeros = "1234567890"
            if len(dni) == 9:
                dig_control = dni[8]
                dni = dni[:8]
                if dni[0] in dig_ext:
                    dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])
                if len(dni) == len([n for n in dni if n in numeros]) and tabla[int(dni) % 23] == dig_control:
                    globals.ui.txtDnicli.setStyleSheet('background-color: rgb(255, 255, 220);')
                else:
                    globals.ui.txtDnicli.setStyleSheet('background-color:#FFC0CB;')
                    globals.ui.txtDnicli.setText(None)
                    globals.ui.txtDnicli.setFocus()
            else:
                globals.ui.txtDnicli.setStyleSheet('background-color:#FFC0CB;')
                globals.ui.txtDnicli.setText(None)
                globals.ui.txtDnicli.setFocus()

        except Exception as error:
            print("error en validar dni ", error)
        finally:
            globals.ui.txtDnicli.editingFinished.connect(Customers.checkDni)

    @staticmethod
    def capitalizar(texto, widget):
        try:
            texto = texto.title()
            widget.setText(texto)
        except Exception as error:
            print("error en capitalizar texto ", error)

    @staticmethod
    def checkEmail(email):
        patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if re.match(patron, email):
            globals.ui.txtEmailcli.setStyleSheet('background-color: rgb(255, 255, 220);')
        else:
            globals.ui.txtEmailcli.setStyleSheet('background-color: #FFC0CB;')
            globals.ui.txtEmailcli.setText(None)
            globals.ui.txtEmailcli.setPlaceholderText("Invalid Email")


    @staticmethod
    def checkMobile(numero):
        patron = r'^[67]\d{8}$'
        if re.match(patron, numero):
            globals.ui.txtMobilecli.setStyleSheet('background-color: rgb(255, 255, 220);')
        else:
            globals.ui.txtMobilecli.setStyleSheet('background-color: #FFC0CB;')
            globals.ui.txtMobilecli.setText(None)
            globals.ui.txtMobilecli.setPlaceholderText("Invalid Number")


    @staticmethod
    def loadTablecli(var):
        try:
            listTabCustomers = Conexion.listCustomers(var)
            index = 0
            for record in listTabCustomers:
                globals.ui.tableCustomerList.setRowCount(index + 1)
                globals.ui.tableCustomerList.setItem(index, 0, QtWidgets.QTableWidgetItem(str(record[2])))
                globals.ui.tableCustomerList.setItem(index, 1, QtWidgets.QTableWidgetItem(str(record[3])))
                globals.ui.tableCustomerList.setItem(index, 2, QtWidgets.QTableWidgetItem(str(" " + record[5]) + " "))
                globals.ui.tableCustomerList.setItem(index, 3, QtWidgets.QTableWidgetItem(str(record[7])))
                globals.ui.tableCustomerList.setItem(index, 4, QtWidgets.QTableWidgetItem(str(record[8])))
                globals.ui.tableCustomerList.setItem(index, 5, QtWidgets.QTableWidgetItem(str(record[9])))
                globals.ui.tableCustomerList.item(index, 0).setTextAlignment(
                    QtCore.Qt.AlignmentFlag.AlignLeft.AlignVCenter)
                globals.ui.tableCustomerList.item(index, 1).setTextAlignment(
                    QtCore.Qt.AlignmentFlag.AlignLeft.AlignVCenter)
                globals.ui.tableCustomerList.item(index, 2).setTextAlignment(
                    QtCore.Qt.AlignmentFlag.AlignCenter.AlignCenter)
                globals.ui.tableCustomerList.item(index, 3).setTextAlignment(
                    QtCore.Qt.AlignmentFlag.AlignCenter.AlignCenter)
                globals.ui.tableCustomerList.item(index, 4).setTextAlignment(
                    QtCore.Qt.AlignmentFlag.AlignCenter.AlignCenter)
                globals.ui.tableCustomerList.item(index, 5).setTextAlignment(
                    QtCore.Qt.AlignmentFlag.AlignCenter.AlignCenter)
                index += 1
        except Exception as error:
            print("error en loadTablecli ", error)

    @staticmethod
    def selectCustomer():
        try:
            row = globals.ui.tableCustomerList.selectedItems()
            data = [dato.text() for dato in row]
            dataComplet = Conexion.dataOneCustomer(data[2].strip())
            boxes = [globals.ui.txtDnicli, globals.ui.txtAltacli, globals.ui.txtApelcli,
                     globals.ui.txtNombrecli, globals.ui.txtEmailcli, globals.ui.txtMobilecli, globals.ui.txtAddresscli]
            for i, box in enumerate(boxes):
                box.setText(str(dataComplet[i]))
            globals.ui.cmbProvincecli.setCurrentText(dataComplet[7])
            globals.ui.cmbCitycli.setCurrentText(dataComplet[8])
            if str(dataComplet[9]) == "paper":
                globals.ui.rbtFacpapel.setChecked(True)
            else:
                globals.ui.rbtFace.setChecked(True)

        except Exception as e:
            print("error en selectCustomer ", e)

    @staticmethod
    def delCustomer():
        try:
            mbox = QtWidgets.QMessageBox()
            mbox.setWindowTitle("Warning")
            mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            mbox.setText("Delete Customer?")
            mbox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
            mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.No)
            if mbox.exec() == QtWidgets.QMessageBox.StandardButton.Yes:
                dni = globals.ui.txtDnicli.text()
                if Conexion.delCli(dni):
                    mbox1 = QtWidgets.QMessageBox()
                    mbox1.setWindowTitle("Information")
                    mbox1.setIcon(QtWidgets.QMessageBox.Icon.Information)
                    mbox1.setText("Delete Customer Exito")
                    mbox1.exec()
                else:
                    mbox1 = QtWidgets.QMessageBox()
                    mbox1.setWindowTitle("Information")
                    mbox1.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                    mbox1.setText("Delete Customer Fail. Contact with administrator or try again later")
                    mbox1.exec()
                Customers.loadTablecli(True)
            else:
                mbox2 = QtWidgets.QMessageBox()
                mbox2.setWindowTitle("Warning")
                mbox2.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox2.setText("Error. Contact with administrator or try again later")
                mbox2.exec()

        except Exception as e:
            print("error en delCustomer ", e)

    @staticmethod
    def historicoCli():
        try:
            if globals.ui.chkHistoriccli.isChecked():
                var = False
            else:
                var = True
            Customers.loadTablecli(var)
        except Exception as e:
            print("error en historicoCli ", e)

    @staticmethod
    def saveCli():
        try:
            newCli = [globals.ui.txtDnicli.text(), globals.ui.txtAltacli.text(), globals.ui.txtApelcli.text(),
                      globals.ui.txtNombrecli.text(), globals.ui.txtEmailcli.text(), globals.ui.txtMobilecli.text(),
                      globals.ui.txtAddresscli.text(), globals.ui.cmbProvincecli.currentText(),
                      globals.ui.cmbCitycli.currentText(),
                      ]
            if globals.ui.rbtFacpapel.isChecked():
                factura = "paper"
            else:
                factura = "electronic"
            newCli.append(factura)
            if Conexion.addCli(newCli) and len(newCli) > 0:
                print("entra aqui1")
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle("Information")
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setText("Client Added")
                mbox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Yes)
                mbox.exec()
            else:
                print("entra aqui 2")
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle("Warning")
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox.setText("Error. Client not added, contact with administrator or try again later")
                mbox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Yes)
                mbox.exec()
            print("llega aqui")
            Customers.loadTablecli(True)
        except Exception as e:
            print("error en saveCli ", e)


    def cleanCli(self):
        try:
            cli = [globals.ui.txtDnicli, globals.ui.txtAltacli, globals.ui.txtApelcli,
                   globals.ui.txtNombrecli, globals.ui.txtEmailcli, globals.ui.txtMobilecli,
                   globals.ui.txtAddresscli,
                   ]
            for i, dato in enumerate(cli):
                cli[i] = dato.setText("")
            Events.loadProvincia(self)
            globals.ui.cmbCitycli.clear()
            globals.ui.txtEmailcli.setStyleSheet('background-color: rgb(255, 255, 255);')
            globals.ui.txtMobilecli.setStyleSheet('background-color: rgb(255, 255, 255);')
            globals.ui.txtDnicli.setStyleSheet('background-color: rgb(255, 255, 255);')



        except Exception as e:
            print("error en cleanCli ", e)
