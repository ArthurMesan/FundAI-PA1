import random
from random import randrange
import statistics

numThings = 50

w = []
p = []
try:
    with open("mochila.txt") as f:
        n = int(f.readline())
        c = int(f.readline())
        blank_line = f.readline()
        for i in range(numThings):
            linha = f.readline()
            partes = linha.split()
            p.append(int(partes[0]))
            w.append(int(partes[1]))
except FileNotFoundError:
    print("Erro: Arquivo 'mochila.txt' não encontrado. Certifique-se de que ele está na mesma pasta.")
    exit()

def random_index(pop_size):
    a = -1
    b = -2
    while(True):
        if(a <= -1 or a == b):
            a = randrange(pop_size)
        elif(b <= -1 or b == a):
            b = randrange(pop_size)
        else:
            return a, b

def cal_fit(target, value, weight, max_w):
    sum_p = 0
    sum_w = 0
    count = 1
    for i in range(numThings):
        if(target[i] == 1):
            sum_p += value[i]
            sum_w += weight[i]
            if(sum_w > max_w):
                sum_p -= count*10000000
                count += 1
    return sum_p

def run_ga(size, cr_prob, mut_prob, max_iter=50000):
    bags = []

    # Inicialização da População
    for i in range(size):
        items = []
        for j in range(numThings):
            items.append(random.randint(0,1))
        bags.append(items)

    iteration = 0
    best_overall_fit = -float('inf')

    while(iteration <= max_iter):
        pa, pb = random_index(size)
        parent_A = bags[pa]
        parent_B = bags[pb]
        p_new = []

        # Cruzamento (Crossover) baseado em probabilidade
        if random.random() <= cr_prob:
            for i in range(numThings):
                if i < 25:
                    p_new.append(parent_A[i])
                else:
                    p_new.append(parent_B[i])
        else:
            # Se não cruzar, o filho é um clone do Pai A
            p_new = list(parent_A)

        # Mutação baseada em probabilidade (mut_prob)
        for i in range(numThings):
            if random.random() <= mut_prob:
                if p_new[i] == 0:
                    p_new[i] = 1
                else:
                    p_new[i] = 0

        # Avaliação
        fit_parent_A = cal_fit(parent_A, p, w, c)
        fit_parent_B = cal_fit(parent_B, p, w, c)
        fit_p_new = cal_fit(p_new, p, w, c)

        # Substituição (Sua lógica original)
        if fit_parent_B < fit_parent_A:
            if(fit_parent_B < fit_p_new):
                bags[pb] = p_new
        else:
            if(fit_parent_A < fit_p_new):
                bags[pa] = p_new

        # Registra o melhor valor encontrado
        if fit_p_new > best_overall_fit:
            best_overall_fit = fit_p_new

        iteration += 1

    # Retorna a melhor mochila gerada nesta execução
    return best_overall_fit

# Configurações: (Tamanho da População, Probabilidade de Cruzamento, Probabilidade de Mutação)
configurations = [
    (20, 1.0, 0.05),
    (50, 1.0, 0.05),
    (50, 0.8, 0.10),
    (50, 0.5, 0.01),
    (100, 1.0, 0.05)
]

num_runs = 30 # 30 vezes para cada configuração

print(f"{'Pop Size':<10} | {'Taxa Cruz.':<10} | {'Taxa Mut.':<10} | {'Media Valor (Fit)':<20} | {'Desvio Padrao':<15}")
print("-" * 75)

for pop_size, cr_prob, mut_prob in configurations:
    results = []
    for run in range(num_runs):
        fit_result = run_ga(pop_size, cr_prob, mut_prob, max_iter=50000)
        results.append(fit_result)

    mean_val = statistics.mean(results)
    std_val = statistics.stdev(results) if len(results) > 1 else 0.0

    print(f"{pop_size:<10} | {cr_prob:<10} | {mut_prob:<10} | {mean_val:<20.1f} | {std_val:<15.2f}")
