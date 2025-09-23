import random

class PacMan:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.puntos = 0

    def mover(self, direccion, tablero):
        if direccion == "w":
            nuevo_x = self.x
            nuevo_y = self.y - 1
        elif direccion == "s":
            nuevo_x = self.x
            nuevo_y = self.y + 1
        elif direccion == "a":
            nuevo_x = self.x - 1
            nuevo_y = self.y
        elif direccion == "d":
            nuevo_x = self.x + 1
            nuevo_y = self.y
        else:
            nuevo_x = self.x
            nuevo_y = self.y

        if tablero.es_valido(nuevo_x, nuevo_y):
            self.x = nuevo_x
            self.y = nuevo_y
            if tablero.hay_punto(self.x, self.y):
                self.puntos += 10
                tablero.quitar_punto(self.x, self.y)

    def mostrar_estado(self):
        print(f"Posición: ({self.x}, {self.y}) | Puntos: {self.puntos}")


class Tablero:
    def __init__(self):
        y=random.randint(5, 25)
        x=random.randint(5, 25)
        self.ancho = y
        self.alto = x
        self.puntos = []
        self.generar_puntos()

    def generar_puntos(self):
        while len(self.puntos) < 6:
            x = random.randint(0, self.ancho - 1)
            y = random.randint(0, self.alto - 1)
            if (x, y) not in self.puntos:
                self.puntos.append((x, y))

    def mostrar(self, pacman):
        for y in range(self.alto):
            fila = ""
            for x in range(self.ancho):
                if (x, y) == (pacman.x, pacman.y):
                    fila += "P "
                elif (x, y) in self.puntos:
                    fila += "* "
                else:
                    fila += ". "
            print(fila)
        print()

    def es_valido(self, x, y):
        return 0 <= x < self.ancho and 0 <= y < self.alto

    def hay_punto(self, x, y):
        return (x, y) in self.puntos

    def quitar_punto(self, x, y):
        if (x, y) in self.puntos:
            self.puntos.remove((x, y))


class Juego:
    def __init__(self):
        self.tablero = Tablero()
        self.pacman = PacMan()

    def iniciar(self):
        print("Bienvenido a PacMan")
        while True:
            self.tablero.mostrar(self.pacman)
            self.pacman.mostrar_estado()
            movimiento = input("Mover (w, s, a, d, salir): ").lower()
            if movimiento == "salir":
                print("Fin del juego")
                break
            self.pacman.mover(movimiento, self.tablero)


# Ejecutar el juego
if __name__ == "__main__":
    juego = Juego()
    juego.iniciar()
