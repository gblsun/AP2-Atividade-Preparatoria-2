#Import
import matplotlib.pyplot as plt

from test_time_heap_sort import (
    result_time_lista_10_Desordenado_hs,
    result_time_lista_25_Desordenado_hs,
    result_time_lista_50_Desordenado_hs,
    result_time_lista_100_Desordenado_hs,
    result_time_lista_1000_Desordenado_hs,
    result_time_lista_10_QuaseOrd_hs,
    result_time_lista_25_QuaseOrd_hs,
    result_time_lista_50_QuaseOrd_hs,
    result_time_lista_100_QuaseOrd_hs,
    result_time_lista_1000_QuaseOrd_hs,
    result_time_lista_10_InversamenteOrd_hs,
    result_time_lista_25_InversamenteOrd_hs,
    result_time_lista_50_InversamenteOrd_hs,
    result_time_lista_100_InversamenteOrd_hs,
    result_time_lista_1000_InversamenteOrd_hs,
)

tempos = {
    'Desordenada': {
        '10': result_time_lista_10_Desordenado_hs,
        '25': result_time_lista_25_Desordenado_hs,
        '50': result_time_lista_50_Desordenado_hs,
        '100': result_time_lista_100_Desordenado_hs,
        '1000': result_time_lista_1000_Desordenado_hs,
    },
    'Quase Ordenada': {
        '10': result_time_lista_10_QuaseOrd_hs,
        '25': result_time_lista_25_QuaseOrd_hs,
        '50': result_time_lista_50_QuaseOrd_hs,
        '100': result_time_lista_100_QuaseOrd_hs,
        '1000': result_time_lista_1000_QuaseOrd_hs,
    },
    'Inversamente Ordenada': {
        '10': result_time_lista_10_InversamenteOrd_hs,
        '25': result_time_lista_25_InversamenteOrd_hs,
        '50': result_time_lista_50_InversamenteOrd_hs,
        '100': result_time_lista_100_InversamenteOrd_hs,
        '1000': result_time_lista_1000_InversamenteOrd_hs,
    },
}

plt.figure(figsize=(10, 6))

for tipo, tempos_lista in tempos.items():
    plt.plot(tempos_lista.keys(), tempos_lista.values(), marker='o', label=tipo)

plt.title('Comparação de Algoritmos de Ordenação Heap Sort')
plt.xlabel('Tamanho da Lista')
plt.ylabel('Tempo de Execução (s)')
plt.legend()
plt.grid(True)
plt.xticks(list(tempos['Desordenada'].keys()))  
plt.tight_layout()

plt.show()