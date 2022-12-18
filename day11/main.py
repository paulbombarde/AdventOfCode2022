import time


class Monkey:
    def __init__(self, items, op, div, true_monkey, false_monkey):
        self.items = items
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey
        self.op = op
        self.div = div
        self.activity = 0

    def turn(self, monkeys, reduce_op):
        for i in self.items:
            i = self.op(i)
            i = reduce_op(i)
            m = self.true_monkey if i % self.div == 0 else self.false_monkey
            monkeys[m].items.append(i)
        self.activity += len(self.items)
        self.items = []

def round(monkeys, reduce_op):
    for m in monkeys:
        m.turn(monkeys, reduce_op)


def rounds(monkeys, reduce_op, n, print_mod = 0):
    for i in range(1,n+1):
        if print_mod and i % print_mod == 0:
            print("== Round", i)
            print(time.asctime(time.localtime()), i)
            for i,m in enumerate(monkeys):
                print(i, m.activity, m.items)
            print()
        round(monkeys, reduce_op)


def sample_monkeys():
    monkeys = []
    monkeys.append(Monkey([79, 98],
                          lambda x: x * 19,
                          23, 2, 3))
    monkeys.append(Monkey([54, 65, 75, 74],
                          lambda x: x + 6,
                          19, 2, 0))
    monkeys.append(Monkey([79, 60, 97],
                          lambda x: x * x,
                          13, 1, 3))
    monkeys.append(Monkey([74],
                          lambda x: x +3,
                          17, 0, 1))
    return monkeys


def input_monkeys():
    monkeys = []
    monkeys.append(Monkey([98, 89, 52],
                          lambda x: x * 2,
                          5, 6, 1))
    monkeys.append(Monkey([57, 95, 80, 92, 57, 78],
                          lambda x: x * 13,
                          2, 2, 6))
    monkeys.append(Monkey([82, 74, 97, 75, 51, 92, 83],
                          lambda x: x + 5,
                          19, 7, 5))
    monkeys.append(Monkey([97, 88, 51, 68, 76],
                          lambda x: x + 6,
                          7, 0, 4))
    monkeys.append(Monkey([63],
                          lambda x: x + 1,
                          17, 0, 1))
    monkeys.append(Monkey([94, 91, 51, 63],
                          lambda x: x + 4,
                          13, 4, 3))
    monkeys.append(Monkey([61, 54, 94, 71, 74, 68, 98, 83],
                          lambda x: x + 2,
                          3, 2, 7))
    monkeys.append(Monkey([90, 56],
                          lambda x: x * x,
                          11, 3, 5))
    return monkeys


def monkey_business(monkeys):
    for i,m in enumerate(monkeys):
        print(i, m.activity)
    smonkeys = sorted(m.activity for m in monkeys)
    return smonkeys[-1] * smonkeys[-2]


if __name__ == '__main__':
    monkeys = input_monkeys()
    rounds(monkeys, lambda i: i // 3, 20)
    print("Part 1:", monkey_business(monkeys))

    monkeys2 = input_monkeys()
    modulo = 1
    for m in monkeys2:
        modulo *= m.div
    rounds(monkeys2, lambda i: i % modulo, 10000)
    print("Part 2:", monkey_business(monkeys2))


