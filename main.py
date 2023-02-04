import csv
import random
import numpy as np
from calcular_distancias import *

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
verificacao = False
ultimo_loop = True
while ultimo_loop:
    novos_centros = []
    grupos = calcular_distancias()[:]
    cont_1 = len(grupos)
    cont_2 = cont_1
    cont_3 = cont_2
    element = 0

    for value in range(cont_3):
        mudanca.append(len(grupos[element]))
        cont_3 -=1
        element +=1
    cont_3 = cont_1

    for value in range(cont_3):
        if grupos[cont_2-1] == mudanca[cont_2-1]:
            ultimo_loop = True
        else:
            verificacao = True
        cont_2 -=1
        cont_3 -=1

    #Calcula a média dos grupos e definir os novos pontos centrais
    cont_4 = len(grupos[0][0])-1
    for grupo in grupos:
        for value in range(cont_4):
            total = 0
            sublista = []	
            for element in grupo:
                total += int(element[cont_4-1])
            total = total/len(grupo)
            sublista.append(total)
            with open('temporario.csv', 'a', newline='') as temporario_csv:
                escrever_sublista = csv.writer(temporario_csv)
                escrever_sublista.writerow(sublista)
            cont_4 -= 1
        with open('temporario.csv', 'r') as centros_csv:
            centros = list(csv.reader(centros_csv))
        novos_centros.append(centros) 
        with open("temporario.csv", "w") as limpar_arquivo:
            limpar_arquivo.truncate()

    #Atribuir os novos centros a var grupos para próxima iteração
    with open('centros.csv', 'w', newline='') as novos_centros_csv:
        writer = csv.writer(novos_centros_csv)
        writer.writerows(novos_centros)
    if True:
        so_para = "fechar o arquivo"

        while verificacao:
            novos_centros = []
            grupos = calcular_distancias()[:]
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
                    #Salva os grupos em um arquivo

                cont_2 -=1
                cont_3 -=1

            #Calcula a média dos grupos e definir os novos pontos centrais
            cont_4 = len(grupos[0][0])-1
            for grupo in grupos:
                for value in range(cont_4):
                    total = 0
                    sublista = []	
                    for element in grupo:
                        total += element[cont_4-1]
                    total = total/len(grupo)
                    sublista.append(total)
                    with open('temporario.csv', 'a', newline='') as temporario_csv:
                        escrever_sublista = csv.writer(temporario_csv)
                        escrever_sublista.writerow(sublista)
                    cont_4 -= 1
                #Novos tá recebendo as listas errado
                #Verificar o valor de grupos
                with open('temporario.csv', 'r') as centros_csv:
                    centros = list(csv.reader(centros_csv))
                novos_centros.append(centros) 
                with open("temporario.csv", "w") as limpar_arquivo:
                    limpar_arquivo.truncate()

            #Atualizar os centros para próxima iteração
            with open('centros.csv', 'w', newline='') as novos_centros_csv:
                writer = csv.writer(novos_centros_csv)
                writer.writerows(novos_centros)