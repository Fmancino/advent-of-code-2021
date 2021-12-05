#!/usr/bin/env python3
import sys
import cProfile
from collections import Counter

class Vent:
    def __init__(self, txt):
        s,e = txt.split(' -> ')
        s1,s2 = s.split(',')
        e1,e2 = e.split(',')
        self.start = (int(s1), int(s2))
        self.end = (int(e1), int(e2))

    def straight_line(self):
        if self.start[0] == self.end[0]:
            s = min(self.start[1], self.end[1])
            e = max(self.start[1], self.end[1])
            return [(self.start[0], i) for i in range(s, e+1)]

        elif self.start[1] == self.end[1]:
            s = min(self.start[0], self.end[0])
            e = max(self.start[0], self.end[0])
            return [(i, self.end[1]) for i in range(s, e+1)]
        return []

    def line(self):
        s = self.straight_line()
        if s:
            return s
        else:
            if self.start[0] > self.end[0]:
                x = range(self.start[0], self.end[0] - 1, -1)
            else:
                x = range(self.start[0], self.end[0] + 1)
            if self.start[1] > self.end[1]:
                y = range(self.start[1], self.end[1] - 1, -1)
            else:
                y = range(self.start[1], self.end[1] + 1)
            return list(zip(x,y))

def parse_in(std_in):
    split = std_in.splitlines()
    return [Vent(l) for l in split]

def first_task(parsed_lines):
    all_points = []
    for v in parsed_lines:
        all_points += v.straight_line()
    c = Counter(all_points)
    return sum([1 for x in  c.values() if x > 1])

def second_task(parsed_lines):
    all_points = []
    for v in parsed_lines:
        all_points += v.line()
    c = Counter(all_points)
    return sum([1 for x in  c.values() if x > 1])

def main():
    std_in = sys.stdin.read()

    parsed = parse_in(std_in)

    pr = cProfile.Profile()
    pr.enable()

    res = first_task(parsed)
    print(f"task 1: {res}")

    res = second_task(parsed)
    print(f"task 2: {res}")

    pr.create_stats()
    pr.print_stats()

if __name__ == "__main__":
    main()
