import sys


def read_elf(e):
    b, e = e.split('-')
    return int(b), int(e)


def read_pair(l):
    e1, e2 = l.split(',')
    return read_elf(e1), read_elf(e2)


def fully_contains_ord(e1, e2):
    return e1[0] <= e2[0] and e2[1] <= e1[1]


def fully_contains(p):
    return fully_contains_ord(p[0], p[1]) or fully_contains_ord(p[1], p[0])


def overlaps_ord(e1, e2):
    return e2[0] <= e1[1] and e1[0] <= e2[1]


def overlaps(p):
    return overlaps_ord(p[0], p[1]) or overlaps_ord(p[1], p[0])


if __name__ == '__main__':
    lines = (l.strip() for l in open(sys.argv[1]))
    pairs = [read_pair(l) for l in lines]
    fullyContained = (fully_contains(p) for p in pairs)
    overlapping = (overlaps(p) for p in pairs)
    print("Part 1: ", sum(fullyContained))
    print("Part 2: ", sum(overlapping))
