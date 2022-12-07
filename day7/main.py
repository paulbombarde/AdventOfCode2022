import sys
from collections import namedtuple

class Dir:
    def __init__(self, path):
        self.path = path
        self.size = 0

class State:
    def __init__(self):
        self.top_dir = Dir('/')
        self.stack = [self.top_dir]
        self.dirs = set()
        self.dirs.add(self.top_dir)
        self.current_dir = self.top_dir

    def pop(self):
        p = self.stack.pop()
        self.current_dir = self.stack[-1]
        self.current_dir.size += p.size

    def push(self, name):
        self.current_dir = Dir(self.current_dir.path + '/' + name)
        self.stack.append(self.current_dir)
        self.dirs.add(self.current_dir)

if __name__ == '__main__':
    s = None
    with open(sys.argv[1]) as f:
        for l in f:
            l = l.strip()
            if l == '$ cd /':
                s = State()
            elif l == '$ cd ..':
                s.pop()
            elif l.startswith('$ cd '):
                s.push(l[5:])
            elif l == '$ ls':
                pass
            elif l.startswith('dir '):
                pass
            else:
                s.current_dir.size += int(l.split()[0])

    while 1 < len(s.stack):
        s.pop()

    sum = 0
    needed = 30000000
    unused = 70000000 - s.top_dir.size
    missing = needed - unused
    closest = s.top_dir.size
    for d in s.dirs:
        # print(d.path, d.size)
        if d.size <= 100000:
            sum += d.size
        if missing <= d.size :
            if d.size < closest:
                closest = d.size

    print('Part 1:', sum)
    print('Part 2:', closest)
