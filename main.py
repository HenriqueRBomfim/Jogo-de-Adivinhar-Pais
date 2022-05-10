#import math
#import random
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

#Jogo

#while tentativas > 0:
    #print("Você tem {0} tentativa(s)".format(tentativas))
    #palpite = input("Qual seu palpite? ")
    #tentativas -= 1