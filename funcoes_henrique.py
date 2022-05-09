def normaliza(dicionario):
    paises_norm = {}
    for continente, paises in dicionario.items():
        for pais, dados in paises.items():
            paises_norm[pais] = dados
            for informacao, valor in dados.items():
                paises_norm[pais][informacao] = valor
            paises_norm[pais]["continente"] = continente
    return paises_norm