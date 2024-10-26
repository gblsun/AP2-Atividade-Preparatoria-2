'''
Listas:

→ 10, 25, 50, 100, 1000 elementos.

→ Aproximadamente ordenada:
    ↳ Quase em ordem, com poucas trocas necessárias.
Sem repetição: 
    ↳ Todos os elementos são únicos, facilitando a ordenação.
→ Tamanhos em décadas: 
    ↳ Listas de diferentes tamanhos, mas com potencial para organização.
→ Estável/instável: 
    ↳ Depende do algoritmo usado, mantendo ou alterando a ordem de itens iguais.
→ Randômica: 
    ↳ Elementos aleatórios, sem padrão.
→ Totalmente desordenada: 
    ↳ Sem qualquer ordem, a mais desorganizada.
'''

# imports
import random

# Lista Aproximadamente ordenada

def generate_approx_sorted_list(n):
    # Gera uma lista com números em ordem crescente de 0 a n-1
    sorted_list = list(range(n))
    
    # Determina o número de elementos a serem embaralhados
    num_to_shuffle = int(n * 0.2)  # 20% da lista será embaralhada
    
    # Embaralha os primeiros num_to_shuffle elementos
    indices_to_shuffle = random.sample(range(n), num_to_shuffle)  # Seleciona índices aleatórios
    '''
    → random.sample(population, k)
        ↳ population: A sequência de onde os elementos serão escolhidos (pode ser uma lista, um intervalo, etc.).
        ↳ k: O número de elementos a serem selecionados aleatoriamente.'''
    random.shuffle(shuffled_values)  # Embaralha esses valores

    # Coloca os valores embaralhados de volta na lista
    for idx, value in zip(indices_to_shuffle, shuffled_values):
        sorted_list[idx] = value  # Substitui o valor original pelo valor embaralhado

    return sorted_list  # Retorna a lista aproximadamente ordenada

# Cria um dicionário para armazenar listas de diferentes tamanhos
lists = {
    "10 elementos": generate_approx_sorted_list(10),   # Gera lista de 10 elementos
    "25 elementos": generate_approx_sorted_list(25),   # Gera lista de 25 elementos
    "50 elementos": generate_approx_sorted_list(50),   # Gera lista de 50 elementos
    "100 elementos": generate_approx_sorted_list(100), # Gera lista de 100 elementos
    "1000 elementos": generate_approx_sorted_list(1000), # Gera lista de 1000 elementos
}

