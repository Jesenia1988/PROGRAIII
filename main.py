# This is a sample Python script.
import random

class Laberinto:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.lab = [[random.choice(['#', ' ']) for j in range(columnas)] for i in
                    range(filas)]  # Randomisado de la matriz para creacion del laberinto
        self.entrada = (random.randint(0, filas - 1), 0)
        self.salida = (random.randint(0, filas - 1), columnas - 1)
        self.posicion_actual = self.entrada  # posicionamiento del usuario
        self.tiempo = 30  # Tiempo en el que el usuar debe encontrar

    def mostrar(self):
        for i in range(self.filas):
            for j in range(self.columnas):
                if self.posicion_actual == (i, j):
                    print('X', end=' ')
                else:
                    print(self.lab[i][j], end=' ')
            print()  # Posicionamiento del jugador dentro del laberinto

    def mover(self, direccion):
        i, j = self.posicion_actual
        if direccion == 'arriba':
            if i > 0 and self.lab[i - 1][j] != '#':
                self.posicion_actual = (i - 1, j)
        elif direccion == 'abajo':
            if i < self.filas - 1 and self.lab[i + 1][j] != '#':
                self.posicion_actual = (i + 1, j)
        elif direccion == 'izquierda':
            if j > 0 and self.lab[i][j - 1] != '#':
                self.posicion_actual = (i, j - 1)
        elif direccion == 'derecha':
            if j < self.columnas - 1 and self.lab[i][j + 1] != '#':
                self.posicion_actual = (i, j + 1)  # programación  del movimiento del jugador

                def jugar(self):
                    print("¡Bienvenido al juego de laberinto!")
                    print("Tu objetivo es encontrar la salida antes de que se acabe el tiempo.")
                    print(f"Tienes {self.tiempo} segundos.")
                    print(
                        "Usa las teclas w, a, s y d para moverte arriba, izquierda, abajo y derecha, respectivamente.")  # bienvenida del programa e instrucciones
                    print("Buena suerte.")
                    import time
                    time.sleep(2)
                    inicio = time.time()
                    while self.posicion_actual != self.salida and time.time() - inicio < self.tiempo:
                        self.mostrar()
                        direccion = input("Introduce una dirección (w/a/s/d): ")
                        if direccion in ('w', 'a', 's', 'd'):
                            self.mover({'w': 'arriba', 'a': 'izquierda', 's': 'abajo', 'd': 'derecha'}[direccion])
                            if self.posicion_actual == self.salida:
                                print("¡Felicidades! ¡Has encontrado la salida!")
                                break
                        else:
                            print("Introduce una dirección válida.")
                    if self.posicion_actual != self.salida:
                        print("¡Lo siento! ¡No encontraste la salida a tiempo!")

            lab = Laberinto(5, 10)
            lab.jugar()



