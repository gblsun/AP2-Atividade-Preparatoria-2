# imports
import time
from listas_desordenadas import (
    lista_1000_Desordenado,
    lista_100_Desordenado,
    lista_50_Desordenado,
    lista_25_Desordenado,
    lista_10_Desordenado
)
from listas_quase_ordenadas import (
    lista_1000_QuaseOrdenado,
    lista_100_QuaseOrdenado,
    lista_50_QuaseOrdenado,
    lista_25_QuaseOrdenado,
    lista_10_QuaseOrdenado
)
from listas_ordenadas_inversamente import (
    lista_1000_InversamenteOrdenado,
    lista_100_InversamenteOrdenado,
    lista_50_InversamenteOrdenado,
    lista_25_InversamenteOrdenado,
    lista_10_InversamenteOrdenado
)




# Sort ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Sort: Lista Desordenada ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Sort: Lista Desordenada: lista_10_Desordenado
start_time_10_desord_sort = time.perf_counter()
lista_10_Desordenado.sort()
end_time_10_desord_sort = time.perf_counter()
result_time_lista_10_Desordenado = end_time_10_desord_sort - start_time_10_desord_sort
print("Tempo para ordenar lista_10_Desordenado:", result_time_lista_10_Desordenado)

# Sort: Lista Desordenada: lista_25_Desordenado
start_time_25_desord_sort = time.perf_counter()  
lista_25_Desordenado.sort()
end_time_25_desord_sort = time.perf_counter()
result_time_lista_25_Desordenado = end_time_25_desord_sort - start_time_25_desord_sort
print("Tempo para ordenar lista_25_Desordenado:", result_time_lista_25_Desordenado)

# Sort: Lista Desordenada: lista_50_Desordenado
start_time_50_desord_sort = time.perf_counter()
lista_50_Desordenado.sort()
end_time_50_desord_sort = time.perf_counter()
result_time_lista_50_Desordenado = end_time_50_desord_sort - start_time_50_desord_sort
print("Tempo para ordenar lista_50_Desordenado:", result_time_lista_50_Desordenado)

# Sort: Lista Desordenada: lista_100_Desordenado
start_time_100_desord_sort = time.perf_counter()
lista_100_Desordenado.sort()
end_time_100_desord_sort = time.perf_counter()
result_time_lista_100_Desordenado = end_time_100_desord_sort - start_time_100_desord_sort
print("Tempo para ordenar lista_100_Desordenado:", result_time_lista_100_Desordenado)

# Sort: Lista Desordenada: lista_1000_Desordenado
start_time_1000_desord_sort = time.perf_counter()
lista_1000_Desordenado.sort()
end_time_1000_desord_sort = time.perf_counter()
result_time_lista_1000_Desordenado = end_time_1000_desord_sort - start_time_1000_desord_sort
print("Tempo para ordenar lista_1000_Desordenado:", result_time_lista_1000_Desordenado)

# Sort: Lista quase ordenada ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Sort: Lista quase ordenada: lista_10_QuaseOrdenado
start_time_10_QuaseOrd_sort = time.perf_counter()
lista_10_QuaseOrdenado.sort()
end_time_10_QuaseOrd_sort = time.perf_counter()
result_time_lista_10_QuaseOrd_sort = end_time_10_QuaseOrd_sort - start_time_10_QuaseOrd_sort
print("Tempo para ordenar lista_10_Quase_Ordenado:",  result_time_lista_10_QuaseOrd_sort)

# Sort: Lista quase ordenada: lista_25_QuaseOrdenado
start_time_25_QuaseOrd_sort = time.perf_counter()
lista_25_QuaseOrdenado.sort()
end_time_25_QuaseOrd_sort = time.perf_counter()
result_time_lista_25_QuaseOrd_sort = end_time_25_QuaseOrd_sort - start_time_25_QuaseOrd_sort
print("Tempo para ordenar lista_25_Quase_Ordenado:",  result_time_lista_25_QuaseOrd_sort)

# Sort: Lista quase ordenada: lista_50_QuaseOrdenado
start_time_50_QuaseOrd_sort = time.perf_counter()
lista_50_QuaseOrdenado.sort()
end_time_50_QuaseOrd_sort = time.perf_counter()
result_time_lista_50_QuaseOrd_sort = end_time_50_QuaseOrd_sort - start_time_50_QuaseOrd_sort
print("Tempo para ordenar lista_50_Quase_Ordenado:",  result_time_lista_50_QuaseOrd_sort)

# Sort: Lista quase ordenada: lista_100_QuaseOrdenado
start_time_100_QuaseOrd_sort = time.perf_counter()
lista_100_QuaseOrdenado.sort()
end_time_100_QuaseOrd_sort = time.perf_counter()
result_time_lista_100_QuaseOrd_sort = end_time_100_QuaseOrd_sort - start_time_100_QuaseOrd_sort
print("Tempo para ordenar lista_100_Quase_Ordenado:",  result_time_lista_100_QuaseOrd_sort)

# Sort: Lista quase ordenada: lista_1000_QuaseOrdenado
start_time_1000_QuaseOrd_sort = time.perf_counter()
lista_1000_QuaseOrdenado.sort()
end_time_1000_QuaseOrd_sort = time.perf_counter()
result_time_lista_1000_QuaseOrd_sort = end_time_1000_QuaseOrd_sort - start_time_1000_QuaseOrd_sort
print("Tempo para ordenar lista_1000_Quase_Ordenado:",  result_time_lista_1000_QuaseOrd_sort)

# Sort: lista inversamente ordenada ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Sort: lista inversamente ordenada: lista_10_InversamenteOrdenado
start_time_10_InversamenteOrd_sort = time.perf_counter()
lista_10_InversamenteOrdenado.sort()
end_time_10_InversamenteOrd_sort = time.perf_counter()
result_time_lista_10_InversamenteOrd_sort = end_time_10_InversamenteOrd_sort - start_time_10_InversamenteOrd_sort
print("Tempo para ordenar lista_10_Inversamente_Ordenado:",  result_time_lista_10_InversamenteOrd_sort)

# Sort: lista inversamente ordenada: lista_25_InversamenteOrdenado
start_time_25_InversamenteOrd_sort = time.perf_counter()
lista_25_InversamenteOrdenado.sort()
end_time_25_InversamenteOrd_sort = time.perf_counter()
result_time_lista_25_InversamenteOrd_sort = end_time_25_InversamenteOrd_sort - start_time_25_InversamenteOrd_sort
print("Tempo para ordenar lista_25_Inversamente_Ordenado:",  result_time_lista_25_InversamenteOrd_sort)

# Sort: lista inversamente ordenada: lista_50_InversamenteOrdenado
start_time_50_InversamenteOrd_sort = time.perf_counter()
lista_50_InversamenteOrdenado.sort()
end_time_50_InversamenteOrd_sort = time.perf_counter()
result_time_lista_50_InversamenteOrd_sort = end_time_50_InversamenteOrd_sort - start_time_50_InversamenteOrd_sort
print("Tempo para ordenar lista_50_Inversamente_Ordenado:",  result_time_lista_50_InversamenteOrd_sort)

# Sort: lista inversamente ordenada: lista_100_InversamenteOrdenado
start_time_100_InversamenteOrd_sort = time.perf_counter()
lista_100_InversamenteOrdenado.sort()
end_time_100_InversamenteOrd_sort = time.perf_counter()
result_time_lista_100_InversamenteOrd_sort = end_time_100_InversamenteOrd_sort - start_time_100_InversamenteOrd_sort
print("Tempo para ordenar lista_100_Inversamente_Ordenado:",  result_time_lista_100_InversamenteOrd_sort)

# Sort: lista inversamente ordenada: lista_1000_InversamenteOrdenado
start_time_1000_InversamenteOrd_sort = time.perf_counter()
lista_1000_InversamenteOrdenado.sort()
end_time_1000_InversamenteOrd_sort = time.perf_counter()
result_time_lista_1000_InversamenteOrd_sort = end_time_1000_InversamenteOrd_sort - start_time_1000_InversamenteOrd_sort
print("Tempo para ordenar lista_1000_Inversamente_Ordenado:",  result_time_lista_1000_InversamenteOrd_sort) 