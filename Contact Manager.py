import funcionesContactManager
##########################################################################################################################################################
#MAIN #MAIN #MAIN #MAIN #MAIN #MAIN #MAIN #MAIN #MAIN #MAIN #MAIN #MAIN #MAIN #MAIN #MAIN #MAIN #MAIN #MAIN #MAIN #MAIN #MAIN #MAIN #MAIN #MAIN #MAIN #MAI
##########################################################################################################################################################
#MAIN #MAIN #MAIN #MAIN #MAIN #MAIN #MAIN #MAIN #MAIN #MAIN #MAIN #MAIN #MAIN #MAIN #MAIN #MAIN #MAIN #MAIN #MAIN #MAIN #MAIN #MAIN #MAIN #MAIN #MAIN #MAI
##########################################################################################################################################################

# diccionarioMaestro = {
#     'stevenwilson': {'nombre': "Steven",'apellido': "Wilson", 'telefono': "45656765"},
#     'davidcorzo': {'nombre': 'David', 'apellido': 'Corzo', 'telefono': '30177050'},
#     'jorgepineda':{'nombre': 'Jorge', 'apellido': 'Pineda', 'telefono': '23456895'},'favorites':{'davidcorzo': {'nombre': 'David', 'apellido': 'Corzo', 'telefono': '30177050'}}
# }
# favorites = {'davidcorzo': {'nombre': 'David', 'apellido': 'Corzo', 'telefono': '30177050'}}


def main():
        print('''
Los métodos de importación de datos son: → 
→ Por medio de un archivo que existe localmente presione "1"
→ Por medio de un link a un sitio web .json presione "2" 
''')
        importacionDeDatos = input('Porfavor seleccione el método de importación de datos: → ')
        #Fase 4 preguntar directorio
        if importacionDeDatos == '1':
                pass
        if importacionDeDatos == '2':
                pass

        #Fase 5 menú
        impresionDeMenu =  input('¿Desea imprimir el menu de opciones? ("si","no") →')
        if impresionDeMenu == 'si':
                print('''
1. Para agregar contacto presione “1”
2. Para enlistar la lista de contactos presione “2”
3. Para eliminar un contacto presione “3”
4. Para llamar a un contacto mediante un contact ID presione “4”
5. Para mandar un mensaje a un o lista de contactos presione “5”
6. Para agregar un contacto a favoritos presione “6”
7. Para remover un contacto de favoritos presione “7”
8. Para salir del menú presione “8”
                ''')

        userChoice = input('Ingrese qué quiere hacer: → ')
        
        if userChoice == '1':
                valid1 = 'no'
                while valid1 == 'no':
                        nombre = input('Ingrese el nombre del contacto: → ')
                        apellido = input('Ingrese el apellido del contacto: → ')
                        telefono = input('Ingrese el telefono del contacto: → ')
                        valid1 = input('¿Ha ingresado correctamente todos los campos ("si","no"): → ')
                funcionesContactManager.addContacts(nombre,apellido,telefono)

        elif userChoice == '2':
                funcionesContactManager.listContacts()

        elif userChoice == '3':
                valid2 = 'no'
                while valid2 == 'no':
                        nombre = input('Ingrese el nombre del contacto')
                        apellido = input('')
                        #la función ya trae su seguro
                        funcionesContactManager.removeContact(nombre,apellido)

        elif userChoice == '4':
                funcionesContactManager.callContact()

        elif userChoice == '5':
                #Fase 3 msgContacts
                mensaje = input('Ingrese su mensaje: → ')
                contactsToSendTo = input('Ingrese contacto(s) al que desea enviar el mensaje (nombre y apellido separado por comas): → ')
                funcionesContactManager.msgContacts(mensaje,contactsToSendTo)

        elif userChoice == '6':
                favorites = {}
                favoriteContactAddition = input('¿Qué contacto desea agregar a favoritos? (contactid) →')
                funcionesContactManager.addFavoriteList(favoriteContactAddition,favorites)

        elif userChoice == '7':
                favoriteContactDelete = input('¿Qué contacto desea eliminar de favoritos? (contactid) →')
                funcionesContactManager.removeFromFavorites(favoriteContactDelete,favorites)

        elif userChoice == '8':
                pass

        
        



#     #for adding contacts
#     nombre=input("Ingrese el nombre del nuevo contacto: → ")
#     apellido=input("Ingrese el apellido del nuevo contacto: → ")
#     telefono=input("Ingrese el numero de teléfono del nuevo contaco: → ")
#     funcionesContactManager.addContacts(nombre,apellido,telefono)

#     #leer/cargar initialContacts.txt and add to dictionary     
#     if activeFile == True:
#             funcionesContactManager.addContactsFromTxt(filename)
#             print()
#     # pprint(diccionarioMaestro)
    
#     else:
#             print("There is no initial contacts list, try changing directory cd (Where the file is)")








if __name__ == "__main__":
    main()
