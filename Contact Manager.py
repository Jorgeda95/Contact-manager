from funcionesContactManager import *
def main():
        print('')
        print('     Los métodos de importación de datos son: → \n          → Por medio de un archivo que existe localmente presione "1" \n          → Por medio de un link a un sitio web .json presione "2" \n          → Por medio de una base de datos que yo crearé en este programa "3"')    
        print('')


###########################################################################################################################################################################################################
#IMPORTACION DE DATOS POR METODOS #IMPORTACION DE DATOS POR METODOS #IMPORTACION DE DATOS POR METODOS #IMPORTACION DE DATOS POR METODOS #IMPORTACION DE DATOS POR METODOS #IMPORTACION DE DATOS POR METODOS 
###########################################################################################################################################################################################################
        

        validacionDeImportacion = 'no'
        while validacionDeImportacion == 'no':
                importacionDeDatos = input('Porfavor seleccione el método de importación de datos: → ')
                
                #Fase 4 preguntar directorio
                if importacionDeDatos == '1':
                        try:
                                filename = input('Ingrese el nombre de sus archivos: → ') 
                                activeFile= os.path.exists(filename) 
                                
                                
                                if activeFile == True:
                                        Esthetics1()
                                        
                                        diccionarioMaestro = {}
                                        favorites = {}

                                        diccionarioMaestro = loadFromFile12(filename, diccionarioMaestro)
                                        Esthetics1()
                                        validacionDeImportacion = 'yes'

                                elif activeFile == False:
                                        print("El archivo no ha sido agregado o no está en el directorio")
                                        validacionDeImportacion = 'no'
                                        
                        except:
                                print("El archivo elegido no está en el directorio")
                                validacionDeImportacion = 'no'

                elif importacionDeDatos == '2':
                        try:

                                diccionarioMaestro = {}
                                favorites = {}
                                print("Método GET: → ")
                                urlGet=input("Ingrese la URL con la desea utilizar el método GET: → ")
                                gid = input(str("Ingresa el gid para GET: → "))
                                diccionarioMaestro = get14(gid,urlGet,diccionarioMaestro)
                                print("")
                                # https://jsonplaceholder.typicode.com/todos/
                                
                                #https://tinyurl.com/yygujcbg/contacts?
                                validacionDeImportacion = 'yes'
                        except:
                                print('La URL seleccionada no es válida.')
                                print("")
                                validacionDeImportacion = 'no'

                elif importacionDeDatos == '3':
                        diccionarioMaestro = {}
                        favorites = {}
                        validacionDeImportacion = 'yes'
                        print("prueba del tercer método de importación : ",diccionarioMaestro)



#####################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################
#OPCIONES DE MENU #OPCIONES DE MENU #OPCIONES DE MENU #OPCIONES DE MENU #OPCIONES DE MENU #OPCIONES DE MENU #OPCIONES DE MENU #OPCIONES DE MENU #OPCIONES DE MENU #OPCIONES DE MENU #OPCIONES DE MENU #OPCIONES DE MENU #OPCIONES DE MENU #OPCIONES DE MENU #OPCIONES DE MENU #OPCIONES DE MENU #OPCIONES DE MENU #OPCIONES DE MENU #OPCIONES DE MENU #OPCIONES DE MENU #OPCIONES DE MENU #OPCIONES DE MENU #OPCIONES DE MENU #OPCIONES DE MENU #OPCIONES DE MENU #OPCIONES DE MENU #OPCIONES DE MENU #OPCIONES DE ME
#####################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################
        


        impresionDeMenu =  input('¿Desea imprimir el menú de opciones? ("si","no") → ')
        if impresionDeMenu == 'si':
                print('')
                print('Menú de opciones: → ')
                print('     1. Para agregar contacto presione “1” \n     2. Para enlistar la lista de contactos presione “2” \n     3. Para eliminar un contacto presione “3” \n     4. Para llamar a un contacto mediante un contact ID presione “4” \n     5. Para mandar un mensaje a un o lista de contactos presione “5” \n     6. Para agregar un contacto a favoritos presione “6” \n     7. Para remover un contacto de favoritos presione “7” \n     8. Para ver lista de contactos en favoritos presione "8" \n     9. Para salir del menú presione “9”')
                print('')
        validacionDeMain = 'si'

        while validacionDeMain == 'si':

                userChoice = input('Ingrese qué quiere hacer: → ')
                
                if userChoice == '1':
                        valid1 = 'no'
                        while valid1 == 'no':
                                nombre = input('Ingrese el nombre del contacto: → ')
                                apellido = input('Ingrese el apellido del contacto: → ')
                                telefono = input('Ingrese el telefono del contacto: → ')
                                valid1 = input('¿Ha ingresado correctamente todos los campos ("si","no"): → ')
                        addContacts3(nombre,apellido,telefono,diccionarioMaestro)

                        validacionDeMain = input('¿Desea continuar ingrese opción ("si","no")? : → ')
                        Esthetics1()

                elif userChoice == '2':
                        listContacts4(diccionarioMaestro)
                        
                        validacionDeMain = input('¿Desea continuar ingrese opción ("si","no")? : → ')
                        Esthetics1()

                elif userChoice == '3':
                        
                        nombre = input('Ingrese el nombre del contacto: → ')
                        apellido = input('Ingrese el apellido del contacto: → ')
                        key = produceContactID2(nombre,apellido)
                        confirmation = input("Estás seguro que quieres borrar el contacto → {} {} ← con el número de → telefono ← {} ← (Ingrese si o no) → ".format(diccionarioMaestro[key]['nombre'],diccionarioMaestro[key]['apellido'],diccionarioMaestro[key]['telefono']))
                        
                        if confirmation == 'si':
                                removeContact5(nombre,apellido,diccionarioMaestro)
                        else:
                                print("No se eliminó el contacto")   
                        
                        Esthetics1()
                        
                        validacionDeMain = input('¿Desea continuar ingrese opción ("si","no")? : → ')
                        
                        Esthetics1()

                elif userChoice == '4':
                        contactID = input('Ingrese el contactID → ')
                        callContact8(contactID, diccionarioMaestro)

                        validacionDeMain = input('¿Desea continuar ingrese opción ("si","no")? : → ')
                        Esthetics1()

                elif userChoice == '5':
                        #Fase 3 msgContacts
                        mensaje = input('Ingrese su mensaje: → ')
                        contactsToSendTo = input('Ingrese contacto(s) al que desea enviar el mensaje (nombre y apellido separado por comas): → ')
                        msgContacts9(mensaje,contactsToSendTo,diccionarioMaestro)

                        validacionDeMain = input('¿Desea continuar ingrese opción ("si","no")? : → ')
                        Esthetics1()

                elif userChoice == '6':
                        
                        favoriteContactAddition = input('¿Qué contacto desea agregar a favoritos? (contactid) → ')
                        addFavoriteList10(favoriteContactAddition,favorites,diccionarioMaestro)

                        validacionDeMain = input('¿Desea continuar ingrese opción ("si","no")? : → ')
                        Esthetics1()


                elif userChoice == '7':
                        favoriteContactDelete = input('¿Qué contacto desea eliminar de favoritos? (contactid) → ')
                        removeFromFavorites11(favoriteContactDelete,favorites,diccionarioMaestro)

                        validacionDeMain = input('¿Desea continuar ingrese opción ("si","no")? : → ')
                        Esthetics1()

                elif userChoice == '8':
                        print('Los contactos en favoritos son: → ')
                        listFavoritesContacts4punto5(favorites)
                        validacionDeMain = input('¿Desea continuar ingrese opción ("si","no")? : → ')

                elif userChoice == '9':
                        break


#####################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################
#EXPORTACION DE DATOS POR METODOS #EXPORTACION DE DATOS POR METODOS #EXPORTACION DE DATOS POR METODOS #EXPORTACION DE DATOS POR METODOS #EXPORTACION DE DATOS POR METODOS #EXPORTACION DE DATOS POR METODOS #EXPORTACION DE DATOS POR METODOS #EXPORTACION DE DATOS POR METODOS #EXPORTACION DE DATOS POR METODOS #EXPORTACION DE DATOS POR METODOS #EXPORTACION DE DATOS POR METODOS #EXPORTACION DE DATOS POR METODOS #EXPORTACION DE DATOS POR METODOS #EXPORTACION DE DATOS POR METODOS #EXPORTACION DE DATOS POR
#####################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################

        exportacion = input('¿Desea exportar los datos modificados? ("si","no") → ')
        
        if exportacion == 'si':
                validacionDeExportacion = 'no'
                while validacionDeExportacion == 'no':
                        print("")
                        print('Método #1: Imprime la información manipulada a la terminal directamente presione "1": → \nMétodo #2: Mete la información manipulada a un archivo que usted nombrará presione "2": → \nMétodo #3: Sube por el método POST la información manipulada a una URL de su elección presione "3"')
                        print("")
                        metodoDeExportacion = input('¿Qué metodo desea emplear para exportar? ')
                        
                        #exportación a la terminal directamente
                        if metodoDeExportacion == '1':
                                impresionDirectaALaTerminal15(diccionarioMaestro,favorites)
                                validacionDeExportacion = input('¿Quiere exportarlo de alguna otra manera? → ')
                        
                        #exportación a un archivo
                        elif metodoDeExportacion == '2':
                                newFileName = str(input('Ingrese el nombre de su archivo: (No olvide ponerle extensión) → '))
                                exportacionDeLaDataAUnArchivoNuevo16(diccionarioMaestro,favorites,newFileName)
                                validacionDeExportacion = input('¿Quiere exportarlo de alguna otra manera? → ')
                        
                        #exportación POST
                        elif metodoDeExportacion == '3':
                                urlP = input("Ingrese la URL: → ")
                                gid = input('Ingrese su gid: → ')
                                urlPost=(urlP+gid)
                                post13(gid,urlPost,diccionarioMaestro)
                                validacionDeExportacion = input('¿Quiere exportarlo de alguna otra manera? → ')
                        
                        
                        
        print("|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|")
        print('|------------------------------------------------ Final Project - Programación I - UFM - Credits: David Corzo, Jorge Pineda & Steven Wilson ------------------------------------------------|')
        print("|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|")
                
                #subirALink
                # print("Método POST: → ")
                # gid = input(str("Ingrese el gid para POST:\n"))
                # Post(gid)
                


  
        

if __name__ == "__main__":
    main()
        