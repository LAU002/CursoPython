# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_principal.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(255, 0, 255);\n"
"font: 16pt \"MV Boli\";\n"
"font: 12pt \"Curlz MT\";")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 70, 611, 281))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 20pt \"MV Boli\";")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 33))
        self.menubar.setObjectName("menubar")
        self.menuPrendas = QtWidgets.QMenu(self.menubar)
        self.menuPrendas.setObjectName("menuPrendas")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.submenu_insertar_prenda = QtWidgets.QAction(MainWindow)
        self.submenu_insertar_prenda.setObjectName("submenu_insertar_prenda")
        self.submenu_listar_prendas = QtWidgets.QAction(MainWindow)
        self.submenu_listar_prendas.setObjectName("submenu_listar_prendas")
        self.submenu_inicio = QtWidgets.QAction(MainWindow)
        self.submenu_inicio.setObjectName("submenu_inicio")
        self.submenu_list_widget_prendas = QtWidgets.QAction(MainWindow)
        self.submenu_list_widget_prendas.setObjectName("submenu_list_widget_prendas")
        self.submenu_listar_widget_prendas = QtWidgets.QAction(MainWindow)
        self.submenu_listar_widget_prendas.setObjectName("submenu_listar_widget_prendas")
        self.submenu_table_widget_prendas = QtWidgets.QAction(MainWindow)
        self.submenu_table_widget_prendas.setObjectName("submenu_table_widget_prendas")
        self.menuPrendas.addAction(self.submenu_insertar_prenda)
        self.menuPrendas.addAction(self.submenu_listar_prendas)
        self.menuPrendas.addAction(self.submenu_listar_widget_prendas)
        self.menuPrendas.addAction(self.submenu_table_widget_prendas)
        self.menuPrendas.addAction(self.submenu_inicio)
        self.menubar.addAction(self.menuPrendas.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "BIENVENID@ A MI TIENDA DE ROPA"))
        self.menuPrendas.setTitle(_translate("MainWindow", "Prendas"))
        self.submenu_insertar_prenda.setText(_translate("MainWindow", "insertar_prenda"))
        self.submenu_listar_prendas.setText(_translate("MainWindow", "listar_prendas"))
        self.submenu_inicio.setText(_translate("MainWindow", "inicio"))
        self.submenu_list_widget_prendas.setText(_translate("MainWindow", "Listar libros usando list widget"))
        self.submenu_listar_widget_prendas.setText(_translate("MainWindow", "Listar prendas usando List Widget"))
        self.submenu_table_widget_prendas.setText(_translate("MainWindow", "Tabla prendas usando Table Widget"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
