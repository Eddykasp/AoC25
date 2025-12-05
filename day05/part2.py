def solve(filename):
    with open(filename) as file:
        fresh_ingredients = 0
        ranges: list[range] = []
        for line in file.readlines():
            line = line.strip()
            if line == "":
                break
            start, end = map(int, line.split("-"))
            ranges.append((start, end+1))
        ranges.sort()
        merged_ranges = []
        for current_start, current_end in ranges:
            if not merged_ranges or merged_ranges[-1][1] < current_start:
                merged_ranges.append((current_start, current_end))
            else:
                merged_ranges[-1] = (merged_ranges[-1][0], max(merged_ranges[-1][1], current_end))

        for r in merged_ranges:
            fresh_ingredients += (r[1] - r[0])
    return fresh_ingredients


if __name__ == "__main__":
    print(solve("day05/input.txt"))