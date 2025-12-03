def read_batteries(file_path: str) -> list[list[int]]:
    with open(file_path, 'r') as file:
        banks = []
        for line in file:
            # convert to list of ints
            banks.append([int(x) for x in list(line.strip())])
    return banks

def turn_on_batteries(batteries: list[int], n: int) -> int:
    # n determines the number of batteries to turn on
    previous = -1
    result = ""
    for index, _ in enumerate(range(n)):
        previous = max(range(previous+1, len(batteries)-(n-index-1)), key=batteries.__getitem__)
        result += str(batteries[previous])
    return int(result)

if __name__ == "__main__":
    banks = read_batteries('day03/input.txt')
    # result = reduce(lambda bank1, bank2: turn_on_batteries(bank1) + turn_on_batteries(bank2), banks, 0)
    result = 0
    for bank in banks:
        result += turn_on_batteries(bank, 12)
    print(result)