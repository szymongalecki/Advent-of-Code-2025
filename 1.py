import sys


def lines() -> list[str]:
    return [l.strip() for l in open(sys.argv[1], "r").readlines()]


def rotations(lines: list[str]) -> list[tuple[str, int]]:
    return [(l[0], int(l[1:])) for l in lines]


def follow(
    start: int,
    positions: list[int],
    rotations: list[tuple[str, int]],
) -> list[int]:
    for direction, distance in rotations:
        if direction == "R":
            positions.append((start + distance) % 100)
        else:
            positions.append((start - distance) % 100)
        start = positions[-1]
    return positions


def part_one():
    return len([p for p in follow(50, [], rotations(lines())) if p == 0])
