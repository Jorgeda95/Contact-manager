import pprint
import colorama

#PRIMERA FASE
#Establecer Varibles Globales
diccionarioMaestro = {}

#desmenusar la información importada de IntialContacts.txt

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def produceContactID(nombre,apellido):
    nombre = nombre.lower()
    apellido = apellido.lower()
    key=str(nombre) + str(apellido)
    return key

def dataInput():
    nombre = input("Ingrese NOMBRE:")
    apellido = input("Ingrese APELLIDO:")
    telefono = input("Ingrese TELEFONO:")
    
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def addContacts(nombre, apellido, telefono):
    key=str(nombre) + str(apellido)
    nestedDictionary = {'nombre':nombre,'apellido':apellido,'telefono':telefono}
    diccionarioMaestro[key] =[nestedDictionary]
    print(diccionarioMaestro)


def listContacts():
    print("Contact List")
    for key in diccionarioMaestro:
        print("Nombre Del Contacto: {} {}, Teléfono: {}".format(diccionarioMaestro[key]['nombre'], diccionarioMaestro[key]['apellido'], diccionarioMaestro[key]['telefono']))




   
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def main():
    dataInput()
    addContacts(nombre,apellido,telefono)

main()
#hola
