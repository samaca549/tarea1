import random

class PacMan:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.puntos = 0

    def mover(self, direccion, tablero):
        movimientos = {
            "arriba": (0, -1),
            "abajo": (0, 1),
            "izquierda": (-1, 0),
            "derecha": (1, 0)
        }

        if direccion in movimientos:
            dx, dy = movimientos[direccion]
            nuevo_x = self.x + dx
            nuevo_y = self.y + dy

            if tablero.es_valido(nuevo_x, nuevo_y):
                self.x = nuevo_x
                self.y = nuevo_y
                if tablero.comer_punto(self.x, self.y):
                    self.puntos += 10

    def estado(self):
        return f"📍 Posición: ({self.x}, {self.y}) | ⭐ Puntos: {self.puntos}"


class Tablero:
    def __init__(self, ancho=7, alto=5):
        self.ancho = ancho
        self.alto = alto
        self.mapa = [["." for _ in range(ancho)] for _ in range(alto)]
        self.generar_puntos()

    def generar_puntos(self):
        for _ in range(10):
            x = random.randint(0, self.ancho - 1)
            y = random.randint(0, self.alto - 1)
            self.mapa[y][x] = "*"

    def mostrar(self, pacman):
        print("\n🟨 TABLERO 🟨")
        for y in range(self.alto):
            fila = ""
            for x in range(self.ancho):
                if pacman.x == x and pacman.y == y:
                    fila += "P "
                else:
                    fila += self.mapa[y][x] + " "
            print(fila)
        print()

    def es_valido(self, x, y):
        return 0 <= x < self.ancho and 0 <= y < self.alto

    def comer_punto(self, x, y):
        if self.mapa[y][x] == "*":
            self.mapa[y][x] = "."
            return True
        return False


class Juego:
    def __init__(self):
        self.tablero = Tablero()
        self.pacman = PacMan()

    def iniciar(self):
        print("🎮 ¡Bienvenido al simulador de PacMan! 🎮")
        while True:
            self.tablero.mostrar(self.pacman)
            print(self.pacman.estado())
            mov = input("Mover (arriba, abajo, izquierda, derecha, salir): ").lower()
            if mov == "salir":
                print("👋 ¡Gracias por jugar!")
                break
            self.pacman.mover(mov, self.tablero)


# Ejecutar el juego
if __name__ == "__main__":
    juego = Juego()
    juego.iniciar()
