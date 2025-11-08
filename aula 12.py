#1=============================================================================
def comparar_par_impar(num1, num2):
    # Variáveis locais para armazenar se os números são pares ou ímpares
    resultado_num1 = "par" if num1 % 2 == 0 else "ímpar"
    resultado_num2 = "par" if num2 % 2 == 0 else "ímpar"
    
    # Comparando os resultados e exibindo a comparação
    if resultado_num1 == resultado_num2:
        print(f"Os dois números são {resultado_num1}s.")
    else:
        print(f"O primeiro número é {resultado_num1} e o segundo número é {resultado_num2}.")

# Testando a função
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

comparar_par_impar(num1, num2)

#2=============================================================================
def multiplicar_tres_numeros(num1, num2, num3):
    # Realiza a multiplicação dos três números
    resultado = num1 * num2 * num3
    return resultado

# Testando a função
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

# Chamando a função e mostrando o resultado
resultado_multiplicacao = multiplicar_tres_numeros(numero1, numero2, numero3)
print(f"O resultado da multiplicação é: {resultado_multiplicacao}")

#3=============================================================================
def elevar_numero(base, expoente):
    # Calcula o valor elevado
    resultado = base ** expoente
    return resultado

# Testando a função
base = float(input("Digite a base: "))
expoente = float(input("Digite o expoente: "))

# Chamando a função e mostrando o resultado
resultado_elevado = elevar_numero(base, expoente)
print(f"O resultado de {base} elevado a {expoente} é: {resultado_elevado}")

#4=============================================================================
def verificar_idade(idade):
    # Verifica se a idade digitada é 18
    if idade == 18:
        print("Parabéns! Você tem 18 anos!")
    else:
        print("A idade não é 18.")

# Testando a função
idade_usuario = int(input("Digite sua idade: "))

# Chamando a função para verificar a idade
verificar_idade(idade_usuario)

#5=============================================================================
from datetime import datetime

def calcular_idade(data_nascimento):
    # Obtém a data atual
    data_atual = datetime.now()
    
    # Calcula a diferença entre a data atual e a data de nascimento
    idade = data_atual.year - data_nascimento.year
    
    # Verifica se o aniversário já aconteceu neste ano
    if (data_atual.month, data_atual.day) < (data_nascimento.month, data_nascimento.day):
        idade -= 1  # Se não, subtrai 1 do resultado
    
    return idade

# Testando a função
data_nascimento_input = input("Digite sua data de nascimento (dd/mm/aaaa): ")

# Converte o input para um objeto de data (datetime)
data_nascimento = datetime.strptime(data_nascimento_input, "%d/%m/%Y")

# Calcula a idade chamando a função
idade = calcular_idade(data_nascimento)

# Exibe a idade
print(f"Sua idade é: {idade} anos.")

#6=============================================================================
def verificar_vitoria_brasil(copa):
    # Verifica se o Brasil ganhou alguma das Copas que o Brasil venceu
    if copa == 1998:
        return "Sim, o Brasil venceu a Copa do Mundo de 1998 na França!"
    elif copa == 2002:
        return "Sim, o Brasil venceu a Copa do Mundo de 2002 no Japão e Coreia!"
    else:
        return "O Brasil não venceu a Copa do Mundo em 1999, nem em outros anos mencionados."

# Testando a função
ano_copa = int(input("Digite o ano da Copa que você quer verificar: "))

# Chamando a função para verificar a vitória
resultado = verificar_vitoria_brasil(ano_copa)

# Exibindo o resultado
print(resultado)

#7=============================================================================
def cumprimentar_cliente():
    """Função para cumprimentar o cliente."""
    print("Bem-vindo ao Restaurante Python!")
    print("Hoje, temos as seguintes opções de pratos:")
    print("1. Salada")
    print("2. Macarronada")
    print("3. Sanduíche")
    print("4. Sorvete")
    print("5. Sair")
    
def restaurante():
    """Função principal do restaurante para escolher os pratos."""
    # Lista de opções de pratos
    opcoes = ["Salada", "Macarronada", "Sanduíche", "Sorvete"]
    
    # Loop para o cliente fazer suas escolhas
    while True:
        cumprimentar_cliente()  # Chama a função para cumprimentar e mostrar opções
        
        # Solicita a escolha do cliente
        try:
            escolha = int(input("Escolha uma opção (1-5): "))
            
            if escolha == 1:
                print(f"Você escolheu {opcoes[0]}. Bom apetite!")
            elif escolha == 2:
                print(f"Você escolheu {opcoes[1]}. Bom apetite!")
            elif escolha == 3:
                print(f"Você escolheu {opcoes[2]}. Bom apetite!")
            elif escolha == 4:
                print(f"Você escolheu {opcoes[3]}. Bom apetite!")
            elif escolha == 5:
                print("Obrigado por visitar nosso restaurante. Até logo!")
                break  # Encerra o loop e termina o programa
            else:
                print("Opção inválida. Por favor, escolha uma opção entre 1 e 5.")
        
        except ValueError:
            print("Por favor, insira um número válido entre 1 e 5.")
        
# Chama a função principal
restaurante()