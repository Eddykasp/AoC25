from functools import reduce
import math

def load_input(filename):
    with open(filename) as file:
        rows = []
        for line in file.readlines():
            rows.append(line.split())
        return rows
    
def solve(tasks):
    total = 0
    for t in range(len(tasks[0])):
        op = math.fsum if tasks[-1][t] == '+' else math.prod
        total += op(map(lambda x: int(x), [tasks[i][t] for i in range(len(tasks[:-1]))]))
    return total


if __name__ == "__main__":
    tasks = load_input('day06/input.txt')
    print(int(solve(tasks)))
