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
        contador=0
        for i in (self.contraseña_rand):
            contador=contador+1
        return contador

    def contar_letras(self):
        contador1=0
        for i in (self.palabras_rand):
            contador1=contador1+1
        return contador1

    def comprobarseguridad(self, contador, contador1):
        if contador1>=10 and contador>=10:
            print(" Contraseña segura")
        elif contador1>=10 and contador<10:
            print(" Contraseña aceptable")
        elif contador>=10 and contador1<10:
            print(" Contraseña aceptable")
        else:
            print(" Contraseña insegura")

    def totalcontraseñas(self, contraseñas):
        self.todas_Contraseñas.append(contraseñas)


    def mostrar_historial(self):
        print("\n Historial de contraseñas generadas:")
        for i in self.todas_Contraseñas:
            print(i)
