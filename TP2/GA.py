import random
from random import randrange

# Initial bags family
size = 50
numThings = 50
bags = []
cr = 0.5

def random_index():
    a = -1
    b = -2
    while(True):
        if(a <= -1 or a == b):
            a = randrange(50)
        elif(b <= -1 or b == a):
            b = randrange(50)
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
def cal_w(target, weight):
    sum_w = 0
    for i in range(numThings):
        if(target[i] == 1):
            sum_w += weight[i]
    return sum_w


for i in range(size):
    items = []
    for j in range(numThings):
        items.append(random.randint(0,1))

    bags.append(items)

for i in range(size):
    for j in range(numThings):
        print(f"{bags[i][j]:>2}", end=" ")
    print()

w = []
p = []
with open("mochila.txt") as f:
    n = int(f.readline())
    c = int(f.readline())
    blank_line = f.readline()
    for i in range(numThings):
        linha = f.readline()
        partes = linha.split()

        p.append(int(partes[0]))
        w.append(int(partes[1]))

# Loop
iteration = 0
while(iteration <= 1000000):
    pa, pb = random_index()
    parent_A = bags[pa]
    parent_B = bags[pb]
    p_new = []

    biggest_fit = -1

    for i in range(numThings):
        if i < 25:
            p_new.append(parent_A[i])
        else:
            p_new.append(parent_B[i])


    #Mutation
    for i in range(numThings):
        if random.random() <= 0.05:
            # If it is 0, make it 1. If it is 1, make it 0.
            if p_new[i] == 0:
                p_new[i] = 1
            else:
                p_new[i] = 0


    fit_parent_A = cal_fit(parent_A, p, w, c)
    fit_parent_B = cal_fit(parent_B, p, w, c)
    fit_p_new = cal_fit(p_new, p, w, c)

    if fit_parent_B < fit_parent_A:
        if(fit_parent_B < fit_p_new):
            # Put the LIST in, not the integer!
            bags[pb] = p_new
        biggest_fit  = pb
    else:
        if(fit_parent_A < fit_p_new):
            # Put the LIST in, not the integer!
            bags[pa] = p_new
        biggest_fit = pa

    iteration += 1

print("Otimum result...")

for i in range(size):
    for j in range(numThings):
        print(f"{bags[i][j]:>2}", end=" ")
    print()
print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("bag: ",biggest_fit)
print(bags[biggest_fit])
print("fit: ", cal_fit(bags[biggest_fit], p, w, c))
print("weight: ", cal_w(bags[biggest_fit], w))
print
