import matplotlib.pyplot as plt

# Tempos de execução para cada tamanho de lista
tempos = [
    result_time_lista_10_Desordenado_bubble,
    result_time_lista_25_Desordenado_bubble,
    result_time_lista_50_Desordenado_bubble,
    result_time_lista_100_Desordenado_bubble,
    result_time_lista_1000_Desordenado_bubble,
    
    result_time_lista_10_QuaseOrd_bubble,
    result_time_lista_25_QuaseOrd_bubble,
    result_time_lista_50_QuaseOrd_bubble,
    result_time_lista_100_QuaseOrd_bubble,
    result_time_lista_1000_QuaseOrd_bubble,
    
    result_time_lista_10_InversamenteOrd_bubble,
    result_time_lista_25_InversamenteOrd_bubble,
    result_time_lista_50_InversamenteOrd_bubble,
    result_time_lista_100_InversamenteOrd_bubble,
    result_time_lista_1000_InversamenteOrd_bubble
]

# Tamanhos das listas correspondentes
tamanhos = [
    10, 25, 50, 100, 1000,  # Desordenado
    10, 25, 50, 100, 1000,  # Quase ordenado
    10, 25, 50, 100, 1000   # Inversamente ordenado
]

# Nomes dos algoritmos e tipos de listas para a legenda
nomes = [
    "Bubble Sort (Desordenado)", "Bubble Sort (Desordenado)", "Bubble Sort (Desordenado)", "Bubble Sort (Desordenado)", "Bubble Sort (Desordenado)",
    "Bubble Sort (Quase Ordenado)", "Bubble Sort (Quase Ordenado)", "Bubble Sort (Quase Ordenado)", "Bubble Sort (Quase Ordenado)", "Bubble Sort (Quase Ordenado)",
    "Bubble Sort (Inversamente Ordenado)", "Bubble Sort (Inversamente Ordenado)", "Bubble Sort (Inversamente Ordenado)", "Bubble Sort (Inversamente Ordenado)", "Bubble Sort (Inversamente Ordenado)"
]

# Criando o gráfico
plt.figure(figsize=(12, 6))

# Plotando os pontos
for i in range(len(tamanhos)):
    plt.scatter(tamanhos[i], tempos[i], label=nomes[i], s=100)  # 's' define o tamanho do marcador

# Configurações do gráfico
plt.title('Tempo de Execução do Bubble Sort')
plt.xlabel('Tamanho da Lista')
plt.ylabel('Tempo (s)')
plt.xticks(tamanhos)
plt.legend()
plt.grid(True)

# Exibindo o gráfico
plt.show()
