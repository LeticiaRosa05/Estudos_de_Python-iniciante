#34. Crie uma função que receba uma lista e retorne o número de elementos repetidos
import random as r
lista = []
rep = []
i = 0
while i < 10:
    n = r.randint(0, 100)
    lista.append(n)
    i += 1

for i in lista:
    for j in lista:
        #j += 1
        if i == j:
            rep.append(i)

if len(rep) < 1:
    print(f"Não há números repetidos na lista {lista}")
else:
    print(f"Na lista {lista}, há {len(rep)} números repetidos. Sendo eles: {rep}")