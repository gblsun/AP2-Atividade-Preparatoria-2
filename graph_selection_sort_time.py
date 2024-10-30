#Import
import matplotlib.pyplot as plt

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

for tipo, tempos_lista in tempos.items():
    plt.plot(tempos_lista.keys(), tempos_lista.values(), marker='o', label=tipo)

plt.title('Comparação de Algoritmos de Ordenação - Selection Sort')
plt.xlabel('Tamanho da Lista')
plt.ylabel('Tempo de Execução (s)')
plt.legend()
plt.grid(True)
plt.xticks(list(tempos['Desordenada'].keys()))  # Adiciona as chaves como ticks
plt.tight_layout()

plt.show()