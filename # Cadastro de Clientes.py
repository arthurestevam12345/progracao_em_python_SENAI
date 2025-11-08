# Cadastro de Clientes
cliente1_nome = input("Digite o nome do cliente 1: ")
cliente1_idade = int(input("Digite a idade do cliente 1: "))

cliente2_nome = input("Digite o nome do cliente 2: ")
cliente2_idade = int(input("Digite a idade do cliente 2: "))

cliente3_nome = input("Digite o nome do cliente 3: ")
cliente3_idade = int(input("Digite a idade do cliente 3: "))

# Reservas de Quartos
# Preços dos quartos
preco_simples = 100
preco_duplo = 150
preco_luxo = 250

# Escolha de quartos para cada cliente
print("\nEscolha o quarto para cada cliente:")
# Cliente 1
quarto_cliente1 = input(f"{cliente1_nome}, escolha o quarto (Simples, Duplo, Luxo): ").strip().lower()
if quarto_cliente1 == "simples":
    preco_cliente1 = preco_simples
elif quarto_cliente1 == "duplo":
    preco_cliente1 = preco_duplo
elif quarto_cliente1 == "luxo":
    preco_cliente1 = preco_luxo
else:
    print("Escolha inválida! O preço do quarto será 0.")
    preco_cliente1 = 0

# Cliente 2
quarto_cliente2 = input(f"{cliente2_nome}, escolha o quarto (Simples, Duplo, Luxo): ").strip().lower()
if quarto_cliente2 == "simples":
    preco_cliente2 = preco_simples
elif quarto_cliente2 == "duplo":
    preco_cliente2 = preco_duplo
elif quarto_cliente2 == "luxo":
    preco_cliente2 = preco_luxo
else:
    print("Escolha inválida! O preço do quarto será 0.")
    preco_cliente2 = 0

# Cliente 3
quarto_cliente3 = input(f"{cliente3_nome}, escolha o quarto (Simples, Duplo, Luxo): ").strip().lower()
if quarto_cliente3 == "simples":
    preco_cliente3 = preco_simples
elif quarto_cliente3 == "duplo":
    preco_cliente3 = preco_duplo
elif quarto_cliente3 == "luxo":
    preco_cliente3 = preco_luxo
else:
    print("Escolha inválida! O preço do quarto será 0.")
    preco_cliente3 = 0

# Cálculo de dias de estadia e valor total para cada cliente
# Cliente 1
dias_cliente1 = int(input(f"Quantos dias {cliente1_nome} ficará no hotel? "))
valor_cliente1 = preco_cliente1 * dias_cliente1

# Cliente 2
dias_cliente2 = int(input(f"Quantos dias {cliente2_nome} ficará no hotel? "))
valor_cliente2 = preco_cliente2 * dias_cliente2

# Cliente 3
dias_cliente3 = int(input(f"Quantos dias {cliente3_nome} ficará no hotel? "))
valor_cliente3 = preco_cliente3 * dias_cliente3

# Exibição dos valores totais a serem pagos por cada cliente
print("\nResumo da reserva:")

print(f"\n{cliente1_nome} ficará {dias_cliente1} dias no quarto {quarto_cliente1.capitalize()} com o valor total de R$ {valor_cliente1:.2f}")
print(f"{cliente2_nome} ficará {dias_cliente2} dias no quarto {quarto_cliente2.capitalize()} com o valor total de R$ {valor_cliente2:.2f}")
print(f"{cliente3_nome} ficará {dias_cliente3} dias no quarto {quarto_cliente3.capitalize()} com o valor total de R$ {valor_cliente3:.2f}")
