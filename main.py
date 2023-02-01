import csv
import random
import numpy as np
from calcular_distancias import *

#Define o número de grupos.
k_centroides_aleatorios = int(input("Digite o número de grupos: "))
gerar_centroide = k_centroides_aleatorios
grupos = []
mudanca = []
novos_centros = []

#Escolhe os centroides aleatoriamente.
while gerar_centroide != 0:
    with open('kmeans.csv', 'r') as kmeans_csv:
        pontos = list(csv.reader(kmeans_csv))
        k_ponto_escolhido = pontos[random.randint(1, len(pontos))]
        pontos.remove(k_ponto_escolhido)
    gerar_centroide -=1

#Adiciona os centros escolhidos em centros.csv
    with open('centros.csv', 'a', newline='') as centros_escolhidos_csv:
        escrever_centro = csv.writer(centros_escolhidos_csv)
        escrever_centro.writerow(k_ponto_escolhido)

for value in range(k_centroides_aleatorios):
     grupos.append([])

#Onde a magia acontece
verificacao = False
ultimo_loop = True
while ultimo_loop:
    calcular_distancias(grupos)
    cont_1 = len(grupos)
    cont_2 = cont_1
    cont_3 = cont_2
    element = 0

    for value in range(cont_3):
        mudanca.append(len(grupos[element]))
        cont_3 -=1
        element +=1
    cont_3 = cont_1

    for value in cont_3:
        if grupos[cont_2-1] == mudanca[cont_2-1]:
            ultimo_loop = True
        else:
            ultimo_loop = False
            verificacao = True
        cont_2 -=1
        cont_3 -=1
    #Calcula a média dos grupos e definir os novos pontos centrais
        ##
    #Atribuir os novos centros a var grupos para próxima iteração
        grupos = novos_centros[:]
        while verificacao:
            calcular_distancias(grupos)
            cont_1 = len(grupos)
            cont_2 = cont_1
            cont_3 = cont_2
            element = 0

            for value in range(cont_3):
                mudanca.append(len(grupos[element]))
                cont_3 -=1
                element +=1
            cont_3 = cont_1

            for value in cont_3:
                if grupos[cont_2-1] == mudanca[cont_2-1]:
                    ultimo_loop = True
                else:
                    ultimo_loop = False
                    verificacao = False
                cont_2 -=1
                cont_3 -=1
            
            #Calcula a média dos grupos e definir os novos pontos centrais
                    ##
    #Atribuir os novos centros a var grupos para próxima iteração
        grupos = novos_centros[:]