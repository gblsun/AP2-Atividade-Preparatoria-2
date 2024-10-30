def troca(s, i, j):
    s[i], s[j] = s[j], s[i]


def empurra(s, n):
    for i in range(n-1):
        if s[i] > s[i+1]:
            troca(s, i, i+1)


def bubble_sort(s):
    n = len(s)
    while n > 1:
        empurra(s, n)
        n -= 1
    return s