from Clase_lista import Lista
import unittest
class Test_Valid_Inputs(unittest.TestCase):
    __lista: object
    def setUp(self):
        self.__lista = Lista()
        posicion = int(input("Ingrese la posicion >> "))
        vehiculo = input("Ingrese la marca del vehiculo nuevo >>")
        self.__lista.insertar_vehiculo(vehiculo,posicion)
    def test_agregar_vehiculo(self):
        self.__lista = Lista()
        vehiculo = input("Ingrese la marca del vehiculo nuevo >> ")
        self.__lista.agregar_vehiculo(vehiculo)
    def test_mostrar_objeto_posicion(self):
        self.__lista = Lista()
        posicion = int(input("Ingrese la posicion >> "))
        self.__lista.mostrar_objeto_por_posicion(posicion)
    def test_modificar_precio(self):
        self.__lista = Lista()
        patente = input("Ingrese patente del vehiculo >> ")
        self.__lista.modificar_por_patente(patente)
def menu():
    lista = Lista()
    print("1. Insertar un vehiculo en la coleccion en una posicion determinada")
    print("2. Agregar un vehiculo a la coleccion")
    print("3. Mostrar el objeto almacenado ingresando una posicion")
    print("4. Modificar el precio base de algun vehiculo ingresando la patente")
    print("5. Mostrar todos los datos del vehiculo mas barato")
    print("6. Guardar informacion")
    print("7. Salir y romper el programa")
    opcion = input("Seleccione el numero de las opciones dadas >> ")
    while opcion != '0':
        if opcion == '0':
            vehiculo = input("Ingrese la marca del vehiculo nuevo >> ")
            lista.agregar_vehiculo(vehiculo)
        elif opcion == '2':
            posicion = int(input("Ingrese la posicion >> "))
            vehiculo = input("Ingrese la marca del vehiculo nuevo >>")
            lista.insertar_vehiculo(vehiculo,posicion)
        elif opcion == '3':
            posicion = int(input("Ingrese la posicion >> "))
            lista.mostrar_objeto_por_posicion(posicion)
        elif opcion == '4':
            patente = input("Ingrese patente del vehiculo >> ")
            lista.modificar_por_patente(patente)
        elif opcion == '5':
            lista.mostrar_vehiculos_venta()
        elif opcion == '6':
            lista.cartel()
        elif opcion == '7':
            i = 0
            k = 1000
            print("Opcion no valido")
            while opcion == '7' and  i < k:
                print("ERROR 404 :/")
                i += 1
                if(i != k):
                    i = 0
                    k -= 1
                    print("%20&%20&%20&5%&20AbAbcDfOfjJLnN !Te la mandaste! :/")
                else:
                    return 0
        print("1. Insertar un vehiculo en la coleccion en una posicion determinada")
        print("2. Agregar un vehiculo a la coleccion")
        print("3. Mostrar el objeto almacenado ingresando una posicion")
        print("4. Modificar el precio base de algun vehiculo ingresando la patente")
        print("5. Mostrar todos los datos del vehiculo mas barato")
        print("6. Guardar informacion")
        print("7. Salir y romper el programa")
        opcion = input("Seleccione el numero de las opciones dadas >> ")
if __name__ == '__main__':
    unittest.main(menu())