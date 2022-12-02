import sys

if __name__ == '__main__':
    calories_per_elf = []
    with open(sys.argv[1]) as f:
        current_elf_calories = 0
        for l in f:
            l = l.strip()
            if len(l) == 0:
                calories_per_elf.append(current_elf_calories)
                current_elf_calories = 0
            else:
                current_elf_calories += int(l)
        calories_per_elf.append(current_elf_calories)

    print("Part 1:", max(calories_per_elf))
    calories_per_elf.sort()
    print("Part 2:", sum(calories_per_elf[-3:]))


