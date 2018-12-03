with open('input.txt') as input:
    numbers = [int(num) for num in input]
    frequencies = set()
    frequency = None
    total = 0

    while not frequency:
        for num in numbers:
            total += num
            if total in frequencies:
                frequency = total 
                break
            frequencies.add(total) 

    print(frequency)