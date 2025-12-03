class Dial:
    size = 100
    current_pos = 50
    zeros = 0

    def rotate(self, step: int):
        self.current_pos = (self.current_pos + step) % self.size
        if self.current_pos == 0:
            self.zeros += 1


def load_input(file):
    steps = []
    with open(file) as input:
        for line in input:
            count = int(line[1:])
            if line[0] == 'R':
                steps.append(count)
            else:
                steps.append(-count)
    return steps

if __name__ == "__main__":
    steps = load_input("day01/input.txt")
    dial = Dial()
    for step in steps:
        dial.rotate(step)
    
    print(dial.zeros)



