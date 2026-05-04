# Old structure

class graph:
    def __init__(self,value):
        self.value =  value

        self.north = None
        self.south = None
        self.east = None
        self.west = None


# Building the Board ------------------------------------------------------------------
puzzle_nodes = [graph(i) for i in range(16)]

for node in range(len(puzzle_nodes)):
    if node in [3,7,11,15]:
        puzzle_nodes[node].east = None
        continue
    puzzle_nodes[node].east = puzzle_nodes[node + 1]

for node in range(len(puzzle_nodes)):
    if node in [0,4,8,12]:
        puzzle_nodes[node].west = None
        continue
    puzzle_nodes[node].west = puzzle_nodes[node - 1]

for i in range(4):
    for j in range(4):
        idx = j*4 + i
        if (idx) in [12,13,14,15]:
            puzzle_nodes[idx].south = None
            continue
        puzzle_nodes[idx].south =  puzzle_nodes[idx + 4]

for i in range(4):
    for j in range(4):
        idx = j*4 + i
        if (idx) in [0,1,2,3]:
            puzzle_nodes[idx].north = None
            continue
        puzzle_nodes[idx].north =  puzzle_nodes[idx - 4]



#os.system("clear")
input_number = 0
while(input_number != -1):
    for i in range(n):
        if count % 4 == 0:
            print()
            print(f"{numbers[i]:<4}", end="")
        else:
            print(f"{numbers[i]:<4}", end="")
        count += 1

    input_number = int(input("\nInput a number: "))

    #os.system("clear")
