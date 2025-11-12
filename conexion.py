import os

from PyQt6 import QtSql, QtWidgets

from globals import mboxStyleSheet


class Conexion:

    def db_conexion(self = None):
        ruta_db = './data/bbdd.sqlite'

        if not os.path.isfile(ruta_db):
            QtWidgets.QMessageBox.critical(None, 'Error', 'El archivo de la base de datos no existe.',
                                           QtWidgets.QMessageBox.StandardButton.Cancel)
            return False
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName(ruta_db)

        if db.open():
            query = QtSql.QSqlQuery()
            query.exec("SELECT name FROM sqlite_master WHERE type='table';")

            if not query.next():  # Si no hay tablas
                QtWidgets.QMessageBox.critical(None, 'Error', 'Base de datos vacía o no válida.',
                                               QtWidgets.QMessageBox.StandardButton.Cancel)
                return False
            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle("Information")
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setText('Conexión Base de Datos realizada')
                mbox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setStyleSheet(mboxStyleSheet)
                mbox.exec()
                return True
        else:
            QtWidgets.QMessageBox.critical(None, 'Error', 'No se pudo abrir la base de datos.',
                                           QtWidgets.QMessageBox.StandardButton.Cancel)
            return False

    def listProv(self=None):
        listProv = []
        query = QtSql.QSqlQuery()
        query.exec("SELECT * FROM provincias;")
        if query.exec():
            while query.next():
                listProv.append(query.value(1))
        return listProv

    @staticmethod
    def listMuniProv( provincia):
        try:
            listMunicipios = []
            query = QtSql.QSqlQuery()
            query.prepare("SELECT * FROM municipios where idprov = ( select idprov from provincias where provincia = :provincia )")
            query.bindValue(":provincia", provincia)
            if query.exec():
                while query.next():
                    listMunicipios.append(query.value(1))
            return listMunicipios
        except Exception as e:
            print("error en listMunicipios", e)

    @staticmethod
    def listCustomers(var):
        listCustomers = []
        query = QtSql.QSqlQuery()
        if var:
            query.prepare("SELECT * FROM customers where historical = :true order by surname;")
            query.bindValue(":true", "True")
        else:
            query.prepare("SELECT * FROM customers order by surname;")
        if query.exec():
            while query.next():
                row = [query.value(i) for i in range(query.record().count())]
                listCustomers.append(row)
        return listCustomers

    @staticmethod
    def dataOneCustomer(dato):
        try:
            list = []
            query = QtSql.QSqlQuery()
            query.prepare("select * from customers where mobile = :dato")
            query.bindValue(":dato", dato)
            if query.exec():
                while query.next():
                    for i in range(query.record().count()):
                        list.append(query.value(i))
            if len(list) == 0:
                query = QtSql.QSqlQuery()
                query.prepare("select * from customers where dni_nie = :dato")
                query.bindValue(":dato", dato)
                if query.exec():
                    while query.next():
                        for i in range(query.record().count()):
                            list.append(query.value(i))


            return list
        except Exception as e:
            print("error en dataOneCustomer", e)

    @staticmethod
    def delCli(dni):
        try:
            query = QtSql.QSqlQuery()
            query.prepare("UPDATE customers set historical = :false WHERE dni_nie = :dni")
            query.bindValue(":dni", dni)
            query.bindValue(":false", "False")
            if query.exec():
                return True
            else:
                return False
        except Exception as e:
            print("error en delCli", e)



    @staticmethod
    def addCli(newcli):
        try:
            query = QtSql.QSqlQuery()
            query.prepare("INSERT INTO customers ( dni_nie, adddata, surname, name, mail, mobile, address, province, "
                          " city, invoicetype, historical ) VALUES (:dnicli, :adddata, :surname, :name, :mail, :mobile, :address, "
                          " :province, :city, :invoicetype, :historical)")
            query.bindValue(":dnicli", str(newcli[0]))
            query.bindValue(":adddata", str(newcli[1]))
            query.bindValue(":surname", str(newcli[2]))
            query.bindValue(":name", str(newcli[3]))
            query.bindValue(":mail", str(newcli[4]))
            query.bindValue(":mobile", str(newcli[5]))
            query.bindValue(":address", str(newcli[6]))
            query.bindValue(":province", str(newcli[7]))
            query.bindValue(":city", str(newcli[8]))
            query.bindValue(":invoicetype", str(newcli[9]))
            query.bindValue(":historical", str(True))
            if query.exec():
                return True
            else:
                return False
        except Exception as error:
            print("error addCli", error)

    @staticmethod
    def modifCli(dni, modifCli):
        try:
            query = QtSql.QSqlQuery()
            query.prepare("update customers set adddata = :adddata, surname = :surname, name = :name, mail = :mail, "
                          "mobile = :mobile, address = :address, province = :province, city = :city, invoicetype = :invoicetype, historical = :historical "
                          "where dni_nie = :dni")
            query.bindValue(":dni", dni)
            query.bindValue(":adddata", str(modifCli[0]))
            query.bindValue(":surname", str(modifCli[1]))
            query.bindValue(":name", str(modifCli[2]))
            query.bindValue(":mail", str(modifCli[3]))
            query.bindValue(":mobile", str(modifCli[4]))
            query.bindValue(":address", str(modifCli[5]))
            query.bindValue(":province", str(modifCli[6]))
            query.bindValue(":city", str(modifCli[7]))
            query.bindValue(":invoicetype", str(modifCli[9]))
            query.bindValue(":historical", str(modifCli[8]))
            if query.exec():
                return True
            else:
                return False

        except Exception as e:
            print("error modifyCli", e)