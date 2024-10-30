#Import
# import matplotlib.pyplot as plt


# from test_time_merge_sort import (
#     result_time_lista_10_Desordenado_merge,
#     result_time_lista_25_Desordenado_merge,
#     result_time_lista_50_Desordenado_merge,
#     result_time_lista_100_Desordenado_merge,
#     result_time_lista_1000_Desordenado_merge,
#     result_time_lista_10_QuaseOrd_merge,
#     result_time_lista_25_QuaseOrd_merge,
#     result_time_lista_50_QuaseOrd_merge,
#     result_time_lista_100_QuaseOrd_merge,
#     result_time_lista_1000_QuaseOrd_merge,
#     result_time_lista_10_InversamenteOrd_merge,
#     result_time_lista_25_InversamenteOrd_merge,
#     result_time_lista_50_InversamenteOrd_merge,
#     result_time_lista_100_InversamenteOrd_merge,
#     result_time_lista_1000_InversamenteOrd_merge,
# )

# # Tempos de execução (substitua pelas suas variáveis)
# tempos_merge = {
#     'Desordenada': {
#         '10': result_time_lista_10_Desordenado_merge,
#         '25': result_time_lista_25_Desordenado_merge,
#         '50': result_time_lista_50_Desordenado_merge,
#         '100': result_time_lista_100_Desordenado_merge,
#         '1000': result_time_lista_1000_Desordenado_merge,
#     },
#     'Quase Ordenada': {
#         '10': result_time_lista_10_QuaseOrd_merge,
#         '25': result_time_lista_25_QuaseOrd_merge,
#         '50': result_time_lista_50_QuaseOrd_merge,
#         '100': result_time_lista_100_QuaseOrd_merge,
#         '1000': result_time_lista_1000_QuaseOrd_merge,
#     },
#     'Inversamente Ordenada': {
#         '10': result_time_lista_10_InversamenteOrd_merge,
#         '25': result_time_lista_25_InversamenteOrd_merge,
#         '50': result_time_lista_50_InversamenteOrd_merge,
#         '100': result_time_lista_100_InversamenteOrd_merge,
#         '1000': result_time_lista_1000_InversamenteOrd_merge,
#     },
# }

# # Criando o gráfico
# plt.figure(figsize=(10, 6))

# # Plotando cada tipo de lista
# for tipo, tempos_lista in tempos_merge.items():
#     plt.plot(tempos_lista.keys(), tempos_lista.values(), marker='o', label=tipo)

# # Configurações do gráfico
# plt.title('Comparação de Algoritmos de Ordenação - Merge Sort')
# plt.xlabel('Tamanho da Lista')
# plt.ylabel('Tempo de Execução (s)')
# plt.legend()
# plt.grid(True)
# plt.xticks(list(tempos_merge['Desordenada'].keys()))  # Adiciona as chaves como ticks
# plt.tight_layout()

# # Exibindo o gráfico
# plt.show()

import matplotlib.pyplot as plt

# Importando os tempos medidos em milissegundos
from test_time_merge_sort import (
    result_time_lista_10_Desordenado_merge,
    result_time_lista_25_Desordenado_merge,
    result_time_lista_50_Desordenado_merge,
    result_time_lista_100_Desordenado_merge,
    result_time_lista_1000_Desordenado_merge,
    result_time_lista_10_QuaseOrd_merge,
    result_time_lista_25_QuaseOrd_merge,
    result_time_lista_50_QuaseOrd_merge,
    result_time_lista_100_QuaseOrd_merge,
    result_time_lista_1000_QuaseOrd_merge,
    result_time_lista_10_InversamenteOrd_merge,
    result_time_lista_25_InversamenteOrd_merge,
    result_time_lista_50_InversamenteOrd_merge,
    result_time_lista_100_InversamenteOrd_merge,
    result_time_lista_1000_InversamenteOrd_merge,
)

# Tempos medidos em milissegundos
tempos = [
    result_time_lista_10_Desordenado_merge,
    result_time_lista_25_Desordenado_merge,
    result_time_lista_50_Desordenado_merge,
    result_time_lista_100_Desordenado_merge,
    result_time_lista_1000_Desordenado_merge,
    result_time_lista_10_QuaseOrd_merge,
    result_time_lista_25_QuaseOrd_merge,
    result_time_lista_50_QuaseOrd_merge,
    result_time_lista_100_QuaseOrd_merge,
    result_time_lista_1000_QuaseOrd_merge,
    result_time_lista_10_InversamenteOrd_merge,
    result_time_lista_25_InversamenteOrd_merge,
    result_time_lista_50_InversamenteOrd_merge,
    result_time_lista_100_InversamenteOrd_merge,
    result_time_lista_1000_InversamenteOrd_merge,
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
plt.title('Tempo de Execução do Merge Sort')
plt.grid(axis='x')
plt.show()
