import mysql.connector
from modelo import constantes_sql, clases
from modelo.clases import Prenda




def conectar():
    conexion = mysql.connector.connect(
        host = "localhost",
        user= "root",
        database = "bd_tienda_ropa"
        )
    return conexion

def registro_prenda(prenda):
        sql = constantes_sql.SQL_INSERCION_PRENDA
        conexion = conectar()
        cursor = conexion.cursor()
        valores_a_insertar = (prenda.talla, prenda.color, prenda.marca, prenda.tipo, prenda.precio, prenda.online, prenda.temporada, prenda.destino)
        cursor.execute(sql, valores_a_insertar)
        conexion.commit()
        conexion.disconnect()
        
def obtener_prendas():    
    sql = constantes_sql.SQL_SELECT_PRENDAS
    conexion= conectar()
    cursor=conexion.cursor()
    cursor.execute(sql)
    lista_resultado= cursor.fetchall()
    conexion.disconnect()
    return lista_resultado        

def borrar_prenda(id_prenda):
    sql = constantes_sql.SQL_BORRAR_PRENDA
    conexion = conectar()
    cursor = conexion.cursor()
    val = (id_prenda,)
    cursor.execute(sql, val)
    conexion.commit()
    conexion.disconnect()
        
def obtener_prenda_por_id(id):
    sql = constantes_sql.SQL_OBTENER_PRENDA_POR_ID
    conexion = conectar()
    cursor = conexion.cursor()
    val = (id,)
    cursor.execute(sql,val)
    resultado = cursor.fetchone()
    print(resultado)
    conexion.disconnect()
    #meter el resultado en un objeto de la clase prenda
    
    prenda = clases.Prenda()
    prenda.id = resultado[0]
    prenda.talla = resultado[1]
    prenda.color = resultado[2]
    prenda.marca = resultado[3]
    prenda.tipo = resultado[4]
    prenda.precio = resultado[5]
    prenda.online = resultado[6]
    prenda.temporada = resultado[7]
    prenda.destino = resultado[8]
    return prenda
    
def guardar_cambios_prenda(prenda_a_guardar_cambios):
    sql = constantes_sql.SQL_GUARDAR_CAMBIOS_PRENDA
    conexion = conectar()
    cursor = conexion.cursor()
    val = (prenda_a_guardar_cambios.talla, prenda_a_guardar_cambios.color, prenda_a_guardar_cambios.marca, prenda_a_guardar_cambios.tipo, prenda_a_guardar_cambios.precio, prenda_a_guardar_cambios.online,prenda_a_guardar_cambios.temporada,prenda_a_guardar_cambios.destino, prenda_a_guardar_cambios.id)
    cursor.execute(sql,val)
    conexion.commit()
    conexion.disconnect()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        