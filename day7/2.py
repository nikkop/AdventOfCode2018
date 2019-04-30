import re

def get_step_time(step):
    return ord(step) - 64 + 60

def all_elves_free(elves):
    return all(e['step'] is None for e in elves)

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

    ordered_steps = list()

    elves = list() 
    for i in range(5):
        elves.append(dict({
            'step': None,
            'time': 0
        }))
    
    elves[0]['step'] = start
    elves[0]['time'] = get_step_time(start)
    
    seconds = 0

    should_continue = True

    while should_continue:
        if len(required_steps) is 0 and all_elves_free(elves):
            should_continue = False
        else:
            seconds += 1
        busy_elves = [elf for elf in elves if elf['step'] is not None and elf['time'] > 0]
        for elf in busy_elves:
            elf['time'] -= 1
            if elf['time'] is 0:
                ordered_steps.append(elf['step'])
                elf['step'] = None
                elf['time'] = 0

        possible_steps = list()
        for step, preq in required_steps.items():
            if all(e in ordered_steps for e in preq):
                possible_steps.append(step)
        possible_steps.sort()
        if len(possible_steps) > 0:
            min_steps = min(len(possible_steps), len(elves))
            next_steps = possible_steps[:min_steps]

            free_elves = [elf for elf in elves if elf['step'] is None and elf['time'] is 0]
            for i in range(min(len(free_elves), len(possible_steps))):
                elf = free_elves[i]
                elf['step'] = possible_steps[i]
                elf['time'] = get_step_time(possible_steps[i])
                del required_steps[possible_steps[i]]

    
    print("".join(ordered_steps))
    print(seconds - 1)