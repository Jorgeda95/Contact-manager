

diccionarioMaestro = {
    'stevenwilson': {'nombre': "Steven",'apellido': "Wilson", 'telefono': "45656765"},
    'davidcorzo': {'nombre': 'David', 'apellido': 'Corzo', 'telefono': '30177050'},
    'jorgepineda':{'nombre': 'Jorge', 'apellido': 'Pineda', 'telefono': '23456895'},'favorites':{'davidcorzo': {'nombre': 'David', 'apellido': 'Corzo', 'telefono': '30177050'}}
}
favorites = {'davidcorzo': {'nombre': 'David', 'apellido': 'Corzo', 'telefono': '30177050'}}
favoriteContactDelete = input('¿Qué contacto desea eliminar de favoritos? (contactid) →')
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


removeFromFavorites(favoriteContactDelete,favorites)

print(diccionarioMaestro)
print(favorites)

    

# nombre = input('n')
# apellido = input('a')
# telefono = input('t')
# addContacts(nombre,apellido,telefono)