import os
import time
import random
from collections import deque
import heapq


n = 16
count = 0
max_iteration = 10000000

def find_zero(board):
    index = 0
    for i in range(n):
        if board[i] == 0:
            index = i
            break
    return index

def new_tuple_generation(mainTuple, value_tuple):
    zero_address = 0
    next_address = 0
    for i in range(len(mainTuple)):
        if mainTuple[i] == 0:
            zero_address = i
        if mainTuple[i] == value_tuple:
            next_address = i

    mainTuple[zero_address], mainTuple[next_address] = mainTuple[next_address], mainTuple[zero_address]

    return mainTuple

def board_move(index_zero_position, board, current_direction_possibilities,
               possibilities):
    if index_zero_position == 0:
        current_direction_possibilities.append((board[index_zero_position + 1],
                                                "east"))
        current_direction_possibilities.append((board[index_zero_position + 4],
                                                "south"))
    elif index_zero_position == 3:
        current_direction_possibilities.append((board[index_zero_position - 1],
                                                "west"))
        current_direction_possibilities.append((board[index_zero_position + 4],
                                                "south"))
    elif index_zero_position == 12:
        current_direction_possibilities.append((board[index_zero_position + 1],
                                                "east"))
        current_direction_possibilities.append((board[index_zero_position - 4],
                                                "north"))
    elif index_zero_position == 15:
        current_direction_possibilities.append((board[index_zero_position - 1],
                                                "west"))
        current_direction_possibilities.append((board[index_zero_position - 4],
                                                "north"))
    elif index_zero_position in [1, 2]:
        current_direction_possibilities.append((board[index_zero_position + 1],
                                                "east"))
        current_direction_possibilities.append((board[index_zero_position - 1],
                                                "west"))
        current_direction_possibilities.append((board[index_zero_position + 4],
                                                "south"))
    elif index_zero_position in [13, 14]:
        current_direction_possibilities.append((board[index_zero_position + 1],
                                                "east"))
        current_direction_possibilities.append((board[index_zero_position - 1],
                                                "west"))
        current_direction_possibilities.append((board[index_zero_position - 4],
                                                "north"))
    elif index_zero_position in [4, 8]:
        current_direction_possibilities.append((board[index_zero_position + 1],
                                                "east"))

        current_direction_possibilities.append((board[index_zero_position - 4],
                                                "north"))

        current_direction_possibilities.append((board[index_zero_position + 4],
                                                "south"))
    elif index_zero_position in [7, 11]:
        current_direction_possibilities.append((board[index_zero_position - 1],
                                                "west"))

        current_direction_possibilities.append((board[index_zero_position - 4],
                                                "north"))

        current_direction_possibilities.append((board[index_zero_position + 4],
                                                "south"))
    else:
        current_direction_possibilities.append((board[index_zero_position + 1],
                                                "east"))
        current_direction_possibilities.append((board[index_zero_position - 1],
                                                "west"))
        current_direction_possibilities.append((board[index_zero_position + 4],
                                                "south"))
        current_direction_possibilities.append((board[index_zero_position - 4],
                                                "north"))


def solve_dfs(init_board):

    stack = []
    visited = set()
    loop_count = 0

    init_snapshot = tuple(init_board) # it pass the initial board as a list
    init_path = []

    stack.append((init_snapshot, init_path))

    while len(stack) > 0:
        current_snapshot, current_path = stack.pop()

        if current_snapshot in visited:
            continue

        visited.add(current_snapshot)

        if current_snapshot == (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
                                15, 0):
            print("Winner board")
            return current_path, list(visited)

        if loop_count >= max_iteration:
            print("Timeout reached! No solution found")
            return [], list(visited)
        loop_count += 1


        board = list(current_snapshot)
        index_zero_position = find_zero(board)
        current_direction_possibilities = []
        possibilities = []

        board_move(index_zero_position, board, current_direction_possibilities,
                   possibilities)

        for target, direction in current_direction_possibilities:
            new_tuple = tuple()
            new_tuple = tuple(new_tuple_generation(list(current_snapshot),
                                                   target))
            new_history = current_path + [direction]
            stack.append((new_tuple, new_history))

def solve_bfs(init_board):

    stack = deque()
    visited = set() # The solver takes O(1) to find the a board using set()'s
    loop_count = 0

    init_snapshot = tuple(init_board) # I will pass the initial board as a list
    init_path = []

    stack.append((init_snapshot, init_path))

    while len(stack) > 0:
        current_snapshot, current_path = stack.popleft()

        if current_snapshot in visited:
            continue

        visited.add(current_snapshot)

        if current_snapshot == (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
                                15, 0):
            print("Winner board")
            return current_path, list(visited)

        if loop_count >= max_iteration:
            print("Timeout reached! No solution found")
            return [], list(visited)
        loop_count += 1


        board = list(current_snapshot)
        index_zero_position = find_zero(board)
        current_direction_possibilities = []
        possibilities = []

        board_move(index_zero_position, board, current_direction_possibilities,
                   possibilities)

        for target, direction in current_direction_possibilities:
            new_tuple = tuple()
            new_tuple = tuple(new_tuple_generation(list(current_snapshot),
                                                   target))
            new_history = current_path + [direction]
            stack.append((new_tuple, new_history))

def get_manhattan_score(board):
    total_score = 0

    for i in range(n):
        tile_value = board[i]
        if tile_value == 0:
            continue

        current_row =  i // 4
        current_column = i % 4

        winning_position = tile_value - 1
        winning_row = winning_position // 4
        winning_column = winning_position % 4

        row_distance = abs(current_row - winning_row)
        column_distance = abs(current_column - winning_column)

        total_score += row_distance + column_distance

    return total_score

def solve_astar(init_board):
    pq = []
    visited = set()
    loop_count = 0

    init_snapshot = tuple(init_board)
    init_path = []
    init_score = get_manhattan_score(init_snapshot)

    heapq.heappush(pq, (init_score, init_snapshot, init_path))

    while len(pq) > 0:
        current_score, current_snapshot, current_path = heapq.heappop(pq)

        if current_snapshot in visited:
            continue

        visited.add(current_snapshot)

        if current_snapshot == (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
                                15, 0):
            print("Winner board")
            return current_path, list(visited)

        if loop_count >= max_iteration:
            print("Timeout reached! No solution found")
            return [], list(visited)

        loop_count += 1

        board = list(current_snapshot)
        index_zero_position = find_zero(board)
        current_direction_possibilities = []
        possibilities = []

        board_move(index_zero_position, board, current_direction_possibilities,
                   possibilities)

        for target, direction in current_direction_possibilities:
            new_tuple = tuple()
            new_tuple = tuple(new_tuple_generation(list(current_snapshot),
                                                   target))
            new_history = current_path + [direction]
            new_score = get_manhattan_score(list(new_tuple)) + len(new_history) # the heuristic need (+ len(new_history))
            heapq.heappush(pq, (new_score, new_tuple, new_history))



while True:
    count_is_even = 0
    numbers = random.sample(range(1,16),15)
    numbers.append(0)


    # Check solutions -----------------------------------------------------
    # If the 0 is on an ODD row from the bottom (Row 1 or 3),
    #  the total number of inversions MUST be an EVEN number.
    for i in range(n):
        for j in range(n):
            if j > i:
                if numbers[i] == 0 or numbers[j] == 0:
                    continue
                if numbers[i] > numbers[j]:
                    count_is_even += 1

    if count_is_even % 2 == 0:
        print("The actual board can be solved!!\n")
        break
    else:
        print("The actual board can't be solved!!\n")
    print(count_is_even)


# Game Loop ---------------------------------------------------------------
# IA Solver


#numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 11, 13, 14, 0, 12]
#numbers.append(0)

os.system("clear")
# Solver dfs
#final_path, modificated_boards = solve_dfs(numbers)
# Solver bfs
#final_path, modificated_boards = solve_bfs(numbers)
#Sorver Astar
start = time.time()
final_path, modificated_boards = solve_astar(numbers)
end = time.time()
print(final_path)
print(len(final_path))
print("time: ", (end - start))

#for board in modificated_boards:
#    for i in range(n):
#        if i > 0 and i % 4 == 0:
#            print()

#        print(f"{board[i]:<4}", end="")

#    print("\n-----------------")
