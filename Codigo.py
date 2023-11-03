class Tetromino:
    def __init__(self, forma_inicial):
        # Constructor de la clase Tetromino. Recibe una forma inicial.
        self.forma = forma_inicial  # Almacena la forma del tetrominó como una lista de 4x4 caracteres.
        self.rotaciones = [forma_inicial]  # Inicializa una lista que contendrá las diferentes rotaciones del tetrominó.
        self.rotacion_actual = 0  # Inicializa el índice de la rotación actual en 0.

    def rotar(self):
        # Realiza una rotación del tetrominó en sentido de las manecillas del reloj.
        self.rotacion_actual = (self.rotacion_actual + 1) % len(self.rotaciones)

    def mostrar(self):
        # Muestra el estado actual del tetrominó en la consola.
        # Utiliza '@' para representar las partes del tetrominó y '.' para el espacio vacío.
        for fila in self.rotaciones[self.rotacion_actual]:
            for celda in fila:
                if celda == '@':
                    print('@', end='')
                else:
                    print('.', end='')
            print()

    def __eq__(self, otro):
        # Sobrecarga del operador de igualdad para comparar dos tetrominós en su rotación actual.
        return self.rotaciones[self.rotacion_actual] == otro.rotaciones[otro.rotacion_actual]

    def __ne__(self, otro):
        # Sobrecarga del operador de desigualdad.
        return not self.__eq__(otro)

    def es_semejante(self, otro):
        # Comprueba si dos tetrominós son semejantes en al menos una de sus rotaciones.
        for rotacion1 in self.rotaciones:
            for rotacion2 in otro.rotaciones:
                if rotacion1 == rotacion2:
                    return True
        return False

    def guardar_en_archivo(self, nombre_archivo):
        # Guarda el estado actual del tetrominó en un archivo con el nombre proporcionado.
        with open(nombre_archivo, 'w') as archivo:
            for fila in self.rotaciones[self.rotacion_actual]:
                archivo.write(''.join(fila) + '\n')


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
