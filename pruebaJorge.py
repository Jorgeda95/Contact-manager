import sys, os

# from funcionesContactManager import *
# import requests



# favoriteContactDelete = 'davidcorzo'

favorites = {}
diccinario = {}
diccionarioMaestro = {}

# {'davidcorzo': {'FirstName': 'David', 'LastName': 'Corzo', 'Phone': '30177050'},
# 'stevenwilson':{'FirstName':'Steven','LastName':'Wilson','Phone': '12121212'},
# 'franciscomendez':{'FirstName':'Francisco','LastName':'Corzo','Phone':'30177050'},
# 'harrypotter':{'FirstName':'Harry','LastName':'Potter','Phone':'45784578'},
# 'JorgePineda':{'FirstName':'Jorge','LastName':'Pineda','Phone':'89568956'}
# }

# diccionarioMaestro = {}

# # 'franciscomendez':{'FirstName':'Francisco','LastName':'Corzo','Phone':'30177050'} #, 'favorites': {}
# # 'davidcorzo':{'nombre':'David','apellido':'Corzo','telefono':'30177050'}, 'favorites': {'davidcorzo': {'nombre': 'David', 'apellido': 'Corzo', 'telefono': '30177050'}}
# # removeFromFavorites11(favoriteContactDelete,favorites,diccionarioMaestro)

# def get14(gid,urlGet,diccionarioMaestro):
#     """Recibe contactos de un URL y los ingresa al diccionario"""
    

    
#     params = {'gid':gid}
#     #Se ingresa el gid que es el valor

#     getResponse=requests.get(urlGet, params = params)
#     dataGet=getResponse.json()
#     # print(getResponse)
#     #imprime el status code
#     # print(dataGet)
#     #imprime la data
#     diccionarioMaestro = dataGet
#     return diccionarioMaestro

# gid=100
# urlGet = "http://demo7862839.mockable.io/contacts?gid=100"

# diccionarioMaestrodeGet = get14(gid,urlGet,diccionarioMaestro)
# def procesarGET(diccionarioMaestrodeGet):
#     # iteration = 0
#     stringize = str(diccionarioMaestrodeGet)
#     a = stringize.replace('FirstName','nombre')
#     b = a.replace('LastName','apellido')
#     c = b.replace('Phone','telefono')
#     return c

# compatibleDictionaryL = procesarGET(diccionarioMaestrodeGet)

# def organizar(compatibleDictionary):
#     iteration = 0
#     for n in compatibleDictionaryL:
#         compatibleDictionary[iteration]


print('''Ingrese una opción: 
Para abrir un archivo en otro directorio "dir" 
Para abrir un archivo en este mismo directorio "file":''')
WhatToUse = input(' → ')
if WhatToUse == 'dir':
    directory = input('Directory: → ')

filename = input('Ingrese el nombre del archivo: → ')
def loadFromFilePruebas(WhatToUse,directory,filename,diccionarioMaestro):
    """Agrega contactos de un archivo externo al diccionario"""
    

    fpath = os.path.join(directory, filename)
    f = open(fpath)
    words = f.read()
    try:
        fpath = True
        print(words)
        words = words.split(',')
        fineWords = words.splitlines()
        print(fineWords)
    except:
        print("No existe ese directorio")
    
    iteration = 0
    for line in words:
        # for words in line:
        key = produceContactID2(fineWords[iteration][0], fineWords[iteration][1])
        print(key)
        diccionarioMaestro.update( {key : {"FirstName": fineWords[iteration][0], "LastName": fineWords[iteration][1], "Phone": fineWords[iteration][2]}})
        iteration = iteration + 1
        
    return diccionarioMaestro

print(loadFromFilePruebas(WhatToUse,directory,filename,diccionarioMaestro))