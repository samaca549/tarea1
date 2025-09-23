import random 
class PacMan: 
    def __init__(self): 
        self.x = 0 
        self.y = 0 
        self.puntos = 0 

    def mover (self, direccion, tablero): 
            self.x, self.y 
            if direccion == "w": self.y -= 1 
            elif direccion == "s": self.y += 1 
            elif direccion == "a": self.x -= 1 
            elif direccion == "d": self.x += 1 
            if tablero.es_valido(self.x, self.y): 
                self.x, self.y 
            if tablero.hay_punto(self.x, self.y): 
                self.puntos += 10 
                tablero.quitar_punto(self.x, self.y)

    def mostrar_estado(self):
        print(f"Posición: ({self.x}, {self.y}) | Puntos: {self.puntos}")


class Tablero:
    def __init__(self):
        self.ancho = random.randint(5, 25)
        self.alto = random.randint(5, 25)
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
        self.nivel = 1

    def iniciar(self):
        print(" Bienvenido a PacMan ")
        while True:
            print(f"\n Nivel {self.nivel}")
            self.tablero.mostrar(self.pacman)
            self.pacman.mostrar_estado()

            if len(self.tablero.puntos) == 0:
                print(" ¡Nivel completado! Generando nuevo tablero...")
                self.tablero = Tablero()
                self.nivel += 1
                self.pacman.x = 0
                self.pacman.y = 0
                continue

            movimiento = input("Mover (w, s, a, d, salir): ").lower()
            if movimiento == "salir":
                print(" Fin del juego")
                break
            self.pacman.mover(movimiento, self.tablero)


# Ejecutar el juego
if __name__ == "__main__":
    juego = Juego()
    juego.iniciar()
