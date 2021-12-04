#!/usr/bin/env python3
import sys
import cProfile
from collections import defaultdict

class MutBool():
    def __init__(self, val):
        self.val = val

    def __bool__(self):
        return self.val
    
    def __repr__(self):
        return str(self.val)

class Board():

    def __init__(self, draw_state, board_state, text):
        self.state_rows = []
        for l in text:
            self.state_rows.append([[int(i), draw_state[int(i)]] for i in l.split()])

        self.fast_rows = []
        for r in self.state_rows:
            self.fast_rows.append([v[1] for v in r])
            for v in r:
                board_state[v[0]].append(self)

        self.fast_cols = []
        for nr, _ in enumerate(self.state_rows[0]):
            self.fast_cols.append([row[nr][1] for row in self.state_rows])

    def winning(self):
        for row in self.fast_rows:
            if all(row):
                return True
        for col in self.fast_cols:
            if all(col):
                return True
        return False

    def score(self, nr):
        un_sum = 0
        for r in self.state_rows:
            for s in r:
                if s[1].val == False:
                    un_sum += s[0]
        return un_sum * nr


    def __str__(self):
        s = ''
        for row in self.state_rows:
            s += str(row)
            s += '\n'
        #s += '-----\n'
        #for row in self.state_cols:
        #    s += str(row)
        #    s += '\n'
        return s

    def __repr__(self):
        return str(self)



def parse_in(std_in):
    split = std_in.splitlines()
    draws = [int(i) for i in split[0].split(',')]
    draw_state = defaultdict(lambda: MutBool(False))
    board_state = defaultdict(list)
    b_txt = split[2:]
    boards = []
    while(len(b_txt) >= 5):
        boards.append(Board(draw_state, board_state, b_txt[:5] ))
        b_txt = b_txt[5:]
        if b_txt:
            b_txt = b_txt[1:]

    return draw_state, draws, boards, board_state

def first_task(parsed_lines):
    draw_state = parsed_lines[0]
    draws = parsed_lines[1]
    boards = parsed_lines[2]
    board_state = parsed_lines[3]
    for d in draws:
        draw_state[d].val = True
        for b in board_state[d]:
            if b.winning():
                return b.score(d)
    return 0

def second_task(parsed_lines):
    draw_state = parsed_lines[0]
    draws = parsed_lines[1]
    boards = parsed_lines[2]
    board_state = parsed_lines[3]
    for d in draws:
        draw_state[d].val = True
        if len(boards) == 1:
            if boards[0].winning():
                return boards[0].score(d)
        else:
            wins = [b for b in board_state[d] if b.winning()]
            for w in wins:
                for key in board_state:
                    if w in board_state[key]:
                        board_state[key].remove(w)
                boards.remove(w)
    return 0

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
