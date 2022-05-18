usuarios = { 
 "iperurena": { 
 "nombre": "Iñaki", 
 "apellido": "Perurena", 
 "password": "123123" 
 }, 
 "fmuguruza": { 
 "nombre": "Fermín", 
 "apellido": "Muguruza", 
 "password": "654321" 
 }, 
 "aolaizola": { 
 "nombre": "Aimar", 
 "apellido": "Olaizola", 
 "password": "123456" 
 } 
 }
intentos=0
#us=str(input("Digite su usuario: "))
#pas=int(input("Digite su contraseña: "))

for key in usuarios: 
    t=usuarios[key]#busca los datos dentro del diccionario
    #print(t)

p=("iperurena" in usuarios) #True. El dato pertenece y existe al diccionario.
cl=("password" in t) #True. Los datos pertenecen y existen en los datos 
#print(p)
#print(cl)

while True:
    if(intentos==3):
        print("Demasiados intentos.")
        break
    us=str(input("Digite su usuario: "))
    pas=int(input("Digite su contraseña: "))
    if((us=="iperurena" and p==True) and (pas==123123 and cl==True)):
        pri= usuarios["iperurena"]
        pri.pop("password")
        print(pri)
        break
    elif((us=="fmuguruza" and p==True) and (pas==654321 and cl==True)):
        seg= usuarios["fmuguruza"]
        seg.pop("password")
        print(seg)
        break
    elif((us=="aolaizola" and p==True) and (pas==123456 and cl==True)):
        tre= usuarios["aolaizola"]
        tre.pop("password")
        print(tre)
        break
    else:
        intentos+=1
        print("Error al ingresar. Vuelva a intentarlo.")
        


