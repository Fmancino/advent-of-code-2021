#!/usr/bin/env python3
import sys
import cProfile
from collections import Counter

def parse_in(std_in):
    split = std_in.splitlines()
    return [int(i) for i in split[0].split(',')]

def count_fish(days, period, reproduced):
    s = 1
    while((days := (days - period)) > 0):
        s += count_fish(days, 9, False)
        if not reproduced:
            period -= 2
            reproduced = True
    return s

def first_task(parsed_lines):
    s  = 0
    days = 80
    c = Counter(parsed_lines)
    for key, val in c.items():
        s += val * (count_fish(days - key, 7, True) + count_fish(days - key, 9, False))
    return s

def second_task(parsed_lines):
    s  = 0
    days = 256
    c = Counter(parsed_lines)
    for key, val in c.items():
        s += val * (count_fish(days - key, 7, True) + count_fish(days - key, 9, False))
        print("one")
    return s

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
