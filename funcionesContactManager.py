# import pprint
import colorama
import sys, traceback
import sys, time
import os
import csv
import requests




def Esthetics():
        print('__________________________________________________________________________________________________________________________________________________________________________________________________________________')

def produceContactID(nombre,apellido):
    nombre = nombre.lower()
    apellido = apellido.lower()
    key=str(nombre) + str(apellido)
    return key

# def pprint(dicc):
#     iteration = 0
#     for k,v in dicc:
#         dicc[iteration][key]
        

#  --------------------------------------------------------------------------------------------------------------------------------------------------------

""" Fase 1:
1. addContact: el cual le pida al usuario Nombre, Apellido y Telefono y cree una estructura contacto (Nombre, Apellido y Telefono) y agregar este nuevo contacto
2. listContacts: que devuelva de una manera “pretty” todos los contactos
3. removeContact: que recibiendo el “Nombre Apellido” del contacto elimine ese contacto de la lista. """


def addContacts(nombre, apellido, telefono):
    key=str(nombre) + str(apellido)
    nestedDictionary = {'nombre':nombre,'apellido':apellido,'telefono':telefono}
    diccionarioMaestro[key] = nestedDictionary
    print(diccionarioMaestro)

def listContacts():
    print("Contact List")
    for key in diccionarioMaestro:
        print("Nombre Del Contacto: {} {}, Teléfono: {}".format(diccionarioMaestro[key]['nombre'], diccionarioMaestro[key]['apellido'], diccionarioMaestro[key]['telefono']))

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
    
#  --------------------------------------------------------------------------------------------------------------------------------------------------------

""" Fase 2: 
1. Leer/cargar (automaticamente) los contactos de un archivo llamado InitialContacts.txt, si y solo si el archivo existe en el mismo directorio que su programa.py
2. Agregarlos a la “lista” que anteriormente estaba vacia , es decir ahora su lista ya va a estar pre-inicializada
3. Obviamente estos contactos deben ser ordenados dentro de la “lista” de contactos

Recuerde que los contactos se clasifican y se ordenan por apellido, si el apellido no esta
presente el nombre dictara en que “Letra” alfabetica se pondra el contacto. Estos contactos
estaran en el archivo de una manera desordenada."""

def readFile(filename):
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

def addContactsFromTxt(filename):
    lines=readFile(filename)
    # lines.strip("-")
    for line in lines:
        words = line.split(",")
        newContactID = words[0]+words[1]

        diccionarioMaestro.update( {newContactID : {"nombre": words[0], "apellido": words[1], "telefono": words[2]}})
    return diccionarioMaestro

#  --------------------------------------------------------------------------------------------------------------------------------------------------------

""" Fase 3:
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
2. Solo mostrando la lista con los contactos y un correlativo y elegir el numero de correlativ"""

def ContactID(nombre,apellido):
    nombre = nombre.lower()
    apellido = apellido.lower()
    key=str(nombre) + str(apellido)
    return key

def callContact():
        try:
                nombre = input("Ingrese el contact ID: → ") #se ingresa el ID para que llame a la persona que desea 
                print("Llamando a: {}".format(nombre)) #imprime el nombre de la persona con el texto llamando a
                for restantes in range(60, 0, -1): #contador de en retroseso de 60 segundos 
                        sys.stdout.write("\r")
                        #sys.stdout.write("Llamando a: {}".format(nombre))
                        sys.stdout.write("{:2d} Segundos restantes".format(restantes)) #se utilizo sys,stdout porque se pueden combinar int y string
                        sys.stdout.flush()
                        time.sleep(1)
                sys.stdout.write("\rSe realizo la llamada con éxito!!            \n")
        except KeyboardInterrupt:
                print("\nla llamada se cancelo")


def msgContacts(mensaje,contactsToSendTo):
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

        

 


def addFavoriteList(favoriteContactAddition,favorites):
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



def removeFromFavorites(favoriteContactdelete,favorites):
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
#  --------------------------------------------------------------------------------------------------------------------------------------------------------

""" Fase 4:
Implemente un metodo que se llame loadFromFile(externalFile), que reciba el nombre de un
archivo del cual se leerán los contactos, su método debe ser failsafe, es decir si el archivo no
existe no ejecutar nada y devolver un “error”
El programa (CLI) debe pedir el full path del archivo “~/Downloads/contacts.txt” y dentro del archivo el contenido debera lucir asi:

Juan,Diaz,123456
Jose,Miranda,1378978
Gabriela,Estrada,798456

Nota: ya tiene una funcion que hace algo similar verdad? (FASE 1), el archivo podría tener
cualquier extension: .txt, .csv, .lists, .contacts, solo asegurese de leer texto y que el contenido
del archivo sea como fue detallado, vea como ejemplo http://demo7862839.mockable.io/example.contacts
"""



filename = 'InitialContacts.txt'
#input('Ingrese el nombre del archivo: → ')

# def loadFromFile(externalFile):
    

#     data = []
#     file = open(filename, "r")
#     for line in file:
#         data.append(line)

#     data = ''.join(data)
#     data = data.split(',')

#     # fileToDict
     
        
#     #asignacion de valores a diccionario maestro
#     # iteration = 0
#     # for n in data:
diccionarioMaestro = {}

def loadFromFile(filename,diccionarioMaestro):
    words = readFile(filename)
    iteration = 0
    for line in words:
        # for words in line:
        key = produceContactID(words[iteration][0], words[iteration][1])
        diccionarioMaestro.update( {key : {"nombre": words[iteration][0], "apellido": words[iteration][1], "telefono": words[iteration][2]}})
        iteration = iteration + 1
    return diccionarioMaestro
    
# print(loadFromFile(filename,diccionarioMaestro))

#  --------------------------------------------------------------------------------------------------------------------------------------------------------

"""Fase 5:
Cree un menú que permita elegir entre las siguientes opciones y que interactue con el usuario:
Usted debe ingeniar como pedir los contactos y como hacer wrap-around dentro del programa
Nota: observe que la imagen muestra “10” fases, no debe ser necesariamente asi, hay mas de
5 fases, aun que la ultima opcion si debe ser Exit. """



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
#POST
def Post(string):
    urlPost="https://reqres.in/api/users"#Metodo 1 Si desea que la url este ingresada pero solo se desea cambiar una vez

    #urlPost=input("Ingrese la url con la desea utilizar el metodo POST:\n  ")#Metodo 2 Si desea que la url se ingrese

    params = {'gid':gid}
    #Se ingresa el gid que es el valor

    payload={'FirstName': 'Michael', 'LastName': 'Kirk', 'phone': '123123'}
    #payload=diccionarioMaestro
    #la información (data) para subir

    postResponse=requests.post(urlPost, params = params, json=payload)
    dataPost=postResponse.json()
    print(postResponse)
    #imprime el status code
    print(dataPost)
    #imprime la data 

def Get(string):
    urlGet="http://demo7862839.mockable.io/contacts?gid=100"#Metodo 1 Si desea que la url este ingresada pero solo se desea cambiar una vez

    #urlGet=input("Ingrese la url con la desea utilizar el metodo GET:\n  ")#Metodo 2 Si desea que la url se ingrese

    params = {'gid':gid}
    #Se ingresa el gid que es el valor

    getResponse=requests.get(urlGet, params = params)
    dataGet=getResponse.json()
    print(getResponse)
    #imprime el status code
    print(dataGet)
    #imprime la data 


def menuPG():
    print("Menu Fase 6:")
    print("Opción#1 POST")
    print("Opción#2 GET\n")

def opcionesPG(opcionPG=0):
	Opcion = int(input("Escoja una opción:\n"))
	return Opcion
menuFase6 = menuPG()

    opcionPG = opcionesPG()
#POST
if (opcionPG == 1):
        gid = input(str("Ingrese el gid para POST:\n"))
        Post(gid)
#GET
elif (opcionPG ==2):
        gid = input(str("Ingresa el gid para GET\n"))
        Get(gid)








#print(diccionarioMaestro)