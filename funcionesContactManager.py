# import pprint
import colorama
import sys, traceback
import sys, time
import os
import csv
import requests




def Esthetics1():
    print('')
    

def produceContactID2(nombre,apellido):
    nombre = nombre.lower()
    apellido = apellido.lower()
    key=str(nombre) + str(apellido)
    return key

# def pprint(diccionario):
#     iteration = 0
#     for k,v in dicciccionario:
#         print("{} : " .format(k,v))
#         for v in k,v:
#             print("Nombre:", {}, "Apellido", {}, "Telefono", {})

# def pprint(dicc):
#     for k,v in dicc.items():
#         print("{}: {}".format(k,v))
        


#################################################################################################################################################################################
#FASE 1 #FASE 1 #FASE 1 #FASE 1 #FASE 1 #FASE 1 #FASE 1 #FASE 1 #FASE 1 #FASE 1 #FASE 1 #FASE 1 #FASE 1 #FASE 1 #FASE 1 #FASE 1 #FASE 1 #FASE 1 #FASE 1 #FASE 1 #FASE 1 #FASE 1 #
#################################################################################################################################################################################
#FASE 1 #FASE 1 #FASE 1 #FASE 1 #FASE 1 #FASE 1 #FASE 1 #FASE 1 #FASE 1 #FASE 1 #FASE 1 #FASE 1 #FASE 1 #FASE 1 #FASE 1 #FASE 1 #FASE 1 #FASE 1 #FASE 1 #FASE 1 #FASE 1 #FASE 1 #
#################################################################################################################################################################################
#def documentacionDeLaFase1():
    '''
    Fase 1:
    1. addContact: Nombre, Apellido y Telefono 
    2. listContacts:  “pretty”
    3. removeContact:  “Nombre Apellido” del contacto y lo elimine 
    '''



def addContacts3(nombre, apellido, telefono,diccionarioMaestro):
    key=produceContactID2(nombre,apellido)
    nestedDictionary = {'nombre':nombre,'apellido':apellido,'telefono':telefono}
    diccionarioMaestro[key] = nestedDictionary
    return diccionarioMaestro
    

def listContacts4(diccionarioMaestro):
    print("Contact List")
    for key in diccionarioMaestro:
        print("Nombre Del Contacto: {} {}, Teléfono: {}".format(diccionarioMaestro[key]['nombre'], diccionarioMaestro[key]['apellido'], diccionarioMaestro[key]['telefono']))

def removeContact5(nombre,apellido,diccionarioMaestro):
    key = produceContactID2(nombre,apellido)
    try:
        del diccionarioMaestro[key]
        valid2 = 'yes'
    except:
        print("El contacto ingresado está mal escrito o no existe en la lista de contactos")

    return diccionarioMaestro
    
#################################################################################################################################################################################
#FASE 2 #FASE 2 #FASE 2 #FASE 2 #FASE 2 #FASE 2 #FASE 2 #FASE 2 #FASE 2 #FASE 2 #FASE 2 #FASE 2 #FASE 2 #FASE 2 #FASE 2 #FASE 2 #FASE 2 #FASE 2 #FASE 2 #FASE 2 #FASE 2 #FASE 2 #
#################################################################################################################################################################################
#FASE 2 #FASE 2 #FASE 2 #FASE 2 #FASE 2 #FASE 2 #FASE 2 #FASE 2 #FASE 2 #FASE 2 #FASE 2 #FASE 2 #FASE 2 #FASE 2 #FASE 2 #FASE 2 #FASE 2 #FASE 2 #FASE 2 #FASE 2 #FASE 2 #FASE 2 #
#################################################################################################################################################################################
#def documentacionDeLaFase2():
    """ Fase 2: 
    1. Leer/cargar (automaticamente) los contactos de un archivo llamado InitialContacts.txt, si y solo si el archivo existe en el mismo directorio que su programa.py
    2. Agregarlos a la “lista” que anteriormente estaba vacia , es decir ahora su lista ya va a estar pre-inicializada
    3. Obviamente estos contactos deben ser ordenados dentro de la “lista” de contactos

    Recuerde que los contactos se clasifican y se ordenan por apellido, si el apellido no esta
    presente el nombre dictara en que “Letra” alfabetica se pondra el contacto. Estos contactos
    estaran en el archivo de una manera desordenada."""



def readFile6(filename):
    with open(filename) as archivo:
        print("el archivo a leer es {}".format(filename))
        reader = archivo.readlines()
        stringedList = "".join(reader)
        #
        listToIterate = stringedList.splitlines()
        # print(listToIterate)
        combinedList = []
        iteration = 0
        for n in listToIterate:
            if listToIterate[iteration] != '':
                combinedList.append(listToIterate[iteration])
            iteration = iteration + 1

        finalList = []
        for line in combinedList:
            separated = line.split(",")
            finalList.append(separated)
        return finalList

# print(readFile(filename))

# def addContactsFromTxt7(filename,diccionarioMaestro):
#     lines=readFile6(filename)
#     # lines.strip("-")
#     for line in lines:
#         words = line.split(",")
#         newContactID = words[0]+words[1]

#         diccionarioMaestro.update( {newContactID : {"nombre": words[0], "apellido": words[1], "telefono": words[2]}})
#     return diccionarioMaestro

#################################################################################################################################################################################
#FASE 3 #FASE 3 #FASE 3 #FASE 3 #FASE 3 #FASE 3 #FASE 3 #FASE 3 #FASE 3 #FASE 3 #FASE 3 #FASE 3 #FASE 3 #FASE 3 #FASE 3 #FASE 3 #FASE 3 #FASE 3 #FASE 3 #FASE 3 #FASE 3 #FASE 3 #
#################################################################################################################################################################################
#FASE 3 #FASE 3 #FASE 3 #FASE 3 #FASE 3 #FASE 3 #FASE 3 #FASE 3 #FASE 3 #FASE 3 #FASE 3 #FASE 3 #FASE 3 #FASE 3 #FASE 3 #FASE 3 #FASE 3 #FASE 3 #FASE 3 #FASE 3 #FASE 3 #FASE 3 #
#################################################################################################################################################################################
#def documentacionDeLaFase3():
    ''' 
    Fase 3:
    ContactID: cada contacto debe estar guardado mediante un contactID (puede ser un numer
    correlativo o algo mas elaborado)

    1. callContact({contactID}): que recibiendo un ID de contacto pueda “llamar” a un contacto, 
    para llamar a un contacto basta con desplegar por 60 segundos o hasta que el usuario presione la letra “C”

        “Llamando a: Antonio Melgar
        Telefono: 777-777-777 ”

    2. msgContacts ({contactIDs}[]) : que reciba una lista de 1 o mas contact IDs (Nombre y Apellido) y que reciba un texto que 
    represente el mensaje que se desea enviar “To: Juan Guzman (55-555-555),Pablo Alvarez (33-333-333),Luis Fernandez (22-222-222)
    Msg: Hola solo queria saber si vendran al laboratorio" 

    3. addToFavorite({contactID}): este metodo debe de agregar el contacto que reciba a una nueva lista de favoritos. 
    (esta es una nueva lista con nuevos contactID)

    4. getFavoriteList() : metodo que despliega esta lista de contactos de una manera “pretty”

    5. removeFromFavorite({contactIDinFavorite}): que recibiendo el apellido y el nombre del contacto elimine ese contacto de la lista.
    Todos estos funciones deberan pertenecer a la fase 3 pero debera mostrar un sub-menu que

    muestre todas estas opciones, y la manera de interactuar con los contactos es de manera list &
    scroll. Es decir los contactos deben mostrarse :
    1. Haciendo un scroll y cada contacto debera tener un correlativo (1. Juan Guzman,555555 )
    2. Solo mostrando la lista con los contactos y un correlativo y elegir el numero de correlativ
    '''



def callContact8(contactID,diccionarioMaestro):
        try:
            if contactID in diccionarioMaestro:
                contactID = diccionarioMaestro[contactID]['nombre'] + ' ' + diccionarioMaestro[contactID]['apellido'] #se ingresa el ID para que llame a la persona que desea 
                Esthetics1()
                print("Llamando a: {}".format(contactID)) #imprime el nombre de la persona con el texto llamando a
                #print("Teléfono: {}".format)
                for restantes in range(60, 0, -1): #contador de en retroseso de 60 segundos 
                        sys.stdout.write("\r")
                        #sys.stdout.write("Llamando a: {}".format(nombre))
                        sys.stdout.write("{:2d} Segundos restantes".format(restantes)) #se utilizo sys,stdout porque se pueden combinar int y string
                        sys.stdout.flush()
                        time.sleep(1)
                sys.stdout.write("\rSe realizo la llamada con éxito!!            \n")
            else:
                print('\nEl contacto está mal escrito o no existe.')
        except KeyboardInterrupt:
                print("\nla llamada se cancelo")
                Esthetics1()


def msgContacts9(mensaje,contactsToSendTo,diccionarioMaestro ):
        listSplit = contactsToSendTo.split(',')
        verifiedSplit = []
        invalidSplit = []
        iteration1 = 0
        for items in listSplit:
            if listSplit[iteration1] in diccionarioMaestro:
                verifiedSplit.append(listSplit[iteration1])
            else:
                invalidSplit.append(listSplit[iteration1])
            iteration1 = iteration1 + 1


        
        if len(invalidSplit) != 0:
            print('Contacto(s) → {} ← parece(n) no existir en la lista de contactos'.format(', '.join(invalidSplit)))
            print("Porfavor asegúrese de haber escrito el contacto correctamente y que el contacto si exista en el directorio.")

        elif len(invalidSplit) == 0:
            print('To: {}'.format(', '.join(verifiedSplit)),' → ', mensaje)

        
def addFavoriteList10(favoriteContactAddition,favorites,diccionarioMaestro):
    listSplit = favoriteContactAddition.split(',')
    verifiedSplit = []
    invalidSplit = []
    iteration1 = 0
    for items in listSplit:
        if listSplit[iteration1] in diccionarioMaestro:
            verifiedSplit.append(listSplit[iteration1])
        else:
            invalidSplit.append(listSplit[iteration1])
        
        iteration1 = iteration1 + 1
    


    
    if len(invalidSplit) != 0:
        print('Contacto(s) → {} ← parece(n) no existir en la lista de contactos'.format(', '.join(invalidSplit)))
        print("Porfavor asegúrese de haber escrito el contacto correctamente y que el contacto si exista en el directorio.")

    elif len(invalidSplit) == 0:
        iteration2 = 0
        for n in verifiedSplit:
            favorites[verifiedSplit[iteration2]] = diccionarioMaestro[verifiedSplit[iteration2]]
            iteration2 = iteration2 + 1
        diccionarioMaestro['favorites'] = favorites
        print('Se a agregado → {} ← a favoritos.'.format(verifiedSplit))


def removeFromFavorites11(favoriteContactdelete,favorites,diccionarioMaestro):
    listSplit = favoriteContactdelete.split(',')
    verifiedSplit = []
    invalidSplit = []
    iteration1 = 0
    for items in listSplit:
        if listSplit[iteration1] in diccionarioMaestro:
            verifiedSplit.append(listSplit[iteration1])
        else:
            invalidSplit.append(listSplit[iteration1])
        
        iteration1 = iteration1 + 1

    print(verifiedSplit)
    
    if len(invalidSplit) != 0:
        print('Contacto(s) → {} ← parece(n) no existir en la lista de contactos'.format(', '.join(invalidSplit)))
        print("Porfavor asegúrese de haber escrito el contacto correctamente y que el contacto si exista en el directorio.")

    elif len(invalidSplit) == 0:
        iteration2 = 0
        for n in verifiedSplit:
            del diccionarioMaestro['favorites'][verifiedSplit[iteration2]]
            del favorites[verifiedSplit[iteration2]]
            iteration2 = iteration2 + 1
        print(', '.join(verifiedSplit))



#################################################################################################################################################################################
#FASE 4 #FASE 4 #FASE 4 #FASE 4 #FASE 4 #FASE 4 #FASE 4 #FASE 4 #FASE 4 #FASE 4 #FASE 4 #FASE 4 #FASE 4 #FASE 4 #FASE 4 #FASE 4 #FASE 4 #FASE 4 #FASE 4 #FASE 4 #FASE 4 #FASE 4 #
#################################################################################################################################################################################
#FASE 4 #FASE 4 #FASE 4 #FASE 4 #FASE 4 #FASE 4 #FASE 4 #FASE 4 #FASE 4 #FASE 4 #FASE 4 #FASE 4 #FASE 4 #FASE 4 #FASE 4 #FASE 4 #FASE 4 #FASE 4 #FASE 4 #FASE 4 #FASE 4 #FASE 4 #
#################################################################################################################################################################################
#def documentacionDeLaFase4():
    '''
    Fase 4:
    loadFromFile(externalFile), que reciba el nombre de un
    archivo del cual se leerán los contactos, su método debe ser failsafe, es decir si el archivo no
    existe no ejecutar nada y devolver un “error”
    El programa (CLI) debe pedir el full path del archivo “~/Downloads/contacts.txt”
    .txt, .csv, .lists, .contacts
    '''



def loadFromFile12(filename,diccionarioMaestro):
    words = readFile6(filename)
    iteration = 0
    for line in words:
        # for words in line:
        key = produceContactID2(words[iteration][0], words[iteration][1])
        diccionarioMaestro.update( {key : {"nombre": words[iteration][0], "apellido": words[iteration][1], "telefono": words[iteration][2]}})
        iteration = iteration + 1
    return diccionarioMaestro
    
# print(loadFromFile(filename,diccionarioMaestro))


#################################################################################################################################################################################
#FASE 6 #FASE 6 #FASE 6 #FASE 6 #FASE 6 #FASE 6 #FASE 6 #FASE 6 #FASE 6 #FASE 6 #FASE 6 #FASE 6 #FASE 6 #FASE 6 #FASE 6 #FASE 6 #FASE 6 #FASE 6 #FASE 6 #FASE 6 #FASE 6 #FASE 6 #
#################################################################################################################################################################################
#FASE 6 #FASE 6 #FASE 6 #FASE 6 #FASE 6 #FASE 6 #FASE 6 #FASE 6 #FASE 6 #FASE 6 #FASE 6 #FASE 6 #FASE 6 #FASE 6 #FASE 6 #FASE 6 #FASE 6 #FASE 6 #FASE 6 #FASE 6 #FASE 6 #FASE 6 #
#################################################################################################################################################################################
#def documentacionDeLaFase6():
    '''
    Fase 6
    Save to Web via HTTP methods, en lo visto en clase aprendimos GET y POST.
    El dia del proyecto se le proveera con una URL (por ejemplo: http://marcosapi.com/) a la cual
    usted debera: crear un contact list y obtener un contact list
    POST:
    - http://demo7862839.mockable.io/contacts?gid=100 usando el metodo POST debera
    exportar y crear su “current” contact list mediante un payload (data) que contenga su
    contact list en forma dictionary (JSON, ver ejemplo abajo)
    GET:
    - http://demo7862839.mockable.io/contacts?gid=100
    - gid=100 es el request parameter (query param) y es igual a 100, por que ese es mi fake
    gid.
    En ambos casos puede usar gid como query parameter o proveer un custom request header
    gid: HTTP
    _ID
    '''



def post13(gid,urlPost,diccionarioMaestro):
    #urlPost="https://reqres.in/api/users"#Metodo 1 Si desea que la url este ingresada pero solo se desea cambiar una vez

    urlPost=input("Ingrese la url con la desea utilizar el método POST:\n  ")#Metodo 2 Si desea que la url se ingrese
    gid = 0
    params = {'gid':gid}
    #Se ingresa el gid que es el valor

    #payload={'FirstName': 'Michael', 'LastName': 'Kirk', 'phone': '123123'}
    payload=diccionarioMaestro
    #la información (data) para subir

    postResponse=requests.post(urlPost, params = params, json=payload)
    dataPost=postResponse.json()
    print(postResponse)
    #imprime el status code
    print(dataPost)
    #imprime la data 

def get14(gid,urlGet,diccionarioMaestro):
    #urlGet="http://demo7862839.mockable.io/contacts?gid=100"#Metodo 1 Si desea que la url este ingresada pero solo se desea cambiar una vez

    
    params = {'gid':gid}
    #Se ingresa el gid que es el valor

    getResponse=requests.get(urlGet, params = params)
    dataGet=getResponse.json()
    print(getResponse)
    #imprime el status code
    print(dataGet)
    #imprime la data
    diccionarioMaestro = dataGet
    return diccionarioMaestro



# urlGet=input("Ingrese la url con la desea utilizar el metodo GET:\n  ")
# gid = input('Inserte Gid: → ')
# Get(23,urlGet,gid)
# Post(100)

#print(diccionarioMaestro)
# diccionarioMaestro = {}
# nombre = 'David'
# apellido = 'Corzo'
# telefono = 30177050
# confirmation = 'si'
# filename = 'InitialContacts.txt'
# key = 'davidcorzo'
# mensaje = 'Hola Que tal.'
# contactsToSendTo = 'davidcorzo'
# favoriteContactAddition = 'davidcorzo'
# favorites = {}
# favoriteContactdelete = 'davidcorzo'
# gid = 100
# urlPost = 'https://reqres.in/api/users'
# urlGet = 'https://reqres.in/api/users'
# contactID = produceContactID2(nombre,apellido)

# print('Funcion #1 Esthetics1 :  ',Esthetics1())
# Esthetics1()
# print('Funcion #2 produceContactID2 : ',produceContactID2(nombre,apellido))
# Esthetics1()
# print('Funcion #3 addContacts3 : ',addContacts3(nombre,apellido,telefono,diccionarioMaestro))
# Esthetics1()
# print('Funcion #4 listContacts4 : ',listContacts4(diccionarioMaestro))
# Esthetics1()
# print('Funcion #5 removeContact5 : ',removeContact5(confirmation,nombre,apellido,diccionarioMaestro))
# Esthetics1()
# print('Funcion #6 readFile6 : ',readFile6(filename))
# Esthetics1()
# # print('Funcion #7 addContactsFromTxt7 : ',addContactsFromTxt7(filename,diccionarioMaestro))
# Esthetics1()
# print('Funcion #8 callContact8 : ',callContact8(contactID,diccionarioMaestro))
# Esthetics1()
# print('Funcion #9 msgContacts9 : ',msgContacts9(mensaje, contactsToSendTo,diccionarioMaestro))
# Esthetics1()
# print('Funcion #10 addFavoriteList10 : ',addFavoriteList10(favoriteContactAddition,favorites,diccionarioMaestro))
# Esthetics1()
# print('Funcion #11 removeFromFavorites11 : ',removeFromFavorites11(favoriteContactdelete,favorites,diccionarioMaestro))
# Esthetics1()
# print('Funcion #12 loadFromFile12 : ',loadFromFile12(filename,diccionarioMaestro))
# Esthetics1()
# print('Funcion #13 post13 : ',post13(gid,urlPost,diccionarioMaestro))
# Esthetics1()
# print('Funcion #14 get14 : ',get14(gid,urlGet,diccionarioMaestro))
# Esthetics1()