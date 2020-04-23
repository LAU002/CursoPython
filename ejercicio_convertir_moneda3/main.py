from PyQt5 import QtCore, QtGui, QtWidgets
from ventanas import ventana_principal
import sys

def convertir_de_euro_a_rublo():
    introducido = ui.entrada_euros.text().replace(",",".")
    introducido_float = float(introducido)
    rublo=introducido_float * 0.012
    ui.label_resultado.setText("En rublo: " + "{:.2f}".format(rublo).replace(".",","))
    
def convertir_de_euro_a_yuan():
    introducido = ui.entrada_euros.text().replace(",",".")
    introducido_float = float(introducido)
    yuan=introducido_float * 0.13
    ui.label_resultado.setText("En yuan: " + "{:.2f}".format(yuan).replace(".",","))
    
def convertir_de_euro_a_dolar():
    introducido = ui.entrada_euros.text().replace(",",".")
    introducido_float = float(introducido)
    dolar=introducido_float * 0.92
    ui.label_resultado.setText("En dolar: " + "{:.2f}".format(dolar).replace(".",","))
    
def convertir_de_euro_a_cordoba():
    introducido = ui.entrada_euros.text().replace(",",".")
    introducido_float = float(introducido)
    cordoba=introducido_float * 0.027
    ui.label_resultado.setText("En cordoba: " + "{:.2f}".format(cordoba).replace(".",","))
    
def convertir_de_euro_a_libra():
    introducido = ui.entrada_euros.text().replace(",",".")
    introducido_float = float(introducido)
    libra=introducido_float * 1.13
    ui.label_resultado.setText("En libra: " + "{:.2f}".format(libra).replace(".",","))
    

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = ventana_principal.Ui_MainWindow()
ui.setupUi(MainWindow)

ui.boton_rublo.clicked.connect(convertir_de_euro_a_rublo)
ui.boton_yuan.clicked.connect(convertir_de_euro_a_yuan)
ui.boton_dolar.clicked.connect(convertir_de_euro_a_dolar)
ui.boton_cordoba.clicked.connect(convertir_de_euro_a_cordoba)
ui.boton_libra.clicked.connect(convertir_de_euro_a_libra)


MainWindow.show()
sys.exit(app.exec_())