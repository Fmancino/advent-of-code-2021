#!/usr/bin/env python3
import sys
import cProfile

def parse_in(std_in):
    #split = std_in.splitlines()
    return 0

def first_task(parsed_lines):
    return 0

def second_task(parsed_lines):
    return 0

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
