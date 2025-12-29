import sys


def numbers_operators() -> tuple[list[list[int]], list[str]]:
    lines = [l.strip() for l in open(sys.argv[1], "r").readlines()]
    numbers = list(map(lambda l: [int(n) for n in l.split()], lines[:-1]))
    operators = lines[-1].split()
    return numbers, operators


def solve(numbers: list[list[int]], operators: list[str]):
    i_max = len(numbers)
    j_max = len(numbers[0])
    res = 0
    for j in range(j_max):
        op = operators[j]
        mul = 1
        add = 0
        for i in range(i_max):
            if op == "*":
                mul *= numbers[i][j]
            if op == "+":
                add += numbers[i][j]
        if op == "*":
            res += mul
        if op == "+":
            res += add
    return res


def part_one() -> int:
    numbers, operators = numbers_operators()
    return solve(numbers, operators)


print(f"Part one: {part_one()}")
