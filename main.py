'''
Implementação dos algoritmos de ordenação a serem testados

Algoritmos de ordenação simples ⚠️

→ Bubble Sort ⚠️
    ↳ time ✅
    ↳ line_profile ⚠️
    ↳ memory_profile ⚠️

→ Selection Sort ⚠️
    ↳ time ✅
    ↳ line_profile ⚠️
    ↳ memory_profile ⚠️

→ Insertion Sort

    ↳ time ⚠️
    ↳ line_profile ⚠️
    ↳ memory_profile ⚠️


→ Algoritmos de ordenação eficiente ⚠️

→ Heap Sort ⚠️
    ↳ time ⚠️
    ↳ line_profile ⚠️
    ↳ memory_profile ⚠️

→ Merge Sort ⚠️
    ↳ time ⚠️
    ↳ line_profile ⚠️
    ↳ memory_profile ⚠️

→ Quick Sort ⚠️
    ↳ time ⚠️
    ↳ line_profile ⚠️
    ↳ memory_profile ⚠️
    
→ Sort (função interna) ⚠️
    ↳ time ⚠️
    ↳ line_profile ⚠️
    ↳ memory_profile ⚠️
'''
# imports
import time
import bubble_sort
import selection_sort
import insertion_sort
import Heap_Sort
import Merge_Sort
import Quick_Sort
import listas

# Time ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Bubble Sort ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Bubble Sort: Lista Desordenada ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Bubble Sort: Lista Desordenada: lista_10_Desordenado
start_time_10_desord_bubble_sort = time.time()
print(bubble_sort(listas.lista_10_Desordenado))
end_time_10_desord_bubble_sort = time.time()
print(f"Tempo de execução com a lista de 10 elementos desordenados com o método de ordenação bubble_sort: {end_time_10_desord_bubble_sort - start_time_10_desord_bubble_sort} segundos")

# Bubble Sort: Lista Desordenada: lista_25_Desordenado
start_time_25_desord_bubble_sort = time.time()  
print(bubble_sort(listas.lista_25_Desordenado))
end_time_25_desord_bubble_sort = time.time()
print(f"Tempo de execução com a lista de 25 elementos desordenados com o método de ordenação bubble_sort: {end_time_25_desord_bubble_sort - start_time_25_desord_bubble_sort} segundos")

# Bubble Sort: Lista Desordenada: lista_50_Desordenado
start_time_50_desord_bubble_sort = time.time()
print(bubble_sort(listas.lista_50_Desordenado))
end_time_50_desord_bubble_sort = time.time()
print(f"Tempo de execução com a lista de 50 elementos desordenados com o método de ordenação bubble_sort: {end_time_50_desord_bubble_sort - start_time_50_desord_bubble_sort} segundos")

# Bubble Sort: Lista Desordenada: lista_100_Desordenado
start_time_100_desord_bubble_sort = time.time()
print(bubble_sort(listas.lista_100_Desordenado))
end_time_100_desord_bubble_sort = time.time()
print(f"Tempo de execução com a lista de 100 elementos desordenados com o método de ordenação bubble_sort:: {end_time_100_desord - start_time_100_desord} segundos")

# Bubble Sort: Lista Desordenada: lista_1000_Desordenado
start_time_1000_desord = time.time()
print(bubble_sort(listas.lista_1000_Desordenado))
end_time_1000_desord_bubble_sort = time.time()
print(f"Tempo de execução com a lista de 1000 elementos desordenados com o método de ordenação bubble_sort: {end_time_1000_desord_bubble_sort - start_time_1000_desord_bubble_sort} segundos")

# Bubble Sort: Lista quase ordenada ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Bubble Sort: Lista quase ordenada: lista_10_QuaseOrdenado
start_time_10_QuaseOrd_bubble_sort = time.time()
print(bubble_sort(listas.lista_10_QuaseOrdenado))
end_time_10_QuaseOrd_bubble_sort = time.time()
print(f"Tempo de execução com a lista de 10 elementos Quase Ordenados com o método de ordenação bubble_sort: {end_time_10_QuaseOrd_bubble_sort - start_time_10_QuaseOrd_bubble_sort} segundos")

# Bubble Sort: Lista quase ordenada: lista_25_QuaseOrdenado
start_time_25_QuaseOrd_bubble_sort = time.time()
print(bubble_sort(listas.lista_25_QuaseOrdenado))
end_time_25_QuaseOrd_bubble_sort = time.time()
print(f"Tempo de execução com a lista de 25 elementos Quase Ordenados  com o método de ordenação bubble_sort: {end_time_25_QuaseOrd_bubble_sort - start_time_25_QuaseOrd_bubble_sort} segundos")

# Bubble Sort: Lista quase ordenada: lista_50_QuaseOrdenado
start_time_50_QuaseOrd_bubble_sort = time.time()
print(bubble_sort(listas.lista_50_QuaseOrdenado))
end_time_50_QuaseOrd_bubble_sort = time.time()
print(f"Tempo de execução com a lista de 50 elementos Quase Ordenados com o método de ordenação bubble_sort: {end_time_50_QuaseOrd_bubble_sort - start_time_50_QuaseOrd_bubble_sort} segundos")

# Bubble Sort: Lista quase ordenada: lista_100_QuaseOrdenado
start_time_100_QuaseOrd_bubble_sort = time.time()
print(bubble_sort(listas.lista_100_QuaseOrdenado))
end_time_100_QuaseOrd_bubble_sort = time.time()
print(f"Tempo de execução com a lista de 100 elementos Quase Ordenados com o método de ordenação bubble_sort: {end_time_100_QuaseOrd_bubble_sort - start_time_100_QuaseOrd_bubble_sort} segundos")

# Bubble Sort: Lista quase ordenada: lista_1000_QuaseOrdenado
start_time_1000_QuaseOrd_bubble_sort = time.time()
print(bubble_sort(listas.lista_1000_QuaseOrdenado))
end_time_1000_QuaseOrd_bubble_sort = time.time()
print(f"Tempo de execução com a lista de 1000 elementos Quase Ordenados com o método de ordenação bubble_sort: {end_time_1000_QuaseOrd_bubble_sort - start_time_1000_QuaseOrd_bubble_sort} segundos")

# Bubble Sort: lista inversamente ordenada ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Bubble Sort: lista inversamente ordenada: lista_10_InversamenteOrdenado
start_time_10_InversamenteOrd_bubble_sort = time.time()
print(bubble_sort(listas.lista_10_InversamenteOrdenado))
end_time_10_InversamenteOrd_bubble_sort = time.time()
print(f"Tempo de execução com a lista de 10 elementos Inversamente Ordenados com o método de ordenação bubble_sort: {end_time_10_InversamenteOrd_bubble_sort - start_time_10_InversamenteOrd_bubble_sort} segundos")

# Bubble Sort: lista inversamente ordenada: lista_25_InversamenteOrdenado
start_time_25_InversamenteOrd_bubble_sort = time.time()
print(bubble_sort(listas.lista_25_InversamenteOrdenado))
end_time_25_InversamenteOrd_bubble_sort = time.time()
print(f"Tempo de execução com a lista de 25 elementos Inversamente Ordenados com o método de ordenação bubble_sort: {end_time_25_InversamenteOrd_bubble_sort - start_time_25_InversamenteOrd_bubble_sort} segundos")

# Bubble Sort: lista inversamente ordenada: lista_50_InversamenteOrdenado
start_time_50_InversamenteOrd_bubble_sort = time.time()
print(bubble_sort(listas.lista_50_InversamenteOrdenado))
end_time_50_InversamenteOrd_bubble_sort = time.time()
print(f"Tempo de execução com a lista de 50 elementos Inversamente Ordenados com o método de ordenação bubble_sort: {end_time_50_InversamenteOrd_bubble_sort - start_time_50_InversamenteOrd_bubble_sort} segundos")

# Bubble Sort: lista inversamente ordenada: lista_100_InversamenteOrdenado
start_time_100_InversamenteOrd_bubble_sort = time.time()
print(bubble_sort(listas.lista_100_InversamenteOrdenado))
end_time_100_InversamenteOrd_bubble_sort = time.time()
print(f"Tempo de execução com a lista de 100 elementos Inversamente Ordenados com o método de ordenação bubble_sort: {end_time_100_InversamenteOrd_bubble_sort - start_time_100_InversamenteOrd_bubble_sort} segundos")

# Bubble Sort: lista inversamente ordenada: lista_1000_InversamenteOrdenado
start_time_1000_InversamenteOrd_bubble_sort = time.time()
print(bubble_sort(listas.lista_1000_InversamenteOrdenado))
end_time_1000_InversamenteOrd_bubble_sort = time.time()
print(f"Tempo de execução com a lista de 1000 elementos Inversamente Ordenados com o método de ordenação bubble_sort: {end_time_1000_InversamenteOrd_bubble_sort - start_time_1000_InversamenteOrd_bubble_sort} segundos")

# Selection Sort  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Selection Sort: Lista Desordenada  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Selection Sortt: Lista Desordenada: lista_10_Desordenado
start_time_10_desord_selection_sort = time.time()
print(selection_sort(listas.lista_10_Desordenado))
end_time_10_desord_selection_sort = time.time()
print(f"Tempo de execução com a lista de 10 elementos desordenados com o método de ordenação Selection Sort: {end_time_10_desord_selection_sort - start_time_10_desord_selection_sort} segundos")

# Selection Sort: Lista Desordenada: lista_25_Desordenado
start_time_25_desord_selection_sort = time.time()  
print(selection_sort(listas.lista_25_Desordenado))
end_time_25_desord_selection_sort = time.time()
print(f"Tempo de execução com a lista de 25 elementos desordenados com o método de ordenação Selection Sort: {end_time_25_desord_selection_sort - start_time_25_desord_selection_sort} segundos")

# Selection Sort: Lista Desordenada: lista_50_Desordenado
start_time_50_desord_selection_sort = time.time()
print(selection_sort(listas.lista_50_Desordenado))
end_time_50_desord_selection_sort = time.time()
print(f"Tempo de execução com a lista de 50 elementos desordenados com o método de ordenação Selection Sort: {end_time_50_desord_selection_sort - start_time_50_desord_selection_sort} segundos")

# Selection Sort: Lista Desordenada: lista_100_Desordenado
start_time_100_desord_selection_sort = time.time()
print(selection_sort(listas.lista_100_Desordenado))
end_time_100_desord_selection_sort = time.time()
print(f"Tempo de execução com a lista de 100 elementos desordenados com o método de ordenação Selection Sort: {end_time_100_desord_selection_sort - start_time_100_desord_selection_sort} segundos")

# Selection Sort: Lista Desordenada: lista_1000_Desordenado
start_time_1000_desord_selection_sort = time.time()
print(selection_sort(listas.lista_1000_Desordenado))
end_time_1000_desord_selection_sort = time.time()
print(f"Tempo de execução com a lista de 1000 elementos desordenados com o método de ordenação Selection Sort: {end_time_1000_desord_selection_sort - start_time_1000_desord_selection_sort} segundos")

# Selection Sort: Lista quase ordenada ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Selection Sort: Lista quase ordenada: lista_10_QuaseOrdenado
start_time_10_QuaseOrd_selection_sort = time.time()
print(selection_sort(listas.lista_10_QuaseOrdenado))
end_time_10_QuaseOrd_selection_sort = time.time()
print(f"Tempo de execução com a lista de 10 elementos Quase Ordenados com o método de ordenação Selection Sort: {end_time_10_QuaseOrd_selection_sort - start_time_10_QuaseOrd_selection_sort} segundos")

# Selection Sort: Lista quase ordenada: lista_25_QuaseOrdenado
start_time_25_QuaseOrd_selection_sort = time.time()
print(selection_sort(listas.lista_25_QuaseOrdenado))
end_time_25_QuaseOrd_selection_sort = time.time()
print(f"Tempo de execução com a lista de 25 elementos Quase Ordenados com o método de ordenação Selection Sort: {end_time_25_QuaseOrd_selection_sort - start_time_25_QuaseOrd_selection_sort} segundos")

# Selection Sort: Lista quase ordenada: lista_50_QuaseOrdenado
start_time_50_QuaseOrd_selection_sort = time.time()
print(selection_sort(listas.lista_50_QuaseOrdenado))
end_time_50_QuaseOrd_selection_sort = time.time()
print(f"Tempo de execução com a lista de 50 elementos Quase Ordenados com o método de ordenação Selection Sort: {end_time_50_QuaseOrd_selection_sort - start_time_50_QuaseOrd_selection_sort} segundos")

# Selection Sort: Lista quase ordenada: lista_100_QuaseOrdenado
start_time_100_QuaseOrd_selection_sort = time.time()
print(selection_sort(listas.lista_100_QuaseOrdenado))
end_time_100_QuaseOrd_selection_sort = time.time()
print(f"Tempo de execução com a lista de 100 elementos Quase Ordenados com o método de ordenação Selection Sort: {end_time_100_QuaseOrd_selection_sort - start_time_100_QuaseOrd_selection_sort} segundos")

# Selection Sort: Lista quase ordenada: lista_1000_QuaseOrdenado
start_time_1000_QuaseOrd_selection_sort = time.time()
print(selection_sort(listas.lista_1000_QuaseOrdenado))
end_time_1000_QuaseOrd_selection_sort = time.time()
print(f"Tempo de execução com a lista de 1000 elementos Quase Ordenados com o método de ordenação Selection Sort: {end_time_1000_QuaseOrd_selection_sort - start_time_1000_QuaseOrd_selection_sort} segundos")

# Selection Sort: lista inversamente ordenada ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Selection Sort: lista inversamente ordenada: lista_10_InversamenteOrdenado
start_time_10_InversamenteOrd_selection_sort = time.time()
print(selection_sort(listas.lista_10_InversamenteOrdenado))
end_time_10_InversamenteOrd_selection_sort = time.time()
print(f"Tempo de execução com a lista de 10 elementos Inversamente Ordenados com o método de ordenação Selection Sort: {end_time_10_InversamenteOrd_selection_sort - start_time_10_InversamenteOrd_selection_sort} segundos")

# Selection Sort: lista inversamente ordenada: lista_25_InversamenteOrdenado
start_time_25_InversamenteOrd_selection_sort = time.time()
print(selection_sort(listas.lista_25_InversamenteOrdenado))
end_time_25_InversamenteOrd_selection_sort = time.time()
print(f"Tempo de execução com a lista de 25 elementos Inversamente Ordenados com o método de ordenação Selection Sort: {end_time_25_InversamenteOrd_selection_sort - start_time_25_InversamenteOrd_selection_sort} segundos")

# Selection Sort: lista inversamente ordenada: lista_50_InversamenteOrdenado
start_time_50_InversamenteOrd_selection_sort = time.time()
print(selection_sort(listas.lista_50_InversamenteOrdenado))
end_time_50_InversamenteOrd_selection_sort = time.time()
print(f"Tempo de execução com a lista de 50 elementos Inversamente Ordenados com o método de ordenação Selection Sort: {end_time_50_InversamenteOrd_selection_sort - start_time_50_InversamenteOrd_selection_sort} segundos")

# Selection Sort: lista inversamente ordenada: lista_100_InversamenteOrdenado
start_time_100_InversamenteOrd_selection_sort = time.time()
print(selection_sort(listas.lista_100_InversamenteOrdenado))
end_time_100_InversamenteOrd_selection_sort = time.time()
print(f"Tempo de execução com a lista de 100 elementos Inversamente Ordenados com o método de ordenação Selection Sort: {end_time_100_InversamenteOrd_selection_sort - start_time_100_InversamenteOrd_selection_sort} segundos")

# Selection Sort: lista inversamente ordenada: lista_1000_InversamenteOrdenado
start_time_1000_InversamenteOrd_selection_sort = time.time()
print(selection_sort(listas.lista_1000_InversamenteOrdenado))
end_time_1000_InversamenteOrd_selection_sort = time.time()
print(f"Tempo de execução com a lista de 1000 elementos Inversamente Ordenados com o método de ordenação Selection Sort: {end_time_1000_InversamenteOrd_selection_sort - start_time_1000_InversamenteOrd_selection_sort} segundos")


# Selection Sort ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Selection Sort : Lista Desordenada  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Selection Sort : Lista Desordenada: lista_10_Desordenado
start_time_10_desord_selection_sort = time.time()
print(selection_sort(listas.lista_10_Desordenado))
end_time_10_desord_selection_sort = time.time()
print(f"Tempo de execução com a lista de 10 elementos desordenados com o método de ordenação Selection Sort: {end_time_10_desord_selection_sort - start_time_10_desord_selection_sort} segundos")

# Selection Sort: Lista Desordenada: lista_25_Desordenado
start_time_25_desord_selection_sort = time.time()  
print(selection_sort(listas.lista_25_Desordenado))
end_time_25_desord_selection_sort = time.time()
print(f"Tempo de execução com a lista de 25 elementos desordenados com o método de ordenação Selection Sort: {end_time_25_desord_selection_sort - start_time_25_desord_selection_sort} segundos")

# Selection Sort: Lista Desordenada: lista_50_Desordenado
start_time_50_desord_selection_sort = time.time()
print(selection_sort(listas.lista_50_Desordenado))
end_time_50_desord_selection_sort = time.time()
print(f"Tempo de execução com a lista de 50 elementos desordenados com o método de ordenação Selection Sort: {end_time_50_desord_selection_sort - start_time_50_desord_selection_sort} segundos")

# Selection Sort: Lista Desordenada: lista_100_Desordenado
start_time_100_desord_selection_sort = time.time()
print(selection_sort(listas.lista_100_Desordenado))
end_time_100_desord_selection_sort = time.time()
print(f"Tempo de execução com a lista de 100 elementos desordenados com o método de ordenação Selection Sort: {end_time_100_desord_selection_sort - start_time_100_desord_selection_sort} segundos")

# Selection Sort: Lista Desordenada: lista_1000_Desordenado
start_time_1000_desord_selection_sort = time.time()
print(selection_sort(listas.lista_1000_Desordenado))
end_time_1000_desord_selection_sort = time.time()
print(f"Tempo de execução com a lista de 1000 elementos desordenados com o método de ordenação Selection Sort: {end_time_1000_desord_selection_sort - start_time_1000_desord_selection_sort} segundos")

# Selection Sort: Lista quase ordenada ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Selection Sort: Lista quase ordenada: lista_10_QuaseOrdenado
start_time_10_QuaseOrd_selection_sort = time.time()
print(selection_sort(listas.lista_10_QuaseOrdenado))
end_time_10_QuaseOrd_selection_sort = time.time()
print(f"Tempo de execução com a lista de 10 elementos Quase Ordenados com o método de ordenação Selection Sort: {end_time_10_QuaseOrd_selection_sort - start_time_10_QuaseOrd_selection_sort} segundos")

# Selection Sort: Lista quase ordenada: lista_25_QuaseOrdenado
start_time_25_QuaseOrd_selection_sort = time.time()
print(selection_sort(listas.lista_25_QuaseOrdenado))
end_time_25_QuaseOrd_selection_sort = time.time()
print(f"Tempo de execução com a lista de 25 elementos Quase Ordenados com o método de ordenação Selection Sort: {end_time_25_QuaseOrd_selection_sort - start_time_25_QuaseOrd_selection_sort} segundos")

# Selection Sort: Lista quase ordenada: lista_50_QuaseOrdenado
start_time_50_QuaseOrd_selection_sort = time.time()
print(selection_sort(listas.lista_50_QuaseOrdenado))
end_time_50_QuaseOrd_selection_sort = time.time()
print(f"Tempo de execução com a lista de 50 elementos Quase Ordenados com o método de ordenação Selection Sort: {end_time_50_QuaseOrd_selection_sort - start_time_50_QuaseOrd_selection_sort} segundos")

# Selection Sort: Lista quase ordenada: lista_100_QuaseOrdenado
start_time_100_QuaseOrd_selection_sort = time.time()
print(insertion_sort(listas.lista_100_QuaseOrdenado))
end_time_100_QuaseOrd_selection_sort = time.time()
print(f"Tempo de execução com a lista de 100 elementos Quase Ordenados com o método de ordenação Selection Sort: {end_time_100_QuaseOrd_selection_sort - start_time_100_QuaseOrd_selection_sort} segundos")

# Selection Sort: Lista quase ordenada: lista_1000_QuaseOrdenado
start_time_1000_QuaseOrd_selection_sort= time.time()
print(insertion_sort(listas.lista_1000_QuaseOrdenado))
end_time_1000_QuaseOrd_selection_sort = time.time()
print(f"Tempo de execução com a lista de 1000 elementos Quase Ordenados com o método de ordenação Selection Sort: {end_time_1000_QuaseOrd_selection_sort - start_time_1000_QuaseOrd_selection_sort} segundos")

# Selection Sort: lista inversamente ordenada ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Selection Sort: lista inversamente ordenada: lista_10_InversamenteOrdenado
start_time_10_InversamenteOrd_selection_sort= time.time()
print(insertion_sort(listas.lista_10_InversamenteOrdenado))
end_time_10_InversamenteOrd_selection_sort = time.time()
print(f"Tempo de execução com a lista de 10 elementos Inversamente Ordenados com o método de ordenação Selection Sort: {end_time_10_InversamenteOrd_selection_sort - start_time_10_InversamenteOrd_selection_sort} segundos")

# Selection Sort: lista inversamente ordenada: lista_25_InversamenteOrdenado
start_time_25_InversamenteOrd_selection_sort = time.time()
print(selection_sort(listas.lista_25_InversamenteOrdenado))
end_time_25_InversamenteOrd_selection_sort = time.time()
print(f"Tempo de execução com a lista de 25 elementos Inversamente Ordenados com o método de ordenação Selection Sort: {end_time_25_InversamenteOrd_selection_sort - start_time_25_InversamenteOrd_selection_sort} segundos")

# Selection Sort: lista inversamente ordenada: lista_50_InversamenteOrdenado
start_time_50_InversamenteOrd_selection_sort = time.time()
print(selection_sort(listas.lista_50_InversamenteOrdenado))
end_time_50_InversamenteOrd_selection_sort = time.time()
print(f"Tempo de execução com a lista de 50 elementos Inversamente Ordenados com o método de ordenação Selection Sort: {end_time_50_InversamenteOrd_selection_sort - start_time_50_InversamenteOrd_selection_sort} segundos")

# Selection Sort: lista inversamente ordenada: lista_100_InversamenteOrdenado
start_time_100_InversamenteOrd_selection_sort = time.time()
print(selection_sort(listas.lista_100_InversamenteOrdenado))
end_time_100_InversamenteOrd_selection_sort = time.time()
print(f"Tempo de execução com a lista de 100 elementos Inversamente Ordenados com o método de ordenação Selection Sort: {end_time_100_InversamenteOrd_selection_sort - start_time_100_InversamenteOrd_selection_sort} segundos")

# Selection Sort: lista inversamente ordenada: lista_1000_InversamenteOrdenado
start_time_1000_InversamenteOrd_selection_sort = time.time()
print(insertion_sort(listas.lista_1000_InversamenteOrdenado))
end_time_1000_InversamenteOrd_selection_sort = time.time()
print(f"Tempo de execução com a lista de 1000 elementos Inversamente Ordenados com o método de ordenação Selection Sort: {end_time_1000_InversamenteOrd_selection_sort - start_time_1000_InversamenteOrd_selection_sort} segundos")

# Selection Sort: Lista quase ordenada ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Selection Sort: Lista quase ordenada: lista_10_QuaseOrdenado
start_time_10_QuaseOrd_selection_sort = time.time()
print(insertion_sort(listas.lista_10_QuaseOrdenado))
end_time_10_QuaseOrd_selection_sort = time.time()
print(f"Tempo de execução com a lista de 10 elementos Quase Ordenados com o método de ordenação Selection Sort: {end_time_10_QuaseOrd_selection_sort - start_time_10_QuaseOrd_selection_sort} segundos")

# Selection Sort: Lista quase ordenada: lista_25_QuaseOrdenado
start_time_25_QuaseOrd_selection_sort = time.time()
print(insertion_sort(listas.lista_25_QuaseOrdenado))
end_time_25_QuaseOrd_selection_sort = time.time()
print(f"Tempo de execução com a lista de 25 elementos Quase Ordenados com o método de ordenação Selection Sort: {end_time_25_QuaseOrd_selection_sort - start_time_25_QuaseOrd_selection_sort} segundos")

# Selection Sort: Lista quase ordenada: lista_50_QuaseOrdenado
start_time_50_QuaseOrd_selection_sort = time.time()
print(selection_sort(listas.lista_50_QuaseOrdenado))
end_time_50_QuaseOrd_selection_sort = time.time()
print(f"Tempo de execução com a lista de 50 elementos Quase Ordenados com o método de ordenação Selection Sort: {end_time_50_QuaseOrd_selection_sort - start_time_50_QuaseOrd_selection_sort} segundos")

# Selection Sort: Lista quase ordenada: lista_100_QuaseOrdenado
start_time_100_QuaseOrd_selection_sort = time.time()
print(insertion_sort(listas.lista_100_QuaseOrdenado))
end_time_100_QuaseOrd_insertion_sort = time.time()
print(f"Tempo de execução com a lista de 100 elementos Quase Ordenados com o método de ordenação Selection Sort: {end_time_100_QuaseOrd_selection_sort - start_time_100_QuaseOrd_selection_sort} segundos")

# Selection Sort: Lista quase ordenada: lista_1000_QuaseOrdenado
start_time_1000_QuaseOrd_selection_sort = time.time()
print(insertion_sort(listas.lista_1000_QuaseOrdenado))
end_time_1000_QuaseOrd_selection_sort = time.time()
print(f"Tempo de execução com a lista de 1000 elementos Quase Ordenados com o método de ordenação Selection Sort: {end_time_1000_QuaseOrd_selection_sort - start_time_1000_QuaseOrd_selection_sort} segundos")

# Selection Sort: lista inversamente ordenada ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Selection Sort: lista inversamente ordenada: lista_10_InversamenteOrdenado
start_time_10_InversamenteOrd_selection_sort= time.time()
print(insertion_sort(listas.lista_10_InversamenteOrdenado))
end_time_10_InversamenteOrd_selection_sort = time.time()
print(f"Tempo de execução com a lista de 10 elementos Inversamente Ordenados com o método de ordenação Selection Sort: {end_time_10_InversamenteOrd_selection_sort - start_time_10_InversamenteOrd_selection_sort} segundos")

# Selection Sort: lista inversamente ordenada: lista_25_InversamenteOrdenado
start_time_25_InversamenteOrd_selection_sort = time.time()
print(insertion_sort(listas.lista_25_InversamenteOrdenado))
end_time_25_InversamenteOrd_selection_sortt = time.time()
print(f"Tempo de execução com a lista de 25 elementos Inversamente Ordenados com o método de ordenação Selection Sort: {end_time_25_InversamenteOrd_selection_sort - start_time_25_InversamenteOrd_selection_sort} segundos")

# Selection Sort: lista inversamente ordenada: lista_50_InversamenteOrdenado
start_time_50_InversamenteOrd_selection_sort = time.time()
print(insertion_sort(listas.lista_50_InversamenteOrdenado))
end_time_50_InversamenteOrd_selection_sort = time.time()
print(f"Tempo de execução com a lista de 50 elementos Inversamente Ordenados com o método de ordenação Selection Sort: {end_time_50_InversamenteOrd_selection_sort - start_time_50_InversamenteOrd_selection_sort} segundos")

# Selection Sort: lista inversamente ordenada: lista_100_InversamenteOrdenado
start_time_100_InversamenteOrd_selection_sort = time.time()
print(insertion_sort(listas.lista_100_InversamenteOrdenado))
end_time_100_InversamenteOrd_selection_sort = time.time()
print(f"Tempo de execução com a lista de 100 elementos Inversamente Ordenados com o método de ordenação Selection Sort: {end_time_100_InversamenteOrd_selection_sort - start_time_100_InversamenteOrd_selection_sort} segundos")

# Selection Sort: lista inversamente ordenada: lista_1000_InversamenteOrdenado
start_time_1000_InversamenteOrd_selection_sort = time.time()
print(insertion_sort(listas.lista_1000_InversamenteOrdenado))
end_time_1000_InversamenteOrd_selection_sort = time.time()
print(f"Tempo de execução com a lista de 1000 elementos Inversamente Ordenados com o método de ordenação Selection Sort: {end_time_1000_InversamenteOrd_selection_sort - start_time_1000_InversamenteOrd_selection_sort} segundos")