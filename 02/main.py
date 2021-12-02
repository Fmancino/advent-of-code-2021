#!/usr/bin/env python3
import sys
import cProfile

def parse_in(std_in):
    split = std_in.splitlines()
    res = []
    for l in split:
        if l.startswith('forward'):
            res.append((int(l[-1]),0))
        elif l.startswith('down'):
            res.append((0,int(l[-1])))
        elif l.startswith('up'):
            res.append((0,-int(l[-1])))
    return res

def first_task(parsed_lines):
    tot = [0 , 0]
    for c in parsed_lines:
        tot[0] += c[0]
        tot[1] += c[1]
    print(tot)
    return tot[0] * tot[1]

def second_task(parsed_lines):
    tot = [0 , 0, 0]
    for c in parsed_lines:
        tot[0] += c[0]
        tot[1] += c[1] #aim
        tot[2] += tot[1] * c[0]
    print(tot)
    return tot[0] * tot[2]

def main():
    std_in = sys.stdin.read()

    pr = cProfile.Profile()
    pr.enable()

    parsed = parse_in(std_in)

    res = first_task(parsed)
    print(f"task 1: {res}")

    res = second_task(parsed)
    print(f"task 2: {res}")

    pr.create_stats()
    pr.print_stats()

if __name__ == "__main__":
    main()
