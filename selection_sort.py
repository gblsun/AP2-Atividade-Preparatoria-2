def troca(s, i, j):
    s[i], s[j] = s[j], s[i]

def indice_menor_elemento(s, n):
    indice_menor = n
    for i in range(n, len(s)):
        if s[i] < s[indice_menor]:
            indice_menor = i
    return indice_menor

def selection_sort(s):
    n = 0
    while n < len(s):
        indice_menor = indice_menor_elemento(s, n)
        if indice_menor != n:
            troca(s, n, indice_menor)
        n += 1