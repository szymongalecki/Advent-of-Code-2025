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


def part_two() -> int:
    ranges, _ = ranges_ingredients()
    sorted_ranges = sorted(ranges)
    r = 0
    low, high = sorted_ranges[0]
    for l, h in sorted_ranges[1:]:
        # all numbers are already included
        if h <= high:
            pass
        # no intersection, add numbers from previous range
        elif l > high:
            r += (high - low) + 1
            high, low = h, l
        # intersection, union the ranges, do not add numbers yet
        elif l <= high:
            low, high = low, h
    r += (high - low) + 1
    return r


print(f"Part one: {part_one()}")
print(f"Part two: {part_two()}")
