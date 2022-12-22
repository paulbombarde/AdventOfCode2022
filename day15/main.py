import re
import sys


class Map:
    def __init__(self, lines):
        self.xmin = 0
        self.xmax = 0
        self.ymin = 0
        self.ymax = 0
        self.links = []
        for l in lines:
            s = l[0:2]
            b = l[2:]
            d = abs(s[0]-b[0]) + abs(s[1]-b[1])
            self.xmin = min(self.xmin, s[0]-d, b[0]-d)
            self.ymin = min(self.ymin, s[1]-d, b[1]-d)
            self.xmax = max(self.xmax, s[0]+d, b[0]+d)
            self.ymax = max(self.ymax, s[1]+d, b[1]+d)
            self.links.append([s, b, d])

    def build_map(self):
        H = self.ymax - self.ymin
        W = self.xmax - self.xmin
        self.map = [['.' for i in range(W + 1)] for j in range(H + 1)]

        for s,b,d in self.links:
            for i in range(d+1):
                for j in range(d+1-i):
                    self.mark(s[0]+i, s[1]+j, "#")
                    self.mark(s[0]-i, s[1]+j, "#")
                    self.mark(s[0]+i, s[1]-j, "#")
                    self.mark(s[0]-i, s[1]-j, "#")
            self.mark(s[0], s[1], 'S')
            self.mark(b[0], b[1], 'B')

    def mark(self, x, y, v):
        self.map[y-self.ymin][x-self.xmin]=v


    def __str__(self):
        return "\n".join(''.join(l) for l in self.map)

    def build_line(self, y):
        l = ["." for i in range(self.xmax - self.xmin + 1)]
        for s,b,d in self.links:
            t = d - abs(y - s[1])
            if t < 0:
                continue
            for x in range(s[0]-t, s[0]+t):
                l[x - self.xmin] = "#"
        for s,b,d in self.links:
            if s[1] == y:
                l[s[0] - self.xmin] = "S"
            if b[1] == y:
                l[b[0] - self.xmin] = "B"
        return l

if __name__ == '__main__':
    r = re.compile("Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)")
    lines = ([int(n) for n in r.match(l).groups()] for l in open(sys.argv[1]))
    m = Map(lines)
    #m.build_map()
    #print(m)

    y = int(sys.argv[2])
    l = m.build_line(y)
    #print("".join(l))
    print("Part 1:", sum(v!="." for v in l))


