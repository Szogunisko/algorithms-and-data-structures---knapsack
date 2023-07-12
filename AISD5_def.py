import random

#Generating input values for n items
def randomize_items(n):
    items = []
    for i in range(n):
        Si = random.randint(10, 1000) #weight
        Wi = random.randint(100, 10000) #value
        items.append([Si,Wi])
    return items

#Calculating b factor depending on the total weight of items and percentage ratio
def b_factor(items, ratio):
    b = 0
    for i in range(len(items)):
        b += items[i][0]
    b *= ratio
    return int(b)

# Exemplary items
# items = [[5,3],[3,4],[2,2],[4,6],[3,1]] #(si weight,wi value)
# b = 10
# n = 5

# Creating one solution for Brute Force method
def bin(digit, n):
   arr = []
   for i in range(digit):
       arr.append(n%2)
       n = n>>1

   bin_list = []
   for i in range(digit-1, -1, -1):
       bin_list.append(arr[i])
   return bin_list

# Creating all solutions for Brute Force method
def generateAllBin(n):
   possibilities = []
   high = int(pow(2, n))
   for i in range(high):
       x = bin(n, i)
       possibilities.append(x)
   return possibilities

# Brute Force method
def bf(items, b):
    possibilities = generateAllBin(len(items))

    possibility = 0
    max_value = 0
    for i in range(len(possibilities)):
        weight = 0
        value = 0
        for j in range(len(items)):
            weight += items[j][0] * possibilities[i][j]
            value += items[j][1] * possibilities[i][j]
        if weight <= b:
            if value > max_value:
                max_value = value
                possibility = possibilities[i]
    return max_value, possibility


# Brute Force method with elimination of unacceptable solutions
def bf2(items, b):
    n = len(items)
    best_value = 0
    best_solution = [0] * n

    def tree(i, current_weight, current_value, current_solution):
        nonlocal best_value, best_solution

        if current_weight > b:
            return

        if i == n:
            if current_value > best_value:
                best_value = current_value
                best_solution = current_solution
            return

        # The case when we take the i-th item
        current_solution[i] = 1
        tree(i + 1, current_weight + items[i][0], current_value + items[i][1], current_solution)

        # The case when we do not take the i-th item
        current_solution[i] = 0
        tree(i + 1, current_weight, current_value, current_solution)

    tree(0, 0, 0, [0] * n)
    return best_value





# lista = generateAllBin(5)
# solution = bf(items, 10)
# print(solution)
# print("--------")

# 1st heuristic - random
def GH1(items, b):
    n = len(items)
    items2 = []
    for i in range(n):
        A = items[i].copy()
        items2.append(A)
    taken = [0]*n
    weight = 0
    value = 0
    while True:
        a = random.randint(0,n-1)
        if weight + items2[a][0] <= b:
            if taken[a] == 0:
                weight += items2[a][0]
                value += items2[a][1]
                taken[a] = 1
        else:
            return value, taken

# 2nd heuristic - min weight
def GH2(items, b):
    n = len(items)
    items2 = []
    for i in range(n):
        A = items[i].copy()
        items2.append(A)
    items2.sort()
    weight = 0
    value = 0
    for i in range(n):
        if weight + items2[i][0] <= b:
            weight += items2[i][0]
            value += items2[i][1]
    return value

# 3rd heuristic - max value
def GH3(items, b):
    n = len(items)
    items2 = []
    for i in range(n):
        A = items[i].copy()
        items2.append(A)
    for i in range(n):
        items2[i][0], items2[i][1] = items2[i][1], items2[i][0]
    items2.sort(reverse = True)
    weight = 0
    value = 0
    for i in range(n):
        if weight + items2[i][1] <= b:
            weight += items2[i][1]
            value += items2[i][0]
    return value

# 4th heuristic - max value to weight ratio
def GH4(items, b):
    n = len(items)
    items2 = []
    for i in range(n):
        A = items[i].copy()
        items2.append(A)
    ratios = [0]*n
    for i in range(n):
        ratios[i] += items2[i][1]/items2[i][0]
        items2[i].append(ratios[i])
        items2[i][0], items2[i][2] = items2[i][2], items2[i][0] #now items(ratio, wi, si)
    items2.sort(reverse = True)
    weight = 0
    value = 0
    for i in range(n):
        if weight + items2[i][2] <= b:
            weight += items2[i][2]
            value += items2[i][1]
    return value

# dynamic programming
def DP(items, array, i, l):
    if l == 0:
        array[i][l] = 0
        return 0
    if i == 0:
        array[i][l] = 0
        return 0
    if items[i-1][0] > l:
        array[i][l] = array[i-1][l]
    if items[i-1][0] <= l:
        array[i][l] = max(array[i-1][l],array[i-1][l-items[i-1][0]]+items[i-1][1])

# dynamic programming matrix
def array_DP(items, b):
    n = len(items)
    array = []
    for i in range(n + 1):
        array.append([0] * (b + 1))
    for i in range(1, n + 1):
        for j in range(b + 1):
            DP(items, array, i, j)
    solution = 0
    for i in range(len(array)):
        if max(array[i]) > solution:
            solution = max(array[i])
    return solution, array

# solution, array = array_DP(items, 5,10)
# for i in range(len(array)):
#     print(array[i])
# print(solution)

