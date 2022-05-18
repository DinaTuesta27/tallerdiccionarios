lista=[1,34,54,767,2,3,4,5,6,8,10,11]
#colecciones
#coleccion={} #se inicializa con llaves
#print("esta es la lista",lista)
#print("colección",coleccion) #Una colección intenta ordenar la lista de manera ascendente y no permiten duplicados
#las colecciones deben estar ordenadas
#Las colecciones no son mutables.
coleccion=set(lista) #convertimos la lista a una collección. (set:colección)
lista2=list(coleccion) #convierte la colección a lista
print(coleccion)
print(lista2)
