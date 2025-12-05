import sys


def ranges() -> list[tuple[int, int]]:
    return [
        (int(r[0]), int(r[1]))
        for r in [r.split("-") for r in open(sys.argv[1], "r").readline().split(",")]
    ]


def valid(n: int) -> int:
    s = str(n)
    l = len(s)
    if l % 2 != 0:
        return 0
    if s[: l // 2] == s[l // 2 :]:
        return n
    return 0


def part_one() -> int:
    return sum(
        sum([valid(n) for n in range(start, stop + 1)]) for start, stop in ranges()
    )


print(f"Part one: {part_one()}")
