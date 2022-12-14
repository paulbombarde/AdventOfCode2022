import sys


class Rope:
    def __init__(self, l):
        self.visited = set()
        self.rope = [[0,0] for i in range(l)]
        self.xmin = 0
        self.xmax = 0
        self.ymin = 0
        self.ymax = 0

    def move(self, cmd):
        #print("==", cmd, "==")
        d, c = cmd.split(" ")
        c = int(c)
        while c:
            self.move_once(d)
            c -= 1
        #self.print()

    def move_once(self, d):
        if d == "R":
            self.rope[0][1] += 1
        elif d == "L":
            self.rope[0][1] -= 1
        elif d == "U":
            self.rope[0][0] += 1
        elif d == "D":
            self.rope[0][0] -= 1

        for i in range(1, len(self.rope)):
            if self.rope[i-1][0] + 1 < self.rope[i][0]:
                # print("case 1", i)
                self.rope[i][0] = self.rope[i-1][0] + 1
                if self.rope[i][1] < self.rope[i-1][1]:
                    self.rope[i][1] += 1
                elif self.rope[i][1] > self.rope[i-1][1]:
                    self.rope[i][1] -= 1
            elif self.rope[i][0] < self.rope[i-1][0] - 1:
                # print("case 2", i)
                self.rope[i][0] = self.rope[i-1][0] - 1
                if self.rope[i][1] < self.rope[i-1][1]:
                    self.rope[i][1] += 1
                elif self.rope[i][1] > self.rope[i-1][1]:
                    self.rope[i][1] -= 1
            elif self.rope[i-1][1] + 1 < self.rope[i][1]:
                # print("case 3", i)
                self.rope[i][1] = self.rope[i-1][1] + 1
                if self.rope[i][0] < self.rope[i-1][0]:
                    self.rope[i][0] += 1
                elif self.rope[i][0] > self.rope[i-1][0]:
                    self.rope[i][0] -= 1
            elif self.rope[i][1] < self.rope[i-1][1] - 1:
                # print("case 4", i)
                self.rope[i][1] = self.rope[i-1][1] - 1
                if self.rope[i][0] < self.rope[i-1][0]:
                    self.rope[i][0] += 1
                elif self.rope[i][0] > self.rope[i-1][0]:
                    self.rope[i][0] -= 1

        self.visited.add(",".join(str(i) for i in self.rope[-1]))
        for p in self.rope:
            self.xmin = min(self.xmin, p[0])
            self.ymin = min(self.ymin, p[1])
            self.xmax = max(self.xmax, p[0])
            self.ymax = max(self.ymax, p[1])

    def print(self):
        print(self.xmin, self.xmax, self.ymin, self.ymax)
        map = []
        for x in range(self.xmin, self.xmax+1):
            map.append(["." for i in range(self.ymin, self.ymax+1)])
        for i,p in enumerate(self.rope):
            map[p[0]-self.xmin][p[1]-self.ymin] = str(i)
        map[-self.xmin][-self.ymin] = "s"
        for l in reversed(map):
            print("".join(l))
        print("")




if __name__ == '__main__':
    s = Rope(2)
    s2 = Rope(10)
    with open(sys.argv[1]) as f:
        for l in f:
            s.move(l.strip())
            s2.move(l.strip())
    print("Part 1:", len(s.visited))
    print("Part 2:", len(s2.visited))


