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
#- Simtaxe: insert(índici, valor)
#- Deslocar elementos existentes para a direita 
my_list.insert(2, 7)
print("Lista após inserir 7 na posição 2:", my_list)

# Removando a primeira ocorrência de um elemento
print("Último elemento", array[-1])

my_list.remove(4)
print("Lista após remover o valor 4:", my_list)

#Tuplas (estruturas imutável de elementos)
#Criando uma tupla - usa parêntese ao invés de colchetes
my_tuple = (1, 2, 3, 4, 5)
print("Tuplas:", my_tuple)

#Acesso a elementos funciona igual ás listas 
print("Primeiro elemento da tupla", my_tuple[0])
print("Ùltimo elemento da tupla:", my_tuple[-1])

#Loops (estruturas de repetição)

#Loops for iterando sobre elemento de uma lista 
fruits = ["maça", "banana", "morango"]
print("Frutas na lista:")
for fruit in fruits:
    print(fruit)

#Loop while executando enquando condição é verdadeira
print("contagem de 0 a 4:")
1 = 0
while 1 < 5:
    print(i)
    1 += 1  #incrementa o contador 

#Loop for com acesso ao índice e elemento simultaniamente usando enumerate
print("Elemento da lista com seus índice:")
my_list = [1, 2, 3, 4, 5]   
for indice, elemento in enumerate(my_list):
    print(f"indice (indice): (elemento)")     