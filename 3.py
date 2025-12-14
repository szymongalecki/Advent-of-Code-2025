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


def part_one() -> int:
    return sum(joltage(bank) for bank in banks())


print(f"Part one: {part_one()}")
