import sys


def ranges_ingredients() -> tuple[list[tuple[int, int]], list[int]]:
    r_, i_ = "".join(open(sys.argv[1], "r").readlines()).split("\n\n")
    ranges = [(int(r.split("-")[0]), int(r.split("-")[1])) for r in r_.split("\n")]
    ingredients = [int(i) for i in i_.split("\n")]
    return ranges, ingredients


def part_one() -> int:
    ranges, ingredients = ranges_ingredients()
    r = 0
    for i in ingredients:
        for r_low, r_high in ranges:
            if r_low <= i <= r_high:
                r += 1
                break
    return r


print(f"Part one: {part_one()}")
