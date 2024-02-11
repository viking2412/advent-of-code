from pathlib import Path
from itertools import combinations


def fileread():
    return Path("12.txt").read_text().splitlines()


def distinct_permutation(line):
    sharps = line.count("#")
    dots = len(line) - sharps
    indices = combinations(range(len(line)), dots)
    for i in indices:
        arr = ["#"] * len(line)
        for pos in i:
            arr[pos] = "."
        yield arr


def optimized_check(line, mapping):
    temp = 0
    map_check = []
    for i, ch in enumerate(line):
        if temp != 0 and ch == ".":
            map_check.append(temp)
            temp = 0
        if ch == "#":
            temp += 1
        if i == len(line)-1 and temp != 0:
            map_check.append(temp)
    if map_check == mapping:
        return 1
    return 0


def arranges(springs, mapping):
    que = []
    for i in range(len(springs)):
        if springs[i] == "?":
            que.append(i)
    sh_amount = springs.count("#")
    subtractor = (sum(mapping) - sh_amount)
    container = "#" * subtractor + "." * (len(que) - subtractor)
    result = 0
    temp = list(springs)
    for line in distinct_permutation(container):
        a = 0
        for i in que:
            temp[i] = line[a]
            a += 1
        result += optimized_check(temp, mapping)
    return result


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
