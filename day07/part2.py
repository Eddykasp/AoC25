def load_manifold(file_path):
    rows = []
    with open(file_path) as file:
        for line in file:
            rows.append(line)
    # merge pairs of rows into own lists
    manifold = []
    for i in range(0, len(rows), 2):
        manifold.append(rows[i].rstrip("\n"))  

    return manifold


def analyse_row(manifold_row, beam_indices):
    output_indices = []
    for i, char in enumerate(manifold_row):
        if char == 'S':
            output_indices.append(i)
        elif char == '^' and i in beam_indices:
            output_indices.append(i - 1)
            output_indices.append(i + 1)
        elif char == '.' and i in beam_indices:
            output_indices.append(i)
    return output_indices

if __name__ == "__main__":
    manifold = load_manifold("day07/input.txt")
    beam_indices = []
    beam_indices_per_row = [beam_indices]
    split_counter = 0
    for row in manifold:
        beam_indices = analyse_row(row, beam_indices)
        beam_indices_per_row.append(beam_indices)

    timelines = [1 if i in beam_indices_per_row[-1] else 0 for i in range(len(manifold[0]))]
    for i, row in enumerate(reversed(manifold)):
        for j, char in enumerate(row):
            if char == '^':
                timelines[j] = timelines[j-1] + timelines[j+1]
            elif j in beam_indices_per_row[-i]:
                timelines[j] = timelines[j]
    print(timelines[beam_indices_per_row[1][0]])    