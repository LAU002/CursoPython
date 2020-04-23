from PyQt5 import QtCore, QtGui, QtWidgets
from ventanas import ventana_principal, ventana_listado_ropa, ventana_registrar_prenda,\
 ventana_list_widget, ventana_table_widget, ventana_editar_prenda
 

import sys
from modelo.clases import Prenda
from modelo import operaciones_bd
from PyQt5.Qt import QMessageBox, QTableWidget, QTableWidgetItem, QPushButton,\
    QFileDialog, QPixmap, QLabel
from _functools import partial
from validadores import validadores_prenda
import shutil #facilidades para copiar archivo de digital
from pathlib import Path#facilidades para rutas



lista_resultado=None

#inicio funciones

def registrar_prenda():
    prenda = Prenda()
    
    prenda.talla = ui_registrar_prenda.entrada_talla_prenda.text()
    prenda.talla = prenda.talla.strip()
    
    resultado_validar_talla = validadores_prenda.validar_talla(prenda.talla)
    if resultado_validar_talla == None:
        ui_registrar_prenda.label_error_talla.setText("<font color='blue'>Indica la talla</font")
        return
    else:
        ui_registrar_prenda.label_error_talla.clear()
    

    prenda.color = ui_registrar_prenda.entrada_color_prenda.text()
    prenda.color = prenda.color.strip()
    
    resultado_validar_color = validadores_prenda.validar_color(prenda.color)
    if resultado_validar_color == None:
        ui_registrar_prenda.label_error_color.setText("<font color='blue'>Indica el color</font")
        return
    else:
        ui_registrar_prenda.label_error_color.clear()

    
    prenda.marca = ui_registrar_prenda.entrada_marca_prenda.text()
    prenda.marca = prenda.marca.strip()
    
    resultado_validar_marca = validadores_prenda.validar_marca(prenda.marca)
    if resultado_validar_marca == None:
        ui_registrar_prenda.label_error_marca.setText("<font color='blue'>marca</font")
        return
    else:
        ui_registrar_prenda.label_error_marca.clear()
    
    
    prenda.tipo = ui_registrar_prenda.entrada_tipo_prenda.text()
    prenda.tipo = prenda.tipo.strip()
    
    resultado_validar_tipo = validadores_prenda.validar_tipo(prenda.tipo)
    if resultado_validar_tipo == None:
        ui_registrar_prenda.label_error_tipo.setText("<font color='blue'>Tipo de prenda</font")
        return
    else:
        ui_registrar_prenda.label_error_tipo.clear()

    prenda.precio = ui_registrar_prenda.entrada_precio_prenda.text()
    prenda.precio = prenda.precio.strip()

    #checkBox:
    if ui_registrar_prenda.checkBox_online.isChecked():
        prenda.online = True 
    #combo:
    indice_seleccionado = ui_registrar_prenda.combo_temporada.currentIndex()
    prenda.temporada = ui_registrar_prenda.combo_temporada.itemText(indice_seleccionado)
    #radio_button:
    if ui_registrar_prenda.radio_peninsula.isChecked():
        prenda.destino = "Peninsula"  
    if ui_registrar_prenda.radio_islas.isChecked():
        prenda.destino = "Islas"  
    if ui_registrar_prenda.radio_internacional.isChecked():
        prenda.destino = "Internacional"
    operaciones_bd.registro_prenda(prenda)
    
    #solo muevo la imagen si existe
    #ruta_imagen = "temporal/imagen.jpg"
    #objeto_path = Path(ruta_imagen)
    #existe = objeto_path.is_file()
    #if existe:
        #ruta_Imagenes_destino = "imagen/" + str(id_generado) + ".jpg"
        #shutil.move("temporal/imagen.jpg",ruta_Imagenes_destino)


    QMessageBox.about(MainWindow,"Info","Registro de prenda OK")
    
def seleccionar_imagen():
    archivo = QFileDialog.getOpenFileName(MainWindow)
    print(archivo)
    ruta_archivo = archivo[0]
    shutil.copy(ruta_archivo,"temporal/tienda.jpg")
    pixmap = QPixmap("temporal/tienda.jpg")
    ancho_label_imagen = ui_registrar_prenda.label_imagen.width()
    pixmap_redim = pixmap.scaledToWidth(ancho_label_imagen)
    ui_registrar_prenda.label_imagen.setPixmap(pixmap_redim)


def mostrar_registrar_prenda():
    ui_registrar_prenda.setupUi(MainWindow)
    ui_registrar_prenda.boton_registrar_prenda.clicked.connect(registrar_prenda)
    ui_registrar_prenda.boton_seleccionar_imagen.clicked.connect(seleccionar_imagen)
   
    
    
def mostrar_listado_ropa():
    ui_listar_prendas.setupUi(MainWindow) 
    lista_resultado=operaciones_bd.obtener_prendas() 
    texto = ""
    for p in lista_resultado:
        texto += "id: " + str(p[0]) + "talla : " + str(p[1]) + " color: " + str(p[2]) + " marca: " + str(p[3]) + " tipo: " + str(p[4])+ " precio: " + str(p[5]) + "\n"
    ui_listar_prendas.listado_ropa.setText(texto) 

def mostrar_list_widget(): 
    global lista_resultado
    ui_ventana_list_widget.setupUi(MainWindow)
    lista_resultado = operaciones_bd.obtener_prendas()
    for p in lista_resultado:
        ui_ventana_list_widget.list_widget_prendas.addItem("talla: " + str(p[1]) + "color: " + str(p[2]) + "marca: " + str(p[3]) + "tipo: " + str(p[4])+ "precio: " + str(p[5]) + "\n")
    ui_ventana_list_widget.list_widget_prendas.itemClicked.connect(mostrar_registro)
    

def mostrar_registro():    
    indice_seleccionado = ui_ventana_list_widget.list_widget_prendas.currentRow()
    texto = ""
    texto += "talla: " + str(lista_resultado[indice_seleccionado][1]) + "\n"
    texto += "color: " + str(lista_resultado[indice_seleccionado][2]) + "\n"
    texto += "marca: " + str(lista_resultado[indice_seleccionado][3]) + "\n"
    texto += "tipo: " + str(lista_resultado[indice_seleccionado][4]) + "\n"
    texto += "precio: " + str(lista_resultado[indice_seleccionado][5])
    QMessageBox.about(MainWindow,"Info", texto)
    
def mostrar_table_widget():
    ui_ventana_table_widget.setupUi(MainWindow)
    prendas = operaciones_bd.obtener_prendas()
    fila = 0
    
    for p in prendas:
        ui_ventana_table_widget.tabla_prendas.insertRow(fila)
        columna_indice = 0
        for valor in p:
            if columna_indice == 6:
                if valor == 0:
                    valor = "no"
                else:
                    valor = "si"
            celda = QTableWidgetItem(str(valor))
            ui_ventana_table_widget.tabla_prendas.setItem(fila,columna_indice,celda)
            columna_indice += 1
        boton_borrar = QPushButton("Borrar")
        boton_borrar.clicked.connect(partial(borrar_prenda, p[0]))
        ui_ventana_table_widget.tabla_prendas.setCellWidget(fila,9,boton_borrar)
    
        boton_editar = QPushButton("Editar")
        boton_editar.clicked.connect(partial(editar_prenda, p[0]))
        ui_ventana_table_widget.tabla_prendas.setCellWidget(fila,10,boton_editar)
        fila += 1                                                                                                                        
    
def editar_prenda(id):
    
    QMessageBox.about(MainWindow,"Info", "Vas a editar un registro id:" + str(id))
    ui_ventana_editar_prenda.setupUi(MainWindow)
    #sacar de base de datos toda la informacion a editar
    prenda_a_editar = operaciones_bd.obtener_prenda_por_id(id)

    ui_ventana_editar_prenda.entrada_talla_prenda.setText(str(prenda_a_editar.talla))
    ui_ventana_editar_prenda.label_error_talla.clear()
    ui_ventana_editar_prenda.entrada_color_prenda.setText(prenda_a_editar.color)
    ui_ventana_editar_prenda.label_error_color.clear()
    ui_ventana_editar_prenda.entrada_marca_prenda.setText(prenda_a_editar.marca)
    ui_ventana_editar_prenda.label_error_marca.clear()
    ui_ventana_editar_prenda.entrada_tipo_prenda.setText(prenda_a_editar.tipo)
    ui_ventana_editar_prenda.label_error_tipo.clear()
    ui_ventana_editar_prenda.entrada_precio_prenda.setText(str(prenda_a_editar.precio))

    
    if prenda_a_editar.online:
        ui_ventana_editar_prenda.checkBox_online.setChecked(True)
        
    ui_ventana_editar_prenda.combo_temporada.setCurrentText(prenda_a_editar.temporada)
    
    if prenda_a_editar.destino == "Peninsula":
        ui_ventana_editar_prenda.radio_peninsula.setChecked(True)
        
    if prenda_a_editar.destino == "Islas":
        ui_ventana_editar_prenda.radio_islas.setChecked(True)
        
    if prenda_a_editar.destino == "Internacional":
        ui_ventana_editar_prenda.radio_internacional.setChecked(True)
            
    ui_ventana_editar_prenda.boton_guardar_cambios_prenda.clicked.connect(partial(guardar_cambios_prenda,prenda_a_editar.id))

def guardar_cambios_prenda(id):
    QMessageBox.about(MainWindow,"Info","Guardar cambios sobre el registro de id: " + str(id))
    prenda_guardar_cambios = Prenda()
    prenda_guardar_cambios.talla = ui_ventana_editar_prenda.entrada_talla_prenda.text()
    
        #asi valido el talla:
    resultado_validar_talla = validadores_prenda.validar_talla(prenda_guardar_cambios.talla)
    if resultado_validar_talla == None:
        ui_ventana_editar_prenda.label_error_talla.setText("<font color='blue'>talla incorrecta</font")
        return
    else:
        ui_ventana_editar_prenda.label_error_talla.clear()
        
        
    prenda_guardar_cambios.color = ui_ventana_editar_prenda.entrada_color_prenda.text()
    
        #asi valido el color:
    resultado_validar_color = validadores_prenda.validar_color(prenda_guardar_cambios.color)
    if resultado_validar_color == None:
        ui_ventana_editar_prenda.label_error_color.setText("<font color='blue'>color incorrecto</font")
        return
    else:
        ui_ventana_editar_prenda.label_error_color.clear()
        
        
    prenda_guardar_cambios.marca = ui_ventana_editar_prenda.entrada_marca_prenda.text()
    
        #asi valido el marca:
    resultado_validar_marca = validadores_prenda.validar_marca(prenda_guardar_cambios.marca)
    if resultado_validar_marca == None:
        ui_ventana_editar_prenda.label_error_marca.setText("<font color='blue'>marca incorrecta</font")
        return
    else:
        ui_ventana_editar_prenda.label_error_marca.clear()
        
        
    prenda_guardar_cambios.tipo = ui_ventana_editar_prenda.entrada_tipo_prenda.text()
    
        #asi valido el tipo:
    resultado_validar_tipo = validadores_prenda.validar_tipo(prenda_guardar_cambios.tipo)
    if resultado_validar_tipo == None:
        ui_ventana_editar_prenda.label_error_tipo.setText("<font color='blue'>tipo incorrecto</font")
        return
    else:
        ui_ventana_editar_prenda.label_error_tipo.clear()
        
        
    prenda_guardar_cambios.precio = ui_ventana_editar_prenda.entrada_precio_prenda.text()
    
        
    prenda_guardar_cambios.id = id
    
    #digital
    if ui_ventana_editar_prenda.checkBox_online.isChecked():
        prenda_guardar_cambios.online = True 
    #combo:
    prenda_guardar_cambios.temporada = ui_ventana_editar_prenda.combo_temporada.currentText()
    #radio_button:
    if ui_ventana_editar_prenda.radio_peninsula.isChecked():
        prenda_guardar_cambios.destino = "Peninsula"  
    if ui_ventana_editar_prenda.radio_islas.isChecked():    
        prenda_guardar_cambios.destino = "Islas"  
    if ui_ventana_editar_prenda.radio_internacional.isChecked():
        prenda_guardar_cambios.destino = "Internacional"

    operaciones_bd.guardar_cambios_prenda(prenda_guardar_cambios)
    mostrar_table_widget()#vuelvo a mostrar todos los libros

def borrar_prenda(id):
    res = QMessageBox.question(MainWindow, "Info", "Vas a borrar un registro de id: "+ str(id))
    if res == QMessageBox.Yes:
        operaciones_bd.borrar_prenda(id)
        mostrar_table_widget()
    
    

def mostrar_inicio():          
    ui.submenu_insertar_prenda.triggered.connect(mostrar_registrar_prenda)
    ui.submenu_listar_prendas.triggered.connect(mostrar_listado_ropa)
    ui.submenu_inicio.triggered.connect(mostrar_inicio)
    ui.submenu_listar_widget_prendas.triggered.connect(mostrar_list_widget)
    ui.submenu_table_widget_prendas.triggered.connect(mostrar_table_widget)

    

#fin funciones


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

ui = ventana_principal.Ui_MainWindow()
ui_registrar_prenda = ventana_registrar_prenda.Ui_MainWindow()
ui_listar_prendas = ventana_listado_ropa.Ui_MainWindow()
ui_ventana_list_widget = ventana_list_widget.Ui_MainWindow()
ui_ventana_table_widget = ventana_table_widget.Ui_MainWindow()
ui_ventana_editar_prenda = ventana_editar_prenda.Ui_MainWindow()
    
ui.setupUi(MainWindow)

ui.submenu_insertar_prenda.triggered.connect(mostrar_registrar_prenda)
ui.submenu_listar_prendas.triggered.connect(mostrar_listado_ropa)
ui.submenu_inicio.triggered.connect(mostrar_inicio)
ui.submenu_listar_widget_prendas.triggered.connect(mostrar_list_widget)
ui.submenu_table_widget_prendas.triggered.connect(mostrar_table_widget)

MainWindow.show()
sys.exit(app.exec_())