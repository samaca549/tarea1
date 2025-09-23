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
