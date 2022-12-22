import sys


def walls_generator(lines):
    for l in lines:
        yield [[int(p) for p in pt.split(',')] for pt in l.split(" -> ")]

class Map:
    def __init__(self, walls):
        self.xmin = 500
        self.xmax = 500
        self.ymin = 0
        self.ymax = 0
        for w in walls:
            self.xmin = min(self.xmin, min(p[0] for p in w))
            self.ymin = min(self.ymin, min(p[1] for p in w))
            self.xmax = max(self.xmax, max(p[0] for p in w))
            self.ymax = max(self.ymax, max(p[1] for p in w))

        self.H = self.ymax - self.ymin + 2 # +2 for the last rows in part 2
        # The whole scene can't be wider than its height on each side
        self.W = 2*self.H + 2

        self.map = [['.' for i in range(self.W + 1)]
                         for j in range(self.H + 1)]
        for w in walls:
            for i in range(len(w) - 1):
                self.draw_wall(w[i], w[i+1])
        for i in range(self.W + 1):
            self.map[-1][i] = "#"
        self.mark(500, 0, '+')

    def draw_wall(self, s, e):
        if s[0] == e[0]:
            for y in range(min(s[1], e[1]), max(s[1], e[1])+1):
                self.mark(s[0], y, "#")
        else:
            for x in range(min(s[0], e[0]), max(s[0], e[0])+1):
                self.mark(x, s[1], "#")
    def mark(self, x, y, val):
        self.map[y - self.ymin][x - self.xmin] = val

    def val(self, x, y):
        return self.map[y - self.ymin][x - self.xmin]

    def print(self):
        for l in self.map:
            print("".join(l))

    def grain(self):
        x = 500
        y = 0
        while True:
            try:
                if self.val(x, y+1) == '.':
                    y += 1
                elif self.val(x-1, y+1) == '.':
                    x -= 1
                    y += 1
                elif self.val(x+1, y+1) == '.':
                    x += 1
                    y += 1
                else:
                    self.mark(x, y, "o")
                    return [x, y]
            except IndexError:
                return None

    def overflow(self, p):
        if not p:
            return True
        return p[0] < self.xmin or p[0] > self.xmax \
            or p[1] < self.ymin or p[1] > self.ymax
            

if __name__ == '__main__':
    walls = [w for w in walls_generator(open(sys.argv[1]))]
    m = Map(walls)
    #m.print()
    i=0
    while not m.overflow(m.grain()):
        #m.print()
        i += 1
    print("Part 1:", i)

    i += 1 # take the latest grain into account
    while [500, 0] != m.grain():
        i += 1
    i += 1 # take the last grain into account
    print("Part 2:", i)