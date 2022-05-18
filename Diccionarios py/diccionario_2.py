dic= {'Mikel': 3, 'Ane': 8, 'Amaia': 12, 'Unai': 5, 'Jon': 8, 'Ainhoa': 7,'Maite': 5}
lista=[]
for k in dic:
    p=(dic[k]) 
    lista.append(p)
    dic2=set(lista)
    lista2=list(dic2)
print(lista2)

#Resultado: [3, 8, 12, 5, 7] 