# imports
from insertion_sort import insertion_sort_modificado 
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





# Insertion Sort ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Insertion Sort: Lista Desordenada ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Insertion Sort: Lista Desordenada: lista_10_Desordenado
start_time_10_desord_insertion_sort_modificado = time.time()
print(insertion_sort_modificado(lista_10_Desordenado))
end_time_10_desord_insertion_sort_modificado = time.time()
print("Tempo para ordenar lista_10_Desordenado:", end_time_10_desord_insertion_sort_modificado - start_time_10_desord_insertion_sort_modificado)

# Insertion Sort: Lista Desordenada: lista_25_Desordenado
start_time_25_desord_insertion_sort_modificado = time.time()  
print(insertion_sort_modificado(lista_25_Desordenado))
end_time_25_desord_insertion_sort_modificado = time.time()
print("Tempo para ordenar lista_25_Desordenado:", end_time_25_desord_insertion_sort_modificado - start_time_25_desord_insertion_sort_modificado)

# Insertion Sort: Lista Desordenada: lista_50_Desordenado
start_time_50_desord_insertion_sort_modificado = time.time()
print(insertion_sort_modificado(lista_50_Desordenado))
end_time_50_desord_insertion_sort_modificado = time.time()
print("Tempo para ordenar lista_50_Desordenado:", end_time_50_desord_insertion_sort_modificado - start_time_50_desord_insertion_sort_modificado)

# Insertion Sort: Lista Desordenada: lista_100_Desordenado
start_time_100_desord_insertion_sort_modificado = time.time()
print(insertion_sort_modificado(lista_100_Desordenado))
end_time_100_desord_insertion_sort_modificado = time.time()
print("Tempo para ordenar lista_100_Desordenado:", end_time_100_desord_insertion_sort_modificado - start_time_100_desord_insertion_sort_modificado)

# Insertion Sort: Lista Desordenada: lista_1000_Desordenado
start_time_1000_desord_insertion_sort_modificado = time.time()
print(insertion_sort_modificado(lista_1000_Desordenado))
end_time_1000_desord_insertion_sort_modificado = time.time()
print("Tempo para ordenar lista_100_Desordenado:", end_time_100_desord_insertion_sort_modificado - start_time_100_desord_insertion_sort_modificado)

# Insertion Sort: Lista quase ordenada ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Insertion Sort: Lista quase ordenada: lista_10_QuaseOrdenado
start_time_10_QuaseOrd_insertion_sort_modificado = time.time()
print(insertion_sort_modificado(lista_10_QuaseOrdenado))
end_time_10_QuaseOrd_insertion_sort_modificado = time.time()
print("Tempo para ordenar lista_10_Quase_Ordenado:", end_time_10_QuaseOrd_insertion_sort_modificado - start_time_10_QuaseOrd_insertion_sort_modificado)

# Insertion Sort: Lista quase ordenada: lista_25_QuaseOrdenado
start_time_25_QuaseOrd_insertion_sort_modificado = time.time()
print(insertion_sort_modificado(lista_25_QuaseOrdenado))
end_time_25_QuaseOrd_insertion_sort_modificado = time.time()
print("Tempo para ordenar lista_25_Quase_Ordenado:", end_time_25_QuaseOrd_insertion_sort_modificado - start_time_25_QuaseOrd_insertion_sort_modificado)

# Insertion Sort: Lista quase ordenada: lista_50_QuaseOrdenado
start_time_50_QuaseOrd_insertion_sort_modificado = time.time()
print(insertion_sort_modificado(lista_50_QuaseOrdenado))
end_time_50_QuaseOrd_insertion_sort_modificado = time.time()
print("Tempo para ordenar lista_50_Quase_Ordenado:", end_time_50_QuaseOrd_insertion_sort_modificado - start_time_50_QuaseOrd_insertion_sort_modificado)

# Insertion Sort: Lista quase ordenada: lista_100_QuaseOrdenado
start_time_100_QuaseOrd_insertion_sort = time.time()
print(insertion_sort_modificado(lista_100_QuaseOrdenado))
end_time_100_QuaseOrd_insertion_sort_modificado = time.time()
print("Tempo para ordenar lista_100_Quase_Ordenado:", end_time_100_QuaseOrd_insertion_sort_modificado - start_time_10_QuaseOrd_insertion_sort_modificado)

# Insertion Sort: Lista quase ordenada: lista_1000_QuaseOrdenado
start_time_1000_QuaseOrd_insertion_sort_modificado = time.time()
print(insertion_sort_modificado(lista_1000_QuaseOrdenado))
end_time_1000_QuaseOrd_insertion_sort_modificado = time.time()
print("Tempo para ordenar lista_1000_Quase_Ordenado:", end_time_1000_QuaseOrd_insertion_sort_modificado - start_time_1000_QuaseOrd_insertion_sort_modificado)

# Insertion Sort: lista inversamente ordenada ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Insertion Sort: lista inversamente ordenada: lista_10_InversamenteOrdenado
start_time_10_InversamenteOrd_insertion_sort_modificado = time.time()
print(insertion_sort_modificado(lista_10_InversamenteOrdenado))
end_time_10_InversamenteOrd_insertion_sort_modificado = time.time()
print("Tempo para ordenar lista_10_Inversamente_Ordenado:", end_time_10_InversamenteOrd_insertion_sort_modificado - start_time_10_InversamenteOrd_insertion_sort_modificado)

# Insertion Sort: lista inversamente ordenada: lista_25_InversamenteOrdenado
start_time_25_InversamenteOrd_insertion_sort_modificado = time.time()
print(insertion_sort_modificado(lista_25_InversamenteOrdenado))
end_time_25_InversamenteOrd_insertion_sort_modificado = time.time()
print("Tempo para ordenar lista_25_Inversamente_Ordenado:", end_time_25_InversamenteOrd_insertion_sort_modificado - start_time_25_InversamenteOrd_insertion_sort_modificado)

# Insertion Sort: lista inversamente ordenada: lista_50_InversamenteOrdenado
start_time_50_InversamenteOrd_insertion_sort_modificado = time.time()
print(insertion_sort_modificado(lista_50_InversamenteOrdenado))
end_time_50_InversamenteOrd_insertion_sort_modificado = time.time()
print("Tempo para ordenar lista_50_Inversamente_Ordenado:", end_time_50_InversamenteOrd_insertion_sort_modificado - start_time_50_InversamenteOrd_insertion_sort_modificado)

# Insertion Sort: lista inversamente ordenada: lista_100_InversamenteOrdenado
start_time_100_InversamenteOrd_insertion_sort_modificado = time.time()
print(insertion_sort_modificado(lista_100_InversamenteOrdenado))
end_time_100_InversamenteOrd_insertion_sort_modificado = time.time()
print("Tempo para ordenar lista_100_Inversamente_Ordenado:", end_time_100_InversamenteOrd_insertion_sort_modificado - start_time_100_InversamenteOrd_insertion_sort_modificado)

# Insertion Sort: lista inversamente ordenada: lista_1000_InversamenteOrdenado
start_time_1000_InversamenteOrd_insertion_sort_modificado = time.time()
print(insertion_sort_modificado(lista_1000_InversamenteOrdenado))
end_time_1000_InversamenteOrd_insertion_sort_modificado = time.time()
print("Tempo para ordenar lista_1000_Inversamente_Ordenado:", end_time_1000_InversamenteOrd_insertion_sort_modificado - start_time_1000_InversamenteOrd_insertion_sort_modificado)