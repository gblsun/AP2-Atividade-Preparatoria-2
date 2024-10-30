# imports
from line_profiler import LineProfiler

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

# Função de perfilamento
def profile_sorting_function(lista):
    lista.sort()
    print(lista)

# Configuração do LineProfiler
profiler = LineProfiler()
profiler.add_function(profile_sorting_function)

# Sort ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Sort: Lista Desordenada ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Sort: Lista Desordenada: lista_10_Desordenado
print("Sort: Lista Desordenada - lista_10_Desordenado")
profiler.enable()
profile_sorting_function(lista_10_Desordenado)
profiler.disable()
profiler.print_stats()

# Sort: Lista Desordenada: lista_25_Desordenado
print("Sort: Lista Desordenada - lista_25_Desordenado")
profiler.enable()
profile_sorting_function(lista_25_Desordenado)
profiler.disable()
profiler.print_stats()

# Sort: Lista Desordenada: lista_50_Desordenado
print("Sort: Lista Desordenada - lista_50_Desordenado")
profiler.enable()
profile_sorting_function(lista_50_Desordenado)
profiler.disable()
profiler.print_stats()

# Sort: Lista Desordenada: lista_100_Desordenado
print("Sort: Lista Desordenada - lista_100_Desordenado")
profiler.enable()
profile_sorting_function(lista_100_Desordenado)
profiler.disable()
profiler.print_stats()

# Sort: Lista Desordenada: lista_1000_Desordenado
print("Sort: Lista Desordenada - lista_1000_Desordenado")
profiler.enable()
profile_sorting_function(lista_1000_Desordenado)
profiler.disable()
profiler.print_stats()

# Sort: Lista Quase Ordenada ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Sort: Lista Quase Ordenada: lista_10_QuaseOrdenado
print("Sort: Lista Quase Ordenada - lista_10_QuaseOrdenado")
profiler.enable()
profile_sorting_function(lista_10_QuaseOrdenado)
profiler.disable()
profiler.print_stats()

# Sort: Lista Quase Ordenada: lista_25_QuaseOrdenado
print("Sort: Lista Quase Ordenada - lista_25_QuaseOrdenado")
profiler.enable()
profile_sorting_function(lista_25_QuaseOrdenado)
profiler.disable()
profiler.print_stats()

# Sort: Lista Quase Ordenada: lista_50_QuaseOrdenado
print("Sort: Lista Quase Ordenada - lista_50_QuaseOrdenado")
profiler.enable()
profile_sorting_function(lista_50_QuaseOrdenado)
profiler.disable()
profiler.print_stats()

# Sort: Lista Quase Ordenada: lista_100_QuaseOrdenado
print("Sort: Lista Quase Ordenada - lista_100_QuaseOrdenado")
profiler.enable()
profile_sorting_function(lista_100_QuaseOrdenado)
profiler.disable()
profiler.print_stats()

# Sort: Lista Quase Ordenada: lista_1000_QuaseOrdenado
print("Sort: Lista Quase Ordenada - lista_1000_QuaseOrdenado")
profiler.enable()
profile_sorting_function(lista_1000_QuaseOrdenado)
profiler.disable()
profiler.print_stats()

# Sort: Lista Inversamente Ordenada ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Sort: Lista Inversamente Ordenada: lista_10_InversamenteOrdenado
print("Sort: Lista Inversamente Ordenada - lista_10_InversamenteOrdenado")
profiler.enable()
profile_sorting_function(lista_10_InversamenteOrdenado)
profiler.disable()
profiler.print_stats()

# Sort: Lista Inversamente Ordenada: lista_25_InversamenteOrdenado
print("Sort: Lista Inversamente Ordenada - lista_25_InversamenteOrdenado")
profiler.enable()
profile_sorting_function(lista_25_InversamenteOrdenado)
profiler.disable()
profiler.print_stats()

# Sort: Lista Inversamente Ordenada: lista_50_InversamenteOrdenado
print("Sort: Lista Inversamente Ordenada - lista_50_InversamenteOrdenado")
profiler.enable()
profile_sorting_function(lista_50_InversamenteOrdenado)
profiler.disable()
profiler.print_stats()

# Sort: Lista Inversamente Ordenada: lista_100_InversamenteOrdenado
print("Sort: Lista Inversamente Ordenada - lista_100_InversamenteOrdenado")
profiler.enable()
profile_sorting_function(lista_100_InversamenteOrdenado)
profiler.disable()
profiler.print_stats()

# Sort: Lista Inversamente Ordenada: lista_1000_InversamenteOrdenado
print("Sort: Lista Inversamente Ordenada - lista_1000_InversamenteOrdenado")
profiler.enable()
profile_sorting_function(lista_1000_InversamenteOrdenado)
profiler.disable()
profiler.print_stats()
