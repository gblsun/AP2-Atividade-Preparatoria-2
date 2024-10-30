
import matplotlib.pyplot as plt
import numpy as np

from test_time_quick_sort import (
    result_time_lista_10_Desordenado_quick,
    result_time_lista_25_Desordenado_quick,
    result_time_lista_50_Desordenado_quick,
    result_time_lista_100_Desordenado_quick,
    result_time_lista_1000_Desordenado_quick,
    result_time_lista_10_QuaseOrd_quick,
    result_time_lista_25_QuaseOrd_quick,
    result_time_lista_50_QuaseOrd_quick,
    result_time_lista_100_QuaseOrd_quick,
    result_time_lista_1000_QuaseOrd_quick,
    result_time_lista_10_InversamenteOrd_quick,
    result_time_lista_25_InversamenteOrd_quick,
    result_time_lista_50_InversamenteOrd_quick,
    result_time_lista_100_InversamenteOrd_quick,
    result_time_lista_1000_InversamenteOrd_quick,
)

# Organizando os tempos em milissegundos
tempos = {
    'Desordenada': {
        '10': result_time_lista_10_Desordenado_quick ,
        '25': result_time_lista_25_Desordenado_quick ,
        '50': result_time_lista_50_Desordenado_quick ,
        '100': result_time_lista_100_Desordenado_quick ,
        '1000': result_time_lista_1000_Desordenado_quick ,
    },
    'Quase Ordenada': {
        '10': result_time_lista_10_QuaseOrd_quick * 1000,
        '25': result_time_lista_25_QuaseOrd_quick * 1000,
        '50': result_time_lista_50_QuaseOrd_quick * 1000,
        '100': result_time_lista_100_QuaseOrd_quick * 1000,
        '1000': result_time_lista_1000_QuaseOrd_quick * 1000,
    },
    'Inversamente Ordenada': {
        '10': result_time_lista_10_InversamenteOrd_quick * 1000,
        '25': result_time_lista_25_InversamenteOrd_quick * 1000,
        '50': result_time_lista_50_InversamenteOrd_quick * 1000,
        '100': result_time_lista_100_InversamenteOrd_quick * 1000,
        '1000': result_time_lista_1000_InversamenteOrd_quick * 1000,
    },
}

# Tamanhos das listas
tamanhos = ['10', '25', '50', '100', '1000']

# Criando o gráfico de barras horizontais
plt.figure(figsize=(10, 6))

# Definindo a largura das barras
bar_width = 0.2
y_positions = np.arange(len(tamanhos))

# Plotando as barras horizontais para cada tipo
for i, (tipo, tempos_lista) in enumerate(tempos.items()):
    plt.barh(y_positions + i * bar_width, list(tempos_lista.values()), bar_width, label=tipo)

# Adicionando detalhes ao gráfico
plt.title('Tempos de Execução do Quick Sort (em milissegundos)')
plt.xlabel('Tempo (milissegundos)')
plt.ylabel('Tamanho da Lista')
plt.yticks(y_positions + bar_width, tamanhos)  # Ticks com os tamanhos
plt.legend()
plt.grid(axis='x')
plt.tight_layout()

plt.show()
