# ===============================================
# ATIVIDADES COM TRY E EXCEPT - PYTHON INICIANTE
# ===============================================

# -----------------------------------------------
# Exercício 1: Verificar se o usuário digitou um número inteiro
# -----------------------------------------------
print("=== Exercício 1 ===")

try:
    numero = int(input("Digite um número inteiro: "))
    print(f"Você digitou o número: {numero}")
except ValueError:
    print("Erro: Você não digitou um número inteiro válido!")

print("-" * 40)  # separador visual

# -----------------------------------------------
# Exercício 2: Divisão entre dois números
# -----------------------------------------------
print("=== Exercício 2 ===")

try:
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    resultado = a / b
    print(f"O resultado da divisão é: {resultado}")
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero!")
except ValueError:
    print("Erro: Você deve digitar apenas números!")

print("-" * 40)

# -----------------------------------------------
# Exercício 3: Acessar um elemento da lista por índice
# -----------------------------------------------
print("=== Exercício 3 ===")

lista = [10, 20, 30, 40, 50]
print(f"Lista atual: {lista}")

try:
    indice = int(input("Digite o índice que deseja acessar (0 a 4): "))
    print(f"O valor no índice {indice} é: {lista[indice]}")
except IndexError:
    print("Erro: Índice fora do intervalo da lista!")
except ValueError:
    print("Erro: Você deve digitar um número inteiro!")

print("-" * 40)

# -----------------------------------------------
# Mensagem final
# ----------------------------------------------


