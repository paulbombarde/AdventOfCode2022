import sys
from collections import deque
from copy import copy

class Map:
    def __init__(self, lines):
        self.map = [[ord(c) for c in l.strip()] for l in lines]
        for i,l in enumerate(self.map):
            for j,c in enumerate(l):
                if c == ord('S'):
                    self.start=(i,j)
                    self.map[i][j]=ord('a')
                elif c == ord('E'):
                    self.target=(i,j)
                    self.map[i][j]=ord('z')
        self.h = len(self.map[0]) - 1
        self.w = len(self.map) - 1


    def dirs(self, o):
        if 0 < o[0]:
            yield o[0]-1, o[1]
        if o[0] < self.w:
            yield o[0]+1, o[1]
        if 0 < o[1]:
            yield o[0], o[1]-1
        if o[1] < self.h:
            yield o[0], o[1]+1

    def val(self, o):
        return self.map[o[0]][o[1]]

class Path:
    def __init__(self, seed, visited=None):
        if visited is None:
            visited = set()
        self.pos = seed
        self.visited = copy(visited)
        self.visited.add(seed)

    def inext(self, map, cmp):
        for d in map.dirs(self.pos):
            if d not in self.visited:
                if cmp(map.val(self.pos), map.val(d)):
                    yield Path(d, self.visited)


def bfs(map, start, cmp, end_cmp):
    bfs = deque()
    bfs.append(Path(start))
    reached = set()
    reached.add(start)
    done = False
    while bfs and not done:
        path = bfs.popleft()
        for p in path.inext(map, cmp):
            if end_cmp(p):
                return p
            elif not p.pos in reached:
                reached.add(p.pos)
                bfs.append(p)


if __name__ == '__main__':
    map = Map(open(sys.argv[1]))

    p1 = bfs(map, map.start, lambda ov, dv: dv <= ov + 1, lambda p: p.pos == map.target)
    print('Part 1:', len(p1.visited) - 1) # 1 for the start position

    p2 = bfs(map, map.target, lambda ov, dv: dv >= ov - 1, lambda p: ord('a') == map.val(p.pos))
    print('Part 2:', len(p2.visited) - 1) # 1 for the start position
