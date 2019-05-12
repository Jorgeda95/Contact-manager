import pprint
import colorama
import sys, traceback
import sys, time


##########################################################################################################################################################
#FUNCIONES #FUNCIONES #FUNCIONES #FUNCIONES #FUNCIONES #FUNCIONES #FUNCIONES #FUNCIONES #FUNCIONES #FUNCIONES #FUNCIONES #FUNCIONES #FUNCIONES #FUNCIONES 
##########################################################################################################################################################
#FUNCIONES #FUNCIONES #FUNCIONES #FUNCIONES #FUNCIONES #FUNCIONES #FUNCIONES #FUNCIONES #FUNCIONES #FUNCIONES #FUNCIONES #FUNCIONES #FUNCIONES #FUNCIONES 
##########################################################################################################################################################

def produceContactID(nombre,apellido):
    nombre = nombre.lower()
    apellido = apellido.lower()
    key=str(nombre) + str(apellido)
    return key


##########################################################################################################################################################
#VARIABLES GLOBALES #VARIABLES GLOBALES #VARIABLES GLOBALES #VARIABLES GLOBALES #VARIABLES GLOBALES #VARIABLES GLOBALES #VARIABLES GLOBALES #VARIABLES GLO
##########################################################################################################################################################
#VARIABLES GLOBALES #VARIABLES GLOBALES #VARIABLES GLOBALES #VARIABLES GLOBALES #VARIABLES GLOBALES #VARIABLES GLOBALES #VARIABLES GLOBALES #VARIABLES GLO
##########################################################################################################################################################
diccionarioMaestro = {}


##########################################################################################################################################################
#FASE #1 #FASE #1 #FASE #1 #FASE #1 #FASE #1 #FASE #1 #FASE #1 #FASE #1 #FASE #1 #FASE #1 #FASE #1 #FASE #1 #FASE #1 #FASE #1 #FASE #1 #FASE #1 #FASE #1 
##########################################################################################################################################################
#FASE #1 #FASE #1 #FASE #1 #FASE #1 #FASE #1 #FASE #1 #FASE #1 #FASE #1 #FASE #1 #FASE #1 #FASE #1 #FASE #1 #FASE #1 #FASE #1 #FASE #1 #FASE #1 #FASE #1 
##########################################################################################################################################################
'''
Fase 1
Usted debe de crear una estructura vacía sin ningún contacto que representara la “lista” (no
necesariamente es una lista ;) ) de contactos. Cada contacto sera representado por 3
“campos”: Nombre, Apellido y Telefono.
Debe crear métodos que permitan interactuar con los contactos:
1. addContact: el cual le pida al usuario Nombre, Apellido y Telefono y cree una estructura
contacto (Nombre, Apellido y Telefono) y agregar este nuevo contacto
2. listContacts: que devuelva de una manera “pretty” todos los contactos
3. removeContact: que recibiendo el “Nombre Apellido” del contacto elimine ese contacto
de la lista.
NOTA: podria utilizar una lista o un diccionario, si es una diccionario utilice de una manera
adecuada los keys del diccionario o mejor una lista de diccionarios (VEA EJEMPLO EN
GET/POST para una idea)
'''

def addContacts(nombre, apellido, telefono):
    key=str(nombre) + str(apellido)
    nestedDictionary = {'nombre':nombre,'apellido':apellido,'telefono':telefono}
    diccionarioMaestro[key] =[nestedDictionary]
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
    
##########################################################################################################################################################
#FASE #2 #FASE #2 #FASE #2 #FASE #2 #FASE #2 #FASE #2 #FASE #2 #FASE #2 #FASE #2 #FASE #2 #FASE #2 #FASE #2 #FASE #2 #FASE #2 #FASE #2 #FASE #2 #FASE #2 
##########################################################################################################################################################
#FASE #2 #FASE #2 #FASE #2 #FASE #2 #FASE #2 #FASE #2 #FASE #2 #FASE #2 #FASE #2 #FASE #2 #FASE #2 #FASE #2 #FASE #2 #FASE #2 #FASE #2 #FASE #2 #FASE #2 
##########################################################################################################################################################
'''
Fase 2
Al iniciar su programa, debe:
● Leer/cargar (automaticamente) los contactos de un archivo llamado InitialContacts.txt, si
y solo si el archivo existe en el mismo directorio que su programa.py
● Agregarlos a la “lista” que anteriormente estaba vacia , es decir ahora su lista ya va a
estar pre-inicializada
● Obviamente estos contactos deben ser ordenados dentro de la “lista” de contactos
El contenido del archivo podra ser de esta(s) manera(s):
James,Butt,504-621-8927
Josephine,Darakjy,856-264-4130
Mitsue,Tollner,773-573-6914
Recuerde que los contactos se clasifican y se ordenan por apellido, si el apellido no esta
presente el nombre dictara en que “Letra” alfabetica se pondra el contacto. Estos contactos
estaran en el archivo de una manera desordenada.
Nota: los contactos no pueden tener espacios, ejemplo: “ Nombre “=> “Nombre”
'''



##########################################################################################################################################################
#FASE #3 #FASE #3 #FASE #3 #FASE #3 #FASE #3 #FASE #3 #FASE #3 #FASE #3 #FASE #3 #FASE #3 #FASE #3 #FASE #3 #FASE #3 #FASE #3 #FASE #3 #FASE #3 #FASE #3 
##########################################################################################################################################################
#FASE #3 #FASE #3 #FASE #3 #FASE #3 #FASE #3 #FASE #3 #FASE #3 #FASE #3 #FASE #3 #FASE #3 #FASE #3 #FASE #3 #FASE #3 #FASE #3 #FASE #3 #FASE #3 #FASE #3 
##########################################################################################################################################################
'''
Fase 3
Mas interaccion con los contactos, debe implementar las siguientes funciones

ContactID: cada contacto debe estar guardado mediante un contactID (puede ser un numer
correlativo o algo mas elaborado)

1. Juan, Dominguez, 555555
2. Jose, Martinez, 44444
3. Maria, Gallardo, 33333

El contactID en este ejemplo es 1, 2,3

● callContact({contactID}): que recibiendo un ID de contacto pueda “llamar” a un contacto,
Para llamar a un contacto basta con desplegar por 60 segundos o hasta que el usuario
presione la letra “C”
“ Llamando a: Antonio Melgar
Telefono: 777-777-777 ”

● msgContacts ({contactIDs}[]) : que reciba una lista de 1 o mas contact IDs (Nombre y
Apellido) y que reciba un texto que represente el mensaje que se desea enviar
“ To: Juan Guzman (55-555-555),Pablo Alvarez (33-333-333),Luis Fernandez (22-222-222)
Msg: Hola solo queria saber si vendran al laboratorio “

● addToFavorite({contactID}): este metodo debe de agregar el contacto que reciba a una
nueva lista de favoritos. (esta es una nueva lista con nuevos contactID

● getFavoriteList() : metodo que despliega esta lista de contactos de una manera “pretty”

● removeFromFavorite({contactIDinFavorite}): que recibiendo el apellido y el nombre del
contacto elimine ese contacto de la lista.
Todos estos funciones deberan pertenecer a la fase 3 pero debera mostrar un sub-menu que
muestre todas estas opciones, y la manera de interactuar con los contactos es de manera list &
scroll. Es decir los contactos deben mostrarse :
1. Haciendo un scroll y cada contacto debera tener un correlativo (1. Juan Guzman,555555 )
2. Solo mostrando la lista con los contactos y un correlativo y elegir el numero de correlativo
'''


def ContactID(nombre,apellido):
    nombre = nombre.lower()
    apellido = apellido.lower()
    key=str(nombre) + str(apellido)
    return key



def callContact():
        try:
                nombre = input("Ingrese el contact ID: → ")
                print("Llamando a: {}".format(nombre))
                #print=input("Si desea cancelar la llamada presione la tecla C:  ")
                for restantes in range(60, 0, -1):
                        sys.stdout.write("\r")
                        #sys.stdout.write("Llamando a: {}".format(nombre))
                        sys.stdout.write("{:2d} Segundos restantes".format(restantes)) 
                        sys.stdout.flush()
                        time.sleep(1)
                sys.stdout.write("\rSe realizo la llamada con éxito!!            \n")
        except KeyboardInterrupt:
                print("\nla llamada se cancelo")



def msgContacts():
        pass



def addFavoriteList():
        pass



def removeFromFavorite():
        pass


##########################################################################################################################################################
#FASE #4 #FASE #4 #FASE #4 #FASE #4 #FASE #4 #FASE #4 #FASE #4 #FASE #4 #FASE #4 #FASE #4 #FASE #4 #FASE #4 #FASE #4 #FASE #4 #FASE #4 #FASE #4 #FASE #4 
##########################################################################################################################################################
#FASE #4 #FASE #4 #FASE #4 #FASE #4 #FASE #4 #FASE #4 #FASE #4 #FASE #4 #FASE #4 #FASE #4 #FASE #4 #FASE #4 #FASE #4 #FASE #4 #FASE #4 #FASE #4 #FASE #4 
##########################################################################################################################################################
'''
Fase 4
Implemente un metodo que se llame loadFromFile(externalFile), que reciba el nombre de un
archivo del cual se leeran los contactos, su metodo debe ser failsafe, es decir si el archivo no
existe no ejecutar nada y devolver un “error”
El programa (CLI) debe pedir el full path del archivo “~/Downloads/contacts.txt” y dentro del archivo el contenido debera lucir asi:

Juan,Diaz,123456
Jose,Miranda,1378978
Gabriela,Estrada,798456

Nota: ya tiene una funcion que hace algo similar verdad? (FASE 1), el archivo podria tener
cualquier extension: .txt, .csv, .lists, .contacts, solo asegurese de leer texto y que el contenido
del archivo sera como fue detallado, vea como ejemplo http://demo7862839.mockable.io/example.contacts
'''
def loadFromFile(externalFile):
        pass


##########################################################################################################################################################
#FASE #5 #FASE #5 #FASE #5 #FASE #5 #FASE #5 #FASE #5 #FASE #5 #FASE #5 #FASE #5 #FASE #5 #FASE #5 #FASE #5 #FASE #5 #FASE #5 #FASE #5 #FASE #5 #FASE #5 
##########################################################################################################################################################
#FASE #5 #FASE #5 #FASE #5 #FASE #5 #FASE #5 #FASE #5 #FASE #5 #FASE #5 #FASE #5 #FASE #5 #FASE #5 #FASE #5 #FASE #5 #FASE #5 #FASE #5 #FASE #5 #FASE #5 
##########################################################################################################################################################
'''
Fase 5
Cree un menú que permita elegir entre las siguientes opciones y que interactue con el usuario:
Usted debe ingeniar como pedir los contactos y como hacer wrap-around dentro del programa
Nota: observe que la imagen muestra “10” fases, no debe ser necesariamente asi, hay mas de
5 fases, aun que la ultima opcion si debe ser Exit.
'''
def menu():
        pass



##########################################################################################################################################################
#FASE #6 #FASE #6 #FASE #6 #FASE #6 #FASE #6 #FASE #6 #FASE #6 #FASE #6 #FASE #6 #FASE #6 #FASE #6 #FASE #6 #FASE #6 #FASE #6 #FASE #6 #FASE #6 #FASE #6 
##########################################################################################################################################################
#FASE #6 #FASE #6 #FASE #6 #FASE #6 #FASE #6 #FASE #6 #FASE #6 #FASE #6 #FASE #6 #FASE #6 #FASE #6 #FASE #6 #FASE #6 #FASE #6 #FASE #6 #FASE #6 #FASE #6 
##########################################################################################################################################################

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
gid: HTTP_ID

Ejemplo:http://demo7862839.mockable.io/contacts?gid=100 ( mi HTTP_ID: 100)
Los grupos tendran un identificador unico, (HTTP_ID), el HTTP_ID (int) dependera del orden
en que se inscriban ese dia, entonces asegurese de hacer esta variable facil de cambiar
'''



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



main()