import random

class cuenta_bancaria:
    def __init__(self):
        self.nombre = None
        self.contraseñainicial = 0
        self.edad = 0
        self.genero = None
        self.__contraseña = []  # protegido

    def pedir_usuarios(self):
        print("Bienvenidos a la app bancaria:")

        # Pedir nombre
        self.nombre = input("Digite su nombre: ")

        # Pedir contraseña inicial
        while True:
            try:
                self.contraseñainicial = int(input("Digite su contraseña de 4 números: "))
                if 1000 <= self.contraseñainicial <= 9999:
                    break
                else:
                    print("⚠️ La contraseña debe tener exactamente 4 dígitos.")
            except ValueError:
                print("⚠️ Debe digitar solo números.")

        # Pedir género
        while True:
            print("Seleccione su género:")
            print("1. Hombre")
            print("2. Mujer")
            try:
                opcion = int(input("Digite su opción: "))
                if opcion == 1:
                    self.genero = "Hombre"
                    break
                elif opcion == 2:
                    self.genero = "Mujer"
                    break
                else:
                    print("⚠️ Opción inválida, intente de nuevo.")
            except ValueError:
                print("⚠️ Solo puede digitar números (1 o 2).")

        # Pedir edad
        while True:
            try:
                self.edad = int(input("Digite su edad (solo mayores de edad): "))
                if self.edad >= 18:
                    print("✅ Bienvenido, acceso permitido.")
                    break
                else:
                    print("❌ Usted no puede estar aquí. Registro cancelado.")
                    return
            except ValueError:
                print("⚠️ Debe digitar un número válido.")

        print("\nUsuario registrado con éxito ✅")
        print(f"Nombre: {self.nombre}")
        print(f"Género: {self.genero}")
        print(f"Edad: {self.edad}")

    def contraseñahacer(self):
        print("Vamos a generar una contraseña de 4 dígitos para su persona...")
        self.__contraseña = [random.randint(0, 9) for _ in range(4)]
        print("Contraseña generada ✅")

    def mostrar_contraseña(self):
        return "".join(map(str, self.__contraseña))  # ahora devuelve el valor


def main():
    a = cuenta_bancaria()
    a.pedir_usuarios()
    if a.edad>=18:
        a.contraseñahacer()
        print("Para poder ver su contraseña generada, digite los numeros pedidos en el inicio:")

        contador = 0
        while contador < 3:  # máximo 3 intentos
            try:
                x = int(input("Digite su contraseña inicial: "))
                if a.contraseñainicial == x:
                    print(f"✅ La contraseña generada es: {a.mostrar_contraseña()}")
                    break
                else:
                    print("❌ Contraseña incorrecta.")
                    contador += 1
            except ValueError:
                print("⚠️ Debe digitar un número válido.")
                contador += 1

        if contador == 3:
            print("🚫 Demasiados intentos fallidos. Bloqueando acceso...")
            return

if __name__ == "__main__":
    main()
