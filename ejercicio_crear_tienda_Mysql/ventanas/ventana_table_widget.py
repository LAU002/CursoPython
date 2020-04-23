# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_table_widget.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1528, 566)
        MainWindow.setStyleSheet("background-color: rgb(255, 170, 255);\n"
"font: 11pt \"Microsoft YaHei UI\";")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabla_prendas = QtWidgets.QTableWidget(self.centralwidget)
        self.tabla_prendas.setGeometry(QtCore.QRect(50, 140, 1391, 351))
        self.tabla_prendas.setObjectName("tabla_prendas")
        self.tabla_prendas.setColumnCount(11)
        self.tabla_prendas.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_prendas.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_prendas.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_prendas.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_prendas.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_prendas.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_prendas.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_prendas.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_prendas.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_prendas.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_prendas.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_prendas.setHorizontalHeaderItem(10, item)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 60, 411, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tabla_prendas.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tabla_prendas.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "TALLA"))
        item = self.tabla_prendas.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "COLOR"))
        item = self.tabla_prendas.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "MARCA"))
        item = self.tabla_prendas.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "TIPO"))
        item = self.tabla_prendas.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "PRECIO"))
        item = self.tabla_prendas.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "ONLINE"))
        item = self.tabla_prendas.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "TEMPORADA"))
        item = self.tabla_prendas.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "DESTINO"))
        item = self.tabla_prendas.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "BORRAR"))
        item = self.tabla_prendas.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "EDITAR"))
        self.label.setText(_translate("MainWindow", "LISTADO USANDO UN TABLE WIDGET"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
