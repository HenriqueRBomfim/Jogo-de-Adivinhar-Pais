#Importação de bibliotecas
from csv import DictReader
import math
import random
import funcoes_henrique as fh
import Funcoes_eduardo_selber as fe
import BaseDePaises as base

#Declaração de Variáveis
base_normalizada = fh.normaliza(base.DADOS)
lista_tds_paises=[]
for pais in base_normalizada:
    lista_tds_paises.append(pais)


tentativas = 20
conta_dica_1, conta_dica_2, conta_dica_3, conta_dica_4, conta_dica_5 = 0,0,0,0,0
letras=[]
lista_cores=[]
lista_cores_sorteadas=[]
populacao=0
contine=0
opcoes_dica="Escolha sua opção [0|1|2|3|4|5]: "
#Início do Jogo
print(" ============================\n|                            |\n| Bem-vindo ao Insper Países |\n|                            |")
print(" ==== Design de Software ==== \n\n Comandos:\n\n    dica       - entra no mercado de dicas\n    desisto    - desiste da rodada")
print("    inventario - exibe sua posição\n\nUm país foi escolhido, tente adivinhar!")

#Sorteando o país
resposta = fh.sorteia_pais(base_normalizada)
band=base_normalizada[resposta]['bandeira']
for cores,valores in base_normalizada[resposta]['bandeira'].items():
    if valores!=0 and cores!='outros':
        lista_cores.append(cores)



a=0
dicas_print=''
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
        opcao = int(input(opcoes_dica))
        if opcao == 1:
            if conta_dica_1 > 0:
                print("Opção inválida")
            else:
                conta_dica_1 = 1
                tentativas -= 4
                cor_sorteada=random.choice(lista_cores)
                lista_cores.remove(cor_sorteada)
                lista_cores_sorteadas.append(cor_sorteada)
                dicas_print+='-Cores da bandeira:{}\n'.format(lista_cores_sorteadas)

        if opcao == 2:
            if conta_dica_2 > 0:
                print("Opção inválida")
            else:
                conta_dica_2 = 1
                tentativas -= 3
                sorteada=fe.sorteia_letra(resposta,letras)
                letras.append(sorteada)
                dicas_print+='-Letras da capital:{}\n'.format(letras)
        if opcao == 3:
            if conta_dica_3 > 0:
                print("Opção inválida")
            else:
                conta_dica_3 = 1
                tentativas -= 6
                a=(base_normalizada[resposta]['area'])
                dicas_print+='-Aréa:{}km²\n'.format(a)
                opcoes_dica.replace('|3','')
        if opcao == 4:
            if conta_dica_4 > 0:
                print("Opção inválida")
            else:
                conta_dica_4 = 1
                tentativas -= 5
                popula=(base_normalizada[resposta]['populacao'])
                dicas_print+='População:{}\n'.format(popula)
                opcoes_dica.replace('|4','')
        if opcao == 5:
            if conta_dica_5 > 0:
                print("Opção inválida")
            else:
                contine=(base_normalizada[resposta]["continente"])
                conta_dica_5 = 1
                tentativas -= 7
                dicas_print+='-Continente:{}\n'.format(contine)
                opcoes_dica.replace('|5','')

        
        if opcao == 0:
            tentativas += 1
        print(dicas_print)    
    if palpite == 'desisto':
        tentativas = 0
        print(resposta)
    if palpite == 'inventario':
        print("Inventário: ")
    verificando_na_lista=fe.esta_na_lista(palpite,lista_tds_paises)
    if verificando_na_lista==False:
        print('País invalido')
    
    tentativas -= 1
 