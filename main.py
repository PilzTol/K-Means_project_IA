import csv
import random
import numpy as np
from calcular_distancias import *

#Define o número de grupos.
k_centroides_aleatorios = int(input("Digite o número de grupos: "))
gerar_centroide = k_centroides_aleatorios
grupos = []
mudanca = []
cont_6 = 2

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
ftime = False
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
         
    for value in range(cont_3):
        mudanca.append(len(grupos[element]))
        cont_3 -=1
        element +=1
    cont_3 = cont_1

    if ftime == True:
        for value in range(cont_3):
            if len(grupos[cont_2]) != mudanca[len(mudanca)-cont_6]: #só falta mexer aqui, 
                ultimo_loop = True
            else:
                verificacao = True
            cont_2 +=1
            cont_3 -=1
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

    #Atribuir os novos centros a var grupos para próxima iteração
    with open('centros.csv', 'w', newline='') as novos_centros_csv:
        for element in novos_centros:
            writer = csv.writer(novos_centros_csv)
            writer.writerow(element)  
    with open("temporario.csv", "w") as limpar_arquivo:
        limpar_arquivo.truncate() 

    ftime = True
    while verificacao:
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

        for value in range(cont_3):
            mudanca.append(len(grupos[element]))
            cont_3 -=1
            element +=1
        cont_3 = cont_1
        for value in range(cont_3):
            if len(grupos[cont_2]) != mudanca[len(mudanca)-cont_6]: 
                ultimo_loop = True
            else:
                ultimo_loop = False
                verificacao = False
            cont_2 +=1
            cont_3 -=1

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

        #Atribuir os novos centros a var grupos para próxima iteração
        with open('centros.csv', 'w', newline='') as novos_centros_csv:
            for element in novos_centros:
                writer = csv.writer(novos_centros_csv)
                writer.writerow(element)  
        with open("temporario.csv", "w") as limpar_arquivo:
            limpar_arquivo.truncate() 