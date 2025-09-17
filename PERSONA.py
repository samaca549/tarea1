class Persona:
    def __init__(self, nombre, edad, genero, peso, altura):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.peso = peso
        self.altura = altura

    def verificar_18_años(self): 
        if self.edad >= 18: 
            print("Usted es mayor de edad.") 
            estado = "mayor de edad"
        else: 
            print("Usted es menor de edad.") 
            estado = "menor de edad"
        return estado


    def calcular_imc(self):
        imc = self.peso / (self.altura ** 2)
        print(f"Su índice de masa corporal es {imc}")
        return imc
    def mostrar_datos(self, estado, imc):
        print("\n Resumen:")
        print(f" Nombre: {self.nombre}")
        print(f" Edad: {self.edad} años ({estado})")
        print(f" Género: {self.genero}")
        print(f" Altura: {self.altura} m")
        print(f" Peso: {self.peso} kg")
        print(f" IMC: {imc}")

class Datos:
    def obtener_datos(self):
        print("Digite los siguientes datos sobre su persona:")
        nombre = input("Nombre: ")
        edad = int(input("Edad: "))
        genero = input("Género: ")
        peso = float(input("Peso en kg: "))
        altura = float(input("Altura en metros: "))
        return Persona(nombre, edad, genero, peso, altura)

