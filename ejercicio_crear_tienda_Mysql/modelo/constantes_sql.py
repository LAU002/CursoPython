SQL_INSERCION_PRENDA = "INSERT INTO `tabla_ropa` (`id`, `talla`, `color`, `marca`, `tipo`,`precio`, online, temporada, destino) VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s);"
SQL_SELECT_PRENDAS = "SELECT id, talla, marca, color, tipo, precio, online, temporada, destino FROM tabla_ropa"
SQL_BORRAR_PRENDA = "DELETE FROM `tabla_ropa` WHERE id = %s ;"
SQL_OBTENER_PRENDA_POR_ID = "SELECT * FROM tabla_ropa WHERE id = %s ;"
SQL_GUARDAR_CAMBIOS_PRENDA = "UPDATE tabla_ropa SET talla = %s, color = %s, marca = %s, tipo = %s, precio = %s, online = %s, temporada = %s, destino = %s WHERE id = %s;"
 