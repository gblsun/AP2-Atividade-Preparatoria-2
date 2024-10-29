#import
from merge_sort import merge_sort as ms

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



# Merge Sort ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Merge Sort: Lista Desordenada ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Merge Sort: Lista Desordenada: lista_10_Desordenado
start_time_10_desord_merge_sort = time.time()
print(ms(lista_10_Desordenado))
end_time_10_desord_merge_sort = time.time()

# merge Sort: Lista Desordenada: lista_25_Desordenado
start_time_25_desord_merge_sort = time.time()  
print(ms(lista_25_Desordenado))
end_time_25_desord_merge_sort = time.time()

# Merge Sort: Lista Desordenada: lista_50_Desordenado
start_time_50_desord_merge_sort = time.time()
print(ms(lista_50_Desordenado))
end_time_50_desord_merge_sort = time.time()

# Merge Sort: Lista Desordenada: lista_100_Desordenado
start_time_100_desord_merge_sort = time.time()
print(ms(lista_100_Desordenado))
end_time_100_desord_merge_sort = time.time()

# Merge Sort: Lista Desordenada: lista_1000_Desordenado
start_time_1000_desord_merge_sort = time.time()
print(ms(lista_1000_Desordenado))
end_time_1000_desord_merge_sort = time.time()

# Merge Sort: Lista quase ordenada ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Merge Sort: Lista quase ordenada: lista_10_QuaseOrdenado
start_time_10_QuaseOrd_merge_sort = time.time()
print(ms(lista_10_QuaseOrdenado))
end_time_10_QuaseOrd_merge_sort = time.time()

# Merge Sort: Lista quase ordenada: lista_25_QuaseOrdenado
start_time_25_QuaseOrd_merge_sort = time.time()
print(ms(lista_25_QuaseOrdenado))
end_time_25_QuaseOrd_merge_sort = time.time()

# Merge Sort: Lista quase ordenada: lista_50_QuaseOrdenado
start_time_50_QuaseOrd_merge_sort = time.time()
print(ms(lista_50_QuaseOrdenado))
end_time_50_QuaseOrd_merge_sort = time.time()

# Merge Sort: Lista quase ordenada: lista_100_QuaseOrdenado
start_time_100_QuaseOrd_merge_sort = time.time()
print(ms(lista_100_QuaseOrdenado))
end_time_100_QuaseOrd_merge_sort = time.time()

# Merge Sort: Lista quase ordenada: lista_1000_QuaseOrdenado
start_time_1000_QuaseOrd_merge_sort = time.time()
print(ms(lista_1000_QuaseOrdenado))
end_time_1000_QuaseOrd_merge_sort = time.time()

# Merge Sort: lista inversamente ordenada ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Merge Sort: lista inversamente ordenada: lista_10_InversamenteOrdenado
start_time_10_InversamenteOrd_merge_sort = time.time()
print(ms(lista_10_InversamenteOrdenado))
end_time_10_InversamenteOrd_merge_sort = time.time()

# Merge Sort: lista inversamente ordenada: lista_25_InversamenteOrdenado
start_time_25_InversamenteOrd_merge_sort = time.time()
print(ms(lista_25_InversamenteOrdenado))
end_time_25_InversamenteOrd_merge_sort = time.time()

# Merge Sort: lista inversamente ordenada: lista_50_InversamenteOrdenado
start_time_50_InversamenteOrd_merge_sort = time.time()
print(ms(lista_50_InversamenteOrdenado))
end_time_50_InversamenteOrd_merge_sort = time.time()

# Merge Sort: lista inversamente ordenada: lista_100_InversamenteOrdenado
start_time_100_InversamenteOrd_merge_sort = time.time()
print(ms(lista_100_InversamenteOrdenado))
end_time_100_InversamenteOrd_merge_sort = time.time()

# Merge Sort: lista inversamente ordenada: lista_1000_InversamenteOrdenado
start_time_1000_InversamenteOrd_merge_sort = time.time()
print(ms(lista_1000_InversamenteOrdenado))
end_time_1000_InversamenteOrd_merge_sort = time.time()