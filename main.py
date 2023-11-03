class Tetromino:
    def __init__(self, forma_inicial):
        # Constructor de la clase Tetromino. Recibe una forma inicial.
        self.forma = forma_inicial  # Almacena la forma del tetrominó como una lista de 4x4 caracteres.
        self.rotaciones = [forma_inicial]  # Inicializa una lista que contendrá las diferentes rotaciones del tetrominó.
        self.rotacion_actual = 0  # Inicializa el índice de la rotación actual en 0.

    def rotar(self):
        # Realiza una rotación del tetrominó en sentido de las manecillas del reloj.
        self.rotacion_actual = (self.rotacion_actual + 1) % len(self.rotaciones) #Esta línea de código actualiza el índice
        # de la rotación actual del Tetromino. Aumenta el valor de self.rotacion_actual en 1 y luego usa el operador módulo %
        # para asegurarse de que el índice se mantenga dentro de los límites de la lista self.rotaciones. Esto permite que el Tetromino
        # cambie a la siguiente rotación en sentido horario. Si ya está en la última rotación, vuelve a la primera.

    def mostrar(self):
        # Muestra el estado actual del tetrominó en la consola.
        # Utiliza '@' para representar las partes del tetrominó y '.' para el espacio vacío.
        for fila in self.rotaciones[
            self.rotacion_actual]:  # Esto inicia un bucle for que recorre las filas de la forma actual del
            # Tetromino. self.rotaciones es la lista que contiene las diferentes rotaciones del Tetromino,
            # y self.rotacion_actual es el índice de la rotación actual.
            for celda in fila:  # Este es un bucle anidado que recorre las celdas dentro de cada fila de la forma del
                # Tetromino.
                if celda == '@': # Esta línea verifica si la celda actual contiene un caracter '@', lo que indica que esa parte del Tetromino debe ser representada como un bloque.
                    print('@', end='') #Si la celda es '@', se imprime el caracter '@', y el parámetro end='' asegura que no se agregue un carácter de nueva línea ('\n') después de imprimir el caracter.
                else:
                    print('.', end='') #Si la celda no es '@', se imprime un carácter de espacio '.', nuevamente con end='' para que se imprima sin una nueva línea al final.
            print() #Esta línea imprime una nueva línea en la consola después de imprimir todas las celdas en una fila, lo que coloca la siguiente fila en la consola en la siguiente línea.

    def __eq__(self, otro): # Este método permite comparar dos objetos de la clase Tetromino utilizando el operador de igualdad (==).
        # Sobrecarga del operador de igualdad para comparar dos tetrominós en su rotación actual.
        return self.rotaciones[self.rotacion_actual] == otro.rotaciones[otro.rotacion_actual] # En esta línea, se compara la forma del Tetromino
        # actual (self) con la forma del Tetromino proporcionado (otro) en su rotación actual. Si las formas son idénticas, la expresión devolverá
        # True, lo que indica que los Tetrominós son iguales en su rotación actual. Si las formas son diferentes, la expresión devolverá False.

    def __ne__(self, otro): # Esto define un método especial llamado __ne__ en la clase Tetromino. Este método permite sobrecargar el operador de desigualdad (!=) para comparar dos objetos de la clase Tetromino.
        # Sobrecarga del operador de desigualdad.
        return not self.__eq__(otro) # En esta línea, se utiliza la función self.__eq__(otro) para verificar si los dos Tetrominós son
        # iguales en su rotación actual. Luego, se utiliza not para negar el resultado de esa igualdad. En otras palabras, si los Tetrominós
        # son iguales en su rotación actual, la función __ne__ devolverá False, lo que indica que no son desiguales. Si los Tetrominós son
        # diferentes en su rotación actual, la función __ne__ devolverá True, lo que indica que son desiguales.

    def es_semejante(self, otro): #Esto define una función llamada es_semejante en la clase Tetromino. Al igual que otras funciones dentro de
        # la clase, toma self como argumento, lo que permite que la función acceda y compare los atributos de la instancia de la clase con los
        # del Tetromino proporcionado como otro. Comprueba si dos tetrominós son semejantes en al menos una de sus rotaciones.
        for rotacion1 in self.rotaciones: #Este bucle for recorre todas las rotaciones del Tetromino actual (self) almacenadas en la lista self.rotaciones.
            for rotacion2 in otro.rotaciones:
                if rotacion1 == rotacion2: #En este punto, se compara una rotación del Tetromino actual con una rotación del Tetromino
                    # proporcionado. Si alguna de las rotaciones coincide, la función devolverá True, lo que indica que los Tetrominós son
                    # semejantes en al menos una de sus rotaciones.
                    return True # Si se encuentra una rotación semejante, la función devuelve True inmediatamente.
        return False #Si no se encuentra ninguna rotación semejante después de comparar todas las posibles combinaciones de rotaciones,
        # la función devuelve False, lo que indica que los Tetrominós no son semejantes en ninguna de sus rotaciones.

    def guardar_en_archivo(self, nombre_archivo): #Esto define una función llamada guardar_en_archivo en la clase Tetromino.
        # La función toma dos argumentos: self, que se refiere a la instancia actual de la clase, y nombre_archivo, que es el nombre del
        # archivo en el que se guardará el estado del Tetromino.
        # Guarda el estado actual del tetrominó en un archivo con el nombre proporcionado.
        with open(nombre_archivo, 'w') as archivo: #Esta línea de código utiliza la declaración with para abrir un archivo en modo escritura ('w').
            # El archivo se abre con el nombre especificado en nombre_archivo. La variable archivo representa el objeto de archivo.
            for fila in self.rotaciones[self.rotacion_actual]:
                archivo.write(''.join(fila) + '\n') #Dentro del bucle, se utiliza el método write() para escribir cada fila en el archivo.
                # ''.join(fila) se utiliza para unir todos los caracteres en la fila en una sola cadena, y luego se agrega un carácter de nueva
                # línea ('\n') al final de la fila para separar las filas en el archivo.


# Pruebas
if __name__ == "__main__":
    # Definir las formas de los tetrominós
    forma_I = [
        ['@', '@', '@', '@'],
    ]
    forma_O = [
        ['@', '@'],
        ['@', '@'],
    ]
    forma_T = [
        ['.', '@', '.'],
        ['@', '@', '@'],
    ]
    # Definir más formas de tetrominós según sea necesario

    # Crear instancias de Tetromino
    tetromino_I = Tetromino(forma_I)
    tetromino_O = Tetromino(forma_O)
    tetromino_T = Tetromino(forma_T)

    # Probar la rotación
    tetromino_T.rotar()

    # Mostrar el estado actual de los tetrominós
    tetromino_I.mostrar()
    tetromino_O.mostrar()
    tetromino_T.mostrar()

    # Probar la igualdad y semejanza
    tetromino_T.rotar()
    tetromino_T.rotar()
    tetromino_T.rotar()

    print("Igualdad entre T y T (después de rotaciones):", tetromino_T == tetromino_T)
    print("Igualdad entre T y O:", tetromino_T == tetromino_O)
    print("Semejanza entre T y O:", tetromino_T.es_semejante(tetromino_O))

    # Guardar el estado actual de un tetrominó en un archivo
    tetromino_I.guardar_en_archivo("tetromino_I.txt")
