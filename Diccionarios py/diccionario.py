estudiante = {
    "nombre": "Iñaki Perurena",
    "edad": 30,
    "nota_media": 7.25,
    "repetidor" : False

 }

#edad=estudiante("edad") #forma 1
#edad=estudiante.get("edad") #forma 2
#print(edad)
#cambiar edad
"""
estudiante["edad"]=20
edad=estudiante.get("edad")
print(estudiante)
print(edad)
"""
#para insertar datos
estudiante.update({'institución':'universidad Ean'}) #forma 1
estudiante["Asignatura"]="Algoritmos" #forma 2
estudiante["edad"]=20
edad=estudiante.get("edad")
print(estudiante)
print(edad)
#para traer las claves
#print(estudiante.keys())
#Para traer los valores
#print(estudiante.values())
"""
#Para eliminar una llave del diccionario
estudiante.pop("edad") #<-necesita parámetros en el momento de usar pop. Elimina y tiene el valor
edad=estudiante.get("edad") #tiene el valor
print(estudiante) #antes de eliminarse devuelve el valor
"""
"""
#para buscar un dato en el diccionario
edad1=estudiante.pop("edad")
edad=estudiante.get("edad")
print(estudiante)
print(7.25 in estudiante.values()) #True
"""
"""
#Cuarta manera de concatenar
diccionario={'a':1,'b':2,'c':3}
for key, value in diccionario.items():#convierte las claves sin valores a una tupla
    print("El valor de %s is %d" % (key,value))
"""

edades = {
2 "Ane" : 22,
3 "Jokin" : 27,
4 "Aitor" : 15
5 }
6 del edades["Aitor"] #el del es para eliminar como el pop, pero no devuelve el valor antes.