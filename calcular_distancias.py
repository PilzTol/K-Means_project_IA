import csv
import random
import numpy as np

def calcular_distancias():
    grupos = []
    with open('centros.csv', 'r') as a_centros_csv:
            a_centros = list(csv.reader(a_centros_csv))

    #Cria grupos vazios para adicionar os pontos(listas de listas).(quantidade de grupos = k)
    for value in range(len(a_centros)):
        grupos.append([])

    #Abre o arquivo "kmeans.csv" para calcular as distâncias de cada ponto.
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
        
        #Calcula a distância da amostra em relação a cada centro.
        for centro in centros:
            cont = 0

            #Conversão do tipo de dado.
            for element in centro:
                centro[cont] = float(element)
                cont +=1 
            #Remove a classe do centro caso ela exsita, (obs: essa condição é ativada só no primeiro ciclo).
            if len(centro) > 2:
                centro.remove(centro[2])

            #Remove a classe do ponto.
            copia_ponto = ponto[:]
            copia_ponto.remove(copia_ponto[2])
            distance = np.linalg.norm(np.array(copia_ponto) - np.array(centro))
            
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
                grupos[cont].append(ponto)    
                break
            cont +=1
            
    #Retorna os pontos agrupados.
    return grupos