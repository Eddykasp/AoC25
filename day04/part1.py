def load_input(filename):
    with open(filename) as file:
        rows = []
        for line in file.readlines():
            rows.append(line[:-1])

        return rows
    

def analyse_paper(rows):
    accessible = 0
    for i, row in enumerate(rows):
        for j, char in enumerate(row):
            count = 0
            if char == '@':
                for x in range(i-1, i+2):
                    for y in range(j-1, j+2):
                        if i == x and y == j or x < 0 or y < 0 or x > len(rows) or y > len(row):
                            continue
                        try:
                            if rows[x][y] == '@':
                                count += 1
                        except:
                            continue
                if count < 4:
                    accessible += 1
    return accessible

if __name__ == "__main__":
    rows = load_input("day04/input.txt")
    print(analyse_paper(rows))