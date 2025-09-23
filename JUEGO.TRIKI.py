from ajuestetriki import Tablero
class JuegoTriki:
    def __init__(self):
        self.tablero = Tablero()
        self.jugador_actual = "X"

    def cambiar_turno(self):
        self.jugador_actual = "O" if self.jugador_actual == "X" else "X"

    def jugar(self):
        print("¡Bienvenido al juego de Triki!")
        self.tablero.mostrar()

        while True:
            try:
                posicion = int(input(f"Jugador {self.jugador_actual}, elige una posición (1-9): "))
                posicion=posicion-1
                if posicion < 0 or posicion > 8:
                    print("Posición inválida. Intenta de nuevo.")
                    continue
            except ValueError:
                print("Entrada inválida. Usa números del 1 al 9.")
                continue

            if self.tablero.actualizar(posicion, self.jugador_actual):
                self.tablero.mostrar()
                if self.tablero.verificar_ganador(self.jugador_actual):
                    print(f"¡Jugador {self.jugador_actual} ha ganado!")
                    break
                elif self.tablero.lleno():
                    print("¡Empate!")
                    break
                else:
                    self.cambiar_turno()
            else:
                print("Esa posición ya está ocupada. Intenta otra.")


# Ejecutar el juego
if __name__ == "__main__":
    juego = JuegoTriki()
    juego.jugar()
