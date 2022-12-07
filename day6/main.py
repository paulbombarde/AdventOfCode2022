import sys


def find_first_n_diff(s, n):
    last_four = s[:n]
    unique_fours = set(last_four)
    i = n
    while len(unique_fours) != n:
        last_four = last_four[1:] + s[i]
        unique_fours = set(last_four)
        i += 1
    return i


if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        for l in f:
            l = l.strip()
            print("Part 1:", find_first_n_diff(l, 4), l)
            print("Part 2:", find_first_n_diff(l, 14), l)
