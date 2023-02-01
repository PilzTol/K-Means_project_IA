import csv
import random
import numpy as np
from calcular_distancias import *

#Define o número de grupos.
k_centroides_aleatorios = int(input("Digite o número de grupos: "))
gerar_centroide = k_centroides_aleatorios
grupos = []
mudanca = []
k= 1

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

ultimo_loop = True
while ultimo_loop:
    novos_grupos = calcular_distancias(grupos)
    cont_1 = len(novos_grupos)
    cont_2 = cont_1
    print(len(novos_grupos[0]))
    print(len(novos_grupos[1]))
    element = 0

    for value in cont_2:
        if novos_grupos[cont_2] == mudanca[cont_2]:
            ultimo_loop = False
        else:
            ultimo_loop = True
        cont_2 -=1

    if ultimo_loop == False:
        
    for value in range(cont_1):
        mudanca.append(len(novos_grupos[element]))
        cont_1 -=1
        element +=1
    k -=1
    cont_1 = 0 

    