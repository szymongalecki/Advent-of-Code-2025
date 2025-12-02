import sys


def lines() -> list[str]:
    return [l.strip() for l in open(sys.argv[1], "r").readlines()]


def rotations(lines: list[str]) -> list[tuple[str, int]]:
    return [(l[0], int(l[1:])) for l in lines]


def follow(
    start: int,
    rotations: list[tuple[str, int]],
) -> list[int]:
    positions = []
    for direction, distance in rotations:
        if direction == "R":
            positions.append((start + distance) % 100)
        else:
            positions.append((start - distance) % 100)
        start = positions[-1]
    return positions


def clicks(start: int, rotations: list[tuple[str, int]]):
    cross = 0
    point = 0
    for dir, dist in rotations:
        cross += dist // 100
        dist %= 100
        if dir == "R":
            end = (start + dist) % 100
            if start > end and start != 0 and end != 0:
                cross += 1
        else:
            end = (start - dist) % 100
            if start < end and start != 0 and end != 0:
                cross += 1
        if end == 0:
            point += 1
        start = end
    return cross + point


def part_one():
    return len([p for p in follow(50, rotations(lines())) if p == 0])


def part_two():
    return clicks(50, rotations(lines()))


print(f"Part one: {part_one()}")
print(f"Part two: {part_two()}")
