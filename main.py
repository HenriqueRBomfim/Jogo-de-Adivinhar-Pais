#Importação de bibliotecas
import math
import random
import funcoes_henrique as fh
import Funcoes_eduardo_selber as fe
import BaseDePaises as base

#Declaração de Variáveis
base_normalizada = fh.normaliza(base.DADOS)
tentativas = 20

#Início do Jogo
print(" ============================\n|                            |\n| Bem-vindo ao Insper Países |\n|                            |")
print(" ==== Design de Software ==== \n\n Comandos:\n\n    dica       - entra no mercado de dicas\n    desisto    - desiste da rodada")
print("    inventario - exibe sua posição\n\nUm país foi escolhido, tente adivinhar!")

#Sorteando o país
resposta = fh.sorteia_pais(base_normalizada)

#Jogo

while tentativas > 0:
    print("Você tem {0} tentativa(s)".format(tentativas))
    palpite = input("Qual seu palpite? ")
    if palpite == 'dica':
        print('''Mercado de Dicas
----------------------------------------
1. Cor da bandeira  - custa 4 tentativas
2. Letra da capital - custa 3 tentativas
3. Área             - custa 6 tentativas
4. População        - custa 5 tentativas
5. Continente       - custa 7 tentativas
0. Sem dica
----------------------------------------''')
        opcao = int(input("Escolha sua opção [0|1|2|3|4|5]: "))
    if palpite == 'desisto':
        tentativas = 0
        print(resposta)
    if palpite == 'inventario':
        print("Inventário: ")
    tentativas -= 1