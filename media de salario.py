import statistics

# Dados dos salários (em Reais)
empresa1 = [1000, 6000, 1200, 8000, 1400]
empresa2 = [5000, 4000, 3000, 2000, 7000]
empresa3 = [1200, 1300, 8000, 3000, 15000]
empresa4 = [1400, 1750, 2000, 4500, 5900]

empresas = {
    "Empresa 1": empresa1,
    "Empresa 2": empresa2,
    "Empresa 3": empresa3,
    "Empresa 4": empresa4
}

# Dicionário para armazenar os resultados da análise
resultados = {}

# Loop para calcular as métricas de cada empresa
for nome, salarios in empresas.items():
    
    # Média: Salário médio (soma/contagem)
    media_salarial = statistics.mean(salarios)
    
    # Mediana: Salário central quando os dados estão ordenados
    mediana_salarial = statistics.median(salarios)
    
    # Desvio Padrão: Medida de dispersão (o quão longe os salários estão da média)
    desvio_padrao = statistics.stdev(salarios)
    
    # Moda: O valor mais frequente. Ocorre um erro se não houver repetição.
    # Usamos try/except pois o conjunto de dados pode não ter moda.
    try:
        moda_salarial = statistics.mode(salarios)
    except statistics.StatisticsError:
        moda_salarial = "Não existe (todos únicos)"
        
    resultados[nome] = {
        "Média": f"R$ {media_salarial:,.2f}",
        "Mediana": f"R$ {mediana_salarial:,.2f}",
        "Moda": moda_salarial,
        "Desvio Padrão": f"R$ {desvio_padrao:,.2f}"
    }

# Imprime os resultados em formato de tabela
print("\n### Resultados da Análise Estatística de Salários ###")
print("-" * 75)
print(f"{'Empresa':<12} | {'Média':<12} | {'Mediana':<12} | {'Moda':<12} | {'Desvio Padrão':<16}")
print("-" * 75)
for nome, dados in resultados.items():
    print(f"{nome:<12} | {dados['Média']:<12} | {dados['Mediana']:<12} | {str(dados['Moda']):<12} | {dados['Desvio Padrão']:<16}")
print("-" * 75)