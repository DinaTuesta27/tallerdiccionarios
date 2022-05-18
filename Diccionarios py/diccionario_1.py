Ejemplo=[12, 23, 5, 12, 92, 5,12, 5, 29, 92, 64,23]
diccionario={}
for i in Ejemplo:
    a=Ejemplo.count(i) #para contar los elementos de la lista.
    diccionario.update({i:a})
print(diccionario)
