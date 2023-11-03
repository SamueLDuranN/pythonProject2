class Tetromino:
    def __init__(self, forma_inicial):
        self.forma = forma_inicial
        self.rotaciones = [forma_inicial]
        self.rotacion_actual = 0

    def rotar(self):
        self.rotacion_actual = (self.rotacion_actual + 1) % len(self.rotaciones)

    def mostrar(self):
        for fila in self.rotaciones[self.rotacion_actual]:
            for celda in fila:
                if celda == '@':
                    print('@', end='')
                else:
                    print('.', end='')
            print()

    def __eq__(self, otro):
        return self.rotaciones[self.rotacion_actual] == otro.rotaciones[otro.rotacion_actual]

    def __ne__(self, otro):
        return not self.__eq__(otro)

    def es_semejante(self, otro):
        for rotacion1 in self.rotaciones:
            for rotacion2 in otro.rotaciones:
                if rotacion1 == rotacion2:
                    return True
        return False

    def guardar_en_archivo(self, nombre_archivo):
        with open(nombre_archivo, 'w') as archivo:
            for fila in self.rotaciones[self.rotacion_actual]:
                archivo.write(''.join(fila) + '\n')


# Pruebas
if __name__ == "__main__":
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

    tetromino_I = Tetromino(forma_I)
    tetromino_O = Tetromino(forma_O)
    tetromino_T = Tetromino(forma_T)

    tetromino_T.rotar()

    tetromino_I.mostrar()
    tetromino_O.mostrar()
    tetromino_T.mostrar()

    tetromino_T.rotar()
    tetromino_T.rotar()
    tetromino_T.rotar()

    print("Igualdad entre T y T (después de rotaciones):", tetromino_T == tetromino_T)
    print("Igualdad entre T y O:", tetromino_T == tetromino_O)
    print("Semejanza entre T y O:", tetromino_T.es_semejante(tetromino_O))

    tetromino_I.guardar_en_archivo("tetromino_I.txt")
