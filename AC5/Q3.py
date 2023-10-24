"""Questão 3"""

try:
    num1 = int(input("Informe um número: "))
    num2 = int(input("Informe um divisor: "))
    resultado = num1 / num2
except ValueError:
    print("Os valores precisam ser inteiros")
except ZeroDivisionError:
    print("Não é possível dividir por 0")
finally:
    if resultado is not None:
        print(f"O resultado é {resultado:.2f}")