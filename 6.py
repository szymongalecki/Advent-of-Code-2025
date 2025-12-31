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


def lines() -> list[list[str]]:
    return [list(l.replace("\n", "")) for l in open(sys.argv[1], "r").readlines()]


def solve_column_wise(lines: list[list[str]]) -> int:
    candidates = ["".join(t) for t in numpy.array(lines[:-1]).transpose().tolist()]
    operators = [o for o in lines[-1] if o != " "]
    numbers = []
    answers = []
    for operator in operators:
        while candidates:
            try:
                numbers.append(int(candidates.pop(0)))
            except:
                answers.append(solve([numbers], [operator]))
                numbers = []
                break
            if candidates == []:
                answers.append(solve([numbers], [operator]))
    return sum(answers)


def part_one() -> int:
    numbers, operators = numbers_operators()
    return solve(numbers, operators)


def part_two() -> int:
    return solve_column_wise(lines())


print(f"Part one: {part_one()}")
print(f"Part two: {part_two()}")
