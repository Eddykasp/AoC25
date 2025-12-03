from functools import reduce

def read_batteries(file_path: str) -> list[list[int]]:
    with open(file_path, 'r') as file:
        banks = []
        for line in file:
            # convert to list of ints
            banks.append([int(x) for x in list(line.strip())])
    return banks

def turn_on_batteries(batteries: list[int]) -> int:
    index_first = max(range(len(batteries)-1), key=batteries.__getitem__)
    last = max(batteries[index_first+1:])
    return int(str(batteries[index_first]) + str(last))

if __name__ == "__main__":
    banks = read_batteries('day03/input.txt')
    result = 0
    for bank in banks:
        result += turn_on_batteries(bank)
    print(result)