import random
from random import randrange
import statistics

maxp = 5
minp = -5

def random_index(index, num_pop):
    a = -1
    b = -2
    c = -3
    while(True):
        if(a == index or a <= -1 or a == b or a == c):
            a = randrange(num_pop)
        elif(b == index or b <= -1 or b == a or b == c):
            b = randrange(num_pop)
        elif(c == index or c <= -1 or c == a or c == b):
            c = randrange(num_pop)
        else:
            return a, b, c

def f_sum(population):
    sum_val = 0
    for i in range(10):
        sum_val += population[i]**2
    return sum_val

def normalize(population):
    for i in range(10):
        if population[i] < -5:
            population[i] = -5
        if population[i] > 5:
            population[i] = 5
    return population

def run_de(numberPopulations, f, cr):
    population = []

    for i in range(numberPopulations):
        people = []
        for j in range(10):
            people.append(random.randint(minp,maxp))
        population.append(people)

    iteration = 0

    while(iteration <= 100000):
        k = randrange(10)
        ring_index = iteration % numberPopulations
        actual_population = population[ring_index]

        a, b, c = random_index(ring_index, numberPopulations)
        p_a, p_b, p_c = population[a], population[b], population[c]

        p_mutant = []

        for i in range(10):
            math_result = p_a[i] + f*(p_b[i] - p_c[i])
            p_mutant.append(math_result)

        p_mutant = normalize(p_mutant)
        p_new = []

        for i in range(10):
            if random.random() <= cr or i == k:
                p_new.append(p_mutant[i])
            else:
                p_new.append(actual_population[i])

        if f_sum(actual_population) > f_sum(p_new):
            population[ring_index] = p_new

            if f_sum(p_new) < 0.0001:
                return iteration // numberPopulations

        iteration += 1

    return iteration // numberPopulations

configurations = [
    (20, 0.8, 0.9),
    (50, 0.6, 0.5),
    (50, 0.9, 0.1),
    (50, 0.1, 0.9),
    (50, 0.8, 0.9),
    (100, 0.5, 0.5),
    (100, 0.8, 0.2)
]

print(f"{'Pop Size':<10} | {'F':<5} | {'CR':<5} | {'Media Geracoes':<15} | {'Desvio Padrao':<15}")
print("-" * 60)

for pop_size, f_val, cr_val in configurations:
    results = []
    for _ in range(30):
        results.append(run_de(pop_size, f_val, cr_val))

    mean_val = statistics.mean(results)
    std_val = statistics.stdev(results)
    print(f"{pop_size:<10} | {f_val:<5} | {cr_val:<5} | {mean_val:<15.1f} | {std_val:<15.2f}")
