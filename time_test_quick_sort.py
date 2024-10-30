#import
from quick_sort import quick_sort as qs
import sys
import time


from listas_quase_ordenadas import (
    lista_10_QuaseOrdenado,
    lista_25_QuaseOrdenado,
    lista_50_QuaseOrdenado,
    lista_100_QuaseOrdenado,
    lista_1000_QuaseOrdenado
)

from listas_desordenadas import (
    lista_10_Desordenado,
    lista_25_Desordenado,
    lista_50_Desordenado,
    lista_100_Desordenado,
    lista_1000_Desordenado
)

from listas_ordenadas_inversamente import (
    lista_10_InversamenteOrdenado,
    lista_25_InversamenteOrdenado,
    lista_50_InversamenteOrdenado,
    lista_100_InversamenteOrdenado,
    lista_1000_InversamenteOrdenado
)

print(sys.getrecursionlimit())
sys.setrecursionlimit(1500)

# Quick Sort ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Quick Sort: Lista Desordenada ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Quick Sort: Lista Desordenada: lista_10_Desordenado
start_time_10_desord_quick_sort = time.time()
qs(lista_10_Desordenado,0,len(lista_10_Desordenado)- 1)
end_time_10_desord_quick_sort = time.time()
print("Tempo para ordenar lista_10_Desordenado:", end_time_10_desord_quick_sort - start_time_10_desord_quick_sort)

# Quick Sort: Lista Desordenada: lista_25_Desordenado
start_time_25_desord_quick_sort = time.time()  
qs(lista_25_Desordenado,0,len(lista_25_Desordenado)- 1)
end_time_25_desord_quick_sort = time.time()
print("Tempo para ordenar lista_25_Desordenado:", end_time_25_desord_quick_sort - start_time_25_desord_quick_sort)

# Quick Sort: Lista Desordenada: lista_50_Desordenado
start_time_50_desord_quick_sort = time.time()
qs(lista_50_Desordenado,0,len(lista_50_Desordenado)- 1)
end_time_50_desord_quick_sort = time.time()
print("Tempo para ordenar lista_50_Desordenado:", end_time_50_desord_quick_sort - start_time_50_desord_quick_sort)

# Quick Sort: Lista Desordenada: lista_100_Desordenado
start_time_100_desord_quick_sort = time.time()
qs(lista_100_Desordenado,0,len(lista_100_Desordenado)- 1)
end_time_100_desord_quick_sort = time.time()
print("Tempo para ordenar lista_100_Desordenado:", end_time_100_desord_quick_sort - start_time_100_desord_quick_sort)


# QuickSort: Lista Desordenada: lista_1000_Desordenado
start_time_1000_desord_quick_sort = time.time()
qs(lista_1000_Desordenado,0,len(lista_1000_Desordenado)- 1)
end_time_1000_desord_quick_sort = time.time()
print("Tempo para ordenar lista_1000_Desordenado:", end_time_1000_desord_quick_sort - start_time_1000_desord_quick_sort)


# Quick Sort: Lista quase ordenada ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Quick Sort: Lista quase ordenada: lista_10_QuaseOrdenado
start_time_10_QuaseOrd_quick_sort = time.time()
qs(lista_10_QuaseOrdenado,0,len(lista_10_QuaseOrdenado)- 1)
end_time_10_QuaseOrd_quick_sort = time.time()
print("Tempo para ordenar lista_10_Quase_Ordenado:", end_time_10_QuaseOrd_quick_sort - start_time_10_QuaseOrd_quick_sort)


# Quick Sort: Lista quase ordenada: lista_25_QuaseOrdenado
start_time_25_QuaseOrd_quick_sort = time.time()
qs(lista_25_QuaseOrdenado,0,len(lista_25_QuaseOrdenado)- 1)
end_time_25_QuaseOrd_quick_sort = time.time()
print("Tempo para ordenar lista_25_Quase_Ordenado:", end_time_25_QuaseOrd_quick_sort - start_time_25_QuaseOrd_quick_sort)

# Quick Sort: Lista quase ordenada: lista_50_QuaseOrdenado
start_time_50_QuaseOrd_quick_sort = time.time()
qs(lista_50_QuaseOrdenado,0,len(lista_50_QuaseOrdenado)- 1)
end_time_50_QuaseOrd_quick_sort = time.time()
print("Tempo para ordenar lista_50_Quase_Ordenado:", end_time_50_QuaseOrd_quick_sort - start_time_50_QuaseOrd_quick_sort)


# Quick Sort: Lista quase ordenada: lista_100_QuaseOrdenado
start_time_100_QuaseOrd_quick_sort = time.time()
qs(lista_100_QuaseOrdenado,0,len(lista_100_QuaseOrdenado)- 1)
end_time_100_QuaseOrd_quick_sort = time.time()
print("Tempo para ordenar lista_100_Quase_Ordenado:", end_time_100_QuaseOrd_quick_sort - start_time_100_QuaseOrd_quick_sort)

# Quick Sort: Lista quase ordenada: lista_1000_QuaseOrdenado
start_time_1000_QuaseOrd_quick_sort = time.time()
qs(lista_1000_QuaseOrdenado,0,len(lista_1000_QuaseOrdenado)- 1)
end_time_1000_QuaseOrd_quick_sort = time.time()
print("Tempo para ordenar lista_1000_Quase_Ordenado:", end_time_1000_QuaseOrd_quick_sort - start_time_1000_QuaseOrd_quick_sort)

# Quick Sort: lista inversamente ordenada ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Quick Sort: lista inversamente ordenada: lista_10_InversamenteOrdenado
start_time_10_InversamenteOrd_quick_sort = time.time()
qs(lista_10_InversamenteOrdenado,0,len(lista_10_InversamenteOrdenado)- 1)
end_time_10_InversamenteOrd_quick_sort = time.time()
print("Tempo para ordenar lista_10_Inversamente_Ordenado:", end_time_10_InversamenteOrd_quick_sort - start_time_10_InversamenteOrd_quick_sort)


# Quick Sort: lista inversamente ordenada: lista_25_InversamenteOrdenado
start_time_25_InversamenteOrd_quick_sort = time.time()
qs(lista_25_InversamenteOrdenado,0,len(lista_25_InversamenteOrdenado)- 1)
end_time_25_InversamenteOrd_quick_sort = time.time()
print("Tempo para ordenar lista_25_Inversamente_Ordenado:", end_time_25_InversamenteOrd_quick_sort - start_time_25_InversamenteOrd_quick_sort)

# Quick Sort: lista inversamente ordenada: lista_50_InversamenteOrdenado
start_time_50_InversamenteOrd_quick_sort = time.time()
qs(lista_50_InversamenteOrdenado,0,len(lista_50_InversamenteOrdenado)- 1)
end_time_50_InversamenteOrd_quick_sort = time.time()
print("Tempo para ordenar lista_50_Inversamente_Ordenado:", end_time_50_InversamenteOrd_quick_sort - start_time_50_InversamenteOrd_quick_sort)

# Quick Sort: lista inversamente ordenada: lista_100_InversamenteOrdenado
start_time_100_InversamenteOrd_quick_sort = time.time()
qs(lista_100_InversamenteOrdenado,0,len(lista_100_InversamenteOrdenado)- 1)
end_time_100_InversamenteOrd_quick_sort = time.time()
print("Tempo para ordenar lista_100_Inversamente_Ordenado:", end_time_100_InversamenteOrd_quick_sort - start_time_100_InversamenteOrd_quick_sort)

# Quick Sort: lista inversamente ordenada: lista_1000_InversamenteOrdenado
start_time_1000_InversamenteOrd_quick_sort = time.time()
qs(lista_1000_InversamenteOrdenado,0,len(lista_1000_InversamenteOrdenado)- 1)
end_time_1000_InversamenteOrd_quick_sort = time.time()
print("Tempo para ordenar lista_1000_Inversamente_Ordenado:", end_time_1000_InversamenteOrd_quick_sort - start_time_1000_InversamenteOrd_quick_sort)

