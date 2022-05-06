def converte_milhas_para_km(distancia_mi): #coverttor de milhas para km
    distancia_km = 1.60934 * distancia_mi
    return distancia_km
milhas= 25
km= converte_milhas_para_km(milhas)
print(km)
