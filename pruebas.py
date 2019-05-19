<<<<<<< HEAD

import requests
import json


#POST
def Post(string):
    urlPost="https://reqres.in/api/users"#Metodo 1 Si desea que la url este ingresada pero solo se desea cambiar una vez

    #urlPost=input("Ingrese la url con la desea utilizar el metodo POST:\n  ")#Metodo 2 Si desea que la url se ingrese

    params = {'gid':gid}
    #Se ingresa el gid que es el valor

    payload={'FirstName': 'Michael', 'LastName': 'Kirk', 'phone': '123123'}
    #la información (data) para subir
=======
""" Fase 4:
Implemente un metodo que se llame loadFromFile(externalFile), que reciba el nombre de un
archivo del cual se leerán los contactos, su método debe ser failsafe, es decir si el archivo no
existe no ejecutar nada y devolver un “error”
El programa (CLI) debe pedir el full path del archivo “~/Downloads/contacts.txt” y dentro del archivo el contenido debera lucir asi:

Juan,Diaz,123456
Jose,Miranda,1378978
Gabriela,Estrada,798456

Nota: ya tiene una funcion que hace algo similar verdad? (FASE 1), el archivo podria tener
cualquier extension: .txt, .csv, .lists, .contacts, solo asegurese de leer texto y que el contenido
del archivo sea como fue detallado, vea como ejemplo http://demo7862839.mockable.io/example.contacts
"""
# import sys,os
# import csv


# filename = input('Ingrese el nombre del archivo: → ')

# def loadFromFile(externalFile):
    

#     data = []
#     file = open(filename, "r")
#     for line in file:
#         data.append(line)
>>>>>>> David

    postResponse=requests.post(urlPost, params = params, json=payload)
    dataPost=postResponse.json()
    print(postResponse)
    #imprime el status code
    print(dataPost)
    #imprime la data 

<<<<<<< HEAD
def Get(string):
    urlGet="http://demo7862839.mockable.io/contacts?gid=100"#Metodo 1 Si desea que la url este ingresada pero solo se desea cambiar una vez

    #urlGet=input("Ingrese la url con la desea utilizar el metodo GET:\n  ")#Metodo 2 Si desea que la url se ingrese
=======

#     data = ''.join(data)
#     data = data.split(',')
>>>>>>> David

    params = {'gid':gid}
    #Se ingresa el gid que es el valor

<<<<<<< HEAD
    getResponse=requests.get(urlGet, params = params)
    dataGet=getResponse.json()
    print(getResponse)
    #imprime el status code
    print(dataGet)
    #imprime la data 


def Menu():
    print("Menu Fase 6:")
    print("Opción#1 POST")
    print("Opción#2 GET\n")

def Opciones(OpcionMenu=0):
	Opcion = int(input("Escoja una opción:\n"))
	return Opcion
MenuPrincipal = Menu()

OpcionMenu = Opciones()
#POST

if (OpcionMenu == 1):
        gid = input(str("Ingrese el gid para POST:\n"))
        Post(gid)
#GET
elif (OpcionMenu ==2):
        gid = input(str("Ingresa el gid para GET\n"))
        Get(gid)



'''
#UrlConsulta=input("Ingrese la Url que desea utilizar:  ")
#UrlConsulta="http://demo7862839.mockable.io/contacts?gid=100"
url="http://demo7862839.mockable.io/contacts?gid=100"


UrlGet="http://demo7862839.mockable.io/contacts?gid=100"



gid = input("Ingrese el gid ")

params = {'gid':gid}

contact_list = [{'FirstName': 'Michael', 'LastName': 'Kirk', 'phone': '123123'}]

get_response =requests.get(url = url,params =params)

data_get = get_response.json()

r = requests.get(url)
print(r.json())
'''



#diccionarioMaestro = {
 #   'stevenwilson': {'nombre': "Steven",'apellido': "Wilson", 'telefono': "45656765"},
  #  'davidcorzo': {'nombre': 'David', 'apellido': 'Corzo', 'telefono': '30177050'}

=======
#     print(data)

# loadFromFile(filename)

# lst = ["aaaa8","bb8","ccc8","dddddd8"]
# print([s.strip('8') for s in lst]) # remove the 8 from the string borders
# print([s.replace('8', '') for s in lst]) # remove all the 8s 

import uuid

print(hash(str(uuid.uuid1())) % 1000)
>>>>>>> David
