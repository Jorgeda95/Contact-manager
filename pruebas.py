
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

