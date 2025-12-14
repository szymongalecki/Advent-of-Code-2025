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


def mark(grid: list[list[str]]) -> list[tuple[int, int]]:
    paper = []
    for y, l in enumerate(grid):
        for x, s in enumerate(l):
            if s != "@":
                continue
            if accessible(y, x, grid):
                paper.append((y, x))
    return paper


def remove(grid: list[list[str]], paper: list[tuple[int, int]]) -> list[list[str]]:
    for y, x in paper:
        grid[y][x] = "x"
    return grid


def part_one() -> int:
    return len(mark(grid()))


def part_two() -> int:
    g = grid()
    r = 0
    while True:
        paper = mark(g)
        if len(paper) == 0:
            return r
        r += len(paper)
        g = remove(g, paper)


print(f"Part one: {part_one()}")
print(f"Part two: {part_two()}")
