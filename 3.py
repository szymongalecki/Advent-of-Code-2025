import sys


def banks() -> list[list[int]]:
    return [
        [int(t) for t in list(b)]
        for b in [l.strip() for l in open(sys.argv[1], "r").readlines()]
    ]


def joltage(bank: list[int]) -> int:
    def sort(bank) -> list[tuple[int, int]]:
        return sorted(enumerate(bank), key=lambda b: b[1], reverse=True)

    i, left = sort(bank[:-1])[0]
    _, right = sort(bank[i + 1 :])[0]
    return left * 10 + right


def overclock(bank: list[int]) -> int:
    def batteries(start: int, selected: list[int]) -> list[int]:
        if len(selected) == 12:
            return selected
        s_v = 0
        s_i = 0
        for i in range(start, len(bank) - 12 + len(selected) + 1):
            if bank[i] > s_v:
                s_v = bank[i]
                s_i = i
        return batteries(s_i + 1, selected + [s_v])

    def joltage(batteries: list[int]) -> int:
        return sum(d * (10**i) for (i, d) in enumerate(reversed(batteries)))

    return joltage(batteries(0, []))


def part_one() -> int:
    return sum(joltage(bank) for bank in banks())


def part_two() -> int:
    return sum(overclock(bank) for bank in banks())


print(f"Part one: {part_one()}")
print(f"Part two: {part_two()}")
