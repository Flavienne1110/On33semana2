#Solicitar ao usuario digitar dois números
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

#Operações aritmeticas
soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2
divisaoInteira = num1 // num2
modulo = num1 % num2
potencia = num1 ** num2

#Exibir os resultados
print("\n Resultados das operações aritmeticas: ")
print("Soma: ", soma)
print("Subtração: ", subtracao)
print("Multiplicação: ", multiplicacao)
print("Divisão: ", divisao)
print("DivisãoInteira: ", divisaoInteira)
print("Módulo: ", modulo)
print("Potência: ", potencia)

# Comparações com operadores
print("\nResultados das operações de comparação: ")
print("Igualdade: ", num1 == num2)
print("Diferença: ", num1 != num2)
print("Maior: ", num1 > num2)
print("Maior ou igual: ", num1 >= num2)
print("Menor: ", num1 < num2)
print("Menor ou igual: ", num1 <= num2)

#Operadores de atribuição
print("\n Resultados dos Operadores de atribuição: ")
num1 += 5
print("num1 +=5: ", num1)
num2 /= 2
print("num2 num2 /= 2: ", num2)

#Verificar presença na lista de elementos  add f para formatar e as chaves
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
if num1 in lista_numeros:
    print(f"o número {num1} está na lista de números")
else:
    print(f"o número {num1} não está na lista de números")

#Compare a identidade de objetos 
x = [1, 2, 3]
y = [1, 2, 3]
z = x
print("\n Resultados das operações de identidade de objetos: ")
print("x is z: ", x is z) #Luiza é irmã gêmea de Luize, porém z é a Luiza ocupando o espaço Z
print("x is y: ", x is y) #Luize
print("x is not y: ", x is not y) #Luiza
