with open("day5/data.aoc", "r") as file: 
    data = [line.strip("\n") for line in file.readlines()]

pairs = []
seqs = []

# data format ----

second = False

for line in data:
    if not line:
        second = True
        continue
    if second: seqs += [[int(x) for x in line.split(",")]]
    else: pairs += [[int(x) for x in line.split("|")]]

# p1 -----

invalids = []
part1 = 0

for seq in seqs:
    for i in range(len(seq)):
        start = seq[i]
        if any([[following, start] in pairs for following in seq[i+1:]]): 
            invalids += [seq]
            break
    else: # axel inspo
        part1 += seq[len(seq)//2]

print(part1)

# p2 bubble sort ;) -----

import copy
part2 = 0

for seq in invalids:
    old_seq = copy.copy(seq)
    while True: # ;)
        for i in range(len(seq)-1):
            if [seq[i+1],seq[i]] in pairs:
                temp = seq[i+1]
                seq[i+1] = seq[i]
                seq[i] = temp
        if seq == old_seq: break
        else: old_seq = copy.copy(seq)
    part2 += seq[len(seq)//2]

print(part2)