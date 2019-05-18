

import requests


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


diccionarioMaestro = {
    'stevenwilson': {'nombre': "Steven",'apellido': "Wilson", 'telefono': "45656765"},
    'davidcorzo': {'nombre': 'David', 'apellido': 'Corzo', 'telefono': '30177050'}

'''