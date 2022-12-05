import sys
from collections import defaultdict
from copy import deepcopy

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        read_stacks = defaultdict(list)
        stacks = []
        stacks2 = []
        in_move = False
        for l in f:
            if len(l) == 1:
                in_move = True
                # white line, reverse stacks
                for s in read_stacks.values():
                    s.reverse()
                for i in range(len(read_stacks)):
                    stacks.append(read_stacks[i])
                stacks2 = deepcopy(stacks)
            elif not in_move:
                i = 0
                while i < len(l):
                    if l[i] != ' ':
                        read_stacks[i // 4].append(l[i + 1])
                    i += 4
            elif l.startswith("move "):
                l = l.strip().split(' ')
                nb_crates = int(l[1])
                from_stack = int(l[3]) - 1
                to_stack = int(l[5]) - 1

                tmp_stack = []
                while 0 < nb_crates:
                    crate = stacks[from_stack].pop()
                    stacks[to_stack].append(crate)
                    crate2 = stacks2[from_stack].pop()
                    tmp_stack.append(crate2)
                    nb_crates -= 1

                while tmp_stack:
                    stacks2[to_stack].append(tmp_stack.pop())

    res = "".join(s[-1] for s in stacks)
    res2 = "".join(s[-1] for s in stacks2)
    print("Part 1:", res)
    print("Part 2:", res2)
