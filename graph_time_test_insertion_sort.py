#Import
import matplotlib.pyplot as plt

from test_time_insertion_sort import (
    result_time_lista_10_desord_insertion_sort,
    result_time_lista_25_desord_insertion_sort,
    result_time_lista_50_desord_insertion_sort,
    result_time_lista_100_desord_insertion_sort,
    result_time_lista_1000_desord_insertion_sort,
    result_time_lista_10_QuaseOrd_insertion_sort,
    result_time_lista_25_QuaseOrd_insertion_sort,
    result_time_lista_50_QuaseOrd_insertion_sort,
    result_time_lista_100_QuaseOrd_insertion_sort,
    result_time_lista_1000_QuaseOrd_insertion_sort,
    result_time_lista_10_InversamenteOrd_insertion,
    result_time_lista_25_InversamenteOrd_insertion,
    result_time_lista_50_InversamenteOrd_insertion,
    result_time_lista_100_InversamenteOrd_insertion,
    result_time_lista_1000_InversamenteOrd_insertion
)

tempos = {
    'Desordenada': {
        '10': result_time_lista_10_desord_insertion_sort,
        '25': result_time_lista_25_desord_insertion_sort,
        '50': result_time_lista_50_desord_insertion_sort,
        '100': result_time_lista_100_desord_insertion_sort,
        '1000': result_time_lista_1000_desord_insertion_sort,
    },
    'Quase Ordenada': {
        '10': result_time_lista_10_QuaseOrd_insertion_sort,
        '25': result_time_lista_25_QuaseOrd_insertion_sort,
        '50': result_time_lista_50_QuaseOrd_insertion_sort,
        '100': result_time_lista_100_QuaseOrd_insertion_sort,
        '1000': result_time_lista_1000_QuaseOrd_insertion_sort,
    },
    'Inversamente Ordenada': {
        '10': result_time_lista_10_InversamenteOrd_insertion,
        '25': result_time_lista_25_InversamenteOrd_insertion,
        '50': result_time_lista_50_InversamenteOrd_insertion,
        '100': result_time_lista_100_InversamenteOrd_insertion,
        '1000': result_time_lista_1000_InversamenteOrd_insertion,
    },
}

plt.figure(figsize=(10, 6))

for tipo, tempos_lista in tempos.items():
    plt.plot(tempos_lista.keys(), tempos_lista.values(), marker='o', label=tipo)

plt.title('Comparação de Algoritmos de Ordenação - insertion_sort Sort')
plt.xlabel('Tamanho da Lista')
plt.ylabel('Tempo de Execução (s)')
plt.legend()
plt.grid(True)
plt.xticks(list(tempos['Desordenada'].keys()))  # Adiciona as chaves como ticks
plt.tight_layout()

plt.show()