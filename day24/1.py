import re

with open('input.txt') as input:
    factions = [re.findall(r"-?\d+|weak.+?\)|immune.+?;", f) for f in input.read().split("\n\n")]
    print(factions)