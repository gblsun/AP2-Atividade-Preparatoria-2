# função troca
def troca(lista, i, j):
    lista[i], lista[j] = lista[j], lista[i]

# função particionamento
def particiona(lista, inicio, fim):
    pivo = lista[inicio]
    i = inicio
    for j in range(inicio + 1, fim + 1):
        if lista[j] <= pivo:
            i += 1
            troca(lista, i, j)
    troca(lista, inicio, i)
    return i

# Função quick_sort
def quick_sort(lista, inicio, fim):
    if inicio < fim:
        posicao = particiona(lista, inicio, fim)
        quick_sort(lista, inicio, posicao - 1)
        quick_sort(lista, posicao + 1, fim)
        