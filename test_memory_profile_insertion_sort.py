# imports
from function_insertion_sort import insertion_sort_modificado
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
    result = insertion_sort_modificado(lista)
    print(result)

# Insertion Sort ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Insertion Sort: Lista Desordenada ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Insertion Sort: Lista Desordenada: lista_10_Desordenado
print("Insertion Sort: Lista Desordenada - lista_10_Desordenado")
profile_sorting_function(lista_10_Desordenado)

# Insertion Sort: Lista Desordenada: lista_25_Desordenado
print("Insertion Sort: Lista Desordenada - lista_25_Desordenado")
profile_sorting_function(lista_25_Desordenado)

# Insertion Sort: Lista Desordenada: lista_50_Desordenado
print("Insertion Sort: Lista Desordenada - lista_50_Desordenado")
profile_sorting_function(lista_50_Desordenado)

# Insertion Sort: Lista Desordenada: lista_100_Desordenado
print("Insertion Sort: Lista Desordenada - lista_100_Desordenado")
profile_sorting_function(lista_100_Desordenado)

# Insertion Sort: Lista Desordenada: lista_1000_Desordenado
print("Insertion Sort: Lista Desordenada - lista_1000_Desordenado")
profile_sorting_function(lista_1000_Desordenado)

# Insertion Sort: Lista Quase Ordenada ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Insertion Sort: Lista quase ordenada: lista_10_QuaseOrdenado
print("Insertion Sort: Lista Quase Ordenada - lista_10_QuaseOrdenado")
profile_sorting_function(lista_10_QuaseOrdenado)

# Insertion Sort: Lista quase ordenada: lista_25_QuaseOrdenado
print("Insertion Sort: Lista Quase Ordenada - lista_25_QuaseOrdenado")
profile_sorting_function(lista_25_QuaseOrdenado)

# Insertion Sort: Lista quase ordenada: lista_50_QuaseOrdenado
print("Insertion Sort: Lista Quase Ordenada - lista_50_QuaseOrdenado")
profile_sorting_function(lista_50_QuaseOrdenado)

# Insertion Sort: Lista quase ordenada: lista_100_QuaseOrdenado
print("Insertion Sort: Lista Quase Ordenada - lista_100_QuaseOrdenado")
profile_sorting_function(lista_100_QuaseOrdenado)

# Insertion Sort: Lista quase ordenada: lista_1000_QuaseOrdenado
print("Insertion Sort: Lista Quase Ordenada - lista_1000_QuaseOrdenado")
profile_sorting_function(lista_1000_QuaseOrdenado)

# Insertion Sort: Lista Inversamente Ordenada ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Insertion Sort: Lista inversamente ordenada: lista_10_InversamenteOrdenado
print("Insertion Sort: Lista Inversamente Ordenada - lista_10_InversamenteOrdenado")
profile_sorting_function(lista_10_InversamenteOrdenado)

# Insertion Sort: Lista inversamente ordenada: lista_25_InversamenteOrdenado
print("Insertion Sort: Lista Inversamente Ordenada - lista_25_InversamenteOrdenado")
profile_sorting_function(lista_25_InversamenteOrdenado)

# Insertion Sort: Lista inversamente ordenada: lista_50_InversamenteOrdenado
print("Insertion Sort: Lista Inversamente Ordenada - lista_50_InversamenteOrdenado")
profile_sorting_function(lista_50_InversamenteOrdenado)

# Insertion Sort: Lista inversamente ordenada: lista_100_InversamenteOrdenado
print("Insertion Sort: Lista Inversamente Ordenada - lista_100_InversamenteOrdenado")
profile_sorting_function(lista_100_InversamenteOrdenado)

# Insertion Sort: Lista inversamente ordenada: lista_1000_InversamenteOrdenado
print("Insertion Sort: Lista Inversamente Ordenada - lista_1000_InversamenteOrdenado")
profile_sorting_function(lista_1000_InversamenteOrdenado)