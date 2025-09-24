class CuentaBancaria:
    def __init__(self):
        self.nombre = None
        self.saldo = 0

    def pedir_nombre(self):
        self.nombre = input("Digite su nombre: ")

    def digitar_saldo(self):
        while True:
            try:
                saldo = float(input("Digite su saldo inicial: "))
                if saldo >= 0:
                    self.saldo = saldo
                    break
                else:
                    print("⚠️ El saldo no puede ser negativo.")
            except ValueError:
                print("⚠️ Digite un valor numérico válido.")

    def retirar_saldo(self):
        while True:
            try:
                retirar = float(input("Digite la cantidad de dinero que quiere retirar: "))
                if retirar <= self.saldo:
                    self.saldo -= retirar
                    print(f"✅ Retiro exitoso. Su saldo ahora es: {self.saldo}")
                    break
                else:
                    print("❌ No tiene suficiente saldo. Intente con un valor menor.")
            except ValueError:
                print("⚠️ Digite un valor numérico válido.")

    def mostrar_nombre_saldo(self):
        print(f"Titular: {self.nombre} | Saldo actual: {self.saldo}")


def main():
    banco = CuentaBancaria()
    banco.pedir_nombre()
    banco.digitar_saldo()

    x = input("¿Desea retirar dinero de su cuenta? (s/n): ").lower()
    if x == "s":
        banco.retirar_saldo()
    elif x == "n":
        print("Muchas gracias.")

    banco.mostrar_nombre_saldo()


if __name__ == "__main__":
    main()
