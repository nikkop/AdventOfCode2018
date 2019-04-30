from collections import Counter

with open('input.txt') as input:
    coords = [tuple(map(int, c.split(','))) for c in input.readlines()]

    test = Counter(coords).most_common
    print(test)