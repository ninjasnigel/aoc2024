with open("day5/data.aoc", "r") as file: 
    data = [line.strip("\n") for line in file.readlines()]

pairs = []
seqs = []

# data format ----

ready = False
for line in data:
    if line == "": 
        ready = True
        continue
    if ready:
        seqs += [[int(x) for x in line.split(",")]]
        continue
    pair = line.split("|")
    pairs.append([int(pair[0]), int(pair[1])])

# part 1 ----

def check_seq(start, seq):
    for following in seq[1:]:
        if [following,start] in pairs:
            return False
    return True

valids = []
part1 = 0

for k,seq in enumerate(seqs):
    for i in range(len(seq)):
        start = seq[i]
        if not check_seq(start, seq[i:]):
            break
    else: # axel inspo
        part1 += seq[int(len(seq)/2)]
        valids += [k]

print(part1)

# bubble sort the arrays ------ p2

new_order = []
import copy

for seq in seqs:
    old_seq = copy.copy(seq)
    while True:
        for i in range(len(seq)-1):
            if [seq[i+1],seq[i]] in pairs:
                temp = seq[i+1]
                seq[i+1] = seq[i]
                seq[i] = temp
        if seq == old_seq: break
        else: old_seq = copy.copy(seq)
    new_order += [seq]
part2 = 0

for i, seq in enumerate(new_order):
    if i not in valids: part2 += seq[int(len(seq)/2)]

print(part2)