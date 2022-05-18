"""
from xml.dom.minidom import Notation

estudiantes = { 
 "1": { 
 "nombre": "Lorea", 
 "nota": 8 
 }, 
 "2": { 
 "nombre": "Markel", 
 "nota": "4.2" 
 }, 
 "3": { 
 "nombre": "Julen", 
 "nota": 6.5 
 } 
 } 
"""
import statistics
grupo={}
reprobados=[]
Aprobados=[]
todos=[]
for i in range(1,11):
    nom=str(input("Ingrese nombre: "))
    nota=float(input("Ingrese nota: "))
    grupo.update({i:{'nombre': nom,'nota': nota}})
    todos.append(nota)
    prom=sum(todos)/(len(todos))#suma todos los valores de la lista y los divide por la cantidad en la lista.
    if(nota>=60):
        Aprobados.append(nom)
    print(f"Los estudiantes aprobados son:{Aprobados}.")
    if(nota<60):
        reprobados.append(nom)
    print(f"Los no aprobados son:{reprobados}")
print(grupo)
print("El promedio del curso es:",prom)

"""

nota in grupo.values()
if(nota>=60):
    Aprobados.append(nom)
print(f"Los estudiantes aprobados son:{Aprobados}.")
if(nota<=60):
    reprobados.append(nom)
print(f"Los no aprobados son:{reprobados}")
"""
#diccionario
#nombre y Notation
#update
#Pedir los datos y nota
#10 estudiantes
#aprobados que sacan 6
#promedio