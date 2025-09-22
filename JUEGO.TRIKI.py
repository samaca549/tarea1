class Tablero:
    def __init__(self):
        self.celdas = [" " for _ in range(9)]

    def mostrar(self):
        print("\n")
        for i in range(3):
            fila = " | ".join(self.celdas[i*3:(i+1)*3])
            print(fila)
            if i < 2:
                print("--+---+--")
        print("\n")

    def actualizar(self, posicion, simbolo):
        if self.celdas[posicion] == " ":
            self.celdas[posicion] = simbolo
            return True
        return False

    def verificar_ganador(self, simbolo):
        combinaciones = [
            [0,1,2], [3,4,5], [6,7,8],  # filas
            [0,3,6], [1,4,7], [2,5,8],  # columnas
            [0,4,8], [2,4,6]            # diagonales
        ]
        for combo in combinaciones:
            if all(self.celdas[i] == simbolo for i in combo):
                return True
        return False

    def lleno(self):
        return all(c != " " for c in self.celdas)


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
