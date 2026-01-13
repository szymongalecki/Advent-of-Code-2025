import sys


def junction_boxes() -> list[tuple[int, int, int]]:
    return [tuple(map(int, j)) for j in [l.strip().split(",") for l in open(sys.argv[1], "r").readlines()]]

def euclidean_distance(a: tuple[int, int, int], b: tuple[int, int, int]) -> float:
    return sum(list(map(lambda j: (j[0]-j[1])**2, list(zip(a, b))))) ** (1/2)

def can_connect(a: tuple[int, int, int], b: tuple[int, int, int], c: dict) -> bool:
    return (a not in c or len(c[a]) < 2) and (b not in c or len(c[b]) < 2)

def connected(a: tuple[int, int, int], b: tuple[int, int, int], c: dict) -> bool:
    return (a in c and b in c[a]) and (b in c and a in c[b])

def add_connection(a: tuple[int, int, int], b: tuple[int, int, int], c: dict) -> dict:
    def add(x, y):
        if x not in c:
            c[x] = [y]
        else:
            c[x].append(y)
    if not connected(a, b, c) and can_connect(a, b, c):
        add(a, b)
        add(b, a)
    return c
