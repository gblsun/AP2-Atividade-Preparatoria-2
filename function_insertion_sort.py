def troca(s, i, j):
    s[i], s[j] = s[j], s[i]
    
def move_para_esquerda(s, i):
    while i > 0 and s[i] < s[i - 1]:
        troca(s, i, i - 1)

def insertion_sort_modificado(s):
    for i in range(1, len(s)):
        move_para_esquerda(s, i)
        i -= 1