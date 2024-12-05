with open("day5/data.aoc", "r") as file: 
    data = [line.strip("\n") for line in file.readlines()]

pairs = []
seqs = []

for line in data:
    if line == "": break
    n1, n2 = line.split("|")
    n1, n2 = int(n1), int(n2)
    pairs.append([n1, n2])

ready = False
for line in data:
    if ready: seqs += [[int(x) for x in line.split(",")]]
    if line == "": ready = True

def check_seq(start, num):
    for following in num[1:]:
        if [following,start] in pairs:
            print([following, start], " in pairs")
            return False
    return True

valids = []
valid = 0

for o,seq in enumerate(seqs):
    this_seq = True
    for i in range(len(seq)):
        start = seq[i]
        if not check_seq(start, seq[i:]):
            this_seq = False
            break
    if this_seq: 
        valid += seq[int(len(seq)/2)]
        valids += [o]

print(valid)


# bubble sort the arrays

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
    if i in valids:
        continue
    part2 += seq[int(len(seq)/2)]