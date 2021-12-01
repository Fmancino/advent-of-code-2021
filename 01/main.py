#!/usr/bin/env python3
import sys
import cProfile

def parse_in(std_in):
    return [int(i) for i in std_in.splitlines()]

def first_task(parsed_lines):
    res = 0
    for idx, nr in enumerate(parsed_lines[1:]):
        if parsed_lines[idx] < nr:
            res += 1
    return res

# List option
#def second_task(parsed_lines):
#    slide = parsed_lines[:2]
#    sum_slides = []
#    for nr in parsed_lines[2:]:
#        slide.append(nr)
#        sum_slides.append(sum(slide))
#        slide.pop(0)
#    return first_task(sum_slides)

# Zip option
def second_task(parsed_lines):
    sum_slides = [sum(i) for i in zip(parsed_lines, parsed_lines[1:], parsed_lines[2:])]
    return first_task(sum_slides)


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
