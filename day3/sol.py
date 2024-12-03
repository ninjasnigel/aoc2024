with open("day3/data.aoc", "r") as file: 
    data = [line.strip("\n") for line in file.readlines()]

def check_mul(data):
    if data[0:3] == 'mul' and data[3] == "(":
        rest = data[4:]
        num1 = ""
        for i in range(len(rest)):
            if rest[i].isnumeric():
                num1 += rest[i]
            else: break
        num2 = ""
        for i in range(len(num1)+1, len(rest)):
            if rest[i].isnumeric():
                num2 += rest[i]
            elif rest[i] != ")":
                break
            else:
                return int(num1) * int(num2)
    return 0

total = 0
for line in data:
    for i in range(len(line)):
        total += check_mul(line[i:])

print(total)

total = 0
go = True
for line in data:
    for i in range(len(line)):
        do = "do()"
        no = "don't()"
        if line[i:i+4] == do:
            go = True
        elif line[i:i+7] == no:
            go = False
        if go:
            total += check_mul(line[i:])

print(total)
        