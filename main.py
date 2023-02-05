import csv
import random
import numpy as np
from calcular_distancias import *
import matplotlib.pyplot as plt
import ast

#Define o número de grupos.
k_centroides_aleatorios = int(input("Digite o número de grupos: "))
gerar_centroide = k_centroides_aleatorios
grupos = []
mudanca = [0, 0]

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
ftime = False
step = 0
while ultimo_loop:
    novos_centros = []
    grupos = calcular_distancias()[:]
    cont_1 = len(grupos)
    cont_2 = 0
    cont_3 = cont_1
    element = 0

    cont_7 = 0
    for var in grupos:
        cont_7 += 1 
        print(f"Grupo {cont_7}:{len(var)}")

    if ftime == True:
        tudo_igual = 0
        for value in range(cont_3):
            if len(grupos[cont_2]) != mudanca[cont_2]:
                ultimo_loop = True
                tudo_igual = 1 
        if tudo_igual == 0:
            ultimo_loop = False

            cont_2 +=1
            cont_3 -=1
    cont_3 = cont_1
    mudanca = []    
    for value in range(cont_3):
        mudanca.append(len(grupos[element]))
        cont_3 -=1
        element +=1
    cont_3 = cont_1
             
    #Calcula a média dos grupos e definir os novos pontos centrais
    cont_4 = len(grupos[0][0])-1
    for grupo in grupos:
        cont_5 = 0
        sublista = []
        for value in range(cont_4):
            total = 0
            for element in grupo:
                total += float(element[cont_5])
            total = total/len(grupo)
            sublista.append(total)
            cont_5 += 1	
        with open('temporario.csv', 'a', newline='') as temporario_csv:
            escrever_sublista = csv.writer(temporario_csv)
            escrever_sublista.writerow(sublista)
        sublista = []

    with open('temporario.csv', 'r') as temporario_leitura_csv:
         novos_centros = list(csv.reader(temporario_leitura_csv))

    #Plotagem
    with open('centros.csv', 'r') as cores_centros_csv:
        marcar_centro = []
        for linha in cores_centros_csv:
            dados_linha = [float(dado) for dado in linha.strip().split(",")]
            marcar_centro.append(dados_linha)    

    cores = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
    for i in range(len(grupos)):
        x = [p[0] for p in grupos[i]]
        y = [p[1] for p in grupos[i]]
        plt.scatter(x, y, color=cores[i % len(cores)])
        plt.scatter(marcar_centro[i][0], marcar_centro[i][1], marker='x', color='black')
    plt.savefig(f'kmeans_step_{step}.png')
    plt.clf()
    step += 1

    #Atribuir os novos centros a var grupos para próxima iteração
    with open('centros.csv', 'w', newline='') as novos_centros_csv:
        for element in novos_centros:
            writer = csv.writer(novos_centros_csv)
            writer.writerow(element)  
    with open("temporario.csv", "w") as limpar_arquivo:
        limpar_arquivo.truncate() 

    ftime = True

print("end")