import sys
from collections import deque

start_array = -1
end_array = -2


def pair_generator(lines):
    pair = []
    for l in lines:
        l = l.strip()
        if l:
            pair.append(l)
        else:
            yield pair
            pair = []
    yield pair


def tokenize(line):
    start = 0
    for i in range(len(line)):
        if line[i] == '[':
            yield start_array
        elif line[i] == ']':
            if 0 < start:
                yield int(line[start:i])
            start = 0
            yield end_array
        elif line[i] == ',':
            if 0 < start:
                yield int(line[start:i])
            start = 0
        elif 0 == start:
            start = i


def check_array(left, right):
    return check_deque(deque(left), deque(right))


def check_deque(left, right):
    while right and left:
        li = left.popleft()
        ri = right.popleft()

        left_array_start = li == start_array
        right_array_start = ri == start_array
        left_array_end = li == end_array
        right_array_end = ri == end_array

        if left_array_start and right_array_start:
            res = check_array(left, right)
        elif left_array_start and right_array_end:
            # print("left shorter")
            res = -1
        elif left_array_end and right_array_start:
            # print("right shorter")
            res = 1
        elif left_array_start:
            # print("replace with array right")
            right.appendleft(end_array)
            right.appendleft(ri)
            res = check_array(left, right)
        elif right_array_start:
            # print("replace with array left")
            left.appendleft(end_array)
            left.appendleft(li)
            res = check_array(left, right)
        elif left_array_end and right_array_end:
            res = 0
        elif right_array_end:
            # print("right shorter (4)")
            res = -1
        elif left_array_end:
            # print("left shorter (4)")
            res = 1
        else:
            res = check_val(li, ri)

        if res:
            return res

    if right:
        # print("left shorter (5)")
        return 1
    if left:
        # print("right shorter (5)")
        return -1
    return 0


def check_val(li, ri):
    if li < ri:
        # print(li, 'lower', ri)
        return 1
    if li > ri:
        # print(li, 'higher', ri)
        return -1
    return 0


if __name__ == '__main__':
    pairs = pair_generator(open(sys.argv[1]))

    correct_ordered_indexes_sum = 0
    divider_2_pos = 1
    divider_6_pos = 2
    divider_2 = [-1, -1, 2, -2, -2]
    divider_6 = [-1, -1, 6, -2, -2]
    for i, p in enumerate(pairs, start=1):
        left = [e for e in tokenize(p[0])]
        right = [e for e in tokenize(p[1])]
        c = check_array(left, right)
        if 0 <= c:
            correct_ordered_indexes_sum += i

        for a in [left, right]:
            c2 = check_array(a, divider_2)
            if 0 <= c2:
                divider_2_pos += 1
                divider_6_pos += 1
                continue

            c6 = check_array(a, divider_6)
            if 0 <= c6:
                divider_6_pos += 1
                continue

    print("Part 1:", correct_ordered_indexes_sum)
    print("Part 2:", divider_2_pos * divider_6_pos)
