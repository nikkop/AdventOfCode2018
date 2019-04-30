import re

with open('input.txt') as input:
    lines = [line.strip() for line in input.readlines()]

    steps = [tuple(re.findall(r"\b[A-Z]\b", instruction)) for instruction in lines]

    required_steps = dict()
    for f,t in steps:
        if t in required_steps:
            required_steps[t] = [f, *required_steps[t]]
        else:
            required_steps[t] = [f]

    start_steps = sorted(list(set([s for s,t in steps if s not in required_steps])))
    start = start_steps[0]
    rest = start_steps[1:]

    for r in rest:
        if r not in required_steps:
            required_steps[r] = []

    ordered_steps = [start]

    while len(required_steps) > 0:
        possible_steps = list()
        for step, preq in required_steps.items():
            if all(e in ordered_steps for e in preq):
                possible_steps.append(step)
        possible_steps.sort()
        if len(possible_steps) > 0:
            next_step = possible_steps[0]
            ordered_steps.append(next_step)
            del required_steps[next_step]
    
    print("".join(ordered_steps))