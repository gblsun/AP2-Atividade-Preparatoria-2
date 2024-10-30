import matplotlib.pyplot as plt
import numpy as np

# Importando os tempos medidos em milissegundos
from test_time_selection_sort import (
    result_time_lista_10_Desordenado_selection,
    result_time_lista_25_Desordenado_selection,
    result_time_lista_50_Desordenado_selection,
    result_time_lista_100_Desordenado_selection,
    result_time_lista_1000_Desordenado_selection,
    result_time_lista_10_QuaseOrd_selection,
    result_time_lista_25_QuaseOrd_selection,
    result_time_lista_50_QuaseOrd_selection,
    result_time_lista_100_QuaseOrd_selection,
    result_time_lista_1000_QuaseOrd_selection,
    result_time_lista_10_InversamenteOrd_selection,
    result_time_lista_25_InversamenteOrd_selection,
    result_time_lista_50_InversamenteOrd_selection,
    result_time_lista_100_InversamenteOrd_selection,
    result_time_lista_1000_InversamenteOrd_selection,
)

tempos = {
    'Desordenada': {
        '10': result_time_lista_10_Desordenado_selection,
        '25': result_time_lista_25_Desordenado_selection,
        '50': result_time_lista_50_Desordenado_selection,
        '100': result_time_lista_100_Desordenado_selection,
        '1000': result_time_lista_1000_Desordenado_selection,
    },
    'Quase Ordenada': {
        '10': result_time_lista_10_QuaseOrd_selection,
        '25': result_time_lista_25_QuaseOrd_selection,
        '50': result_time_lista_50_QuaseOrd_selection,
        '100': result_time_lista_100_QuaseOrd_selection,
        '1000': result_time_lista_1000_QuaseOrd_selection,
    },
    'Inversamente Ordenada': {
        '10': result_time_lista_10_InversamenteOrd_selection,
        '25': result_time_lista_25_InversamenteOrd_selection,
        '50': result_time_lista_50_InversamenteOrd_selection,
        '100': result_time_lista_100_InversamenteOrd_selection,
        '1000': result_time_lista_1000_InversamenteOrd_selection,
    },
}

plt.figure(figsize=(10, 6))

# Definindo a largura das barras
largura = 0.2
posicoes = np.arange(len(tempos['Desordenada']))  # Posições no eixo Y

# Plotando as barras horizontais para cada tipo
for i, (tipo, tempos_lista) in enumerate(tempos.items()):
    plt.barh(posicoes + i * largura, list(tempos_lista.values()), largura, label=tipo)

# Adicionando detalhes ao gráfico
plt.title('Comparação de Algoritmos de Ordenação - Selection Sort')
plt.ylabel('Tamanho da Lista')
plt.xlabel('Tempo de Execução (ms)')
plt.yticks(posicoes + largura, list(tempos['Desordenada'].keys()))  # Ticks com os tamanhos
plt.legend()
plt.grid(axis='x')
plt.tight_layout()

plt.show()