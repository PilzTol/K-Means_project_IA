import csv
import random
import numpy as np
from algumnome import *

#Define o número de grupos.
k_centroides_aleatorios = int(input("Digite o número de grupos: "))
gerar_centroide = k_centroides_aleatorios
grupos = []
mudanca = []

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
while True:
    novos_grupos = kmeans(grupos)
    cont = len(novos_grupos)
    for value in range(cont-1):
        mudanca.append(len(novos_grupos[cont-1]))
        cont -=1
    