
# **AP2 - Atividade Preparatória 2**

A nota da AP2 será composta por uma prova parcial realizada em sala de aula com peso 80% e atividades preparatórias a serem realizadas e entregues na data estipulada, com peso 20%. A média das atividades preparatórias da AP2 contribui, portanto, com até 5% (meio ponto) da média final da disciplina. 
A simples entrega da atividade preparatória confere nota 10, porém a entrega da atividade será desconsiderada se, durante a correção da atividade em sala de aula, alguma questão não for devidamente respondida em aula. A seleção de quem deverá responder às questões em sala será feita mediante sorteio. 

# **Enunciado**

## A escolha do algoritmo de ordenação para uma dada situação não depende apenas de sua complexidade teórica, mas das características dos dados que se deseja ordenar, tais como a quantidade e distribuição dos dados. Você deve elaborar um relatório explorando o desempenho dos algoritmos de ordenação abordados no curso (com exceção do Bogo Sort). O relatório deve conter:

1. **Introdução**: pesquise e explique como o tamanho da lista e a distribuição dos dados podem influenciar na escolha do algoritmo de ordenação a ser adotado;
2. **Materiais e métodos** : demonstre empiricamente o efeito do tamanho e distribuição dos dados no desempenho de cada algoritmo de ordenação.
Mencione como os algoritmos foram implementados, os cenários de teste e como será avaliado o desempenho. Se possível, inclua as versões dos softwares (versão do Python, versão da IDE) e configurações do hardware (Sistema operacional, CPU, memória) utilizados para realizar os experimentos. IMPORTANTE: a linguagem Python disponibiliza a função sort, que realiza a ordenação de uma lista sem que tenhamos que nos preocupar com o algoritmo utilizado. Pesquise qual(is) algoritmo(s) a função sort adota ao fazer a ordenação de uma lista e como esta escolha é feita. Inclua esta função em seus experimentos;
3. **Resultados e discussão**: apresente os resultados dos experimentos por meio de gráficos e tabelas para exibir o desempenho dos diferentes algoritmos em função do tamanho da lista e da distribuição dos dados, com a interpretação destes resultados;
4. **Conclusão**: descreva as principais conclusões obtidas com os experimentos, indicando quais algoritmos seriam mais adequados para cada situação. Mencione possíveis limitações dos experimentos realizados;
5. **Anexos**:  Inclua o código fonte utilizado para os experimentos.



obs:
~~~
project_root/
│
├── lists.py                         # Define listas de diferentes tamanhos para os testes
├── main.py                          # Executa o projeto principal, chamando todos os testes de cada algoritmo
│
├── sorting_algorithms/              # Pasta principal para os algoritmos de ordenação
│   │
│   ├── simple/                      # Pasta para algoritmos de ordenação simples
│   │   ├── bubble_sort/
│   │   │   ├── bubble_sort.py       # Implementação do Bubble Sort
│   │   │   ├── time_test_bubble_sort.py         # Teste de tempo para Bubble Sort
│   │   │   ├── line_profile_test_bubble_sort.py # Teste de desempenho por linha para Bubble Sort
│   │   │   └── memory_test_bubble_sort.py       # Teste de memória para Bubble Sort
│   │   │
│   │   ├── selection_sort/
│   │   │   ├── selection_sort.py    # Implementação do Selection Sort
│   │   │   ├── time_test_selection_sort.py         # Teste de tempo para Selection Sort
│   │   │   ├── line_profile_test_selection_sort.py # Teste de desempenho por linha para Selection Sort
│   │   │   └── memory_test_selection_sort.py       # Teste de memória para Selection Sort
│   │   │
│   │   └── insertion_sort/
│   │       ├── insertion_sort.py    # Implementação do Insertion Sort
│   │       ├── time_test_insertion_sort.py         # Teste de tempo para Insertion Sort
│   │       ├── line_profile_test_insertion_sort.py # Teste de desempenho por linha para Insertion Sort
│   │       └── memory_test_insertion_sort.py       # Teste de memória para Insertion Sort
│   │
│   └── efficient/                   # Pasta para algoritmos de ordenação eficiente
│       ├── heap_sort/
│       │   ├── heap_sort.py         # Implementação do Heap Sort
│       │   ├── time_test_heap_sort.py         # Teste de tempo para Heap Sort
│       │   ├── line_profile_test_heap_sort.py # Teste de desempenho por linha para Heap Sort
│       │   └── memory_test_heap_sort.py       # Teste de memória para Heap Sort
│       │
│       ├── merge_sort/
│       │   ├── merge_sort.py        # Implementação do Merge Sort
│       │   ├── time_test_merge_sort.py         # Teste de tempo para Merge Sort
│       │   ├── line_profile_test_merge_sort.py # Teste de desempenho por linha para Merge Sort
│       │   └── memory_test_merge_sort.py       # Teste de memória para Merge Sort
│       │
│       ├── quick_sort/
│       │   ├── quick_sort.py        # Implementação do Quick Sort
│       │   ├── time_test_quick_sort.py         # Teste de tempo para Quick Sort
│       │   ├── line_profile_test_quick_sort.py # Teste de desempenho por linha para Quick Sort
│       │   └── memory_test_quick_sort.py       # Teste de memória para Quick Sort
│       │
│       └── sort_internal/
│           ├── sort_internal.py     # Função interna de ordenação (Python `sorted`)
│           ├── time_test_sort_internal.py         # Teste de tempo para função interna
│           ├── line_profile_test_sort_internal.py # Teste de desempenho por linha para função interna
│           └── memory_test_sort_internal.py       # Teste de memória para função interna
~~~