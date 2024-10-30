import time
import matplotlib.pyplot as plt

# Supondo que essas listas estejam definidas em seus respectivos módulos
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

# Função para medir o tempo de execução do sort
def medir_tempo_sort(lista):
    start_time = time.perf_counter()
    lista.sort()
    end_time = time.perf_counter()
    return (end_time - start_time) * 1000  # Converte para milissegundos

# Medindo os tempos de execução
tempos = {
    'Desordenada': [
        medir_tempo_sort(lista_10_Desordenado),
        medir_tempo_sort(lista_25_Desordenado),
        medir_tempo_sort(lista_50_Desordenado),
        medir_tempo_sort(lista_100_Desordenado),
        medir_tempo_sort(lista_1000_Desordenado)
    ],
    'Quase Ordenada': [
        medir_tempo_sort(lista_10_QuaseOrdenado),
        medir_tempo_sort(lista_25_QuaseOrdenado),
        medir_tempo_sort(lista_50_QuaseOrdenado),
        medir_tempo_sort(lista_100_QuaseOrdenado),
        medir_tempo_sort(lista_1000_QuaseOrdenado)
    ],
    'Inversamente Ordenada': [
        medir_tempo_sort(lista_10_InversamenteOrdenado),
        medir_tempo_sort(lista_25_InversamenteOrdenado),
        medir_tempo_sort(lista_50_InversamenteOrdenado),
        medir_tempo_sort(lista_100_InversamenteOrdenado),
        medir_tempo_sort(lista_1000_InversamenteOrdenado)
    ],
}

# Rótulos para o eixo y
tamanhos = ['10', '25', '50', '100', '1000']

# Criando o gráfico
plt.figure(figsize=(10, 6))

# Bar width
bar_width = 0.25
y = range(len(tamanhos))

# Plotando os tempos de execução para cada tipo de lista
for i, (tipo, tempos_lista) in enumerate(tempos.items()):
    plt.barh([p + bar_width * i for p in y], tempos_lista, height=bar_width, label=tipo)

# Adicionando detalhes ao gráfico
plt.title('Tempo de Execução do Algoritmo de Ordenação - Sort (ms)')
plt.xlabel('Tempo de Execução (ms)')
plt.ylabel('Tamanho da Lista')
plt.yticks([p + bar_width for p in y], tamanhos)  # Ajusta os ticks do eixo y
plt.legend()
plt.grid(axis='x')
plt.tight_layout()

# Exibindo o gráfico
plt.show()

