import os
import sys


def puzzle_1():
    counts = 0
    lines = read_lines("./puzzle-1.input")
    return sum_values(lines, is_sliding_window=False)

def puzzle_2():
    counts = 0
    lines = sliding_window(read_lines("./puzzle-1.input"))
    return sum_values(lines, is_sliding_window=True)

def read_lines(path):
    with open(path) as f:
        return f.readlines()

def is_greater(a, b):
    if type(a) == str and type(b) == str:
        a = a.strip()
        b = b.strip()
    return int(a)>int(b)

def sum_values(lines, is_sliding_window):
    if is_sliding_window:
        inner = lambda lst: sum([int(x.strip()) for x in lst])
        return sum([is_greater(inner(x), inner(lines[i-1])) for i, x in enumerate(lines) if i > 0])
    else:
        return sum([is_greater(x, lines[i-1]) for i, x in enumerate(lines) if i > 0])

def sliding_window(lines):
    windows = []
    window_size = 3

    for i, _ in enumerate(lines):
        window = lines[i:window_size+i:1]

        if len(window) == 3:
            windows.append(window)
    return windows


print(f'Solution is {puzzle_2()}')
