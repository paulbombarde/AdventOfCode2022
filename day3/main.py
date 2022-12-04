import sys


def priority(l):
    if 'a' <= l <= 'z':
        return ord(l) - ord('a') + 1
    else:
        return ord(l) - ord('A') + 27


def badItem(r):
    mid = len(r) // 2
    c1 = set(r[0:mid])
    c2 = set(r[mid:])
    i = c1.intersection(c2)
    return i.pop()


def commonsGenerator(rucksacks):
    commons = set()
    for i, r in enumerate(rucksacks, start=1):
        if len(commons) == 0:
            commons = set(r)
        else:
            commons = commons.intersection(set(r))
        if 0 == i % 3:
            yield commons.pop()


if __name__ == '__main__':
    rucksacks = [l.strip() for l in open(sys.argv[1])]

    badItems = (badItem(r) for r in rucksacks)
    priorities1 = (priority(l) for l in badItems)
    priorities2 = (priority(l) for l in commonsGenerator(rucksacks))
    print('Part 1: ', sum(priorities1))
    print("Part 2: ", sum(priorities2))
