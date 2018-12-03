with open('input.txt') as input:
    ids = [id.strip() for id in input]
    collection = dict({ 2: set(), 3: set() })

    for id in ids:
        for char in id:
            count = id.count(char)
            if count in collection:
                collection[count].add(id)

    result = len(collection[2]) * len(collection[3])
    print(result)