import sys


def ops_parser(lines):
    for l in lines:
        # print("==",l.strip())
        if l.startswith('addx'):
            i=int(l.strip().split(" ")[1])
            yield 0
            yield i
        else:
            yield 0


if __name__ == '__main__':
    vals = ops_parser(open(sys.argv[1]))
    interesting = {20, 60, 100, 140, 180, 220}

    CRT = [[" "]*40 for i in range(6)]
    x=1
    s=0
    for i,v in enumerate(vals, start=1):
        # print("tick", i,v,x)
        if i in interesting:
            st = i * x
            s += st

        j = i-1
        row = j // 40
        index = j % 40
        # print(i, j, x, row, index)
        if x - 1 <= index and index <= x + 1:
            CRT[row][index] = "#"
        else:
            CRT[row][index] = " "

        x += v

    print("Part 1:",s)
    for r in CRT:
        print("".join(r))