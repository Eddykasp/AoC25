from functools import reduce

def check_id(id: int) -> bool:
    # An id is invalid if it consists of a repetition of numbers i.e. 11 or 123123 but not 101 or 111
    id_str = str(id)
    length = len(id_str)
    if length % 2 != 0:
        return False
    half = length // 2
    if id_str[:half] == id_str[half:]:
        return True
    return False

class IDRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def contains_invalid_id(self) -> list[int] | None:
        ids = []
        for id in range(self.start, self.end + 1):
            if check_id(id):
                ids.append(id)
                print(f"Invalid ID found: {id}")
        if ids:
            return ids
        return None


def read_input():
    with open('day02/input.txt', 'r') as file:
        ranges = file.read().strip().split(',')
        id_ranges = []
        for range in ranges:
            start, end = map(int, range.split('-'))
            id_ranges.append(IDRange(start, end))
        return id_ranges
            

if __name__ == "__main__":
    id_ranges = read_input()
    total = 0
    for id_range in id_ranges:
        invalid_ids = id_range.contains_invalid_id()
        total += reduce(lambda x, y: x + y, invalid_ids) if invalid_ids else 0
    print(total)