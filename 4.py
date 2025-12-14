import sys


def grid() -> list[list[str]]:
    return [list(l) for l in [l.strip() for l in open(sys.argv[1], "r").readlines()]]


def accessible(y: int, x: int, grid: list[list[str]]) -> bool:
    positions = [
        (y - 1, x),
        (y + 1, x),
        (y, x - 1),
        (y, x + 1),
        (y - 1, x - 1),
        (y - 1, x + 1),
        (y + 1, x - 1),
        (y + 1, x + 1),
    ]
    count = 0
    for yp, xp in positions:
        if yp < 0 or xp < 0:
            continue
        try:
            if grid[yp][xp] == "@":
                count += 1
        except IndexError:
            continue
    if count < 4:
        return True
    return False


def part_one() -> int:
    g = grid()
    a = 0
    for y, l in enumerate(g):
        for x, s in enumerate(l):
            if s != "@":
                continue
            if accessible(y, x, g):
                a += 1
    return a


print(f"Part one: {part_one()}")
