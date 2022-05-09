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