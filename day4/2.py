import re
from collections import Counter

with open('input.txt') as input:
    stamps = sorted([stamp.strip() for stamp in input])
    chunks = [i for i, stamp in enumerate(stamps) if "Guard" in stamp]

    guard_sleep = dict()

    guards = set(re.search(r"#\w+", stamp).group() for stamp in stamps if "Guard" in stamp)
    print(guards)
    for guard in guards:
        guard_sleep[guard] = list()
    
    current_guard = None
    sleep_start = 0 
    sleep_end = 0 
    for stamp in stamps:
        if "Guard" in stamp:
            current_guard = re.search(r"#\w+", stamp).group()
        if "asleep" in stamp:
            sleep_start = int(re.search(r":(\d+)", stamp).group(1))
        if "wakes" in stamp:
            sleep_end = int(re.search(r":(\d+)", stamp).group(1))
            minutes = [minute for minute in range(sleep_start, sleep_end)]
            guard_sleep[current_guard].extend(minutes)
    
    for guard in guard_sleep.items():
        test = (guard[0], Counter(guard[1]).most_common(1))
        print(test)
    for guard in guard_sleep.items():


"""
1901
"""        