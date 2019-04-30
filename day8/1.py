def extract_meta(nodes):
    indexes = list()

    n_c = nodes[0]
    n_m = nodes[1]

    meta_end_index = 2
    for i in range(n_c):
        index, meta = extract_meta(nodes[meta_end_index:])
        for m in meta:
            indexes.append(m)
        meta_end_index += index
    
    meta = nodes[meta_end_index:meta_end_index+n_m]
    for m in meta:
        indexes.append(m)

    return (meta_end_index + n_m, indexes)

with open('input.txt') as input:
    nodes = list(map(int, input.readline().split(' ')))
    result = sum(extract_meta(nodes)[1])
    print(result)



