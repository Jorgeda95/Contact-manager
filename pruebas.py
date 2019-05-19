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



#     data = ''.join(data)
#     data = data.split(',')


#     print(data)

# loadFromFile(filename)

# lst = ["aaaa8","bb8","ccc8","dddddd8"]
# print([s.strip('8') for s in lst]) # remove the 8 from the string borders
# print([s.replace('8', '') for s in lst]) # remove all the 8s 

# import uuid

# print(hash(str(uuid.uuid1())) % 1000)

import csv
f = open("IntialContacts.txt")
r = csv.reader(f)
print(r.next())