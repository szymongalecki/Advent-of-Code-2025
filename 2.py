import sys


def ranges() -> list[range]:
    return [
        range(int(r[0]), int(r[1]) + 1)
        for r in [r.split("-") for r in open(sys.argv[1], "r").readline().split(",")]
    ]


def repeated_twice(n: int) -> bool:
    s = str(n)
    l = len(s)
    if l % 2 != 0:
        return False
    if s[: l // 2] == s[l // 2 :]:
        return True
    return False


def repeated_any(n: int) -> bool:
    s = str(n)
    l = len(s)
    w = len(s) // 2
    while w > 0:
        sequences = [s[i : i + w] for i in range(0, l, w)]
        unique = set(sequences)
        if len(sequences) > 1 and len(unique) == 1:
            return True
        w -= 1
    return False


def part_one() -> int:
    return sum([sum(n for n in r if repeated_twice(n)) for r in ranges()])


def part_two() -> int:
    return sum([sum(n for n in r if repeated_any(n)) for r in ranges()])


print(f"Part one: {part_one()}")
print(f"Part two: {part_two()}")
