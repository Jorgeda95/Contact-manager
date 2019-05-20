# from funcionesContactManager import *
import requests



favoriteContactDelete = 'davidcorzo'

favorites = {'davidcorzo': {'nombre': 'David', 'apellido': 'Corzo', 'telefono': '30177050'},'stevenwilson':{'nombre':'Steven','apellido':'Wilson','telefono': '12121212'}}
diccinario = {}
diccionarioMaestro = {}
# 'davidcorzo':{'nombre':'David','apellido':'Corzo','telefono':'30177050'}, 'favorites': {}
# 'davidcorzo':{'nombre':'David','apellido':'Corzo','telefono':'30177050'}, 'favorites': {'davidcorzo': {'nombre': 'David', 'apellido': 'Corzo', 'telefono': '30177050'}}
# removeFromFavorites11(favoriteContactDelete,favorites,diccionarioMaestro)

def get14(gid,urlGet,diccionarioMaestro):
    """Recibe contactos de un URL y los ingresa al diccionario"""
    #urlGet="http://demo7862839.mockable.io/contacts?gid=100"#Metodo 1 Si desea que la url este ingresada pero solo se desea cambiar una vez

    
    params = {'gid':gid}
    #Se ingresa el gid que es el valor

    getResponse=requests.get(urlGet, params = params)
    dataGet=getResponse.json()
    # print(getResponse)
    #imprime el status code
    # print(dataGet)
    #imprime la data
    diccionarioMaestro = dataGet
    return diccionarioMaestro

gid=100
urlGet = "http://demo7862839.mockable.io/contacts?gid=100"

diccionarioMaestrodeGet = get14(gid,urlGet,diccionarioMaestro)
def procesarGET(diccionarioMaestrodeGet):
    # iteration = 0
    stringize = str(diccionarioMaestrodeGet)
    a = stringize.replace('FirstName','nombre')
    b = a.replace('LastName','apellido')
    c = b.replace('Phone','telefono')
    return c

compatibleDictionaryL = procesarGET(diccionarioMaestrodeGet)

# def organizar(compatibleDictionary):
#     iteration = 0
#     for n in compatibleDictionaryL:
#         compatibleDictionary[iteration]
