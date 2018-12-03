with open('input.txt') as input:
    numbers = [int(num) for num in input]
    result = sum(numbers)
    print(result)