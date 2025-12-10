from functools import reduce
from math import fsum, inf

def load_machines(filename):
    machines = []
    with open(filename) as file:
        for line in file.readlines():
            machines.append(load_machine(line))
    return machines

def load_machine(line):
    parts = line.split(' ')
    joltage = [int(char) for char in parts[-1][1:-2].split(',')]
    print(joltage)
    length = len(joltage)
    buttons = []
    for part in parts[1:-1]:
        numbers = part[1:-1].split(',')
        b = ['0'] * length
        for number in numbers:
            b[int(number)] = '1'
        buttons.append(int(''.join(reversed(b)),2))
    return (joltage, buttons)

def solve_machine(machine):
    # solve g = a0*b0 + a1*b1 + ... + an*bn
    # find the correct set of values for a0 to an
    joltage_goal = machine[0]
    buttons = machine[1]
    minimum = inf
    for i in range(1,2**len(buttons)): # TODO: iterate in such a way that the smallest powersets are done first, so that we can safely terminate early
        # i is the bitmask representing the elements to be included in the subset
        # i = 3 = 11 means the button 0 and button 1 are in the set
        powerset = [subset for subset, bit in zip(buttons, format(i, f"{len(buttons)}b")) if bit == '1']
        if len(powerset) > minimum:
            continue
        total = reduce(lambda s0, s1: s0 ^ s1, powerset)
        if total == goal:
            minimum = len(powerset)
    return minimum

if __name__ == "__main__":
    machines = load_machines("day10/test.txt")
    total = int(fsum(map(solve_machine, machines)))
    print(total)