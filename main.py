#Importação de bibliotecas
from csv import DictReader
import math
from ntpath import join
import random
import funcoes_henrique as fh
import Funcoes_eduardo_selber as fe
import BaseDePaises as base
import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)

#Normalizando a base e listando todos os países
base_normalizada = fh.normaliza(base.DADOS)
#print(base_normalizada)
lista_tds_paises = []
for pais in base_normalizada:
    lista_tds_paises.append(pais)
#print(lista_tds_paises)

#Início do Jogo
print(" ============================\n|                            |\n| Bem-vindo ao Insper Países |\n|                            |")
print(" ==== Design de Software ==== \n\n Comandos:\n\n    dica       - entra no mercado de dicas\n    desisto    - desiste da rodada")
print("    inventario - exibe sua posição\n\nUm país foi escolhido, tente adivinhar!")

#Fazendo um def para rodar o jogo quantas vezes a pessoa quiser:
def jogo(num):
    #Declarando variáveis
    tentativas = 20
    tentativas_max = 20
    conta_dica_3, conta_dica_4, conta_dica_5 = 0,0,0
    acertou=0
    cores_sorteadas=''
    confirmacao = ''
    letra_not=''
    letras = []
    dicas_print_2={'cores':'0','letras':'0','area':'0','população':'0','continente':'0'}
    join_c=''
    join_l=''

    lista_cores = []
    lista_cores_sorteadas = []
    contine = 0
    ordem_paises_print=''
    ordem_paises_print2=''
    ordenando=[]
    dica_invalida=0
    mercado_dicas='''Mercado de Dicas
    ----------------------------------------
    \n1. Cor da bandeira  - custa 4 tentativas\n2. Letra da capital - custa 3 tentativas\n3. Área             - custa 6 tentativas\n4. População        - custa 5 tentativas\n5. Continente       - custa 7 tentativas
0. Sem dica\n
    ----------------------------------------'''
    mercado_dica_atualizado=''
    reg=0
    i=0
    opcoes_dica = "Escolha sua opção [0|1|2|3|4|5]: "
    opcoes_dica_atualizado=''
    #Sorteando o país
    resposta = fh.sorteia_pais(base_normalizada)
    latitude_resposta=base_normalizada[resposta]['geo']['latitude']
    longitude_resposta=base_normalizada[resposta]['geo']['longitude']
    band = base_normalizada[resposta]['bandeira']
    for cores,valores in base_normalizada[resposta]['bandeira'].items():
        if valores != 0 and cores != 'outras':
            lista_cores.append(cores)

    a=0
    dicas_print = ''

    #Jogo
    while tentativas > 0:
        if tentativas > 10:
            print("Você tem " + f"{Fore.CYAN}{Style.BRIGHT}{tentativas}{Fore.RESET}" + " tentativa(s)")
        if (tentativas > 5) and (tentativas < 11):
            print("Você tem " + f"{Fore.YELLOW}{Style.BRIGHT}{tentativas}{Fore.RESET}" + " tentativa(s)")
        if tentativas <= 5:
            print("Você tem " + f"{Fore.RED}{Style.BRIGHT}{tentativas}{Fore.RESET}" + " tentativa(s)")
        palpite = input("Qual seu palpite? ")
        if palpite == 'dica':
            print(mercado_dicas)
            opcao = str(input(opcoes_dica))
            while dica_invalida!=1:
                if opcao == '1':
                        tentativas -= 4
                        cor_sorteada = random.choice(lista_cores)
                        lista_cores.remove(cor_sorteada)

                        lista_cores_sorteadas.append(cor_sorteada)
                        join_c=','.join(lista_cores_sorteadas)
                        dicas_print_2['cores']=( '-Cores da bandeira:{}\n'.format(join_c))
                        tentativas+=1
                        dica_invalida=1
                if opcao == '2':
                        tentativas -= 3
                        sorteada = fe.sorteia_letra(resposta, letras)
                        letras.append(sorteada)
                        join_l=','.join(letras)
                        dicas_print_2['letras']=('-Letras da capital:{}\n'.format(join_l))
                        tentativas+=1
                        dica_invalida=1
                if opcao == '3':
                    if conta_dica_3 > 0:
                        print("Opção inválida")
                        tentativas+=1
                    else:
                        conta_dica_3 = 1
                        tentativas -= 6
                        a = base_normalizada[resposta]['area']
                        dicas_print_2['area']=( '-Área:{}km²\n'.format(a))
                        opcoes_dica_atualizado =opcoes_dica.replace('|3','')
                        mercado_dica_atualizado=mercado_dicas.replace('3. Área             - custa 6 tentativas\n','')
                        mercado_dicas=mercado_dica_atualizado
                        opcoes_dica=opcoes_dica_atualizado
                        tentativas+=1
                        dica_invalida=1
                if opcao == '4':
                    if conta_dica_4 > 0:
                        print("Opção inválida")
                        tentativas+=1
                    else:
                        conta_dica_4 = 1
                        tentativas -= 5
                        popula = base_normalizada[resposta]['populacao']
                        dicas_print_2['população']=('População:{}\n'.format(popula))
                        opcoes_dica_atualizado=opcoes_dica.replace('|4','')
                        mercado_dica_atualizado=mercado_dicas.replace(    '4. População        - custa 5 tentativas\n','')
                        mercado_dicas=mercado_dica_atualizado
                        opcoes_dica=opcoes_dica_atualizado
                        tentativas+=1
                        dica_invalida=1
                if opcao == '5':
                    if conta_dica_5 > 0:
                        print("Opção inválida")
                        tentativas+=1
                    else:
                        contine = base_normalizada[resposta]["continente"]
                        conta_dica_5 = 1
                        tentativas -= 7
                        dicas_print_2['continente']=('-Continente:{}\n'.format(contine))
                        opcoes_dica_atualizado=opcoes_dica.replace('|5','')
                        mercado_dica_atualizado=mercado_dicas.replace('5. Continente       - custa 7 tentativas\n','')
                        mercado_dicas=mercado_dica_atualizado
                        opcoes_dica=opcoes_dica_atualizado
                        tentativas+=1  
                        dica_invalida=1                 
                if opcao == '0':
                    tentativas += 1
                    dica_invalida=1
                if opcao!='0' and opcao!='1' and opcao!='2' and opcao!='3' and opcao!='4' and opcao!='5':
                    print('Opção inválida')
                    opcao = str(input(opcoes_dica))
                    dica_invalida=0
            dica_invalida=0
            dicas_print=''
            for v in dicas_print_2.values():
                if v!='0':
                    dicas_print+=v
            print('''Dicas:\n{}\nDistancias:\n{}'''.format(dicas_print,ordem_paises_print))    

        if palpite == 'desisto':
            confirmacao = input("Tem certeza que deseja desistir da rodada? [s|n] ")
            if confirmacao == 's':
                print(">>> Que deselegante desistir, o país era: {}".format(resposta))
                tentativas = 0
            if confirmacao == 'n':
                tentativas += 1

        if palpite == 'inventario':
            dicas_print=''
            for v in dicas_print_2.values():
                if v!='0':
                    dicas_print+=v
            print('''Dicas:\n{}\nDistancias:\n{}'''.format(dicas_print,ordem_paises_print)) 
            tentativas+=1  

        if palpite.lower() not in lista_tds_paises and palpite != 'desisto' and palpite!='dica' and palpite!='inventario':
            print('País invalido')
            tentativas+=1
        if palpite.lower() in lista_tds_paises:
            latitude_palpite=base_normalizada[palpite.lower()]['geo']['latitude']
            longitude_palpite=base_normalizada[palpite.lower()]['geo']['longitude']
            distancia = int(fh.haversine(base.EARTH_RADIUS,latitude_palpite,longitude_palpite,latitude_resposta,longitude_resposta))
            ordenando = fh.adiciona_em_ordem(palpite.lower(),distancia,ordenando)
            while i<len(ordenando):
                reg=ordenando[i]
                if reg[1] > 10000:
                    ordem_paises_print2+= Fore.LIGHTBLACK_EX + '  {}km -> {}\n'.format(reg[1],reg[0])
                elif reg[1] > 5000 and reg[1] <= 10000:
                    ordem_paises_print2+= Fore.MAGENTA + '  {}km -> {}\n'.format(reg[1],reg[0])
                elif reg[1] > 2000 and reg[1] <= 5000:
                    ordem_paises_print2+= Fore.RED + '  {}km -> {}\n'.format(reg[1],reg[0])
                elif reg[1] > 500 and reg[1] <= 2000:
                    ordem_paises_print2+= Fore.YELLOW + '  {}km -> {}\n'.format(reg[1],reg[0])
                elif reg[1] <= 500:
                    ordem_paises_print2+= Fore.LIGHTGREEN_EX + '  {}km -> {}\n'.format(reg[1],reg[0])
                i += 1
            i = 0
            ordem_paises_print=ordem_paises_print2
            ordem_paises_print2=''

            print('''Dicas:\n{}\nDistancias:\n{}'''.format(dicas_print,ordem_paises_print)) 
            dicas_print=''
            if palpite.lower()==resposta:
                print('***Parabéns voce acertou--após {} tentativas'.format(tentativas_max - tentativas))
                tentativas = 0
                acertou = 1
            
        tentativas -= 1
    if acertou == 0 and confirmacao == '':
        print('''>>> Você perdeu, o país era: {}'''.format(resposta))
    jogar_denovo = input("Jogar novamente? [s|n] ")
    if jogar_denovo == 's':
        jogo(1)
    elif jogar_denovo == 'n':
        print("\n\n\nAté a próxima!")

jogo(1)