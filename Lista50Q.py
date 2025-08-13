#1. Escreva um algoritmo que exiba os números de 1 a 100
for i in range(0, 101):
    print(i)

#2. Crie uma função que receba um número e retorne se ele é par ou ímpar
num = int(input("Digite um número inteiro: "))
if num % 2 == 0:
    print("O número é par")
else:
    print("O número é ímpar")

#3. Escreva um programa que calcule o fatorial de um número fornecido pelo usuário
import math as m
num = int(input("Digite um número inteiro: "))
num = m.factorial(num)

print(f"O fatorial do número é: {num}")

#4. Crie uma função que receba dois números e retorne o maior entre eles
n1 = int(input("Digite um número inteiro: "))
n2 = int(input("Digite outro número inteiro: "))
maior = max(n1, n2)
print(f"O maior entre eles é: {maior}")

#5. Implemente um algoritmo para calcular a soma dos números pares entre 1 e 50
soma = 0
for i in range(0, 51):
    if i % 2 == 0:
        soma += i
        print(f"A soma é: {soma}")

#6. Escreva um programa que peça ao usuário uma palavra e exiba-a de trás para frente
p = input("Escreva uma palavra: ")
reverso = p[::-1]
print(f"Sua palavra, de trás para frente: {reverso}")

#7. Crie uma função que verifique se uma palavra é um palíndromo
p = input("Escreva uma palavra: ")
reverso = p[::-1]
if p == reverso:
    print("A palavra é um palíndromo!")
else:
    print("A palavra não é um palíndromo")

#8. Implemente um algoritmo que calcule a média de uma lista de números fornecida pelo usuário
nums = []
i = 0
while i < 5:
    n = int(input("Digite 5 números em sequência: "))
    nums.append(n)
    i += 1
media = sum(nums)/len(nums)
print(f"A média dos números é: {media}")

#9. Escreva um programa que exiba a tabuada de um número fornecido pelo usuário
i = 0
num = int(input("Digite um número para ser exibida sua tabuada: "))
while i <= 10:
    print(f"{i}x{num} = {num*i}")
    i += 1

#10. Crie um algoritmo para calcular o valor de uma sequência aritmética
pa = []
a = 0
i = 0
r = int(input("Digite a razão da PA: "))
while i < 10:
    a += r
    pa.append(a)
    i += 1
print(f"PA de razão {r} com 10 elementos: {pa}")

#11. Implemente uma função que receba uma lista e retorne o menor valor da lista
lista = []
i = 0
qtd = int(input("Quantidade de elementos que a lista vai ter: "))
while i < qtd:
    n = int(input("Digite os números em sequência: "))
    lista.append(n)
    i += 1
print(f"O menor valor da lista é: {min(lista)}")

#12. Escreva um algoritmo que determine se um número é primo
n = int(input("Digite um número: "))
if n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0:
    print("Não é primo")
else:
    print("É um número primo")

#13. Crie uma função que receba uma lista de números e retorne a soma dos números ímpares
lista = []
i = 0
j = 0
soma = 0
qtd = int(input("Quantidade de elementos que a lista vai ter: "))
while i < qtd:
    n = int(input(f"Número {i+1}: "))
    lista.append(n)
    i += 1
for n in lista:
    if n % 2 != 0:
        soma += n
print(f"A soma dos números ímpares é: {soma}")

#14. Implemente um programa que calcule a soma dos números de 1 a 100
soma = 0
for i in range(1, 101):
    soma += i
print(f"A soma de todos os números entre 0 e 100 é: {soma}")

#15. Escreva um programa que receba a idade de 10 pessoas e exiba a média das idades
idade = []
i = 0
while i < 10:
    n = int(input(f"Digite a idade da pessoa {i+1}: "))
    idade.append(n)
    i += 1
media = sum(idade)/len(idade)
print(f"A média das idades é: {media}")

#16. Crie uma função que receba três números e retorne o maior e o menor deles
lista = []
i = 0
while i < 3:
    n = int(input("Digite 3 números: "))
    lista.append(n)
    i += 1
print(f"O menor valor da lista é {min(lista)} e o maior é {max(lista)}")

#17. Implemente um programa que peça um número e exiba todos os divisores desse número
div = []
n = int(input("Digite um número: "))
i = n
while i <= n and i > 0:
    if n % i == 0:
        div.append(i)
        i -= 1
    i -= 1
print(f"Divisores de {n}: {div}")

#18. Escreva um algoritmo que conte quantas vogais existem em uma palavra
count = 0
p = input("Escreva uma palavra: ")
vogais = ['a','e','i','o','u','A','E','I','O','U']
for v in p:
    if v in vogais:
        count += 1
print(f"Na palavra '{p}' há {count} vogais")

#19. Crie uma função que gere uma lista de números aleatórios e retorne o maior e o menor valor
import random as r
lista = []
i = 0
qtd = int(input("Quantidade de números que a lista vair ter: "))
while i < qtd:
    n = r.randint(1, 100)
    lista.append(n)
    i += 1
print(f"O menor valor da lista é {min(lista)} e o maior é {max(lista)}, sendo a lista : {lista}")

#20. Implemente um programa que calcule o número de Fibonacci para um dado valor de entrada
num = int(input("Digite um número que não seja 0 ou 1: "))
fibo = [0,1]
i = 2
while i<= num:
    next_fibo = fibo[i-1] + fibo[i-2]
    fibo.append(next_fibo)
    i += 1
print(f"O número de Fibonacci gerado a partir de {num} é {next_fibo}, sendo a sequência: {fibo}")

#21. Escreva um programa que converta temperaturas de Celsius para Fahrenheit e vice-versa
temp = input("Digite\nF para Fahrenheit\nC para Celsius\n")
if temp == "F" or temp == "f":
    C = float(input("Temperatura em Celsius que deseja converter: "))
    fahrenheit = (C * 9/5) + 32
    print(f"{C} graus Celsius são {fahrenheit} graus Fahrenheit")
elif temp == "C" or temp == "c":
    F = float(input("Temperatura em Fahrenheit que deseja converter: "))
    celsius = (F - 32) * 5/9
    print(f"{F} graus Fahrenheit são {celsius} graus Celsius")

#22. Crie uma função que receba uma lista e retorne o segundo maior valor da lista
lista = []
i = 0
qtd = int(input("Quantidade de elementos que a lista vai ter: "))
while i < qtd:
    n = int(input(f"Número {i+1}: "))
    lista.append(n)
    i += 1
pMaior = max(lista)
lista.remove(pMaior)
print(f"O segundo maior número da lista é {max(lista)}, sendo o primeiro maior {pMaior}")

#23. Implemente um algoritmo que gere uma sequência de números de Fibonacci até um número fornecido pelo usuário
num = int(input("Digite um número limite para a sequência: "))
fibo = [0,1]
i = 0
count = 0
while i < 1:
    next_fibo = fibo[i-1] + fibo[i-2]
    fibo.append(next_fibo)
    count += 1
    if num in fibo:
        print(f"A sequência Fibonacci até a ocorrência do número {num} é {fibo}")
        i = 1
    elif count == 100:
        print("Esse número provavelmente não ocorre na sequência Fibonacci")
        i = 1

#24. Escreva um programa que simule o lançamento de dois dados e exiba a soma dos resultados
import random as r
lancamento1 = r.randint(1, 6)
lancamento2 = r.randint(1, 6)
soma = lancamento1 + lancamento2
print(f"Sendo {lancamento1} o resultado do primeiro lançamento e {lancamento2} o resultado do segundo, a soma deles é: {soma}")

#25. Crie uma função que receba uma string e remova todos os espaços em branco
frase = input("Escreva uma frase: ")
semEsp = frase.replace(" ", "")
print(f"Sua frase sem espaços em branco: {semEsp}")

#26. Implemente um algoritmo que simule um jogo de adivinhação de números
import random as r
import time as t
i = 5
print("Pense em um número de 0 a 10")
while i <= 5 and i > 0:
    print(f"{i}...")
    i -= 1
    t.sleep(1)
num = r.randint(0, 10)
perg = input(f"Você pensou em {num}?\n")
if perg.lower() == "sim" or perg.lower() == "s":
    print("Acertei!")
else:
    print("Que pena!")

#27. Escreva um programa que receba uma lista de números e exiba a média, o maior e o menor valor
lista = []
i = 0
qtd = int(input("Quantidade de números que a lista vair ter: "))
while i < qtd:
    n = int(input(f"Número {i+1}: "))
    lista.append(n)
    i += 1
media = sum(lista)/len(lista)
print(f"A média da lista é {media}, o menor valor é {min(lista)} e o maior é {max(lista)}")

#28. Crie uma função que receba um número e retorne sua representação binária
bits = []
n = int(input("Digite um número para ser convertido para binário: "))
while n > 0:
    bits.append(n%2)
    n = n // 2
bits.reverse()
binary = ''
for bit in bits:
    binary += str(bit)
print("O número em binário é igual a: ", binary)

#29. Implemente um algoritmo que inverta os valores de uma lista
import random as r
lista = []
i = 0
qtd = int(input("Quantidade de números que a lista vair ter: "))
while i < qtd:
    n = r.randint(1, 100)
    lista.append(n)
    i += 1
print(f"Lista normal: {lista}")
lista.reverse()
print(f"Lista ivertida: {lista}")

#30. Escreva um programa que calcule a soma dos dígitos de um número fornecido pelo usuário
n = int(input("Digite um número: "))
soma = 0
while n > 0:
    digito = n % 10
    soma += digito
    n //= 10
print(f"A soma dos algarismos é: {soma}")

#31. Crie uma função que gere um número aleatório e peça ao usuário para adivinhar
import random as r
import time as t
i = 5
num = r.randint(0, 10)
print("De 0 a 10, adivinhe o número em que estou pensado! Você tem 5 segundos")
while i <= 5 and i > 0:
    print(f"{i}...")
    i -= 1
    t.sleep(1)
n = int(input("Seu chute: "))
if n == num:
    print("Parabéns! Você acertou!")
else:
    print(f"Não foi dessa vez T-T\nO número era {num}")

#32. Implemente um algoritmo que converta um número binário para decimal
decimal = 0
potencia = 0
binario = input("Digite um número binário: ")
for digito in str(binario)[::-1]:
    digito = int(digito)
    decimal += digito * (2 ** potencia)
    potencia += 1
print(f"O número decimal equivalente é: {decimal}")

#33. Escreva um programa que leia duas listas de números e exiba a interseção entre elas
import random as r
lista1 = []
lista2 = []
intersecao = []
i = 0
while i < 5: #quantidade pequena pois é mais fácil de verificar quando não há interseção
    n = r.randint(0, 100)
    lista1.append(n)
    num = r.randint(0, 100)
    lista2.append(num)
    i += 1
for i in lista1:
    if i in lista2:
        intersecao.append(i)
if intersecao != []:
    print(f"Lista 1: {lista1}\nLista 2: {lista2}\nInterseção: {intersecao}")
else:
    print(f"Não há números que estejam em ambas as listas\nLista 1: {lista1}\nLista 2: {lista2}")










#35. Implemente um algoritmo que calcule a área de um círculo a partir do raio fornecido pelo usuário.
#36. Escreva um programa que peça ao usuário para inserir notas de alunos e calcule a média da turma.
#37. Crie uma função que receba uma string e retorne o número de caracteres que não são letras.
#38. Implemente um algoritmo que simule uma fila de banco, exibindo a ordem de atendimento.
#39. Escreva um programa que ordene uma lista de números fornecida pelo usuário.
#40. Crie uma função que receba uma string e substitua todas as vogais por "*"
vogais = ['a','e','i','o','u','A','E','I','O','U'] ##ERRO >> concertar
frase = input("Escreva uma frase: ")
def tirarVogal(frase):
    for v in frase:
        if v in vogais:
            v = "*"
    return frase
tirarVogal(frase)
print(f"Sua frase sem vogais: {tirarVogal(frase)}")

#41. Implemente um algoritmo que leia 5 números e exiba o maior valor.
#42. Escreva um programa que determine se um número é perfeito.
#43. Crie uma função que receba duas strings e verifique se são anagramas.
#44. Implemente um algoritmo que calcule o número de dias entre duas datas fornecidas pelo usuário
#45. Escreva um programa que receba o peso e altura de uma pessoa e calcule seu IMC.
#46. Crie uma função que gere a matriz identidade de ordem N.
#47. Implemente um algoritmo que simule um sistema de caixa eletrônico, com saques e depósitos
#48. Escreva um programa que peça ao usuário uma frase e conte o número de palavras.
#49. Crie uma função que receba uma lista de números e retorne o segundo menor valor
#50. Implemente um algoritmo que calcule o MMC de dois números fornecidos pelo usuário