def hamming_dist(s1, s2):
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))

with open('input.txt') as input:
    ids = [id.strip() for id in input]
    found_ids = set()

    for id in ids:
        for char in id:
            count = id.count(char)
            if count == 2 or count == 3:
                found_ids.add(id)
    
    result = None
    for found_id in found_ids:
        for id in found_ids:
            if hamming_dist(found_id, id) == 1:
                result = "".join(c1 for c1, c2 in zip(found_id, id) if c1 == c2)
                break
        else:
            continue
        break

    print(result)