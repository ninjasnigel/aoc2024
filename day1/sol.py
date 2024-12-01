with open("day1/data.aoc", "r") as file: 
    data = [line.strip("\n") for line in file.readlines()]

left = []
right = []

for line in data:
    split = line.split(" ")
    right += [int(split[-1])]
    left += [int(split[0])]

left = sorted(left)
right = sorted(right)

one = 0

for i in range(len(left)):
    one += abs(left[i] - right[i])

two = 0

for l in left:
    this_am = 0
    for r in right:
        if l == r:
            this_am += 1
    two += this_am * l

print('one:', one)
print('two:', two)