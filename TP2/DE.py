import random
from random import randrange
import os

x = []
vet_index = []
population = []
numberPopulations = 50

maxp = 5
minp = -5

def random_index(index):
    a = -1
    b = -2
    c = -3
    while(True):
        if(a == index or a <= -1 or a == b or a == c):
            a = randrange(50)
        elif(b == index or b <= -1 or b == a or b == c):
            b = randrange(50)
        elif(c == index or c <= -1 or c == a or c == b):
            c = randrange(50)
        else:
            return a, b, c

def f_sum(population):
    sum = 0
    for i in range(10):
        sum += population[i]**2
    return sum



def normalize(population):
    for i in range(10):
        if population[i] < -5:
            population[i] = -5
        if population[i] > 5:
            population[i] = 5
    return population



# Initial population family
size = 10
for i in range(numberPopulations):
    people = []
    for j in range(10):
        people.append(random.randint(minp,maxp))

    population.append(people)


print("------------------------------------------")

for i in range(numberPopulations):
    for j in range(10):
        print(f"{population[i][j]:>5.1f}", end=" ")
    print()

#print(population[0])

iteration = 0
f = 0.6
cr = 0.5
loading_size = 5

while(iteration <= numberPopulations*100):
    k = randrange(10)
    ring_index = iteration % numberPopulations
    actual_population = population[ring_index]

    a, b, c = random_index(ring_index)
    p_a, p_b, p_c = population[a], population[b], population[c]

    p_mutant = []

    for i in range(10):
        #Mutation $$v_i = x_{r1} + F \cdot (x_{r2} - x_{r3})$$
        math_result = p_a[i] + f*(p_b[i] - p_c[i])
        p_mutant.append(math_result)

    p_mutant = normalize(p_mutant)
    p_new = []
    #print("p_mutant: ", p_mutant)
    for i in range(10):
        if random.random() <= cr or i == k:
            p_new.append(p_mutant[i])
        else:
            p_new.append(actual_population[i])

    if f_sum(actual_population) > f_sum(p_new):
        population[ring_index] = p_new

    ring_loading = iteration
    iteration += 1

print("Otimum result")
#print("p_new: ",p_new)

print("------------------------------------------")

for i in range(numberPopulations):
    for j in range(10):
        print(f"{population[i][j]:>5.1f}", end=" ")
    print()
