import sys
import time

from PyQt6 import QtWidgets, QtCore, QtGui
import globals


class Events:
    @staticmethod
    def messageExit(self=None):
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