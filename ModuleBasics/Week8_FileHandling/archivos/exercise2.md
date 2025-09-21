| Método        | Descripción                                                                 |
|-------------- |-----------------------------------------------------------------------------|
| `read()`      | Lee y retorna todo el contenido del archivo como una cadena de texto.       |
| `readlines()` | Lee todo el contenido del archivo y retorna una lista donde cada elemento es una línea del archivo. |
| `write()`     | Escribe una cadena de texto en el archivo. Si el archivo no existe, lo crea. |
| `writelines()`| Escribe una lista de cadenas de texto en el archivo. Cada cadena se escribe como una línea separada. |
| `flush()`     | Fuerza a que se escriban los datos en el archivo desde el buffer.           |
| `seek()`      | Cambia la posición actual del puntero en el archivo a una posición específica. |
| `tell()`      | Retorna la posición actual del puntero en el archivo.                       |
| `truncate()`  | Redimensiona el archivo a un tamaño específico, eliminando el contenido que exceda ese tamaño. |
| `fileno()`    | Retorna el descriptor de archivo entero asociado con el archivo.            |
| `isatty()`    | Retorna True si el archivo es un terminal interactivo, de lo contrario, retorna False. |
| `readable()`  | Retorna True si el archivo se puede leer, de lo contrario, retorna False.   |
| `writable()`  | Retorna True si el archivo se puede escribir, de lo contrario, retorna False.|
| `seekable()`  | Retorna True si el archivo permite cambiar la posición de lectura/escritura, de lo contrario, retorna False. |
| `readline()`  | Lee y retorna una sola línea del archivo como una cadena de texto (string).          |
| `detach()`    | Separa el buffer del archivo del objeto de archivo, retornando el buffer.   |
| `close()`     | Cierra el stream entre el archivo en memoria y el archivo en disco, liberando recursos. |
