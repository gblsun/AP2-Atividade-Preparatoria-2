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

# Tempos medidos em milissegundos
tempos = [
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
]
# Rótulos para os diferentes tamanhos de lista
rotulos = [
    "10 Desord", "25 Desord", "50 Desord", "100 Desord", "1000 Desord",
    "10 Quase Ord", "25 Quase Ord", "50 Quase Ord", "100 Quase Ord", "1000 Quase Ord",
    "10 Inver Ord", "25 Inver Ord", "50 Inver Ord", "100 Inver Ord", "1000 Invers Ord"
]
# Criando o gráfico
plt.figure(figsize=(10, 6))
plt.barh(rotulos, tempos, color='skyblue')
plt.xlabel('Tempo (ms)')
plt.title('Tempo de Execução do Selection Sort')
plt.grid(axis='x')
plt.show()