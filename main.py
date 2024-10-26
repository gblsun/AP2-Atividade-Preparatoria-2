'''
Implementação dos algoritmos de ordenação a serem testados

Algoritmos de ordenação simples

→ Bubble Sort
    ↳ time
    ↳ line_profile
    ↳ memory_profile

→ Selection Sort
    ↳ time
    ↳ line_profile
    ↳ memory_profile

→ Insertion Sort

    ↳ time
    ↳ line_profile
    ↳ memory_profile


→ Algoritmos de ordenação eficiente

→ Heap Sort
    ↳ time
    ↳ line_profile
    ↳ memory_profile

→ Merge Sort
    ↳ time
    ↳ line_profile
    ↳ memory_profile

→ Quick Sort
    ↳ time
    ↳ line_profile
    ↳ memory_profile

→ Sort (função interna)
    ↳ time
    ↳ line_profile
    ↳ memory_profile
→ 
↳ 
'''
# imports
import time
from bubble_sort import bubble_sort
import listas

# Time ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Bubble Sort ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Lista Desordenada ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Lista Desordenada: lista_10_Desordenado
start_time_10_desord = time.time()
print(bubble_sort(listas.lista_10_Desordenado))
end_time_10_desord = time.time()
print(f"Tempo de execução com a lista de 10 elementos desordenados: {end_time_10_desord - start_time_10_desord} segundos")

# Lista Desordenada: lista_25_Desordenado
start_time_25_desord = time.time()  
print(bubble_sort(listas.lista_25_Desordenado))
end_time_25_desord = time.time()
print(f"Tempo de execução com a lista de 25 elementos desordenados: {end_time_25_desord - start_time_25_desord} segundos")

# Lista Desordenada: lista_50_Desordenado
start_time_50_desord = time.time()
print(bubble_sort(listas.lista_50_Desordenado))
end_time_50_desord = time.time()
print(f"Tempo de execução com a lista de 50 elementos desordenados: {end_time_50_desord - start_time_50_desord} segundos")

# Lista Desordenada: lista_100_Desordenado
start_time_100_desord = time.time()
print(bubble_sort(listas.lista_100_Desordenado))
end_time_100_desord = time.time()
print(f"Tempo de execução com a lista de 100 elementos desordenados: {end_time_100_desord - start_time_100_desord} segundos")

# Lista Desordenada: lista_1000_Desordenado
start_time_1000_desord = time.time()
print(bubble_sort(listas.lista_1000_Desordenado))
end_time_1000_desord = time.time()
print(f"Tempo de execução com a lista de 1000 elementos desordenados: {end_time_1000_desord - start_time_1000_desord} segundos")

# Lista quase ordenada ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Lista quase ordenada: lista_10_QuaseOrdenado
start_time_10_QuaseOrd = time.time()
print(bubble_sort(listas.lista_10_QuaseOrdenado))
end_time_10_QuaseOrd = time.time()
print(f"Tempo de execução com a lista de 10 elementos Quase Ordenados: {end_time_10_QuaseOrd - start_time_10_QuaseOrd} segundos")

# Lista quase ordenada: lista_25_QuaseOrdenado
start_time_25_QuaseOrd = time.time()
print(bubble_sort(listas.lista_25_QuaseOrdenado))
end_time_25_QuaseOrd = time.time()
print(f"Tempo de execução com a lista de 25 elementos Quase Ordenados: {end_time_25_QuaseOrd - start_time_25_QuaseOrd} segundos")

# Lista quase ordenada: lista_50_QuaseOrdenado
start_time_50_QuaseOrd = time.time()
print(bubble_sort(listas.lista_50_QuaseOrdenado))
end_time_50_QuaseOrd = time.time()
print(f"Tempo de execução com a lista de 50 elementos Quase Ordenados: {end_time_50_QuaseOrd - start_time_50_QuaseOrd} segundos")

# Lista quase ordenada: lista_100_QuaseOrdenado
start_time_100_QuaseOrd = time.time()
print(bubble_sort(listas.lista_100_QuaseOrdenado))
end_time_100_QuaseOrd = time.time()
print(f"Tempo de execução com a lista de 100 elementos Quase Ordenados: {end_time_100_QuaseOrd - start_time_100_QuaseOrd} segundos")

# Lista quase ordenada: lista_1000_QuaseOrdenado
start_time_1000_QuaseOrd = time.time()
print(bubble_sort(listas.lista_1000_QuaseOrdenado))
end_time_1000_QuaseOrd = time.time()
print(f"Tempo de execução com a lista de 1000 elementos Quase Ordenados: {end_time_1000_QuaseOrd - start_time_1000_QuaseOrd} segundos")

# lista inversamente ordenada ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# lista inversamente ordenada: lista_10_InversamenteOrdenado
start_time_10_InversamenteOrd = time.time()
print(bubble_sort(listas.lista_10_InversamenteOrdenado))
end_time_10_InversamenteOrd = time.time()
print(f"Tempo de execução com a lista de 10 elementos Inversamente Ordenados: {end_time_10_InversamenteOrd - start_time_10_InversamenteOrd} segundos")

# lista inversamente ordenada: lista_25_InversamenteOrdenado
start_time_25_InversamenteOrd = time.time()
print(bubble_sort(listas.lista_25_InversamenteOrdenado))
end_time_25_InversamenteOrd = time.time()
print(f"Tempo de execução com a lista de 25 elementos Inversamente Ordenados: {end_time_25_InversamenteOrd - start_time_25_InversamenteOrd} segundos")
# lista inversamente ordenada: lista_50_InversamenteOrdenado
start_time_50_InversamenteOrd = time.time()
print(bubble_sort(listas.lista_50_InversamenteOrdenado))
end_time_50_InversamenteOrd = time.time()
print(f"Tempo de execução com a lista de 50 elementos Inversamente Ordenados: {end_time_50_InversamenteOrd - start_time_50_InversamenteOrd} segundos")

# lista inversamente ordenada: lista_100_InversamenteOrdenado
start_time_100_InversamenteOrd = time.time()
print(bubble_sort(listas.lista_100_InversamenteOrdenado))
end_time_100_InversamenteOrd = time.time()
print(f"Tempo de execução com a lista de 100 elementos Inversamente Ordenados: {end_time_100_InversamenteOrd - start_time_100_InversamenteOrd} segundos")

# lista inversamente ordenada: lista_1000_InversamenteOrdenado
start_time_1000_InversamenteOrd = time.time()
print(bubble_sort(listas.lista_1000_InversamenteOrdenado))
end_time_1000_InversamenteOrd = time.time()
print(f"Tempo de execução com a lista de 1000 elementos Inversamente Ordenados: {end_time_1000_InversamenteOrd - start_time_1000_InversamenteOrd} segundos")

