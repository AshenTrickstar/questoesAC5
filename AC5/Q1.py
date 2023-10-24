"""Questão 1"""

n = int(input("Informe um número: "))

def questao1(n):
    for x in range(1, n + 1):
        for y in range(1, x + 1):
            print(y, end=" ")
        print()

questao1(n)

