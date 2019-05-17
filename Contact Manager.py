
##########################################################################################################################################################
#MAIN #MAIN #MAIN #MAIN #MAIN #MAIN #MAIN #MAIN #MAIN #MAIN #MAIN #MAIN #MAIN #MAIN #MAIN #MAIN #MAIN #MAIN #MAIN #MAIN #MAIN #MAIN #MAIN #MAIN #MAIN #MAI
##########################################################################################################################################################
#MAIN #MAIN #MAIN #MAIN #MAIN #MAIN #MAIN #MAIN #MAIN #MAIN #MAIN #MAIN #MAIN #MAIN #MAIN #MAIN #MAIN #MAIN #MAIN #MAIN #MAIN #MAIN #MAIN #MAIN #MAIN #MAI
##########################################################################################################################################################

def main():

    #for adding contacts
    nombre=input("Ingrese el nombre del nuevo contacto: → ")
    apellido=input("Ingrese el apellido del nuevo contacto: → ")
    telefono=input("Ingrese el numero de teléfono del nuevo contaco: → ")
    addContacts(nombre,apellido,telefono)

    #leer/cargar initialContacts.txt and add to dictionary     
    if activeFile ==True:
            addContactsFromTxt(filename)
            print()
    # pprint(diccionarioMaestro)
    
    else:
            print("There is no initial contacts list, try changing directory cd (Where the file is)")



main()