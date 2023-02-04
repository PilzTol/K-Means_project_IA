import csv
import random
import numpy as np
import matplotlib.pyplot as plt

def calcular_distancias(centros, pontos):
    grupos = [[] for _ in range(len(centros))]
    for ponto in pontos:
        ponto = [float(x) for x in ponto]
        distancias = [np.linalg.norm(np.array(ponto[:2]) - np.array(centro[:2])) for centro in centros]
        grupo_index = distancias.index(min(distancias))
        grupos[grupo_index].append(ponto)
    return grupos

k_centroides_aleatorios = int(input("Digite o número de grupos: "))
with open('kmeans.csv', 'r') as kmeans_csv:
    pontos = list(csv.reader(kmeans_csv))

centros = []
for _ in range(k_centroides_aleatorios):
    k_ponto_escolhido = pontos.pop(random.randint(0, len(pontos) - 1))
    centros.append([float(x) for x in k_ponto_escolhido])

verificacao = False
step = 0
while not verificacao:
    grupos = calcular_distancias(centros, pontos)
    novos_centros = []
    for grupo in grupos:
        novos_centros.append([sum(x)/len(x) for x in zip(*grupo)])
    if novos_centros == centros:
        verificacao = True
    else:
        centros = novos_centros

    cores = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
    for i in range(len(grupos)):
        x = [p[0] for p in grupos[i]]
        y = [p[1] for p in grupos[i]]
        plt.scatter(x, y, color=cores[i % len(cores)])
        plt.scatter(centros[i][0], centros[i][1], marker='x', color='black')
    plt.savefig(f'kmeans_step_{step}.png')
    plt.clf()
    step += 1

    for i in range(len(grupos)):
        print(f"Grupo {i + 1}: {len(grupos[i])} pontos")
