import sys
import numpy
import functools


def numbers_operators() -> tuple[list[list[int]], list[str]]:
    lines = [l.strip() for l in open(sys.argv[1], "r").readlines()]
    numbers = (
        numpy.array(list(map(lambda l: [int(n) for n in l.split()], lines[:-1])))
        .transpose()
        .tolist()
    )
    operators = lines[-1].split()
    return numbers, operators


def solve(numbers: list[list[int]], operators: list[str]) -> int:
    answers = []
    for i, o in enumerate(operators):
        if o == "*":
            answers.append(functools.reduce(lambda x, y: x * y, numbers[i]))
        if o == "+":
            answers.append(functools.reduce(lambda x, y: x + y, numbers[i]))
    return sum(answers)


def part_one() -> int:
    numbers, operators = numbers_operators()
    return solve(numbers, operators)


print(f"Part one: {part_one()}")
