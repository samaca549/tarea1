import random
import string

class contraseñasegura:
    def __init__(self):
        self.contraseña_rand = []
        self.palabras_rand = []
        self.todas_Contraseñas = []

    def numero_random(self):
        numerodedigitos = random.randint(5, 15)
        self.contraseña_rand = [random.randint(0, 9) for _ in range(numerodedigitos)]
        return ''.join(str(n) for n in self.contraseña_rand)

    def letras_aleatorias(self):
        cantidadletras = random.randint(5, 15)
        self.palabras_rand = [random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(cantidadletras)]
        return ''.join(self.palabras_rand)

    def mostrarcontraseña(self, grupoletras, gruponumeros):
        cadenafinal = grupoletras + gruponumeros
        return cadenafinal

    def contar(self):
        return len(self.contraseña_rand)

    def contar_letras(self):
        return len(self.palabras_rand)

    def comprobarseguridad(self, contador, contadorletras):
        nivel_num = 1 if contador >= 10 else 0
        nivel_letras = 1 if contadorletras >= 10 else 0

        if nivel_num == 1 and nivel_letras == 1:
            print(" Contraseña segura")
        elif nivel_num == 1 or nivel_letras == 1:
            print(" Contraseña aceptable")
        else:
            print(" Contraseña insegura")

    def totalcontraseñas(self, contraseñas):
        self.todas_Contraseñas.append(contraseñas)


    def mostrar_historial(self):
        print("\n Historial de contraseñas generadas:")
        for i in self.todas_Contraseñas:
            print(i)
