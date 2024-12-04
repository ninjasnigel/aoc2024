with open("day4/data.aoc", "r") as file: 
    data = [line.strip("\n") for line in file.readlines()]

order = ['X', 'M', 'A', 'S']

def search(order, i=0, j=0, direction=(0,0)):
    tot = 0
    if not order:
        return 1
    elif direction == (0,0):
        nei = neighbors(i,j)
        for n in nei:
            if data[n[0]][n[1]] == order[0]:
                direction = (n[0]-i, n[1]-j)
                tot += search(order[1:], n[0], n[1], direction=direction)
    else:
        n = (i+direction[0], j+direction[1])
        if 0 <= n[0] < len(data) and 0 <= n[1] < len(data[0]) and data[n[0]][n[1]] == order[0]:
            tot += search(order[1:], n[0], n[1], direction)
    return tot
    
def neighbors(i,j):
    potential_neighbors = [(i+1,j), (i-1,j), (i,j+1), (i,j-1), (i+1,j+1), (i-1,j-1), (i+1,j-1), (i-1,j+1)]
    valid_neighbors = [(x, y) for x, y in potential_neighbors if 0 <= x < len(data) and 0 <= y < len(data)]
    return valid_neighbors

def neightbors_diagonal(i,j):
    potential_neighbors = [(i+1,j+1), (i-1,j-1), (i+1,j-1), (i-1,j+1)]
    valid_neighbors = [(x, y) for x, y in potential_neighbors if 0 <= x < len(data) and 0 <= y < len(data)]
    return valid_neighbors

words = 0

for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] == order[0]:
            words += search(order[1:], i, j)

print(words)

# ---------

crosses = 0

for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] == "A":
            n = [data[x[0]][x[1]] for x in neightbors_diagonal(i,j)]
            if len(n) == 4:
                if n.count("M") == 2 and n.count("S") == 2:
                    if n[0] != n[1] and n[2] != n[3]:
                        crosses += 1

print(crosses)