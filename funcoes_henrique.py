import random
import math
def normaliza(dicionario):
    paises_norm = {}
    for continente, paises in dicionario.items():
        for pais, dados in paises.items():
            paises_norm[pais] = dados
            for informacao, valor in dados.items():
                paises_norm[pais][informacao] = valor
            paises_norm[pais]["continente"] = continente
    return paises_norm

def sorteia_pais(paises):
    lista_de_paises = []
    for pais in paises.keys():
        lista_de_paises.append(pais)
    return random.choice(lista_de_paises)

def haversine(r, o1, l1, o2, l2):
    o1 = math.radians(o1)
    o2 = math.radians(o2)
    l1 = math.radians(l1)
    l2 = math.radians(l2)
    x = (math.sin((o2-o1)/2))**2
    y = (math.cos(o1))*(math.cos(o2))*((math.sin((l2-l1)/2))**2)
    z = math.sqrt(x+y)
    return 2*r*math.asin(z)

def adiciona_em_ordem(nome, distancia, lista):
    pais_novo = [nome, distancia]
    i = 0
    distancia2 = 0
    for pais in lista:
        if pais[1] > distancia2 and pais[1] < distancia:
            distancia2 = pais[1]
            i += 1
    if pais_novo not in lista:
        lista.insert(i, pais_novo)
    return lista

def coloca_ponto(distancia):
    string_dist = str(distancia)
    dist_caracteres = []
    for caractere in string_dist:
        dist_caracteres.append(caractere)
    distancia_pontuada = ''
    i = 0
    while i <= len(dist_caracteres):
        char = dist_caracteres[i]
        distancia_pontuada += char
        if i == -3: 
            ponto = '.'
            distancia_pontuada += ponto
    return distancia_pontuada