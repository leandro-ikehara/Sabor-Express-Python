lista_de_numeros = [1,2,3,4,5,6,7,8,9,10]
lista_de_nomes = ['Leandro','Bruna','Marcella','Carla']
lista_de_anos = [1982,2024]

print('Percorrer itens da lista')
lista_de_numeros = [1,2,3,4,5,6,7,8,9,10]
for numero in lista_de_numeros:
    print(numero)

print('Soma de números ímpares')
soma_impares = 0
for i in range(1, 11, 2):
    soma_impares += i
print(soma_impares)

print('Imprimir números de 1 a 10 decrescente')
for i in range(10, 0, -1):
    print(i)

print('Tabuada interativa ')
numero_tabuada = int(input("Digite um número para a tabuada: "))
for i in range(1, 11):
    resultado = numero_tabuada * i
    print(f"{numero_tabuada} x {i} = {resultado}")

print('Soma dos elementos de uma lista ')
lista_numeros = [10, 5, 8, 3, 7]
soma = 0

try:
    for numero in lista_numeros:
        soma += numero
    print(f"Soma dos elementos: {soma}")
except Exception as e:
    print(f"Ocorreu um erro: {e}")

print('Solucionando lista vazia ')
lista_valores = [15, 20, 25, 30]
soma_valores = 0

try:
    for valor in lista_valores:
        soma_valores += valor
    media = soma_valores / len(lista_valores)
    print(f"Média dos valores: {media}")
except ZeroDivisionError:
    print("A lista está vazia, não é possível calcular a média.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")

