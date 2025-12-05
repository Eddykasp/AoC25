def solve(filename):
    with open(filename) as file:
        fresh_ranges = []
        reading_ranges = True
        fresh_count = 0
        for line in file.readlines():
            if (reading_ranges):
                line = line.strip()
                if line == "":
                    reading_ranges = False
                    continue
                start, end = map(int, line.split("-"))
                fresh_ranges.append(range(start, end+1))
            else:
                for r in fresh_ranges:
                    if int(line) in r:
                        fresh_count += 1
                        break
    return fresh_count


if __name__ == "__main__":
    print(solve("day05/input.txt"))