#!/usr/bin/env python3

from pathlib import Path

from aoc.day01 import part1, part2

def read_file(filename):
    path = Path(__file__).parent.resolve()
    with open(path / filename, 'r') as f:
        lines = f.read().splitlines()
        return lines

def main():
    input = read_file("./resources/input.txt")

    print("--- Part One ---")
    print("Result:", part1.result(input))

    print("--- Part Two ---")
    print("Result:", part2.result(input))

if __name__ == "__main__":
    main()
