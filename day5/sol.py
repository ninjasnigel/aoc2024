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
# part 1 ----

valids = []
part1 = 0

for k,seq in enumerate(seqs):
    for i in range(len(seq)):
        start = seq[i]
        if any([[following, start] in pairs for following in seq[i+1:]]): break
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