# diccionarioMaestro = {}
# def addContacts(nombre, apellido, telefono):
#     key=str(nombre) + str(apellido)
#     nestedDictionary = {'nombre':nombre,'apellido':apellido,'telefono':telefono}
#     diccionarioMaestro[key] =[nestedDictionary]
#     print(diccionarioMaestro)

# nombre = input('NAME: ')
# apellido = input('APELLIDO')
# telefono = input(str('telefono'))

# addContacts(nombre,apellido,telefono)

diccionarioMaestro = {
    'stevenwilson': {'nombre': "Steven",'apellido': "Wilson", 'telefono': "45656765"},
    'davidcorzo': {'nombre': 'David', 'apellido': 'Corzo', 'telefono': '30177050'}
}



# remove = input(str("Ingrese el contacto a eliminar: → ")) davidcorzo
# remove = remove.lower


def produceContactID(nombre,apellido):
    nombre = nombre.lower()
    apellido = apellido.lower()
    key=str(nombre) + str(apellido)
    return key

nombre = input('NOMBRE del contacto que desea borrar: ')
apellido = input('APELLIDO del contacto que desea borrar: ')


def removeContact(nombre,apellido):
    key = produceContactID(nombre,apellido)
    confirmation = input("Estás seguro que quieres borrar el contacto → {} {} ← con el número de → telefono ← {} ← (Ingrese si o no) → ".format(diccionarioMaestro[key]['nombre'],diccionarioMaestro[key]['apellido'],diccionarioMaestro[key]['telefono']))
    if confirmation == "si":
        try:
            del diccionarioMaestro[key]
        except TypeError:
            print("El contacto ingresado está mal escrito o no existe en la lista de contactos")
        except KeyError:
            print("El contacto ingresado está mal escrito o no existe en la lista de contactos")
    else: 
        print("No se eliminó el contacto") 

removeContact(nombre,apellido)
print(diccionarioMaestro)