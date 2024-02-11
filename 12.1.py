from pathlib import Path
cache = {}


def decorator(func):
    def wrapper(springs, mapping):
        if (springs, tuple(mapping)) not in cache:
            cache[(springs, tuple(mapping))] = func(springs, mapping)
        return cache[(springs, tuple(mapping))]
    return wrapper


def fileread():
    return Path("12.txt").read_text().splitlines()


def sharp_count(springs, mapping):
    if all(a in ["#", "?"] for a in springs[-mapping[-1]:]) and mapping[-1] == len(springs):
        return arranges(springs[:-mapping[-1]], mapping[:-1])
    if all(a in ["#", "?"] for a in springs[-mapping[-1]:]) and springs[-mapping[-1] - 1] in [".", "?"]:
        return arranges(springs[:-mapping[-1] - 1], mapping[:-1])
    return 0


@decorator
def arranges(springs, mapping):
    if springs == "":
        if not mapping:
            return 1
        else:
            return 0
    if not mapping:
        if "#" in springs:
            return 0
        else:
            return 1
    if mapping[-1] > len(springs):
        return 0
    match springs[-1]:
        case ".":
            return arranges(springs[:-1], mapping)
        case "#":
            return sharp_count(springs, mapping)
        case "?":
            return arranges(springs[:-1], mapping) + sharp_count(springs, mapping)


def solve():
    result = 0
    for line in fileread():
        springs, mapping = line.split(" ")
        springs += 4 * ("?" + springs)
        mapping += 4 * ("," + mapping)
        mapping = [int(x) for x in mapping.split(",")]
        result += arranges(springs, mapping)
    print(result)


if __name__ == '__main__':
    solve()
