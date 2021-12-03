#!/usr/bin/env python3
import sys
import cProfile

def parse_in(std_in):
    split = std_in.splitlines()
    return split

def first_task(parsed_lines):
    lgt = len(parsed_lines)
    gamma = ''
    epsilon = ''
    for i, _ in enumerate(parsed_lines[0]):
        tot = 0
        for l in parsed_lines:
            tot += int(l[i])
        if tot > lgt / 2:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'
    return int(gamma,2) * int(epsilon,2)

def second_task(parsed_lines):
    lgt = len(parsed_lines)
    gamma = ''
    epsilon = ''

    left = parsed_lines
    for i, _ in enumerate(parsed_lines[0]):
        vals_0 = []
        vals_1 = []
        for l in left:
            if l[i] == '0':
                vals_0.append(l)
            else:
                vals_1.append(l)

        if len(vals_0) > len(vals_1):
            left = vals_0
        else:
            left = vals_1
        if len(left) == 1:
            break
    oxy = int(left[0],2)
    left = parsed_lines
    for i, _ in enumerate(parsed_lines[0]):
        vals_0 = []
        vals_1 = []
        for l in left:
            if l[i] == '0':
                vals_0.append(l)
            else:
                vals_1.append(l)

        if len(vals_0) > len(vals_1):
            left = vals_1
        else:
            left = vals_0
        if len(left) == 1:
            break
    co = int(left[0],2)
    return oxy * co

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
