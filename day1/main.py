import sys

def elf_calories(path):
    with open(sys.argv[1]) as f:
        current_elf_calories = 0
        for l in f:
            l = l.strip()
            if len(l) == 0:
                yield current_elf_calories
                current_elf_calories = 0
            else:
                current_elf_calories += int(l)
        yield current_elf_calories

if __name__ == '__main__':
    calories_per_elf = list(elf_calories(sys.argv[1]))
    calories_per_elf.sort()
    print("Part 1:", calories_per_elf[-1])
    print("Part 2:", sum(calories_per_elf[-3:]))


