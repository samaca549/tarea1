from contraseña import contraseñasegura
from PERSONA import Persona, Datos

class Menu:
    def mostrar_menu(self):
        salirprograma = False
        opcion1 = 0
        contraseñas_generadas = []
        datos_ingresados = False
        contraseña_generada = False
        contador = 1

        while salirprograma == False and opcion1 == 0:
            print("//////////////////////////////")
            print(" BIENVENIDO AL MENÚ ")
            print("1. Digite sus datos personales para calcular IMC")
            print("2. Generar una contraseña y verificar si es segura")
            print("3. Salir")

            opcion = int(input("Seleccione una opción (1-3): "))

            if opcion == 1:
                recolector = Datos()
                persona = recolector.obtener_datos()
                print("//////////////////////////////")
                estado = persona.verificar_18_años()
                imc = persona.calcular_imc()
                datos_ingresados = True

            elif opcion == 2:
                generador = contraseñasegura()
                numeros = generador.numero_random()
                letras = generador.letras_aleatorias()
                final = generador.mostrarcontraseña(letras, numeros)
                contraseñas_generadas.append(final)
                print(" Contraseña generada:", final)
                cantidad_numeros = generador.contar()
                cantidad_letras = generador.contar_letras()
                generador.comprobarseguridad(cantidad_numeros, cantidad_letras)
                contraseña_generada = True

            elif opcion == 3:
                print(" Gracias por usar el programa. ¡Hasta luego!")
                salirprograma = True

            else:
                print(" Opción inválida. Intente nuevamente.")

            while salirprograma == False and opcion1 != 1:
                print("//////////////////////////////")
                print(" MENÚ DE OPCIONES ADICIONALES ")
                print("1. Ver datos personales e IMC")
                print("2. Generar otra contraseña")
                print("3. Ver contraseñas anteriores")
                print("4. Salir")

                opcion = int(input("Seleccione una opción (1-4): "))

                if opcion == 1:
                    if datos_ingresados:
                        persona.mostrar_datos(estado, imc)
                    else:
                        print(" Primero debe ingresar sus datos personales (opción 1).")
                        recolector = Datos()
                        persona = recolector.obtener_datos()
                        print("//////////////////////////////")
                        estado = persona.verificar_18_años()
                        imc = persona.calcular_imc()
                        datos_ingresados = True

                elif opcion == 2:
                    generador = contraseñasegura()
                    numeros = generador.numero_random()
                    letras = generador.letras_aleatorias()
                    final = generador.mostrarcontraseña(letras, numeros)
                    print(" Contraseña generada:", final)
                    contraseñas_generadas.append(final)
                    cantidad_numeros = generador.contar()
                    cantidad_letras = generador.contar_letras()
                    generador.comprobarseguridad(cantidad_numeros, cantidad_letras)
                    contraseña_generada = True

                elif opcion == 3:
                    if contraseña_generada:
                        print("\n Contraseñas generadas anteriormente:")
                        contador = 1
                        for c in contraseñas_generadas:
                            print(f"{contador}. {c}")
                            contador += 1
                    else:
                        print(" Primero debe generar una contraseña (opción 2).")

                elif opcion == 4:
                    print(" Gracias por usar el programa. ¡Hasta luego!")
                    opcion1 = 1

                else:
                    print(" Opción inválida. Intente nuevamente.")

def main():
    app = Menu()
    app.mostrar_menu()

if __name__ == "__main__":
    main()
