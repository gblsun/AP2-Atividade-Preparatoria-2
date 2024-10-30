#Import
import matplotlib.pyplot as plt

from test_time_bubble_sort import (
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
    result_time_lista_1000_InversamenteOrd_bubble,
)

tempos = {
    'Desordenada': {
        '10': result_time_lista_10_Desordenado_bubble,
        '25': result_time_lista_25_Desordenado_bubble,
        '50': result_time_lista_50_Desordenado_bubble,
        '100': result_time_lista_100_Desordenado_bubble,
        '1000': result_time_lista_1000_Desordenado_bubble,
    },
    'Quase Ordenada': {
        '10': result_time_lista_10_QuaseOrd_bubble,
        '25': result_time_lista_25_QuaseOrd_bubble,
        '50': result_time_lista_50_QuaseOrd_bubble,
        '100': result_time_lista_100_QuaseOrd_bubble,
        '1000': result_time_lista_1000_QuaseOrd_bubble,
    },
    'Inversamente Ordenada': {
        '10': result_time_lista_10_InversamenteOrd_bubble,
        '25': result_time_lista_25_InversamenteOrd_bubble,
        '50': result_time_lista_50_InversamenteOrd_bubble,
        '100': result_time_lista_100_InversamenteOrd_bubble,
        '1000': result_time_lista_1000_InversamenteOrd_bubble,
    },
}

plt.figure(figsize=(10, 6))

for tipo, tempos_lista in tempos.items():
    plt.plot(tempos_lista.keys(), tempos_lista.values(), marker='o', label=tipo)

plt.title('Comparação de Algoritmos de Ordenação - Bubble Sort')
plt.xlabel('Tamanho da Lista')
plt.ylabel('Tempo de Execução (s)')
plt.legend()
plt.grid(True)
plt.xticks(list(tempos['Desordenada'].keys()))  # Adiciona as chaves como ticks
plt.tight_layout()

plt.show()