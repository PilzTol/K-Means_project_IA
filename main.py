import csv
import random
import numpy as np

#Define o número de grupos.
k_centroides_aleatorios = int(input("Digite o número de grupos: "))
gerar_centroide = k_centroides_aleatorios
grupos = []

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
lol=1
while lol !=0:
    #Abre o arquivo "kmeans.csv" para calcular as distâncias.
    with open('kmeans.csv', 'r') as kmeans_csv:
        pontos = list(csv.reader(kmeans_csv))    
    
    #Itera cada amostra em "kmeans.csv".
    for ponto in pontos:
        cont = 0
        distancia_min = 0

        #Limpa o arquivo distância para próxima iteração
        with open("distancias.csv", "w") as limpar_arquivo:
            limpar_arquivo.truncate()
        #Converte o tipo de dado das amostras.
        for element in ponto:
            ponto[cont] = float(element)
            cont +=1

        #Abre o arquivo centros.csv para calcular a distância entre a amostra e cada centro.
        with open('centros.csv', 'r') as centros_csv:
            centros = list(csv.reader(centros_csv))
        
        for centro in centros:
            cont = 0
            for element in centro:
                centro[cont] = float(element)
                cont +=1 
            distance = np.linalg.norm(np.array(ponto) - np.array(centro))
            #Abre o arquivo distancias para salvar as distancias entre a amostra e cada centro.
            with open('distancias.csv', 'a', newline='') as distancias_csv:
                escrever_distancia = csv.writer(distancias_csv)
                escrever_distancia.writerow([distance])

        #Compara as distancias e adiciona o ponto em um grupo.
        with open('distancias.csv', 'r') as distancias_csv:
            distance = list(csv.reader(distancias_csv))
        distancia_min = distance[0]

        for element in distance:
            if element < distancia_min:
                distancia_min = element
        cont = 0
        for element in distance: 
            if element == distancia_min:
                grupos[cont].append(element)    
                break
            cont +=1
    lol -=1