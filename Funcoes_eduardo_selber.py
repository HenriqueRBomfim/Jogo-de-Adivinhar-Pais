import random
 
def sorteia_letra(plv,res):
    letras=[]
    c=['.', ',', '-', ';', ' ']
    for i in plv:
        if i.lower() not in c and i.lower() not in res:
            letras.append(i.lower())
    if len(letras)==0:
        return ''
    
    return random.choice(letras)
def esta_na_lista(nome,lista):
    for i in lista:
        if i[0]==nome:
            return True
    return False
def adiciona_em_ordem(nome,distancia,lista):
    combinado=[nome,distancia]
    c=0
    if len(lista)==0:
        lista.append(combinado)
        return lista
    for i in lista:

        if i[1]>distancia and i[0] not in lista:
            lista.insert(c,combinado)
            return lista 

        c+=1
    if nome not in lista:
        lista.append(combinado) 
        return lista
    return lista