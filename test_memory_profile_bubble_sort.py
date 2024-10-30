# imports
from function_bubble_sort import bubble_sort
from memory_profiler import profile

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

# Função de perfilamento com memory_profile
@profile
def profile_sorting_function(lista):
    result = bubble_sort(lista)
    print(result)

# Bubble Sort ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Bubble Sort: Lista Desordenada ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Bubble Sort: Lista Desordenada: lista_10_Desordenado
print("Bubble Sort: Lista Desordenada - lista_10_Desordenado")
profile_sorting_function(lista_10_Desordenado)

# Bubble Sort: Lista Desordenada: lista_25_Desordenado
print("Bubble Sort: Lista Desordenada - lista_25_Desordenado")
profile_sorting_function(lista_25_Desordenado)

# Bubble Sort: Lista Desordenada: lista_50_Desordenado
print("Bubble Sort: Lista Desordenada - lista_50_Desordenado")
profile_sorting_function(lista_50_Desordenado)

# Bubble Sort: Lista Desordenada: lista_100_Desordenado
print("Bubble Sort: Lista Desordenada - lista_100_Desordenado")
profile_sorting_function(lista_100_Desordenado)

# Bubble Sort: Lista Desordenada: lista_1000_Desordenado
print("Bubble Sort: Lista Desordenada - lista_1000_Desordenado")
profile_sorting_function(lista_1000_Desordenado)

# Bubble Sort: Lista Quase Ordenada ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Bubble Sort: Lista quase ordenada: lista_10_QuaseOrdenado
print("Bubble Sort: Lista Quase Ordenada - lista_10_QuaseOrdenado")
profile_sorting_function(lista_10_QuaseOrdenado)

# Bubble Sort: Lista quase ordenada: lista_25_QuaseOrdenado
print("Bubble Sort: Lista Quase Ordenada - lista_25_QuaseOrdenado")
profile_sorting_function(lista_25_QuaseOrdenado)

# Bubble Sort: Lista quase ordenada: lista_50_QuaseOrdenado
print("Bubble Sort: Lista Quase Ordenada - lista_50_QuaseOrdenado")
profile_sorting_function(lista_50_QuaseOrdenado)

# Bubble Sort: Lista quase ordenada: lista_100_QuaseOrdenado
print("Bubble Sort: Lista Quase Ordenada - lista_100_QuaseOrdenado")
profile_sorting_function(lista_100_QuaseOrdenado)

# Bubble Sort: Lista quase ordenada: lista_1000_QuaseOrdenado
print("Bubble Sort: Lista Quase Ordenada - lista_1000_QuaseOrdenado")
profile_sorting_function(lista_1000_QuaseOrdenado)

# Bubble Sort: Lista Inversamente Ordenada ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Bubble Sort: Lista inversamente ordenada: lista_10_InversamenteOrdenado
print("Bubble Sort: Lista Inversamente Ordenada - lista_10_InversamenteOrdenado")
profile_sorting_function(lista_10_InversamenteOrdenado)

# Bubble Sort: Lista inversamente ordenada: lista_25_InversamenteOrdenado
print("Bubble Sort: Lista Inversamente Ordenada - lista_25_InversamenteOrdenado")
profile_sorting_function(lista_25_InversamenteOrdenado)

# Bubble Sort: Lista inversamente ordenada: lista_50_InversamenteOrdenado
print("Bubble Sort: Lista Inversamente Ordenada - lista_50_InversamenteOrdenado")
profile_sorting_function(lista_50_InversamenteOrdenado)

# Bubble Sort: Lista inversamente ordenada: lista_100_InversamenteOrdenado
print("Bubble Sort: Lista Inversamente Ordenada - lista_100_InversamenteOrdenado")
profile_sorting_function(lista_100_InversamenteOrdenado)

# Bubble Sort: Lista inversamente ordenada: lista_1000_InversamenteOrdenado
print("Bubble Sort: Lista Inversamente Ordenada - lista_1000_InversamenteOrdenado")
profile_sorting_function(lista_1000_InversamenteOrdenado)