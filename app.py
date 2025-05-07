'''Python'''
#Arrays (vetores/matrizes utilizando a biblioteca NumPy)
import numpy as np
 
#Criando um array Numpy unidimenaional a partir de uma lista array - np.array([1, 2, 3, 4, 5])
print("array:", array)

#Acessando elementos do array:
#-Indices começam em 0 
#-Indice negativo acessam a partir do final 
print("primeiro elemento:", array[0])
print("Ùltimo elemento:", array[-1])

#Slicing (Fatiamento) de arrays:
#-Sintaxe: [início:fim]
#-O indice final não é incluido
print("Elemento do indice 1 a 3 (exclusivo):", array[1:3])

#Listas (estruturas mutável de elementos)
#Criando uma lista básica 
my_list = [1, 2, 3, 4, 5]
print("Lista origonal:", my_list)

#Adicionando um elemento ao final da lista 
my_list.append(6)
print("Lista após adicionar 6:", my_list)

#Inserindo um elemento em posição específica:
#- 