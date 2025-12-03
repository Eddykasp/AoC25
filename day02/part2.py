from functools import reduce

def check_id_alternative(id: int) -> bool:
    # any repetitions make an id invalid e.g. 1111, 121212, 123123123 but not 1234 or 1231234
    id_str = str(id)
    length = len(id_str)
    for sub_len in range(1, length // 2 + 1):
        if length % sub_len == 0:
            if id_str[:sub_len] * (length // sub_len) == id_str:
                return True
    return False

class IDRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def contains_invalid_id(self) -> list[int] | None:
        ids = []
        for id in range(self.start, self.end + 1):
            if check_id_alternative(id):
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