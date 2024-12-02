with open("day2/data.aoc", "r") as file: 
    data = [line.strip("\n") for line in file.readlines()]

data = [[int(x) for x in line.split(" ")] for line in data]

def run_tests(seq, i): # replace: preivous, current, next
    test_one = test_seq(seq[:i] + seq[i+1:], fault_used=True)
    test_two = test_seq(seq[:i+1] + seq[i+2:], fault_used=True)
    test_three = test_seq(seq[:i+2] + seq[i+3:], fault_used=True)
    if test_one == 1 or test_two == 1 or test_three == 1:
        return 1
    return 0

def test_seq(seq, fault_used=False):
    dec, inc = False, False
    if seq[1] > seq[0] and seq[1] - seq[0] <= 3:
        inc = True
    elif seq[1] < seq[0] and seq[0] - seq[1] <= 3:
        dec = True
    if not inc and not dec and not fault_used: # equal start
        test_one = test_seq(seq[1:], fault_used=True)
        test_two = test_seq(seq[:1] + seq[2:], fault_used=True)
        if test_one == 1 or test_two == 1:
            return 1
        return 0
    rest = seq[1:]
    if inc:
        for i in range(len(rest)-1):
            if rest[i+1] > rest[i]+3:
                if not fault_used:
                    return run_tests(seq, i)
                return 0
            elif rest[i+1] <= rest[i]:
                if not fault_used:
                    return run_tests(seq, i)
                return 0
    if dec:
        for i in range(len(rest)-1):
            if rest[i+1] < rest[i]-3:
                if not fault_used:
                    return run_tests(seq, i)
                return 0
            elif rest[i+1] >= rest[i]:
                if not fault_used:
                    return run_tests(seq, i)
                return 0
    if inc:
        return 1
    if dec:
        return 1
    return 0

#part1
p1 = 0
p2 = 0
for seq in data:
    p1 += test_seq(seq, fault_used=True)
    p2 += test_seq(seq, fault_used=False)

print(p1)
print(p2)